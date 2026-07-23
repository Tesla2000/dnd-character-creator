from __future__ import annotations

from typing import TYPE_CHECKING, Generic, Literal

from dnd.character._ability_name import AbilityName
from dnd.character.actions._base_action import BonusAction
from dnd.fight._combatant_slot import SlotT
from dnd.fight.fight_character import FightCharacter

if TYPE_CHECKING:
    from dnd.fight.battlemap import Battlemap


class RevertWildShape(BonusAction[SlotT], Generic[SlotT]):
    name: Literal[AbilityName.WILD_SHAPE] = AbilityName.WILD_SHAPE
    range_tails: Literal[0] = 0
    radius_tails: Literal[0] = 0
    actor_slot: SlotT

    @classmethod
    def create(
        cls,
        actor_slot: SlotT,
        fighter: FightCharacter[SlotT],
        battlemap: Battlemap[SlotT],
    ) -> tuple[RevertWildShape[SlotT], ...]:
        if not (
            fighter.has_bonus_action
            and AbilityName.WILD_SHAPE in fighter.active_features
        ):
            return ()
        return (cls(actor_slot=actor_slot),)

    def perform(self, battlemap: Battlemap[SlotT]) -> Battlemap[SlotT]:
        match battlemap.get_combatant(self.actor_slot):
            case FightCharacter() as fighter:
                pass
            case _:
                return battlemap
        updated = fighter.model_copy(
            update={
                "has_bonus_action": False,
                "active_features": fighter.active_features
                - {
                    AbilityName.WILD_SHAPE,
                    AbilityName.ATTACK_WITH_BROWN_BEAR_CLAW,
                    AbilityName.ATTACK_WITH_POLAR_BEAR_CLAW,
                },
                "temporary_health": 0,
            }
        )
        return battlemap.replace_combatant(self.actor_slot, updated)
