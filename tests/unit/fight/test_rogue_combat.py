from __future__ import annotations

from enum import IntEnum
from typing import Self

import pytest

import dnd.character.actions._melee_attack as melee_attack_module
from dnd._combat_event import MeleeDamageEvent, TurnStartEvent
from dnd._position import Position
from dnd.character._ability_name import AbilityName
from dnd.character.actions.advantage_modifier import (
    DisadvantageModifier,
    RecklessAdvantageModifier,
)
from dnd.character.actions.combat.attack_with_axe import AttackWithAxe
from dnd.character.actions.combat.attack_with_dagger import AttackWithDagger
from dnd.character.actions.combat.attack_with_hand_crossbow import (
    AttackWithHandCrossbow,
)
from dnd.character.actions.combat.attack_with_rapier import AttackWithRapier
from dnd.character.actions.combat.attack_with_shortbow import AttackWithShortbow
from dnd.character.actions.combat.attack_with_shortsword import AttackWithShortsword
from dnd.character.actions.combat.dash import Dash
from dnd.character.actions.combat.disengage import Disengage
from dnd.character.actions.combat.move import Move
from dnd.character.presentable_character import PresentableCharacter
from dnd.character.stats import Stats
from dnd.choices.equipment_creation.weapons import WeaponName
from dnd.choices.stats_creation.statistic import Statistic
from dnd.fight._team_id import TeamId
from dnd.fight.battlemap import Battlemap
from dnd.fight.fight_character import (
    AnyActiveCombatant,
    DownedFightCharacter,
    FightCharacter,
)


class _Rec:
    def __init__(self, *values: object) -> None:
        self._it = iter(values)

    def __call__(self, *args: object, **kwargs: object) -> object:
        return next(self._it)


class _AlwaysDisadvantageModifier(DisadvantageModifier):
    def apply(self, attacker: FightCharacter, _defender: FightCharacter) -> bool:
        return True


class _TwoSlot(IntEnum):
    A = 0
    B = 1


class _TwoBattlemap(Battlemap[_TwoSlot]):
    combatants: tuple[AnyActiveCombatant, AnyActiveCombatant]

    def get_combatant(self, slot: _TwoSlot) -> AnyActiveCombatant:
        match slot:
            case _TwoSlot.A:
                return self.combatants[0]
            case _TwoSlot.B:
                return self.combatants[1]

    def replace_combatant(self, slot: _TwoSlot, updated: AnyActiveCombatant) -> Self:
        match slot:
            case _TwoSlot.A:
                return self.model_copy(
                    update={"combatants": (updated, self.combatants[1])}
                )
            case _TwoSlot.B:
                return self.model_copy(
                    update={"combatants": (self.combatants[0], updated)}
                )


class _ThreeSlot(IntEnum):
    A = 0
    B = 1
    C = 2


