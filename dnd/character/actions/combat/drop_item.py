from __future__ import annotations

from typing import TYPE_CHECKING, Generic, Literal

from dnd.character._ability_name import AbilityName
from dnd.character.actions._base_action import FreeAction
from dnd.fight._combatant_slot import SlotT
from dnd.fight.fight_character import FightCharacter

if TYPE_CHECKING:
    from dnd.fight.battlemap import Battlemap


class DropItem(FreeAction[SlotT], Generic[SlotT]):
    name: Literal[AbilityName.DROP_ITEM] = AbilityName.DROP_ITEM
    range_tails: Literal[0] = 0
    actor_slot: SlotT
    which_hand: Literal["main", "off"]

    @classmethod
    def create(
        cls,
        actor_slot: SlotT,
        fighter: FightCharacter,
        battlemap: Battlemap[SlotT],
    ) -> tuple[DropItem[SlotT], ...]:
        options: list[DropItem[SlotT]] = []
        if fighter.main_hand is not None:
            options.append(cls(actor_slot=actor_slot, which_hand="main"))
        if fighter.off_hand is not None and fighter.off_hand != fighter.main_hand:
            options.append(cls(actor_slot=actor_slot, which_hand="off"))
        return tuple(options)

    def perform(self, battlemap: Battlemap[SlotT]) -> Battlemap[SlotT]:
        match battlemap.get_combatant(self.actor_slot):
            case FightCharacter() as fighter:
                pass
            case _:
                return battlemap
        if fighter.main_hand == fighter.off_hand and fighter.main_hand is not None:
            updated = fighter.model_copy(update={"main_hand": None, "off_hand": None})
        else:
            field = "main_hand" if self.which_hand == "main" else "off_hand"
            updated = fighter.model_copy(update={field: None})
        return battlemap.replace_combatant(self.actor_slot, updated)
