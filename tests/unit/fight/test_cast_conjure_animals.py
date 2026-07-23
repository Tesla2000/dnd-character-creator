from enum import IntEnum
from typing import Self

import pytest

import dnd.character.actions._melee_attack as melee_attack_module
import dnd.fight.battlemap as battlemap_module
from dnd._position import Position
from dnd._combat_event import ConcentrationBrokenEvent
from dnd.character._ability_name import AbilityName
from dnd.character.actions.combat.attack_with_wolf_bite import AttackWithWolfBite
from dnd.character.actions.combat.cast_conjure_animals import CastConjureAnimals
from dnd.character.actions.combat.command_summoned_beast import CommandSummonedBeast
from dnd.character.presentable_character import PresentableCharacter
from dnd.character.spells.max_spell_levels import SpellSlots
from dnd.character.stats import Stats
from dnd.fight._condition import Condition
from dnd.fight._team_id import TeamId
from dnd.fight.battlemap import Battlemap
from dnd.fight.fight_character import (
    AnyActiveCombatant,
    DownedFightCharacter,
    FightCharacter,
    SpellcasterFightCharacter,
    UnsummonedFightCharacter,
)

_STATS = Stats(
    strength=10,
    dexterity=10,
    constitution=10,
    intelligence=10,
    wisdom=10,
    charisma=10,
)

_BASE_PC_DATA: dict[str, object] = {
    "race": "Human",
    "stats": _STATS.model_dump(),
    "health_base": 20,
    "character_data": {"name": "test"},
    "classes": {
        "wizard": 0,
        "sorcerer": 0,
        "fighter": 0,
        "barbarian": 0,
        "rogue": 0,
        "cleric": 0,
        "druid": 5,
        "paladin": 0,
        "ranger": 0,
        "monk": 0,
        "bard": 0,
        "warlock": 0,
        "artificer": 0,
    },
    "speed": 30,
    "dark_vision_range": 0,
    "saving_throw_proficiencies": [],
    "other_active_abilities": [],
}

_SPELL_SLOTS_WITH_L3 = SpellSlots(
    level_1=4,
    level_2=3,
    level_3=2,
    level_4=0,
    level_5=0,
    level_6=0,
    level_7=0,
    level_8=0,
    level_9=0,
)
_SPELL_SLOTS_NO_L3 = SpellSlots(
    level_1=4,
    level_2=3,
    level_3=0,
    level_4=0,
    level_5=0,
    level_6=0,
    level_7=0,
    level_8=0,
    level_9=0,
)


def _make_caster(**kwargs: object) -> SpellcasterFightCharacter:
    pc = PresentableCharacter.model_validate(
        {**_BASE_PC_DATA, "actions": [AbilityName.CONJURE_ANIMALS]}
    )
    return SpellcasterFightCharacter(
        character=pc,
        initiative=20,
        max_health=pc.health,
        current_health=pc.health,
        remaining_spell_slots=_SPELL_SLOTS_WITH_L3,
    ).model_copy(update=kwargs)


def _make_enemy(**kwargs: object) -> FightCharacter:
    pc = PresentableCharacter.model_validate(_BASE_PC_DATA)
    fc = FightCharacter.from_presentable(pc, initiative=5).model_copy(
        update={"team_id": TeamId.B, "position": Position(x=1, y=0)}
    )
    return fc.model_copy(update=kwargs)


def _make_wolf(**kwargs: object) -> FightCharacter:
    pc = PresentableCharacter.model_validate(_BASE_PC_DATA)
    fc = FightCharacter.from_presentable(pc, initiative=1).model_copy(
        update={
            "summoned_by": _SixSlot.CASTER,
            "active_features": frozenset({AbilityName.ATTACK_WITH_WOLF_BITE}),
            "attacks_remaining": 1,
            "team_id": TeamId.A,
        }
    )
    return fc.model_copy(update=kwargs)


def _make_reserved_slot(
    position: Position, team_id: TeamId = TeamId.A
) -> UnsummonedFightCharacter:
    pc = PresentableCharacter.model_validate(_BASE_PC_DATA)
    return UnsummonedFightCharacter.reserved_for_summon(
        pc, initiative=1, team_id=team_id, position=position
    )


class _SixSlot(IntEnum):
    CASTER = 0
    ENEMY = 1
    R1 = 2
    R2 = 3
    R3 = 4
    R4 = 5


