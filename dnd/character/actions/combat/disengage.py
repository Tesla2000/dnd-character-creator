from __future__ import annotations

from typing import TYPE_CHECKING, Generic, Literal

from dnd.character._ability_name import AbilityName
from dnd.character.actions._base_action import BonusAction
from dnd.fight._combatant_slot import SlotT
from dnd.fight.fight_character import FightCharacter

if TYPE_CHECKING:
    from dnd.fight.battlemap import Battlemap


class Disengage(BonusAction[SlotT], Generic[SlotT]):
    name: Literal[AbilityName.DISENGAGE] = AbilityName.DISENGAGE
    range_tails: Literal[0] = 0
    actor_slot: SlotT

    @classmethod
    def create(
        cls,
        actor_slot: SlotT,
        fighter: FightCharacter[SlotT],
        battlemap: Battlemap[SlotT],
    ) -> tuple[Disengage[SlotT], ...]:
        if not (
            fighter.has_bonus_action
            and AbilityName.CUNNING_ACTION in fighter.character.actions
        ):
            return ()
        return (cls(actor_slot=actor_slot),)

    def perform(self, battlemap: Battlemap[SlotT]) -> Battlemap[SlotT]:
        fighter = battlemap.get_combatant(self.actor_slot)
        if not isinstance(fighter, FightCharacter):
            return battlemap
        updated = fighter.model_copy(
            update={"has_bonus_action": False, "disengaging": True}
        )
        return battlemap.replace_combatant(self.actor_slot, updated)
