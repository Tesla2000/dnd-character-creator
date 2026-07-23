from __future__ import annotations

from enum import IntEnum
from typing import Self

import pytest

from dnd._position import Position
from dnd.character._ability_name import AbilityName
from dnd.character.actions.combat import AnyCombatAction
from dnd.character.actions.combat.dash import Dash
from dnd.character.actions.combat.disengage import Disengage
from dnd.character.actions.combat.move import Move
from dnd.character.presentable_character import PresentableCharacter
from dnd.character.stats import Stats
from dnd.choices.equipment_creation.weapons import WeaponName
from dnd.fight._team_id import TeamId
from dnd.fight.battlemap import Battlemap
from dnd.fight.fight_character import AnyActiveCombatant, FightCharacter
from dnd.fight.simulator import Simulator

_STATS = Stats(
    strength=10,
    dexterity=10,
    constitution=10,
    intelligence=10,
    wisdom=10,
    charisma=10,
)


class _Slot(IntEnum):
    A = 0
    B = 1


class _TwoBattlemap(Battlemap[_Slot]):
    combatants: tuple[AnyActiveCombatant, AnyActiveCombatant]

    def get_combatant(self, slot: _Slot) -> AnyActiveCombatant:
        if slot is _Slot.A:
            return self.combatants[0]
        return self.combatants[1]

    def replace_combatant(self, slot: _Slot, updated: AnyActiveCombatant) -> Self:
        if slot is _Slot.A:
            return self.model_copy(update={"combatants": (updated, self.combatants[1])})
        return self.model_copy(update={"combatants": (self.combatants[0], updated)})


class _DashThenFarthestMoveStrategy:
    """Always Dash first if available, then the farthest reachable Move, else Pass."""

    def choose(
        self,
        candidates: tuple[AnyCombatAction[_Slot], ...],
        battlemap: Battlemap[_Slot],
        actor_slot: _Slot,
    ) -> AnyCombatAction[_Slot]:
        dashes = [c for c in candidates if isinstance(c, Dash)]
        if dashes:
            return dashes[0]
        moves = [c for c in candidates if isinstance(c, Move)]
        if moves:
            return max(moves, key=lambda m: m.movement_cost)
        return candidates[0]


class _DisengageThenFarthestMoveStrategy:
    """Always Disengage first if available, then the farthest reachable Move, else Pass."""

    def choose(
        self,
        candidates: tuple[AnyCombatAction[_Slot], ...],
        battlemap: Battlemap[_Slot],
        actor_slot: _Slot,
    ) -> AnyCombatAction[_Slot]:
        disengages = [c for c in candidates if isinstance(c, Disengage)]
        if disengages:
            return disengages[0]
        moves = [c for c in candidates if isinstance(c, Move)]
        if moves:
            return max(moves, key=lambda m: m.movement_cost)
        return candidates[0]


class _AlwaysAttackStrategy:
    def choose(
        self,
        candidates: tuple[AnyCombatAction[_Slot], ...],
        battlemap: Battlemap[_Slot],
        actor_slot: _Slot,
    ) -> AnyCombatAction[_Slot]:
        return candidates[0]


def _make_rogue(position: Position, speed: int) -> FightCharacter:
    pc = PresentableCharacter.model_validate(
        {
            "race": "Human",
            "stats": _STATS.model_dump(),
            "health_base": 30,
            "character_data": {"name": "Rogue"},
            "classes": {
                "wizard": 0,
                "sorcerer": 0,
                "fighter": 0,
                "barbarian": 0,
                "rogue": 2,
                "cleric": 0,
                "druid": 0,
                "paladin": 0,
                "ranger": 0,
                "monk": 0,
                "bard": 0,
                "warlock": 0,
                "artificer": 0,
            },
            "speed": speed,
            "dark_vision_range": 0,
            "saving_throw_proficiencies": [],
            "other_active_abilities": [],
            "actions": [AbilityName.CUNNING_ACTION],
        }
    )
    return FightCharacter.from_presentable(
        pc, initiative=20, team_id=TeamId.A
    ).model_copy(update={"position": position})


def _make_enemy_with_axe(position: Position) -> FightCharacter:
    pc = PresentableCharacter.model_validate(
        {
            "race": "Human",
            "stats": _STATS.model_dump(),
            "health_base": 30,
            "character_data": {"name": "Enemy"},
            "classes": {
                "wizard": 0,
                "sorcerer": 0,
                "fighter": 0,
                "barbarian": 0,
                "rogue": 0,
                "cleric": 0,
                "druid": 0,
                "paladin": 0,
                "ranger": 0,
                "monk": 0,
                "bard": 0,
                "warlock": 0,
                "artificer": 0,
            },
            "speed": 5,
            "dark_vision_range": 0,
            "saving_throw_proficiencies": [],
            "other_active_abilities": [],
            "actions": [AbilityName.ATTACK_WITH_AXE],
            "weapons": [WeaponName.BATTLEAXE],
        }
    )
    return FightCharacter.from_presentable(
        pc, initiative=5, team_id=TeamId.B
    ).model_copy(update={"position": position})


@pytest.mark.unit
class TestTurnLoopMerge:
    def test_dash_extra_movement_is_usable_same_turn(self) -> None:
        rogue = _make_rogue(position=Position(x=0, y=0), speed=15)
        enemy = _make_enemy_with_axe(position=Position(x=50, y=50))
        battlemap = _TwoBattlemap(combatants=(rogue, enemy))
        strategy_a = _DashThenFarthestMoveStrategy()
        strategy_b = _AlwaysAttackStrategy()
        # Neither side can ever eliminate the other in this scenario (Rogue
        # has no attack, enemy is out of reach) -- both SimResult and
        # RoundCapExceededError carry final_battlemap, so a small round cap
        # is enough to inspect round 1's outcome without either result type.
        result = Simulator(
            battlemap, strategy_a=strategy_a, strategy_b=strategy_b, max_rounds=2
        ).run()
        final_rogue = result.final_battlemap.get_combatant(_Slot.A)
        assert isinstance(final_rogue, FightCharacter)
        distance = max(abs(final_rogue.position.x), abs(final_rogue.position.y))
        assert distance > 3

    def test_disengage_prevents_opportunity_attack_same_turn(self) -> None:
        rogue = _make_rogue(position=Position(x=0, y=0), speed=30)
        enemy = _make_enemy_with_axe(position=Position(x=1, y=0))
        battlemap = _TwoBattlemap(combatants=(rogue, enemy))
        strategy_a = _DisengageThenFarthestMoveStrategy()
        strategy_b = _AlwaysAttackStrategy()
        result = Simulator(
            battlemap, strategy_a=strategy_a, strategy_b=strategy_b, max_rounds=2
        ).run()
        final_rogue = result.final_battlemap.get_combatant(_Slot.A)
        assert isinstance(final_rogue, FightCharacter)
        assert final_rogue.current_health == final_rogue.max_health