class _SixBattlemap(Battlemap[_SixSlot]):
    combatants: tuple[
        AnyActiveCombatant,
        AnyActiveCombatant,
        AnyActiveCombatant,
        AnyActiveCombatant,
        AnyActiveCombatant,
        AnyActiveCombatant,
    ]

    def get_combatant(self, slot: _SixSlot) -> AnyActiveCombatant:
        return self.combatants[slot]

    def replace_combatant(self, slot: _SixSlot, updated: AnyActiveCombatant) -> Self:
        combatants = list(self.combatants)
        combatants[slot] = updated
        return self.model_copy(update={"combatants": tuple(combatants)})


def _make_full_battlemap(
    caster: AnyActiveCombatant | None = None,
    enemy: AnyActiveCombatant | None = None,
) -> _SixBattlemap:
    caster = caster if caster is not None else _make_caster()
    enemy = enemy if enemy is not None else _make_enemy()
    reserved = tuple(_make_reserved_slot(Position(x=0, y=i + 1)) for i in range(4))
    return _SixBattlemap(combatants=(caster, enemy, *reserved))


@pytest.mark.unit
class TestCastConjureAnimals:
    def test_create_returns_empty_for_non_spellcaster(self) -> None:
        pc = PresentableCharacter.model_validate(
            {**_BASE_PC_DATA, "actions": [AbilityName.CONJURE_ANIMALS]}
        )
        fc = FightCharacter.from_presentable(pc, initiative=20)
        bm = _make_full_battlemap(caster=fc)
        assert CastConjureAnimals.create(_SixSlot.CASTER, fc, bm) == ()

    def test_create_returns_empty_when_no_action(self) -> None:
        caster = _make_caster(has_action=False)
        bm = _make_full_battlemap(caster=caster)
        assert CastConjureAnimals.create(_SixSlot.CASTER, caster, bm) == ()

    def test_create_returns_empty_when_no_level_3_slot(self) -> None:
        caster = _make_caster(remaining_spell_slots=_SPELL_SLOTS_NO_L3)
        bm = _make_full_battlemap(caster=caster)
        assert CastConjureAnimals.create(_SixSlot.CASTER, caster, bm) == ()

    def test_create_returns_empty_when_no_conjure_animals_ability(self) -> None:
        pc = PresentableCharacter.model_validate(
            {**_BASE_PC_DATA, "actions": [AbilityName.FIREBALL]}
        )
        caster = SpellcasterFightCharacter(
            character=pc,
            initiative=20,
            max_health=pc.health,
            current_health=pc.health,
            remaining_spell_slots=_SPELL_SLOTS_WITH_L3,
        )
        bm = _make_full_battlemap(caster=caster)
        assert CastConjureAnimals.create(_SixSlot.CASTER, caster, bm) == ()

    def test_create_returns_empty_when_fewer_than_four_reserved_slots(self) -> None:
        caster = _make_caster()
        enemy = _make_enemy()
        reserved = tuple(_make_reserved_slot(Position(x=0, y=i + 1)) for i in range(3))
        bm = _SixBattlemap(combatants=(caster, enemy, *reserved, _make_enemy()))
        assert CastConjureAnimals.create(_SixSlot.CASTER, caster, bm) == ()

    def test_create_returns_one_action_when_eligible(self) -> None:
        caster = _make_caster()
        bm = _make_full_battlemap(caster=caster)
        assert len(CastConjureAnimals.create(_SixSlot.CASTER, caster, bm)) == 1

    def test_perform_spends_action_slot_and_sets_concentration(self) -> None:
        caster = _make_caster()
        bm = _make_full_battlemap(caster=caster)
        actions = CastConjureAnimals.create(_SixSlot.CASTER, caster, bm)
        new_bm = actions[0].perform(bm)
        new_caster = new_bm.get_combatant(_SixSlot.CASTER)
        assert isinstance(new_caster, SpellcasterFightCharacter)
        assert not new_caster.has_action
        assert (
            new_caster.remaining_spell_slots.level_3
            == _SPELL_SLOTS_WITH_L3.level_3 - 1
        )
        assert Condition.CONCENTRATION in new_caster.conditions

    def test_perform_summons_four_wolves(self) -> None:
        caster = _make_caster()
        bm = _make_full_battlemap(caster=caster)
        actions = CastConjureAnimals.create(_SixSlot.CASTER, caster, bm)
        new_bm = actions[0].perform(bm)
        wolves = [
            new_bm.get_combatant(s)
            for s in (_SixSlot.R1, _SixSlot.R2, _SixSlot.R3, _SixSlot.R4)
        ]
        for wolf in wolves:
            assert isinstance(wolf, FightCharacter)
            assert wolf.summoned_by == _SixSlot.CASTER
            assert wolf.current_health == 11
            assert wolf.max_health == 11
            assert wolf.has_action is False
            assert wolf.attacks_remaining == 0
            assert AbilityName.ATTACK_WITH_WOLF_BITE in wolf.active_features

    def test_perform_returns_unchanged_when_actor_not_spellcaster(self) -> None:
        pc = PresentableCharacter.model_validate(_BASE_PC_DATA)
        fc = FightCharacter.from_presentable(pc, initiative=1)
        downed = DownedFightCharacter.from_active(fc)
        bm = _make_full_battlemap(caster=downed)
        action = CastConjureAnimals(actor_slot=_SixSlot.CASTER)
        assert action.perform(bm) is bm


