import json
import sys
import termios
import tty
from collections.abc import Callable, Iterator
from functools import partial
from itertools import islice
from pathlib import Path

import pytest

import dnd.fight._attack as attack_module
import dnd.fight._creature as creature_module
import dnd.fight._saving_throw as saving_throw_module
import dnd.fight._spell_attack as spell_attack_module
import scripts.fight as fight_module
from dnd.character._creature_base import _CreatureBase
from dnd.character.stats import Stats
from dnd.choices.stats_creation.statistic import Statistic
from dnd.fight._action_group import _And, _Or
from dnd.fight._attack import _Attack
from dnd.fight._attack_result import _AttackResult
from dnd.fight._creature import _Creature, _PlayerFightCreature
from dnd.fight._multi_attack import _MultiAttack
from dnd.fight._non_attack import _NonAttack
from dnd.fight._saving_throw import _SavingThrow
from dnd.fight._saving_throw_result import _SavingThrowResult
from dnd.fight._spell_attack import _SpellAttack
from scripts.fight import (
    _EncounterEntry,
    _FightCli,
    _PlayerEntry,
    _describe,
    _dmg,
    _fire,
    _load_character,
    _load_creature,
    _pick,
    _select,
    _stats,
)


class _Rec:
    """Records calls; replaces unittest.mock.patch."""

    def __init__(
        self, *values: object, fn: Callable[..., object] | None = None
    ) -> None:
        self._it: Iterator[object] | None = iter(values) if values else None
        self._fn: Callable[..., object] | None = fn
        self.call_args_list: list[tuple[tuple[object, ...], dict[str, object]]] = []
        self.call_count = 0

    def __call__(self, *args: object, **kwargs: object) -> object:
        self.call_args_list.append((args, kwargs))
        self.call_count += 1
        if self._fn is not None:
            return self._fn(*args, **kwargs)
        if self._it is not None:
            return next(self._it)
        return None

    def __get__(self, obj: object, objtype: object = None) -> object:
        if obj is None:
            return self
        return partial(self, obj)


_STATS = Stats(
    strength=10,
    dexterity=10,
    constitution=10,
    intelligence=10,
    wisdom=10,
    charisma=10,
)

_BASE_DATA: dict[str, object] = {
    "name": "test",
    "stats": _STATS.model_dump(),
    "speed": 30,
    "dark_vision_range": 0,
    "initiative_bonus": 2,
    "saving_throw_proficiencies": [],
    "other_active_abilities": [],
}

_CREATURE_DATA: dict[str, object] = {
    **_BASE_DATA,
    "n_hit_dice": 1,
    "hit_die_size": 8,
    "attacks": [
        {
            "n_dice": 1,
            "dice_size": 6,
            "attack_bonus": 2,
            "damage_bonus": 0,
            "name": "punch",
        }
    ],
}


class _FloatBonusCreature(_Creature):
    initiative_bonus: float = 21.37


class _IntNameCreature(_Creature):
    name: int = 0


