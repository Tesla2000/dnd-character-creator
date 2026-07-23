import sys
from enum import IntEnum
from typing import Self

from dnd._position import Position
from dnd.character._ability_name import AbilityName
from dnd.character.blueprint.building_blocks.level_up.barbarian.berserker.level_3 import (
    BarbarianLevel3Berserker,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.level_1 import (
    BarbarianLevel1,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.level_2 import (
    BarbarianLevel2,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.level_4 import (
    BarbarianLevel4,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.level_5 import (
    BarbarianLevel5,
)
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
from dnd.character.blueprint.character_data import CharacterData
from dnd.character.blueprint.states._caster_info import CasterInfo
from dnd.character.blueprint.states.state import Blueprint
from dnd.character.presentable_character import PresentableCharacter
from dnd.character.race.race import Race
from dnd.character.stats import Stats
from dnd.choices.equipment_creation.weapons import WeaponName
from dnd.fight._team_id import TeamId
from dnd.fight.battlemap import Battlemap
from dnd.fight.fight_character import (
    AnyActiveCombatant,
    FightCharacter,
    SpellcasterFightCharacter,
)
from dnd.fight.simulator import ActionCapExceededError, RoundCapExceededError, Simulator
from dnd.fight.strategy import AggressiveStrategy


class _TwoFighterSlot(IntEnum):
    A = 0
    B = 1


class _TwoFighterBattlemap(Battlemap[_TwoFighterSlot]):
    combatants: tuple[AnyActiveCombatant, AnyActiveCombatant]

    def get_combatant(self, slot: _TwoFighterSlot) -> AnyActiveCombatant:
        match slot:
            case _TwoFighterSlot.A:
                return self.combatants[0]
            case _TwoFighterSlot.B:
                return self.combatants[1]

    def replace_combatant(
        self, slot: _TwoFighterSlot, updated: AnyActiveCombatant
    ) -> Self:
        match slot:
            case _TwoFighterSlot.A:
                return self.model_copy(
                    update={"combatants": (updated, self.combatants[1])}
                )
            case _TwoFighterSlot.B:
                return self.model_copy(
                    update={"combatants": (self.combatants[0], updated)}
                )


_STATS = Stats(
    strength=17,
    dexterity=13,
    constitution=16,
    intelligence=9,
    wisdom=11,
    charisma=8,
)

_SORC_STATS = Stats(
    strength=8,
    dexterity=14,
    constitution=14,
    intelligence=10,
    wisdom=10,
    charisma=17,
)

_SORCERER_SPELL_ACTIONS = (
    AbilityName.CHROMATIC_ORB,
    AbilityName.MAGIC_MISSILE,
    AbilityName.SCORCHING_RAY,
    AbilityName.FIREBALL,
    AbilityName.LIGHTNING_BOLT,
    AbilityName.ICE_STORM,
)


def _make_barbarian(name: str, initiative: int, team_id: TeamId) -> FightCharacter:
    bp = Blueprint(race=Race.HUMAN, stats=_STATS)
    bp = BarbarianLevel1().apply(bp)
    bp = BarbarianLevel2().apply(bp)
    bp = BarbarianLevel3Berserker().apply(bp)
    bp = BarbarianLevel4().apply(bp)
    bp = BarbarianLevel5().apply(bp)
    bp = bp.model_copy(
        update={
            "character_data": CharacterData(name=name),
            "weapons": (WeaponName.BATTLEAXE,),
            "actions": bp.actions + (AbilityName.ATTACK_WITH_BATTLEAXE,),
        }
    )
    pc = PresentableCharacter.model_validate(bp.model_dump())
    return FightCharacter.from_presentable(
        pc, initiative=initiative, team_id=team_id
    ).model_copy(
        update={
            "position": Position(x=0, y=0)
            if team_id == TeamId.A
            else Position(x=1, y=0)
        }
    )


def _make_sorcerer(
    name: str, initiative: int, team_id: TeamId
) -> SpellcasterFightCharacter:
    health = D6HealthIncreaseAverage()
    spells = SorcererRandomSpellAssigner()
    bp = Blueprint(race=Race.HUMAN, stats=_SORC_STATS, health_base=6)
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
            "position": Position(x=0, y=0)
            if team_id == TeamId.A
            else Position(x=1, y=0)
        }
    )


def main() -> None:
    fc_a = _make_barbarian("Grog", initiative=15, team_id=TeamId.A)
    fc_b = _make_sorcerer("Zog", initiative=12, team_id=TeamId.B)
    battlemap = _TwoFighterBattlemap(combatants=(fc_a, fc_b))
    strategy = AggressiveStrategy()
    result = Simulator(battlemap, strategy_a=strategy, strategy_b=strategy).run()
    if isinstance(result, (RoundCapExceededError, ActionCapExceededError)):
        raise result
    for line in result.log:
        sys.stdout.write(line + "\n")
    winner = f"Team {result.winner.name}" if result.winner is not None else "Draw"
    sys.stdout.write(f"{winner} wins in {result.rounds} rounds.\n")


if __name__ == "__main__":  # pragma: no cover
    main()