class _ThreeBattlemap(Battlemap[_ThreeSlot]):
    combatants: tuple[AnyActiveCombatant, AnyActiveCombatant, AnyActiveCombatant]

    def get_combatant(self, slot: _ThreeSlot) -> AnyActiveCombatant:
        match slot:
            case _ThreeSlot.A:
                return self.combatants[0]
            case _ThreeSlot.B:
                return self.combatants[1]
            case _ThreeSlot.C:
                return self.combatants[2]

    def replace_combatant(self, slot: _ThreeSlot, updated: AnyActiveCombatant) -> Self:
        match slot:
            case _ThreeSlot.A:
                return self.model_copy(
                    update={
                        "combatants": (
                            updated,
                            self.combatants[1],
                            self.combatants[2],
                        )
                    }
                )
            case _ThreeSlot.B:
                return self.model_copy(
                    update={
                        "combatants": (
                            self.combatants[0],
                            updated,
                            self.combatants[2],
                        )
                    }
                )
            case _ThreeSlot.C:
                return self.model_copy(
                    update={
                        "combatants": (
                            self.combatants[0],
                            self.combatants[1],
                            updated,
                        )
                    }
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
    "health_base": 8,
    "character_data": {"name": "test"},
    "classes": {
        "wizard": 0,
        "sorcerer": 0,
        "fighter": 0,
        "barbarian": 0,
        "rogue": 1,
        "cleric": 0,
        "druid": 0,
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


def _make_fc(
    actions: list[AbilityName] | None = None, **kwargs: object
) -> FightCharacter:
    data = {**_BASE_PC_DATA, "actions": actions or []}
    pc = PresentableCharacter.model_validate(data)
    return FightCharacter.from_presentable(pc, initiative=14).model_copy(update=kwargs)


def _make_target(**kwargs: object) -> FightCharacter:
    pc = PresentableCharacter.model_validate(_BASE_PC_DATA)
    base = FightCharacter.from_presentable(pc, initiative=5).model_copy(
        update={"position": Position(x=1, y=0), "team_id": TeamId.B}
    )
    return base.model_copy(update=kwargs)


def _make_battlemap(a: AnyActiveCombatant, b: AnyActiveCombatant) -> _TwoBattlemap:
    return _TwoBattlemap(combatants=(a, b))


def _make_battlemap3(
    a: AnyActiveCombatant, b: AnyActiveCombatant, c: AnyActiveCombatant
) -> _ThreeBattlemap:
    return _ThreeBattlemap(combatants=(a, b, c))


@pytest.mark.unit
class TestFinesseWeapons:
    def test_dagger_uses_dex_when_dex_higher(self) -> None:
        stats = Stats(
            strength=10,
            dexterity=16,
            constitution=10,
            intelligence=10,
            wisdom=10,
            charisma=10,
        )
        pc = PresentableCharacter.model_validate(
            {
                **_BASE_PC_DATA,
                "stats": stats.model_dump(),
                "actions": [AbilityName.ATTACK_WITH_DAGGER],
            }
        )
        fc = FightCharacter.from_presentable(pc, initiative=14).model_copy(
            update={"main_hand": WeaponName.DAGGER}
        )
        target = _make_target()
        bm = _make_battlemap(fc, target)
        attacks = AttackWithDagger.create(_TwoSlot.A, fc, bm)
        assert len(attacks) == 1
        assert attacks[0].executor.ability_modifier == 3

    def test_dagger_uses_str_when_str_higher(self) -> None:
        stats = Stats(
            strength=16,
            dexterity=10,
            constitution=10,
            intelligence=10,
            wisdom=10,
            charisma=10,
        )
        pc = PresentableCharacter.model_validate(
            {
                **_BASE_PC_DATA,
                "stats": stats.model_dump(),
                "actions": [AbilityName.ATTACK_WITH_DAGGER],
            }
        )
        fc = FightCharacter.from_presentable(pc, initiative=14).model_copy(
            update={"main_hand": WeaponName.DAGGER}
        )
        target = _make_target()
        bm = _make_battlemap(fc, target)
        attacks = AttackWithDagger.create(_TwoSlot.A, fc, bm)
        assert len(attacks) == 1
        assert attacks[0].executor.ability_modifier == 3

    def test_stat_classmethod_returns_dexterity(self) -> None:
        assert AttackWithDagger._stat() is Statistic.DEXTERITY
        assert AttackWithRapier._stat() is Statistic.DEXTERITY
        assert AttackWithShortsword._stat() is Statistic.DEXTERITY

    def test_rapier_create_and_perform(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(melee_attack_module, "randint", lambda *a: 15)
        fc = _make_fc(
            actions=[AbilityName.ATTACK_WITH_RAPIER], main_hand=WeaponName.RAPIER
        )
        target = _make_target()
        bm = _make_battlemap(fc, target)
        attacks = AttackWithRapier.create(_TwoSlot.A, fc, bm)
        assert len(attacks) == 1
        new_bm = attacks[0].perform(bm)
        event_types = [type(e).__name__ for e in new_bm.event_log]
        assert "MeleeDamageEvent" in event_types

    def test_shortsword_create_and_perform(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(melee_attack_module, "randint", lambda *a: 15)
        fc = _make_fc(
            actions=[AbilityName.ATTACK_WITH_SHORTSWORD],
            main_hand=WeaponName.SHORTSWORD,
        )
        target = _make_target()
        bm = _make_battlemap(fc, target)
        attacks = AttackWithShortsword.create(_TwoSlot.A, fc, bm)
        assert len(attacks) == 1
        new_bm = attacks[0].perform(bm)
        event_types = [type(e).__name__ for e in new_bm.event_log]
        assert "MeleeDamageEvent" in event_types


@pytest.mark.unit
class TestRangedWeapons:
    def test_no_candidate_beyond_long_range(self) -> None:
        fc = _make_fc(
            actions=[AbilityName.ATTACK_WITH_SHORTBOW],
            main_hand=WeaponName.SHORTBOW,
            off_hand=WeaponName.SHORTBOW,
        )
        target = _make_target(position=Position(x=100, y=100))
        bm = _make_battlemap(fc, target)
        assert AttackWithShortbow.create(_TwoSlot.A, fc, bm) == ()

    def test_long_range_flag_set_beyond_normal_range(self) -> None:
        fc = _make_fc(
            actions=[AbilityName.ATTACK_WITH_SHORTBOW],
            main_hand=WeaponName.SHORTBOW,
            off_hand=WeaponName.SHORTBOW,
        )
        target = _make_target(position=Position(x=30, y=0))
        bm = _make_battlemap(fc, target)
        attacks = AttackWithShortbow.create(_TwoSlot.A, fc, bm)
        assert len(attacks) == 1
        assert attacks[0].executor.long_range is True

    def test_no_long_range_flag_within_normal_range(self) -> None:
        fc = _make_fc(
            actions=[AbilityName.ATTACK_WITH_HAND_CROSSBOW],
            main_hand=WeaponName.CROSSBOW_HAND,
        )
        target = _make_target(position=Position(x=3, y=0))
        bm = _make_battlemap(fc, target)
        attacks = AttackWithHandCrossbow.create(_TwoSlot.A, fc, bm)
        assert len(attacks) == 1
        assert attacks[0].executor.long_range is False

    def test_long_range_causes_disadvantage(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        rec = _Rec(18, 5, 3)
        monkeypatch.setattr(melee_attack_module, "randint", rec)
        fc = _make_fc(
            actions=[AbilityName.ATTACK_WITH_SHORTBOW],
            main_hand=WeaponName.SHORTBOW,
            off_hand=WeaponName.SHORTBOW,
        )
        target = _make_target(position=Position(x=30, y=0), base_ac=1)
        bm = _make_battlemap(fc, target)
        attacks = AttackWithShortbow.create(_TwoSlot.A, fc, bm)
        new_bm = attacks[0].perform(bm)
        damage_event = next(
            e for e in new_bm.event_log if isinstance(e, MeleeDamageEvent)
        )
        assert damage_event.damage == 3

    def test_normal_range_no_disadvantage(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(melee_attack_module, "randint", lambda *a: 15)
        fc = _make_fc(
            actions=[AbilityName.ATTACK_WITH_HAND_CROSSBOW],
            main_hand=WeaponName.CROSSBOW_HAND,
        )
        target = _make_target(position=Position(x=3, y=0))
        bm = _make_battlemap(fc, target)
        attacks = AttackWithHandCrossbow.create(_TwoSlot.A, fc, bm)
        new_bm = attacks[0].perform(bm)
        event_types = [type(e).__name__ for e in new_bm.event_log]
        assert "MeleeDamageEvent" in event_types


@pytest.mark.unit
class TestSneakAttack:
    def test_advantage_grants_sneak_attack_die(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        rec = _Rec(15, 18, 3, 5)
        monkeypatch.setattr(melee_attack_module, "randint", rec)
        fc = _make_fc(
            actions=[AbilityName.ATTACK_WITH_DAGGER, AbilityName.SNEAK_ATTACK],
            main_hand=WeaponName.DAGGER,
            modifiers=(RecklessAdvantageModifier(),),
        )
        target = _make_target()
        bm = _make_battlemap(fc, target)
        attacks = AttackWithDagger.create(_TwoSlot.A, fc, bm)
        new_bm = attacks[0].perform(bm)
        damage_event = next(
            e for e in new_bm.event_log if isinstance(e, MeleeDamageEvent)
        )
        assert damage_event.damage == 8
        updated_fc = new_bm.get_combatant(_TwoSlot.A)
        assert isinstance(updated_fc, FightCharacter)
        assert updated_fc.sneak_attack_used_this_turn is True

    def test_ally_adjacent_grants_sneak_attack_die(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        rec = _Rec(15, 3, 5)
        monkeypatch.setattr(melee_attack_module, "randint", rec)
        fc = _make_fc(
            actions=[AbilityName.ATTACK_WITH_DAGGER, AbilityName.SNEAK_ATTACK],
            main_hand=WeaponName.DAGGER,
            position=Position(x=0, y=0),
        )
        target = _make_target(position=Position(x=1, y=0))
        ally = _make_fc(position=Position(x=2, y=0))
        bm = _make_battlemap3(fc, target, ally)
        attacks = AttackWithDagger.create(_ThreeSlot.A, fc, bm)
        new_bm = attacks[0].perform(bm)
        damage_event = next(
            e for e in new_bm.event_log if isinstance(e, MeleeDamageEvent)
        )
        assert damage_event.damage == 8

    def test_no_advantage_no_ally_no_sneak_attack(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        rec = _Rec(15, 3)
        monkeypatch.setattr(melee_attack_module, "randint", rec)
        fc = _make_fc(
            actions=[AbilityName.ATTACK_WITH_DAGGER, AbilityName.SNEAK_ATTACK],
            main_hand=WeaponName.DAGGER,
        )
        target = _make_target()
        bm = _make_battlemap(fc, target)
        attacks = AttackWithDagger.create(_TwoSlot.A, fc, bm)
        new_bm = attacks[0].perform(bm)
        damage_event = next(
            e for e in new_bm.event_log if isinstance(e, MeleeDamageEvent)
        )
        assert damage_event.damage == 3

    def test_ally_present_but_not_adjacent_no_sneak_attack(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        rec = _Rec(15, 3)
        monkeypatch.setattr(melee_attack_module, "randint", rec)
        fc = _make_fc(
            actions=[AbilityName.ATTACK_WITH_DAGGER, AbilityName.SNEAK_ATTACK],
            main_hand=WeaponName.DAGGER,
            position=Position(x=0, y=0),
        )
        target = _make_target(position=Position(x=1, y=0))
        far_ally = _make_fc(position=Position(x=10, y=10))
        bm = _make_battlemap3(fc, target, far_ally)
        attacks = AttackWithDagger.create(_ThreeSlot.A, fc, bm)
        new_bm = attacks[0].perform(bm)
        damage_event = next(
            e for e in new_bm.event_log if isinstance(e, MeleeDamageEvent)
        )
        assert damage_event.damage == 3

    def test_enemy_adjacent_to_target_does_not_count_as_ally(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        rec = _Rec(15, 3)
        monkeypatch.setattr(melee_attack_module, "randint", rec)
        fc = _make_fc(
            actions=[AbilityName.ATTACK_WITH_DAGGER, AbilityName.SNEAK_ATTACK],
            main_hand=WeaponName.DAGGER,
            position=Position(x=0, y=0),
        )
        target = _make_target(position=Position(x=1, y=0))
        other_enemy = _make_target(position=Position(x=2, y=0))
        bm = _make_battlemap3(fc, target, other_enemy)
        attacks = AttackWithDagger.create(_ThreeSlot.A, fc, bm)
        new_bm = attacks[0].perform(bm)
        damage_event = next(
            e for e in new_bm.event_log if isinstance(e, MeleeDamageEvent)
        )
        assert damage_event.damage == 3

    def test_disadvantage_voids_ally_adjacency_path(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        rec = _Rec(18, 5, 4)
        monkeypatch.setattr(melee_attack_module, "randint", rec)
        fc = _make_fc(
            actions=[AbilityName.ATTACK_WITH_DAGGER, AbilityName.SNEAK_ATTACK],
            main_hand=WeaponName.DAGGER,
            position=Position(x=0, y=0),
        )
        target = _make_target(position=Position(x=1, y=0), base_ac=1)
        ally = _make_fc(position=Position(x=2, y=0))
        bm = _make_battlemap3(fc, target, ally)
        # Attach the ad-hoc modifier via replace_combatant (a non-revalidating
        # model_copy) rather than the battlemap constructor, since the AnyModifier
        # discriminated union can't tag an unregistered test-local modifier type.
        bm = bm.replace_combatant(
            _ThreeSlot.A,
            fc.model_copy(update={"modifiers": (_AlwaysDisadvantageModifier(),)}),
        )
        fc = bm.get_combatant(_ThreeSlot.A)
        assert isinstance(fc, FightCharacter)
        attacks = AttackWithDagger.create(_ThreeSlot.A, fc, bm)
        new_bm = attacks[0].perform(bm)
        damage_event = next(
            e for e in new_bm.event_log if isinstance(e, MeleeDamageEvent)
        )
        assert damage_event.damage == 4

    def test_once_per_turn_cap(self, monkeypatch: pytest.MonkeyPatch) -> None:
        rec = _Rec(15, 17, 3, 5, 16, 18, 4)
        monkeypatch.setattr(melee_attack_module, "randint", rec)
        fc = _make_fc(
            actions=[AbilityName.ATTACK_WITH_DAGGER, AbilityName.SNEAK_ATTACK],
            main_hand=WeaponName.DAGGER,
            modifiers=(RecklessAdvantageModifier(),),
            attacks_remaining=2,
            number_of_attacks=2,
        )
        target = _make_target(max_health=100, current_health=100)
        bm = _make_battlemap(fc, target)
        first_attacks = AttackWithDagger.create(_TwoSlot.A, fc, bm)
        bm2 = first_attacks[0].perform(bm)
        first_damage = next(e for e in bm2.event_log if isinstance(e, MeleeDamageEvent))
        assert first_damage.damage == 8

        fc2 = bm2.get_combatant(_TwoSlot.A)
        assert isinstance(fc2, FightCharacter)
        second_attacks = AttackWithDagger.create(_TwoSlot.A, fc2, bm2)
        bm3 = second_attacks[0].perform(bm2)
        damage_events = [e for e in bm3.event_log if isinstance(e, MeleeDamageEvent)]
        assert damage_events[-1].damage == 4

    def test_turn_start_resets_sneak_attack_used(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(melee_attack_module, "randint", lambda *a: 15)
        fc = _make_fc(
            actions=[AbilityName.ATTACK_WITH_DAGGER, AbilityName.SNEAK_ATTACK],
            main_hand=WeaponName.DAGGER,
            modifiers=(RecklessAdvantageModifier(),),
        )
        target = _make_target()
        bm = _make_battlemap(fc, target)
        attacks = AttackWithDagger.create(_TwoSlot.A, fc, bm)
        new_bm = attacks[0].perform(bm)
        used_fc = new_bm.get_combatant(_TwoSlot.A)
        assert isinstance(used_fc, FightCharacter)
        assert used_fc.sneak_attack_used_this_turn is True

        reset_bm = new_bm.emit(TurnStartEvent(target_id=used_fc.id))
        reset_fc = reset_bm.get_combatant(_TwoSlot.A)
        assert isinstance(reset_fc, FightCharacter)
        assert reset_fc.sneak_attack_used_this_turn is False

    def test_crit_doubles_sneak_attack_dice(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        rec = _Rec(20, 20, 3, 4, 6)
        monkeypatch.setattr(melee_attack_module, "randint", rec)
        fc = _make_fc(
            actions=[AbilityName.ATTACK_WITH_DAGGER, AbilityName.SNEAK_ATTACK],
            main_hand=WeaponName.DAGGER,
            modifiers=(RecklessAdvantageModifier(),),
        )
        target = _make_target()
        bm = _make_battlemap(fc, target)
        attacks = AttackWithDagger.create(_TwoSlot.A, fc, bm)
        new_bm = attacks[0].perform(bm)
        damage_event = next(
            e for e in new_bm.event_log if isinstance(e, MeleeDamageEvent)
        )
        assert damage_event.damage == 13

    def test_non_finesse_weapon_never_sneak_attacks(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        rec = _Rec(15, 18, 4)
        monkeypatch.setattr(melee_attack_module, "randint", rec)
        fc = _make_fc(
            actions=[AbilityName.ATTACK_WITH_AXE, AbilityName.SNEAK_ATTACK],
            main_hand=WeaponName.BATTLEAXE,
            modifiers=(RecklessAdvantageModifier(),),
        )
        target = _make_target()
        bm = _make_battlemap(fc, target)
        attacks = AttackWithAxe.create(_TwoSlot.A, fc, bm)
        new_bm = attacks[0].perform(bm)
        damage_event = next(
            e for e in new_bm.event_log if isinstance(e, MeleeDamageEvent)
        )
        assert damage_event.damage == 4


@pytest.mark.unit
class TestDash:
    def test_create_returns_none_without_cunning_action(self) -> None:
        fc = _make_fc()
        bm = _make_battlemap(fc, _make_target())
        assert Dash.create(_TwoSlot.A, fc, bm) == ()

    def test_create_returns_none_without_bonus_action(self) -> None:
        fc = _make_fc(actions=[AbilityName.CUNNING_ACTION], has_bonus_action=False)
        bm = _make_battlemap(fc, _make_target())
        assert Dash.create(_TwoSlot.A, fc, bm) == ()

    def test_perform_increases_movement_and_spends_bonus_action(self) -> None:
        fc = _make_fc(actions=[AbilityName.CUNNING_ACTION], movement_remaining=10)
        bm = _make_battlemap(fc, _make_target())
        dashes = Dash.create(_TwoSlot.A, fc, bm)
        assert len(dashes) == 1
        new_bm = dashes[0].perform(bm)
        updated_fc = new_bm.get_combatant(_TwoSlot.A)
        assert isinstance(updated_fc, FightCharacter)
        assert updated_fc.movement_remaining == 10 + fc.speed
        assert updated_fc.has_bonus_action is False

    def test_perform_returns_unchanged_when_actor_not_fight_character(self) -> None:
        downed = DownedFightCharacter.from_active(_make_fc())
        bm = _make_battlemap(downed, _make_target())
        action = Dash(actor_slot=_TwoSlot.A)
        assert action.perform(bm) is bm


@pytest.mark.unit
class TestDisengage:
    def test_create_returns_none_without_cunning_action(self) -> None:
        fc = _make_fc()
        bm = _make_battlemap(fc, _make_target())
        assert Disengage.create(_TwoSlot.A, fc, bm) == ()

    def test_perform_sets_disengaging_and_spends_bonus_action(self) -> None:
        fc = _make_fc(actions=[AbilityName.CUNNING_ACTION])
        bm = _make_battlemap(fc, _make_target())
        disengages = Disengage.create(_TwoSlot.A, fc, bm)
        assert len(disengages) == 1
        new_bm = disengages[0].perform(bm)
        updated_fc = new_bm.get_combatant(_TwoSlot.A)
        assert isinstance(updated_fc, FightCharacter)
        assert updated_fc.disengaging is True
        assert updated_fc.has_bonus_action is False

    def test_perform_returns_unchanged_when_actor_not_fight_character(self) -> None:
        downed = DownedFightCharacter.from_active(_make_fc())
        bm = _make_battlemap(downed, _make_target())
        action = Disengage(actor_slot=_TwoSlot.A)
        assert action.perform(bm) is bm


@pytest.mark.unit
class TestMoveDisengaging:
    def test_disengaging_prevents_opportunity_attack(self) -> None:
        mover = _make_fc(
            position=Position(x=0, y=0),
            team_id=TeamId.A,
            movement_remaining=30,
            disengaging=True,
        )
        enemy = _make_fc(
            position=Position(x=1, y=0), team_id=TeamId.B, has_reaction=True
        )
        bm = _make_battlemap(mover, enemy)
        moves = Move.create(_TwoSlot.A, mover, bm)
        far_moves = [m for m in moves if max(abs(m.to.x - 1), abs(m.to.y)) > 1]
        assert far_moves
        assert all(m.triggered_oa_from == () for m in far_moves)

    def test_non_disengaging_mover_triggers_opportunity_attack(self) -> None:
        mover = _make_fc(
            position=Position(x=0, y=0),
            team_id=TeamId.A,
            movement_remaining=30,
            disengaging=False,
        )
        enemy = _make_fc(
            position=Position(x=1, y=0), team_id=TeamId.B, has_reaction=True
        )
        bm = _make_battlemap(mover, enemy)
        moves = Move.create(_TwoSlot.A, mover, bm)
        far_moves = [m for m in moves if max(abs(m.to.x - 1), abs(m.to.y)) > 1]
        assert far_moves
        assert any(m.triggered_oa_from == (_TwoSlot.B,) for m in far_moves)
