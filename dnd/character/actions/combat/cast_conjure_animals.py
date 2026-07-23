from __future__ import annotations

from typing import TYPE_CHECKING, Generic, Literal, Self

from dnd.character._ability_name import AbilityName
from dnd.character.actions._base_action import Action
from dnd.character.actions.combat._wild_shape_forms import _WOLF
from dnd.character.presentable_character import PresentableCharacter
from dnd.character.race.race import Race
from dnd.choices.stats_creation.statistic import Statistic
from dnd.fight._combatant_slot import SlotT
from dnd.fight._condition import Condition
from dnd.fight._team_id import TeamId
from dnd.fight.fight_character import (
    FightCharacter,
    SpellcasterFightCharacter,
    UnsummonedFightCharacter,
)

if TYPE_CHECKING:
    from dnd.fight.battlemap import Battlemap

_N_WOLVES = 4

_WOLF_CLASSES: dict[str, int] = {
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
}


class CastConjureAnimals(Action[SlotT], Generic[SlotT]):
    name: Literal[AbilityName.CONJURE_ANIMALS] = AbilityName.CONJURE_ANIMALS
    range_tails: Literal[0] = 0
    actor_slot: SlotT

    @staticmethod
    def _make_wolf_presentable() -> PresentableCharacter:
        return PresentableCharacter.model_validate(
            {
                "race": Race.HUMAN,
                "stats": _WOLF.stats.model_dump(),
                "health_base": _WOLF.hp,
                "character_data": {"name": "Wolf"},
                "classes": _WOLF_CLASSES,
                "speed": _WOLF.speed,
                "dark_vision_range": 0,
                "saving_throw_proficiencies": [],
                "other_active_abilities": [],
                "actions": [AbilityName.BEAST_ATTACK],
            }
        )

    @staticmethod
    def _reserved_slots(
        team_id: TeamId, battlemap: Battlemap[SlotT]
    ) -> list[SlotT]:
        return [
            slot
            for slot in battlemap.all_slots()
            if isinstance(
                combatant := battlemap.get_combatant(slot), UnsummonedFightCharacter
            )
            and combatant.team_id == team_id
        ]

    @classmethod
    def create(
        cls,
        actor_slot: SlotT,
        fighter: FightCharacter[SlotT],
        battlemap: Battlemap[SlotT],
    ) -> tuple[CastConjureAnimals[SlotT], ...]:
        if not isinstance(fighter, SpellcasterFightCharacter):
            return ()
        if not fighter.has_action:
            return ()
        if fighter.remaining_spell_slots.level_3 == 0:
            return ()
        if AbilityName.CONJURE_ANIMALS not in fighter.character.actions:
            return ()
        if len(cls._reserved_slots(fighter.team_id, battlemap)) < _N_WOLVES:
            return ()
        return (cls(actor_slot=actor_slot),)

    def perform(self, battlemap: Battlemap[SlotT]) -> Battlemap[SlotT]:
        match battlemap.get_combatant(self.actor_slot):
            case SpellcasterFightCharacter() as fighter:
                pass
            case _:
                return battlemap
        battlemap = battlemap.replace_combatant(
            self.actor_slot,
            fighter.spend_action()
            .spend_level_3_slot()
            .add_condition(Condition.CONCENTRATION),
        )
        dex_modifier = _WOLF.stats.get_modifier(Statistic.DEXTERITY)
        base_ac = 10 + dex_modifier + _WOLF.ac_bonus
        wolf_presentable = self._make_wolf_presentable()
        slots = self._reserved_slots(fighter.team_id, battlemap)[:_N_WOLVES]
        for slot in slots:
            reserved = battlemap.get_combatant(slot)
            wolf: FightCharacter[SlotT] = FightCharacter(
                character=wolf_presentable,
                initiative=reserved.initiative,
                max_health=_WOLF.hp,
                current_health=_WOLF.hp,
                base_ac=base_ac,
                team_id=reserved.team_id,
                speed=_WOLF.speed,
                position=reserved.position,
                active_features=frozenset({AbilityName.ATTACK_WITH_WOLF_BITE}),
                summoned_by=self.actor_slot,
                has_action=False,
                has_bonus_action=False,
                has_reaction=False,
                attacks_remaining=0,
            )
            battlemap = battlemap.replace_combatant(slot, wolf)
        return battlemap
