from enum import IntEnum
from typing import Self

import pytest

from dnd._position import Position
from dnd.character.presentable_character import PresentableCharacter
from dnd.character.stats import Stats
from dnd.fight._team_id import TeamId
from dnd.fight.aspect import AoeVulnerabilityAspect, EnemyClusterAspect
from dnd.fight.battlemap import Battlemap
from dnd.fight.fight_character import (
    AnyActiveCombatant,
    DeadFightCharacter,
    FightCharacter,
)

_STATS = Stats(
    strength=17,
    dexterity=13,
    constitution=16,
    intelligence=9,
    wisdom=11,
    charisma=8,
)

_PC_DATA: dict[str, object] = {
    "race": "Human",
    "stats": _STATS.model_dump(),
    "health_base": 20,
    "character_data": {"name": ""},
    "classes": {
        "wizard": 0,
        "sorcerer": 0,
        "fighter": 0,
        "barbarian": 1,
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
    "speed": 30,
    "dark_vision_range": 0,
    "saving_throw_proficiencies": [],
    "other_active_abilities": [],
    "weapons": [],
    "actions": [],
}


class _ThreeSlot(IntEnum):
    A0 = 0
    A1 = 1
    B0 = 2


class _ThreeFightBattlemap(Battlemap[_ThreeSlot]):
    combatants: tuple[AnyActiveCombatant, AnyActiveCombatant, AnyActiveCombatant]

    def get_combatant(self, slot: _ThreeSlot) -> AnyActiveCombatant:
        match slot:
            case _ThreeSlot.A0:
                return self.combatants[0]
            case _ThreeSlot.A1:
                return self.combatants[1]
            case _ThreeSlot.B0:
                return self.combatants[2]

    def replace_combatant(self, slot: _ThreeSlot, updated: AnyActiveCombatant) -> Self:
        match slot:
            case _ThreeSlot.A0:
                return self.model_copy(
                    update={
                        "combatants": (
                            updated,
                            self.combatants[1],
                            self.combatants[2],
                        )
                    }
                )
            case _ThreeSlot.A1:
                return self.model_copy(
                    update={
                        "combatants": (
                            self.combatants[0],
                            updated,
                            self.combatants[2],
                        )
                    }
                )
            case _ThreeSlot.B0:
                return self.model_copy(
                    update={
                        "combatants": (
                            self.combatants[0],
                            self.combatants[1],
                            updated,
                        )
                    }
                )


def _make_fc(name: str, team_id: TeamId, position: Position) -> FightCharacter:
    data = {**_PC_DATA, "character_data": {"name": name}}
    pc = PresentableCharacter.model_validate(data)
    return FightCharacter.from_presentable(
        pc, initiative=10, team_id=team_id
    ).model_copy(update={"position": position})


@pytest.mark.unit
class TestAoeVulnerabilityAspect:
    def test_penalizes_clustered_allies_more_than_spread_allies(self) -> None:
        b0 = _make_fc("B0", TeamId.B, Position(x=20, y=20))

        clustered = _ThreeFightBattlemap(
            combatants=(
                _make_fc("A0", TeamId.A, Position(x=0, y=0)),
                _make_fc("A1", TeamId.A, Position(x=1, y=0)),
                b0,
            )
        )
        spread = _ThreeFightBattlemap(
            combatants=(
                _make_fc("A0", TeamId.A, Position(x=0, y=0)),
                _make_fc("A1", TeamId.A, Position(x=10, y=10)),
                b0,
            )
        )

        aspect: AoeVulnerabilityAspect[_ThreeSlot] = AoeVulnerabilityAspect()
        clustered_value = aspect.value(clustered, clustered, _ThreeSlot.A0)
        spread_value = aspect.value(spread, spread, _ThreeSlot.A0)

        assert clustered_value == -2.0
        assert spread_value == -1.0
        assert clustered_value < spread_value

    def test_returns_zero_when_actor_slot_is_not_a_fight_character(self) -> None:
        a0 = _make_fc("A0", TeamId.A, Position(x=0, y=0))
        a1 = _make_fc("A1", TeamId.A, Position(x=1, y=0))
        dead_b0 = DeadFightCharacter(
            character=a0.character,
            initiative=10,
            max_health=20,
            current_health=0,
            team_id=TeamId.B,
            speed=30,
            position=Position(x=20, y=20),
        )
        bm = _ThreeFightBattlemap(combatants=(a0, a1, dead_b0))

        aspect: AoeVulnerabilityAspect[_ThreeSlot] = AoeVulnerabilityAspect()
        assert aspect.value(bm, bm, _ThreeSlot.B0) == 0.0


@pytest.mark.unit
class TestEnemyClusterAspect:
    def test_counts_enemies_whose_health_decreased(self) -> None:
        a0 = _make_fc("A0", TeamId.A, Position(x=0, y=0))
        a1 = _make_fc("A1", TeamId.A, Position(x=1, y=0))
        b0 = _make_fc("B0", TeamId.B, Position(x=20, y=20))
        before = _ThreeFightBattlemap(combatants=(a0, a1, b0))

        aspect: EnemyClusterAspect[_ThreeSlot] = EnemyClusterAspect()

        no_change = before
        assert aspect.value(before, no_change, _ThreeSlot.B0) == 0.0

        one_hit = before.replace_combatant(
            _ThreeSlot.A0, a0.model_copy(update={"current_health": 15})
        )
        assert aspect.value(before, one_hit, _ThreeSlot.B0) == 1.0

        both_hit = one_hit.replace_combatant(
            _ThreeSlot.A1, a1.model_copy(update={"current_health": 10})
        )
        assert aspect.value(before, both_hit, _ThreeSlot.B0) == 2.0

    def test_returns_zero_when_actor_slot_is_not_a_fight_character(self) -> None:
        a0 = _make_fc("A0", TeamId.A, Position(x=0, y=0))
        a1 = _make_fc("A1", TeamId.A, Position(x=1, y=0))
        dead_b0 = DeadFightCharacter(
            character=a0.character,
            initiative=10,
            max_health=20,
            current_health=0,
            team_id=TeamId.B,
            speed=30,
            position=Position(x=20, y=20),
        )
        bm = _ThreeFightBattlemap(combatants=(a0, a1, dead_b0))

        aspect: EnemyClusterAspect[_ThreeSlot] = EnemyClusterAspect()
        assert aspect.value(bm, bm, _ThreeSlot.B0) == 0.0