@pytest.mark.unit
class TestAttack:
    _attack = _Attack(
        n_dice=2, dice_size=6, attack_bonus=3, damage_bonus=1, name="sword"
    )

    def test_perform_normal_rolls(self, monkeypatch: pytest.MonkeyPatch) -> None:
        rec = _Rec(10, 15, 4, 3, 2, 1, 3, 2)
        monkeypatch.setattr(attack_module, "randint", rec)
        result = self._attack.perform()
        assert result.first_roll == 13
        assert result.second_roll == 18
        assert isinstance(result, _AttackResult)

    def test_perform_first_roll_critical(self, monkeypatch: pytest.MonkeyPatch) -> None:
        rec = _Rec(20, 10, 3, 4, 2, 1, 3, 2)
        monkeypatch.setattr(attack_module, "randint", rec)
        result = self._attack.perform()
        assert result.first_roll == "critical"
        assert result.second_roll == 13

    def test_perform_second_roll_critical(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        rec = _Rec(10, 20, 3, 4, 2, 1, 3, 2)
        monkeypatch.setattr(attack_module, "randint", rec)
        result = self._attack.perform()
        assert result.first_roll == 13
        assert result.second_roll == "critical"

    def test_perform_both_critical(self, monkeypatch: pytest.MonkeyPatch) -> None:
        rec = _Rec(20, 20, 3, 4, 2, 1, 3, 2)
        monkeypatch.setattr(attack_module, "randint", rec)
        result = self._attack.perform()
        assert result.first_roll == "critical"
        assert result.second_roll == "critical"


@pytest.mark.unit
class TestAttackResult:
    def test_str_no_crit(self) -> None:
        r = _AttackResult(first_roll=10, second_roll=8, damage=5, crit_damage=0)
        s = str(r)
        assert "first_roll=10" in s
        assert "second_roll=8" in s
        assert "damage=5" in s

    def test_str_first_crit(self) -> None:
        r = _AttackResult(first_roll="critical", second_roll=8, damage=5, crit_damage=9)
        assert "crit: 9" in str(r)

    def test_str_second_crit(self) -> None:
        r = _AttackResult(
            first_roll=10, second_roll="critical", damage=5, crit_damage=9
        )
        assert "crit with adv: 9" in str(r)

    def test_str_both_crit(self) -> None:
        r = _AttackResult(
            first_roll="critical", second_roll="critical", damage=5, crit_damage=9
        )
        assert "crit with disadvantage: 9" in str(r)


@pytest.mark.unit
class TestSavingThrow:
    def test_perform_half_on_success(self, monkeypatch: pytest.MonkeyPatch) -> None:
        st = _SavingThrow(
            n_dice=2,
            dice_size=6,
            damage_bonus=0,
            dc=15,
            name="fireball",
            saving_throw_type=Statistic.DEXTERITY,
            half_on_success=True,
        )
        rec = _Rec(4, 4)
        monkeypatch.setattr(saving_throw_module, "randint", rec)
        result = st.perform()
        assert isinstance(result, _SavingThrowResult)
        assert result.dc == 15
        assert result.saving_throw_type == Statistic.DEXTERITY
        assert result.damage_on_fail == 8
        assert result.damage_on_success == 4

    def test_perform_no_half_on_success(self, monkeypatch: pytest.MonkeyPatch) -> None:
        st = _SavingThrow(
            n_dice=1,
            dice_size=8,
            damage_bonus=2,
            dc=13,
            name="poison",
            saving_throw_type=Statistic.CONSTITUTION,
            half_on_success=False,
        )
        rec = _Rec(6)
        monkeypatch.setattr(saving_throw_module, "randint", rec)
        result = st.perform()
        assert result.damage_on_fail == 8
        assert result.damage_on_success == 0

    def test_saving_throw_result_str(self) -> None:
        result = _SavingThrowResult(
            dc=15,
            saving_throw_type=Statistic.DEXTERITY,
            damage_on_fail=10,
            damage_on_success=5,
        )
        assert str(result) == "DC 15 dexterity save | fail: 10 | success: 5"


@pytest.mark.unit
class TestMultiAttack:
    def test_perform_calls_each_attack(self, monkeypatch: pytest.MonkeyPatch) -> None:
        attack1 = _Attack(n_dice=1, dice_size=6, attack_bonus=2, damage_bonus=1)
        attack2 = _Attack(n_dice=1, dice_size=8, attack_bonus=3, damage_bonus=2)
        multi = _MultiAttack(attacks=(attack1, attack2))
        mock_result = _AttackResult(
            first_roll=10, second_roll=15, damage=5, crit_damage=8
        )
        mock_perform = _Rec(fn=lambda self: mock_result)
        monkeypatch.setattr(_Attack, _Attack.perform.__name__, mock_perform)
        results = multi.perform()
        assert mock_perform.call_count == 2
        assert results == [mock_result, mock_result]


@pytest.mark.unit
class TestSpellAttack:
    _spell = _SpellAttack(
        base_n_dice=1,
        extra_dice_per_level=1,
        dice_size=6,
        attack_bonus=5,
        damage_bonus=0,
        min_level=1,
        max_level=3,
        name="magic missile",
    )

    def test_perform_returns_one_result_per_level(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(spell_attack_module, "randint", lambda *a: 10)
        results = self._spell.perform()
        assert len(results) == 3

    def test_perform_at_level_critical(self, monkeypatch: pytest.MonkeyPatch) -> None:
        rec = _Rec(20, 10, 3, 4, 2)
        monkeypatch.setattr(spell_attack_module, "randint", rec)
        result = self._spell._perform_at_level(1)
        assert result.first_roll == "critical"
        assert result.second_roll == 15

    def test_perform_at_level_second_critical(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        rec = _Rec(10, 20, 3, 4, 2, 1)
        monkeypatch.setattr(spell_attack_module, "randint", rec)
        result = self._spell._perform_at_level(1)
        assert result.first_roll == 15
        assert result.second_roll == "critical"

    def test_extra_dice_scale_with_level(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(spell_attack_module, "randint", lambda *a: 3)
        result_l1 = self._spell._perform_at_level(1)
        result_l2 = self._spell._perform_at_level(2)
        assert result_l2.damage > result_l1.damage


@pytest.mark.unit
class TestCreatureInit:
    def test_roll_initiative_with_bonus(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(creature_module, "randint", lambda *a: 10)
        creature = _Creature.model_validate({**_CREATURE_DATA, "initiative_bonus": 5})
        assert creature.initiative == 15

    def test_roll_initiative_invalid_bonus_type(self) -> None:
        with pytest.raises(ValueError, match="initiative_bonus must be int"):
            _FloatBonusCreature.model_validate(
                {**_CREATURE_DATA, "initiative_bonus": 21.37}
            )

    def test_default_type_uses_name(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(creature_module, "randint", lambda *a: 1)
        creature = _Creature.model_validate(_CREATURE_DATA)
        assert creature.type == "test"

    def test_default_type_invalid_name_type(self) -> None:
        with pytest.raises(ValueError, match="name must be str"):
            _IntNameCreature.model_validate({**_CREATURE_DATA, "name": 0})

    def test_explicit_initiative_bypasses_roll(self) -> None:
        creature = _Creature.model_validate({**_CREATURE_DATA, "initiative": 18})
        assert creature.initiative == 18

    def test_creature_requires_attacks(self) -> None:
        with pytest.raises(ValueError, match="creature must have at least one attack"):
            _Creature.model_validate({**_CREATURE_DATA, "attacks": [], "initiative": 1})

    def test_invalid_stats_type_raises_type_error(self) -> None:
        with pytest.raises(TypeError, match="stats must be Stats"):
            creature_module._default_hp({"stats": "not a Stats object"})


@pytest.mark.unit
class TestPlayerFightCreature:
    def test_construction(self) -> None:
        player = _PlayerFightCreature(
            name="test",
            stats=_STATS,
            speed=30,
            dark_vision_range=0,
            initiative_bonus=2,
            saving_throw_proficiencies=(),
            other_active_abilities=(),
            initiative=14,
        )
        assert player.name == "test"
        assert player.initiative == 14


@pytest.mark.unit
class TestNonAttack:
    def test_perform_returns_description(self) -> None:
        na = _NonAttack(name="Stomp", description="massive crush")
        assert na.perform() == "massive crush"

    def test_default_name_empty(self) -> None:
        na = _NonAttack(description="roar")
        assert na.name == ""


@pytest.mark.unit
class TestActionGroups:
    _attack = _Attack(
        n_dice=1, dice_size=6, attack_bonus=2, damage_bonus=0, name="claw"
    )
    _st = _SavingThrow(
        n_dice=1,
        dice_size=6,
        damage_bonus=0,
        dc=12,
        name="venom",
        saving_throw_type=Statistic.CONSTITUTION,
        half_on_success=False,
    )

    def test_or_perform(self, monkeypatch: pytest.MonkeyPatch) -> None:
        mock_result = _AttackResult(
            first_roll=10, second_roll=8, damage=4, crit_damage=0
        )
        monkeypatch.setattr(_Attack, _Attack.perform.__name__, lambda self: mock_result)
        result = _Or(options=(self._attack,)).perform()
        assert result == mock_result

    def test_and_perform(self, monkeypatch: pytest.MonkeyPatch) -> None:
        mock_result = _AttackResult(
            first_roll=10, second_roll=8, damage=4, crit_damage=0
        )
        monkeypatch.setattr(_Attack, _Attack.perform.__name__, lambda self: mock_result)
        results = _And(options=(self._attack, self._attack)).perform()
        assert len(results) == 2


@pytest.mark.unit
class TestFightHelpers:
    def test_dmg_no_bonus(self) -> None:
        assert _dmg(2, 6, 0) == "2d6"

    def test_dmg_positive_bonus(self) -> None:
        assert _dmg(1, 8, 3) == "1d8+3"

    def test_dmg_negative_bonus(self) -> None:
        assert _dmg(1, 8, -2) == "1d8-2"

    def test_stats_non_attack(self) -> None:
        na = _NonAttack(description="roar")
        assert _stats(na) == "roar"

    def test_stats_saving_throw(self) -> None:
        st = _SavingThrow(
            n_dice=2,
            dice_size=6,
            damage_bonus=0,
            dc=14,
            name="fireball",
            saving_throw_type=Statistic.DEXTERITY,
            half_on_success=True,
        )
        result = _stats(st)
        assert "DC 14" in result
        assert "half on save" in result

    def test_stats_saving_throw_no_half(self) -> None:
        st = _SavingThrow(
            n_dice=1,
            dice_size=6,
            damage_bonus=0,
            dc=12,
            name="poison",
            saving_throw_type=Statistic.CONSTITUTION,
            half_on_success=False,
        )
        result = _stats(st)
        assert "half on save" not in result

    def test_stats_attack(self) -> None:
        attack = _Attack(
            n_dice=1, dice_size=6, attack_bonus=4, damage_bonus=2, name="sword"
        )
        result = _stats(attack)
        assert "+4 to hit" in result

    def test_stats_and(self) -> None:
        attack = _Attack(n_dice=1, dice_size=6, attack_bonus=2, damage_bonus=0)
        and_group = _And(options=(attack, attack))
        result = _stats(and_group)
        assert "2 attacks" in result

    def test_stats_or(self) -> None:
        attack = _Attack(n_dice=1, dice_size=6, attack_bonus=2, damage_bonus=0)
        or_group = _Or(options=(attack, attack))
        result = _stats(or_group)
        assert "2 options" in result

    def test_describe_non_attack(self) -> None:
        na = _NonAttack(name="Stomp", description="crush")
        assert _describe(na) == "Stomp"

    def test_describe_non_attack_no_name(self) -> None:
        na = _NonAttack(description="crush")
        assert _describe(na) == "(action)"

    def test_describe_attack(self) -> None:
        attack = _Attack(
            n_dice=1, dice_size=6, attack_bonus=3, damage_bonus=1, name="sword"
        )
        result = _describe(attack)
        assert "sword" in result
        assert "+3 to hit" in result

    def test_describe_and_no_name(self) -> None:
        attack = _Attack(n_dice=1, dice_size=6, attack_bonus=2, damage_bonus=0)
        and_group = _And(options=(attack, attack))
        result = _describe(and_group)
        assert "Multiattack" in result

    def test_select_single_option(self) -> None:
        attack = _Attack(
            n_dice=1, dice_size=6, attack_bonus=2, damage_bonus=0, name="claw"
        )
        result = _select((attack,), "Choose")
        assert result is attack

    def test_select_multiple_options(self, monkeypatch: pytest.MonkeyPatch) -> None:
        attack1 = _Attack(
            n_dice=1, dice_size=6, attack_bonus=2, damage_bonus=0, name="claw"
        )
        attack2 = _Attack(
            n_dice=1, dice_size=8, attack_bonus=3, damage_bonus=1, name="bite"
        )
        monkeypatch.setattr(fight_module, "_pick", lambda *a, **k: 1)
        result = _select((attack1, attack2), "Choose")
        assert result is attack2

    def test_fire_non_attack(self, monkeypatch: pytest.MonkeyPatch) -> None:
        na = _NonAttack(name="Roar", description="loud noise")
        written: list[str] = []
        monkeypatch.setattr(sys.stdout, "write", written.append)
        _fire("monster", na)
        assert any("Roar" in s and "loud noise" in s for s in written)

    def test_fire_and(self, monkeypatch: pytest.MonkeyPatch) -> None:
        attack = _Attack(
            n_dice=1, dice_size=6, attack_bonus=2, damage_bonus=0, name="claw"
        )
        and_group = _And(name="multiattack", options=(attack, attack))
        mock_result = _AttackResult(
            first_roll=10, second_roll=8, damage=4, crit_damage=0
        )
        written: list[str] = []
        monkeypatch.setattr(_Attack, _Attack.perform.__name__, lambda self: mock_result)
        monkeypatch.setattr(sys.stdout, "write", written.append)
        _fire("wolf", and_group)
        assert len(written) == 2

    def test_fire_attack(self, monkeypatch: pytest.MonkeyPatch) -> None:
        attack = _Attack(
            n_dice=1, dice_size=6, attack_bonus=2, damage_bonus=0, name="bite"
        )
        mock_result = _AttackResult(
            first_roll=10, second_roll=8, damage=4, crit_damage=0
        )
        written: list[str] = []
        monkeypatch.setattr(_Attack, _Attack.perform.__name__, lambda self: mock_result)
        monkeypatch.setattr(sys.stdout, "write", written.append)
        _fire("wolf", attack)
        assert any("wolf" in s and "bite" in s for s in written)

    def test_fire_or_single(self, monkeypatch: pytest.MonkeyPatch) -> None:
        attack = _Attack(
            n_dice=1, dice_size=6, attack_bonus=2, damage_bonus=0, name="scratch"
        )
        or_group = _Or(name="or_move", options=(attack,))
        mock_result = _AttackResult(
            first_roll=10, second_roll=8, damage=4, crit_damage=0
        )
        written: list[str] = []
        monkeypatch.setattr(_Attack, _Attack.perform.__name__, lambda self: mock_result)
        monkeypatch.setattr(sys.stdout, "write", written.append)
        _fire("cat", or_group)
        assert any("scratch" in s for s in written)

    def test_fire_or_multiple(self, monkeypatch: pytest.MonkeyPatch) -> None:
        attack1 = _Attack(
            n_dice=1, dice_size=6, attack_bonus=2, damage_bonus=0, name="claw"
        )
        attack2 = _Attack(
            n_dice=1, dice_size=8, attack_bonus=3, damage_bonus=1, name="bite"
        )
        or_group = _Or(name="multiopt", options=(attack1, attack2))
        mock_result = _AttackResult(
            first_roll=10, second_roll=8, damage=4, crit_damage=0
        )
        written: list[str] = []
        monkeypatch.setattr(_Attack, _Attack.perform.__name__, lambda self: mock_result)
        monkeypatch.setattr(fight_module, "_pick", lambda *a, **k: 0)
        monkeypatch.setattr(sys.stdout, "write", written.append)
        _fire("monster", or_group)
        assert len(written) >= 1


@pytest.mark.unit
class TestPick:
    def test_pick_non_tty_empty_input_returns_zero(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(sys.stdin, "isatty", lambda: False)
        monkeypatch.setattr("builtins.input", lambda *a, **k: "")
        monkeypatch.setattr(sys.stdout, "write", lambda *a: None)
        result = _pick(["option1", "option2"], "Choose:")
        assert result == 0

    def test_pick_non_tty_valid_number(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(sys.stdin, "isatty", lambda: False)
        rec = _Rec("2")
        monkeypatch.setattr("builtins.input", rec)
        monkeypatch.setattr(sys.stdout, "write", lambda *a: None)
        result = _pick(["option1", "option2"], "Choose:")
        assert result == 1

    def test_pick_non_tty_invalid_then_valid(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(sys.stdin, "isatty", lambda: False)
        rec = _Rec("99", "abc", "1")
        monkeypatch.setattr("builtins.input", rec)
        monkeypatch.setattr(sys.stdout, "write", lambda *a: None)
        result = _pick(["option1", "option2"], "Choose:")
        assert result == 0

    def test_pick_tty_enter_key(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(sys.stdin, "isatty", lambda: True)
        monkeypatch.setattr(sys.stdin, "fileno", lambda: 0)
        monkeypatch.setattr(termios, "tcgetattr", lambda *a: [])
        monkeypatch.setattr(tty, "setraw", lambda *a: None)
        monkeypatch.setattr(termios, "tcsetattr", lambda *a: None)
        rec = _Rec("\r")
        monkeypatch.setattr(sys.stdin, "read", rec)
        monkeypatch.setattr(sys.stdout, "write", lambda *a: None)
        monkeypatch.setattr(sys.stdout, "flush", lambda: None)
        result = _pick(["option1", "option2"], "Choose:")
        assert result == 0

    def test_pick_tty_down_arrow_then_enter(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(sys.stdin, "isatty", lambda: True)
        monkeypatch.setattr(sys.stdin, "fileno", lambda: 0)
        monkeypatch.setattr(termios, "tcgetattr", lambda *a: [])
        monkeypatch.setattr(tty, "setraw", lambda *a: None)
        monkeypatch.setattr(termios, "tcsetattr", lambda *a: None)
        rec = _Rec("\x1b", "[B", "\r")
        monkeypatch.setattr(sys.stdin, "read", rec)
        monkeypatch.setattr(sys.stdout, "write", lambda *a: None)
        monkeypatch.setattr(sys.stdout, "flush", lambda: None)
        result = _pick(["option1", "option2"], "Choose:")
        assert result == 1

    def test_pick_tty_up_arrow_clamps_at_zero(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(sys.stdin, "isatty", lambda: True)
        monkeypatch.setattr(sys.stdin, "fileno", lambda: 0)
        monkeypatch.setattr(termios, "tcgetattr", lambda *a: [])
        monkeypatch.setattr(tty, "setraw", lambda *a: None)
        monkeypatch.setattr(termios, "tcsetattr", lambda *a: None)
        rec = _Rec("\x1b", "[A", "\r")
        monkeypatch.setattr(sys.stdin, "read", rec)
        monkeypatch.setattr(sys.stdout, "write", lambda *a: None)
        monkeypatch.setattr(sys.stdout, "flush", lambda: None)
        result = _pick(["option1", "option2"], "Choose:")
        assert result == 0

    def test_pick_tty_ctrl_c_raises(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(sys.stdin, "isatty", lambda: True)
        monkeypatch.setattr(sys.stdin, "fileno", lambda: 0)
        monkeypatch.setattr(termios, "tcgetattr", lambda *a: [])
        monkeypatch.setattr(tty, "setraw", lambda *a: None)
        monkeypatch.setattr(termios, "tcsetattr", lambda *a: None)
        rec = _Rec("\x03")
        monkeypatch.setattr(sys.stdin, "read", rec)
        monkeypatch.setattr(sys.stdout, "write", lambda *a: None)
        monkeypatch.setattr(sys.stdout, "flush", lambda: None)
        with pytest.raises(KeyboardInterrupt):
            _pick(["option1", "option2"], "Choose:")

    def test_pick_tty_unknown_escape_ignored(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(sys.stdin, "isatty", lambda: True)
        monkeypatch.setattr(sys.stdin, "fileno", lambda: 0)
        monkeypatch.setattr(termios, "tcgetattr", lambda *a: [])
        monkeypatch.setattr(tty, "setraw", lambda *a: None)
        monkeypatch.setattr(termios, "tcsetattr", lambda *a: None)
        rec = _Rec("\x1b", "[X", "\n")
        monkeypatch.setattr(sys.stdin, "read", rec)
        monkeypatch.setattr(sys.stdout, "write", lambda *a: None)
        monkeypatch.setattr(sys.stdout, "flush", lambda: None)
        result = _pick(["option1", "option2"], "Choose:")
        assert result == 0


@pytest.mark.unit
class TestLoadCreature:
    def test_returns_creature_unchanged(self) -> None:
        creature = _Creature.model_validate({**_CREATURE_DATA, "initiative": 10})
        assert _load_creature(creature) is creature

    def test_loads_from_file(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        creatures_dir = tmp_path / "creatures"
        creatures_dir.mkdir()
        (creatures_dir / "goblin.json").write_text(
            json.dumps({**_CREATURE_DATA, "name": "goblin", "initiative": 5})
        )
        monkeypatch.setattr(fight_module, "_CREATURE_DIR", creatures_dir)
        result = _load_creature("goblin")
        assert isinstance(result, _Creature)
        assert result.name == "goblin"

    def test_raises_on_missing_file(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        creatures_dir = tmp_path / "creatures"
        creatures_dir.mkdir()
        monkeypatch.setattr(fight_module, "_CREATURE_DIR", creatures_dir)
        with pytest.raises(ValueError, match="Unknown creature type"):
            _load_creature("goblin")

    def test_raises_on_invalid_type(self) -> None:
        with pytest.raises(ValueError, match="creature must be a str"):
            _load_creature(42)


@pytest.mark.unit
class TestLoadCharacter:
    def test_returns_creature_base_unchanged(self) -> None:
        base = _CreatureBase.model_validate(_BASE_DATA)
        assert _load_character(base) is base

    def test_loads_from_file(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        characters_dir = tmp_path / "characters"
        characters_dir.mkdir()
        (characters_dir / "hero.json").write_text(json.dumps(_BASE_DATA))
        monkeypatch.setattr(fight_module, "_CHARACTER_DIR", characters_dir)
        result = _load_character("hero")
        assert isinstance(result, _CreatureBase)
        assert result.name == "test"

    def test_raises_on_missing_file(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        characters_dir = tmp_path / "characters"
        characters_dir.mkdir()
        monkeypatch.setattr(fight_module, "_CHARACTER_DIR", characters_dir)
        with pytest.raises(ValueError, match="Unknown character"):
            _load_character("hero")

    def test_raises_on_invalid_type(self) -> None:
        with pytest.raises(ValueError, match="character must be a str"):
            _load_character(42)


@pytest.mark.unit
class TestRunFight:
    def test_player_turn_no_attack_output(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        creatures_dir = tmp_path / "creatures"
        creatures_dir.mkdir()
        characters_dir = tmp_path / "characters"
        characters_dir.mkdir()
        (creatures_dir / "skeleton.json").write_text(
            json.dumps({**_CREATURE_DATA, "name": "skeleton", "initiative": 5})
        )
        (characters_dir / "hero.json").write_text(
            json.dumps({**_BASE_DATA, "name": "hero"})
        )
        monkeypatch.setattr(fight_module, "_CREATURE_DIR", creatures_dir)
        monkeypatch.setattr(fight_module, "_CHARACTER_DIR", characters_dir)
        cli = _FightCli.model_construct(
            encounter=[
                _EncounterEntry.model_validate(
                    {"creature": "skeleton", "n_entities": 1}
                )
            ],
            players=[
                _PlayerEntry.model_validate({"character": "hero", "initiative": 20})
            ],
        )
        mock_input = _Rec("", "", "", "")
        monkeypatch.setattr("builtins.input", mock_input)
        mock_print = _Rec()
        monkeypatch.setattr("builtins.print", mock_print)
        monkeypatch.setattr(fight_module, "cycle", lambda it: islice(it, 2))
        cli.cli_cmd()
        printed_args = [str(call) for call in mock_print.call_args_list]
        assert not any("hero" in arg for arg in printed_args)

    def test_monster_turn_prints_attacks(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        creatures_dir = tmp_path / "creatures"
        creatures_dir.mkdir()
        attack = _Attack(
            n_dice=1, dice_size=6, attack_bonus=2, damage_bonus=1, name="claw"
        )
        creature_data = {
            **_CREATURE_DATA,
            "name": "wolf",
            "initiative": 5,
            "attacks": [attack.model_dump()],
        }
        (creatures_dir / "wolf.json").write_text(json.dumps(creature_data))
        monkeypatch.setattr(fight_module, "_CREATURE_DIR", creatures_dir)
        cli = _FightCli.model_construct(
            encounter=[
                _EncounterEntry.model_validate({"creature": "wolf", "n_entities": 1})
            ],
            players=[],
        )
        mock_result = _AttackResult(
            first_roll=12, second_roll=8, damage=5, crit_damage=9
        )
        written: list[str] = []
        mock_input = _Rec("", "")
        monkeypatch.setattr("builtins.input", mock_input)
        monkeypatch.setattr(sys.stdout, "write", written.append)
        monkeypatch.setattr(fight_module, "cycle", lambda it: islice(it, 1))
        monkeypatch.setattr(_Attack, _Attack.perform.__name__, lambda self: mock_result)
        cli.cli_cmd()
        all_prompts = [call[0][0] for call in mock_input.call_args_list]
        assert any("wolf" in p and "moves now" in p for p in all_prompts)
        assert any("wolf [claw]" in line for line in written)

    def test_duplicate_attack_names_grouped(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        creatures_dir = tmp_path / "creatures"
        creatures_dir.mkdir()
        attack = _Attack(
            n_dice=1, dice_size=6, attack_bonus=2, damage_bonus=1, name="claw"
        )
        creature_data = {
            **_CREATURE_DATA,
            "name": "wolf",
            "initiative": 5,
            "attacks": [attack.model_dump(), attack.model_dump()],
        }
        (creatures_dir / "wolf.json").write_text(json.dumps(creature_data))
        monkeypatch.setattr(fight_module, "_CREATURE_DIR", creatures_dir)
        cli = _FightCli.model_construct(
            encounter=[
                _EncounterEntry.model_validate({"creature": "wolf", "n_entities": 1})
            ],
            players=[],
        )
        mock_result = _AttackResult(
            first_roll=12, second_roll=8, damage=5, crit_damage=9
        )
        written: list[str] = []
        monkeypatch.setattr("builtins.input", _Rec("", ""))
        monkeypatch.setattr(sys.stdout, "write", written.append)
        monkeypatch.setattr(fight_module, "cycle", lambda it: islice(it, 1))
        monkeypatch.setattr(_Attack, _Attack.perform.__name__, lambda self: mock_result)
        monkeypatch.setattr(fight_module, "_pick", lambda *a, **k: 0)
        cli.cli_cmd()
        assert any("wolf [claw]" in line for line in written)

    def test_offhand_attack_fires(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        creatures_dir = tmp_path / "creatures"
        creatures_dir.mkdir()
        main_attack = _Attack(
            n_dice=1, dice_size=6, attack_bonus=2, damage_bonus=1, name="sword"
        )
        offhand_attack = _Attack(
            n_dice=1,
            dice_size=4,
            attack_bonus=2,
            damage_bonus=0,
            name="dagger (offhand)",
        )
        creature_data = {
            **_CREATURE_DATA,
            "name": "fighter",
            "initiative": 5,
            "attacks": [main_attack.model_dump(), offhand_attack.model_dump()],
        }
        (creatures_dir / "fighter.json").write_text(json.dumps(creature_data))
        monkeypatch.setattr(fight_module, "_CREATURE_DIR", creatures_dir)
        cli = _FightCli.model_construct(
            encounter=[
                _EncounterEntry.model_validate({"creature": "fighter", "n_entities": 1})
            ],
            players=[],
        )
        mock_result = _AttackResult(
            first_roll=12, second_roll=8, damage=5, crit_damage=9
        )
        written: list[str] = []
        monkeypatch.setattr("builtins.input", _Rec("", ""))
        monkeypatch.setattr(sys.stdout, "write", written.append)
        monkeypatch.setattr(fight_module, "cycle", lambda it: islice(it, 1))
        monkeypatch.setattr(_Attack, _Attack.perform.__name__, lambda self: mock_result)
        cli.cli_cmd()
        assert any("dagger (offhand)" in line for line in written)

    def test_hp_tracking_after_player_deals_damage(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        creatures_dir = tmp_path / "creatures"
        creatures_dir.mkdir()
        characters_dir = tmp_path / "characters"
        characters_dir.mkdir()
        attack = _Attack(
            n_dice=1, dice_size=6, attack_bonus=2, damage_bonus=1, name="sword"
        )
        creature_data = {
            **_CREATURE_DATA,
            "name": "goblin",
            "initiative": 1,
            "attacks": [attack.model_dump()],
        }
        (creatures_dir / "goblin.json").write_text(json.dumps(creature_data))
        (characters_dir / "hero.json").write_text(
            json.dumps({**_BASE_DATA, "name": "hero"})
        )
        monkeypatch.setattr(fight_module, "_CREATURE_DIR", creatures_dir)
        monkeypatch.setattr(fight_module, "_CHARACTER_DIR", characters_dir)
        cli = _FightCli.model_construct(
            encounter=[
                _EncounterEntry.model_validate({"creature": "goblin", "n_entities": 1})
            ],
            players=[
                _PlayerEntry.model_validate({"character": "hero", "initiative": 20})
            ],
        )
        written: list[str] = []
        monkeypatch.setattr("builtins.input", _Rec("", "5", "", ""))
        monkeypatch.setattr(sys.stdout, "write", written.append)
        monkeypatch.setattr(fight_module, "cycle", lambda it: islice(it, 1))
        monkeypatch.setattr(fight_module, "_pick", _Rec(1, 0))
        cli.cli_cmd()
        assert any("→" in line for line in written)

    def test_hp_tracking_empty_damage_breaks_inner_loop(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        creatures_dir = tmp_path / "creatures"
        creatures_dir.mkdir()
        characters_dir = tmp_path / "characters"
        characters_dir.mkdir()
        attack = _Attack(
            n_dice=1, dice_size=6, attack_bonus=2, damage_bonus=1, name="sword"
        )
        creature_data = {
            **_CREATURE_DATA,
            "name": "goblin",
            "initiative": 1,
            "attacks": [attack.model_dump()],
        }
        (creatures_dir / "goblin.json").write_text(json.dumps(creature_data))
        (characters_dir / "hero.json").write_text(
            json.dumps({**_BASE_DATA, "name": "hero"})
        )
        monkeypatch.setattr(fight_module, "_CREATURE_DIR", creatures_dir)
        monkeypatch.setattr(fight_module, "_CHARACTER_DIR", characters_dir)
        cli = _FightCli.model_construct(
            encounter=[
                _EncounterEntry.model_validate({"creature": "goblin", "n_entities": 1})
            ],
            players=[
                _PlayerEntry.model_validate({"character": "hero", "initiative": 20})
            ],
        )
        written: list[str] = []
        monkeypatch.setattr("builtins.input", _Rec("", "", ""))
        monkeypatch.setattr(sys.stdout, "write", written.append)
        monkeypatch.setattr(fight_module, "cycle", lambda it: islice(it, 1))
        monkeypatch.setattr(fight_module, "_pick", _Rec(1, 0))
        cli.cli_cmd()
        assert written is not None

    def test_hp_tracking_invalid_damage_then_valid(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        creatures_dir = tmp_path / "creatures"
        creatures_dir.mkdir()
        characters_dir = tmp_path / "characters"
        characters_dir.mkdir()
        attack = _Attack(
            n_dice=1, dice_size=6, attack_bonus=2, damage_bonus=1, name="sword"
        )
        creature_data = {
            **_CREATURE_DATA,
            "name": "goblin",
            "initiative": 1,
            "attacks": [attack.model_dump()],
        }
        (creatures_dir / "goblin.json").write_text(json.dumps(creature_data))
        (characters_dir / "hero.json").write_text(
            json.dumps({**_BASE_DATA, "name": "hero"})
        )
        monkeypatch.setattr(fight_module, "_CREATURE_DIR", creatures_dir)
        monkeypatch.setattr(fight_module, "_CHARACTER_DIR", characters_dir)
        cli = _FightCli.model_construct(
            encounter=[
                _EncounterEntry.model_validate({"creature": "goblin", "n_entities": 1})
            ],
            players=[
                _PlayerEntry.model_validate({"character": "hero", "initiative": 20})
            ],
        )
        written: list[str] = []
        monkeypatch.setattr("builtins.input", _Rec("", "bad", "3", "", ""))
        monkeypatch.setattr(sys.stdout, "write", written.append)
        monkeypatch.setattr(fight_module, "cycle", lambda it: islice(it, 1))
        monkeypatch.setattr(fight_module, "_pick", _Rec(1, 0))
        cli.cli_cmd()
        assert any("valid number" in line for line in written)

    def test_multi_entity_index_in_prefix(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        creatures_dir = tmp_path / "creatures"
        creatures_dir.mkdir()
        attack = _Attack(
            n_dice=1, dice_size=6, attack_bonus=2, damage_bonus=1, name="claw"
        )
        creature_data = {
            **_CREATURE_DATA,
            "name": "wolf",
            "initiative": 5,
            "attacks": [attack.model_dump()],
        }
        (creatures_dir / "wolf.json").write_text(json.dumps(creature_data))
        monkeypatch.setattr(fight_module, "_CREATURE_DIR", creatures_dir)
        cli = _FightCli.model_construct(
            encounter=[
                _EncounterEntry.model_validate({"creature": "wolf", "n_entities": 3})
            ],
            players=[],
        )
        mock_result = _AttackResult(
            first_roll=12, second_roll=8, damage=5, crit_damage=9
        )
        mock_input = _Rec("", "", "", "", "", "")
        monkeypatch.setattr("builtins.input", mock_input)
        monkeypatch.setattr("builtins.print", lambda *a, **k: None)
        monkeypatch.setattr(fight_module, "cycle", lambda it: islice(it, 3))
        monkeypatch.setattr(_Attack, _Attack.perform.__name__, lambda self: mock_result)
        cli.cli_cmd()
        move_prompts = [
            call[0][0]
            for call in mock_input.call_args_list
            if "moves now" in call[0][0]
        ]
        assert len(move_prompts) == 3
        assert "wolf 1" in move_prompts[0]
        assert "wolf 2" in move_prompts[1]
        assert "wolf 3" in move_prompts[2]
