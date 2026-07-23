import sys
from enum import IntEnum
from typing import Self

from dnd._position import Position
from dnd.character._ability_name import AbilityName
from dnd.character.blueprint.building_blocks.level_up.health_increase import (
    D6HealthIncreaseAverage,
)
from dnd.character.blueprint.building_blocks.level_up.sorcerer.level_2 import (
    SorcererLevel2,
)
from dnd.character.blueprint.building_blocks.level_up.sorcerer.level_3 import (
    SorcererLevel3,
)
from dnd.character.blueprint.building_blocks.level_up.sorcerer.level_4 import (
    SorcererLevel4,
)
from dnd.character.blueprint.building_blocks.level_up.sorcerer.level_5 import (
    SorcererLevel5,
)
from dnd.character.blueprint.building_blocks.level_up.sorcerer.level_7 import (
    SorcererLevel7,
)
from dnd.character.blueprint.building_blocks.level_up.sorcerer.wild_magic.level_1 import (
    SorcererLevel1WildMagic,
)
from dnd.character.blueprint.building_blocks.level_up.sorcerer.wild_magic.level_6 import (
    SorcererLevel6WildMagic,
)
from dnd.character.blueprint.building_blocks.level_up.spell_assignment import (
    SorcererRandomSpellAssigner,
)
from dnd.character.actions._damage_type import DamageType
from dnd.character.blueprint.character_data import CharacterData
from dnd.character.blueprint.states._caster_info import CasterInfo
from dnd.character.blueprint.states.state import Blueprint
from dnd.character.health_modifier import AmuletOfHealthModifier
from dnd.character.presentable_character import PresentableCharacter
from dnd.character.race.race import Race
from dnd.character.stats import Stats
from dnd.fight._team_id import TeamId
from dnd.fight.aspect import AoeVulnerabilityAspect, EnemyClusterAspect
from dnd.fight.battlemap import Battlemap
from dnd.fight.fight_character import AnyActiveCombatant, SpellcasterFightCharacter
from dnd.fight.simulator import ActionCapExceededError, RoundCapExceededError, Simulator
from dnd.fight.strategy import CompositeStrategy


class _FourSlot(IntEnum):
    A0 = 0
    A1 = 1
    B0 = 2
    B1 = 3


class _FourFightBattlemap(Battlemap[_FourSlot]):
    combatants: tuple[
        AnyActiveCombatant, AnyActiveCombatant, AnyActiveCombatant, AnyActiveCombatant
    ]

    def get_combatant(self, slot: _FourSlot) -> AnyActiveCombatant:
        match slot:
            case _FourSlot.A0:
                return self.combatants[0]
            case _FourSlot.A1:
                return self.combatants[1]
            case _FourSlot.B0:
                return self.combatants[2]
            case _FourSlot.B1:
                return self.combatants[3]

    def replace_combatant(self, slot: _FourSlot, updated: AnyActiveCombatant) -> Self:
        match slot:
            case _FourSlot.A0:
                return self.model_copy(
                    update={
                        "combatants": (
                            updated,
                            self.combatants[1],
                            self.combatants[2],
                            self.combatants[3],
                        )
                    }
                )
            case _FourSlot.A1:
                return self.model_copy(
                    update={
                        "combatants": (
                            self.combatants[0],
                            updated,
                            self.combatants[2],
                            self.combatants[3],
                        )
                    }
                )
            case _FourSlot.B0:
                return self.model_copy(
                    update={
                        "combatants": (
                            self.combatants[0],
                            self.combatants[1],
                            updated,
                            self.combatants[3],
                        )
                    }
                )
            case _FourSlot.B1:
                return self.model_copy(
                    update={
                        "combatants": (
                            self.combatants[0],
                            self.combatants[1],
                            self.combatants[2],
                            updated,
                        )
                    }
                )


_SORC_STATS = Stats(
    strength=8,
    dexterity=14,
    constitution=14,
    intelligence=10,
    wisdom=10,
    charisma=17,
)

_SORCERER_SPELL_ACTIONS = (AbilityName.FIREBALL, AbilityName.FIRE_BOLT)


def _make_sorcerer(
    name: str, initiative: int, team_id: TeamId, position: Position
) -> SpellcasterFightCharacter:
    health = D6HealthIncreaseAverage()
    spells = SorcererRandomSpellAssigner()
    bp = Blueprint(
        race=Race.HUMAN,
        stats=_SORC_STATS,
        health_base=6,
        health_modifiers=(AmuletOfHealthModifier(),),
    )
    bp = SorcererLevel1WildMagic(health_increase=health, spell_assigner=spells).apply(bp)
    bp = SorcererLevel2(health_increase=health, spell_assigner=spells).apply(bp)
    bp = SorcererLevel3(health_increase=health, spell_assigner=spells).apply(bp)
    bp = SorcererLevel4(health_increase=health, spell_assigner=spells).apply(bp)
    bp = SorcererLevel5(health_increase=health, spell_assigner=spells).apply(bp)
    bp = SorcererLevel6WildMagic(health_increase=health, spell_assigner=spells).apply(bp)
    bp = SorcererLevel7(health_increase=health, spell_assigner=spells).apply(bp)
    bp = bp.model_copy(
        update={
            "character_data": CharacterData(name=name),
            "actions": bp.actions + _SORCERER_SPELL_ACTIONS,
            "caster": CasterInfo(
                spell_slots=bp.spell_slots, caster_level=bp.caster_level
            ),
        }
    )
    pc = PresentableCharacter.model_validate(bp.model_dump())
    return SpellcasterFightCharacter.from_presentable(
        pc, initiative=initiative, team_id=team_id
    ).model_copy(
        update={
            "position": position,
            "damage_resistance": frozenset({DamageType.FIRE}),
        }
    )


def main() -> None:
    fc_a0 = _make_sorcerer("Aria", initiative=18, team_id=TeamId.A, position=Position(x=0, y=0))
    fc_a1 = _make_sorcerer("Aria2", initiative=16, team_id=TeamId.A, position=Position(x=1, y=0))
    fc_b0 = _make_sorcerer("Boris", initiative=14, team_id=TeamId.B, position=Position(x=10, y=0))
    fc_b1 = _make_sorcerer("Boris2", initiative=12, team_id=TeamId.B, position=Position(x=11, y=0))

    battlemap = _FourFightBattlemap(combatants=(fc_a0, fc_a1, fc_b0, fc_b1))
    strategy_a: CompositeStrategy[_FourSlot] = CompositeStrategy(
        aspects=(EnemyClusterAspect(),)
    )
    strategy_b: CompositeStrategy[_FourSlot] = CompositeStrategy(
        aspects=(EnemyClusterAspect(), AoeVulnerabilityAspect())
    )
    result = Simulator(
        battlemap, strategy_a=strategy_a, strategy_b=strategy_b, max_rounds=100
    ).run()
    if isinstance(result, (ActionCapExceededError, RoundCapExceededError)):
        raise result
    for line in result.log:
        sys.stdout.write(line + "\n")
    winner = f"Team {result.winner.name}" if result.winner is not None else "Draw"
    sys.stdout.write(f"{winner} wins in {result.rounds} rounds.\n")


if __name__ == "__main__":  # pragma: no cover
    main()