@pytest.mark.unit
class TestBattlemapDealDamage:
    def test_deal_damage_noop_when_not_fight_character(self) -> None:
        pc = PresentableCharacter.model_validate(_BASE_PC_DATA)
        fc = FightCharacter.from_presentable(pc, initiative=1)
        downed = DownedFightCharacter.from_active(fc)
        bm = _make_full_battlemap(caster=downed)
        new_bm = bm.deal_damage(_SixSlot.CASTER, 10)
        assert new_bm is bm

    def test_deal_damage_without_concentration_just_applies_damage(self) -> None:
        caster = _make_caster(current_health=50, max_health=50)
        bm = _make_full_battlemap(caster=caster)
        new_bm = bm.deal_damage(_SixSlot.CASTER, 10)
        new_caster = new_bm.get_combatant(_SixSlot.CASTER)
        assert isinstance(new_caster, FightCharacter)
        assert new_caster.current_health == 40
        assert not any(
            isinstance(e, ConcentrationBrokenEvent) for e in new_bm.event_log
        )

    def test_deal_damage_failed_save_breaks_concentration_and_vanishes_summons(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(battlemap_module, "randint", lambda *_: 1)
        caster = _make_caster(
            current_health=50,
            max_health=50,
            conditions=frozenset({Condition.CONCENTRATION}),
        )
        wolf = _make_wolf()
        bm = _SixBattlemap(
            combatants=(
                caster,
                _make_enemy(),
                wolf,
                _make_reserved_slot(Position(x=0, y=2)),
                _make_reserved_slot(Position(x=0, y=3)),
                _make_reserved_slot(Position(x=0, y=4)),
            )
        )
        new_bm = bm.deal_damage(_SixSlot.CASTER, 10)
        new_caster = new_bm.get_combatant(_SixSlot.CASTER)
        assert isinstance(new_caster, FightCharacter)
        assert Condition.CONCENTRATION not in new_caster.conditions
        new_wolf = new_bm.get_combatant(_SixSlot.R1)
        assert isinstance(new_wolf, UnsummonedFightCharacter)
        assert any(
            isinstance(e, ConcentrationBrokenEvent) and e.caster_slot == _SixSlot.CASTER
            for e in new_bm.event_log
        )

    def test_deal_damage_successful_save_keeps_concentration(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(battlemap_module, "randint", lambda *_: 20)
        caster = _make_caster(
            current_health=50,
            max_health=50,
            conditions=frozenset({Condition.CONCENTRATION}),
        )
        bm = _make_full_battlemap(caster=caster)
        new_bm = bm.deal_damage(_SixSlot.CASTER, 10)
        new_caster = new_bm.get_combatant(_SixSlot.CASTER)
        assert isinstance(new_caster, FightCharacter)
        assert Condition.CONCENTRATION in new_caster.conditions

    def test_deal_damage_downing_the_caster_breaks_concentration_without_a_save(
        self,
    ) -> None:
        caster = _make_caster(
            current_health=5,
            max_health=50,
            conditions=frozenset({Condition.CONCENTRATION}),
        )
        wolf = _make_wolf()
        bm = _SixBattlemap(
            combatants=(
                caster,
                _make_enemy(),
                wolf,
                _make_reserved_slot(Position(x=0, y=2)),
                _make_reserved_slot(Position(x=0, y=3)),
                _make_reserved_slot(Position(x=0, y=4)),
            )
        )
        new_bm = bm.deal_damage(_SixSlot.CASTER, 100)
        new_caster = new_bm.get_combatant(_SixSlot.CASTER)
        assert isinstance(new_caster, DownedFightCharacter)
        new_wolf = new_bm.get_combatant(_SixSlot.R1)
        assert isinstance(new_wolf, UnsummonedFightCharacter)
        assert any(
            isinstance(e, ConcentrationBrokenEvent) and e.caster_slot == _SixSlot.CASTER
            for e in new_bm.event_log
        )


@pytest.mark.unit
class TestResetSummonedCreatures:
    def test_reset_resets_action_economy_for_matching_summoned_by(self) -> None:
        caster = _make_caster()
        wolf = _make_wolf(
            has_action=False,
            has_bonus_action=False,
            has_reaction=False,
            attacks_remaining=0,
        )
        bm = _SixBattlemap(
            combatants=(
                caster,
                _make_enemy(),
                wolf,
                _make_reserved_slot(Position(x=0, y=2)),
                _make_reserved_slot(Position(x=0, y=3)),
                _make_reserved_slot(Position(x=0, y=4)),
            )
        )
        new_bm = bm.reset_summoned_creatures(_SixSlot.CASTER)
        new_wolf = new_bm.get_combatant(_SixSlot.R1)
        assert isinstance(new_wolf, FightCharacter)
        assert new_wolf.has_action
        assert new_wolf.attacks_remaining == 1

    def test_reset_ignores_creatures_summoned_by_someone_else(self) -> None:
        caster = _make_caster()
        other_wolf = _make_wolf(has_action=False, summoned_by=_SixSlot.ENEMY)
        bm = _SixBattlemap(
            combatants=(
                caster,
                _make_enemy(),
                other_wolf,
                _make_reserved_slot(Position(x=0, y=2)),
                _make_reserved_slot(Position(x=0, y=3)),
                _make_reserved_slot(Position(x=0, y=4)),
            )
        )
        new_bm = bm.reset_summoned_creatures(_SixSlot.CASTER)
        new_wolf = new_bm.get_combatant(_SixSlot.R1)
        assert isinstance(new_wolf, FightCharacter)
        assert not new_wolf.has_action


@pytest.mark.unit
class TestCommandSummonedBeast:
    def test_create_returns_empty_when_no_summoned_beast(self) -> None:
        caster = _make_caster()
        bm = _make_full_battlemap(caster=caster)
        assert CommandSummonedBeast.create(_SixSlot.CASTER, caster, bm) == ()

    def test_create_returns_empty_when_wolf_has_no_attacks_remaining(self) -> None:
        caster = _make_caster()
        wolf = _make_wolf(position=Position(x=1, y=0), attacks_remaining=0)
        bm = _SixBattlemap(
            combatants=(
                caster,
                _make_enemy(),
                wolf,
                _make_reserved_slot(Position(x=0, y=2)),
                _make_reserved_slot(Position(x=0, y=3)),
                _make_reserved_slot(Position(x=0, y=4)),
            )
        )
        assert CommandSummonedBeast.create(_SixSlot.CASTER, caster, bm) == ()

    def test_create_returns_candidate_for_adjacent_enemy(self) -> None:
        caster = _make_caster(position=Position(x=100, y=100))
        wolf = _make_wolf(position=Position(x=1, y=0))
        enemy = _make_enemy(position=Position(x=2, y=0))
        bm = _SixBattlemap(
            combatants=(
                caster,
                enemy,
                wolf,
                _make_reserved_slot(Position(x=0, y=2)),
                _make_reserved_slot(Position(x=0, y=3)),
                _make_reserved_slot(Position(x=0, y=4)),
            )
        )
        candidates = CommandSummonedBeast.create(_SixSlot.CASTER, caster, bm)
        assert len(candidates) == 1
        assert candidates[0].executor.actor_slot == _SixSlot.R1

    def test_perform_spends_wolfs_own_attack_not_casters_action(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(melee_attack_module, "randint", lambda *_: 15)
        caster = _make_caster(position=Position(x=100, y=100))
        wolf = _make_wolf(position=Position(x=1, y=0))
        enemy = _make_enemy(
            position=Position(x=2, y=0),
            base_ac=5,
            max_health=100,
            current_health=100,
        )
        bm = _SixBattlemap(
            combatants=(
                caster,
                enemy,
                wolf,
                _make_reserved_slot(Position(x=0, y=2)),
                _make_reserved_slot(Position(x=0, y=3)),
                _make_reserved_slot(Position(x=0, y=4)),
            )
        )
        candidates = CommandSummonedBeast.create(_SixSlot.CASTER, caster, bm)
        new_bm = candidates[0].perform(bm)
        new_wolf = new_bm.get_combatant(_SixSlot.R1)
        new_enemy = new_bm.get_combatant(_SixSlot.ENEMY)
        new_caster = new_bm.get_combatant(_SixSlot.CASTER)
        assert isinstance(new_wolf, FightCharacter)
        assert new_wolf.attacks_remaining == 0
        assert isinstance(new_caster, SpellcasterFightCharacter)
        assert new_caster.has_action
        expected_damage = 2 * 15 + AttackWithWolfBite._damage_bonus()
        assert new_enemy.current_health == 100 - expected_damage
