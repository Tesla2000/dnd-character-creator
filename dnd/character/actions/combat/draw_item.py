from __future__ import annotations

from typing import TYPE_CHECKING, Generic, Literal

from dnd.character._ability_name import AbilityName
from dnd.character.actions._base_action import FreeAction
from dnd.choices.equipment_creation.weapons import TWO_HANDED_WEAPONS, WeaponName
from dnd.fight._combatant_slot import SlotT
from dnd.fight.fight_character import FightCharacter

if TYPE_CHECKING:
    from dnd.fight.battlemap import Battlemap


class DrawItem(FreeAction[SlotT], Generic[SlotT]):
    name: Literal[AbilityName.DRAW_ITEM] = AbilityName.DRAW_ITEM
    range_tails: Literal[0] = 0
    actor_slot: SlotT
    item: WeaponName
    which_hand: Literal["main", "off"]

    @classmethod
    def create(
        cls,
        actor_slot: SlotT,
        fighter: FightCharacter,
        battlemap: Battlemap[SlotT],
    ) -> tuple[DrawItem[SlotT], ...]:
        if not fighter.has_free_action:
            return ()
        available: list[WeaponName] = list(fighter.character.weapons)
        if WeaponName.SHIELD in fighter.character.other_equipment:
            available.append(WeaponName.SHIELD)

        both_free = fighter.main_hand is None and fighter.off_hand is None
        options: list[DrawItem[SlotT]] = []
        for item in available:
            if item in TWO_HANDED_WEAPONS:
                if both_free:
                    options.append(
                        cls(actor_slot=actor_slot, item=item, which_hand="main")
                    )
                continue
            if fighter.main_hand is None and fighter.off_hand != item:
                options.append(cls(actor_slot=actor_slot, item=item, which_hand="main"))
            if fighter.off_hand is None and fighter.main_hand != item:
                options.append(cls(actor_slot=actor_slot, item=item, which_hand="off"))
        return tuple(options)

    def perform(self, battlemap: Battlemap[SlotT]) -> Battlemap[SlotT]:
        match battlemap.get_combatant(self.actor_slot):
            case FightCharacter() as fighter:
                pass
            case _:
                return battlemap
        if self.item in TWO_HANDED_WEAPONS:
            updated = fighter.model_copy(
                update={
                    "main_hand": self.item,
                    "off_hand": self.item,
                    "has_free_action": False,
                }
            )
        else:
            field = "main_hand" if self.which_hand == "main" else "off_hand"
            updated = fighter.model_copy(
                update={field: self.item, "has_free_action": False}
            )
        return battlemap.replace_combatant(self.actor_slot, updated)
