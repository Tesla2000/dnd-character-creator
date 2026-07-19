from __future__ import annotations

from typing import TYPE_CHECKING, Generic, Literal

from dnd.character._ability_name import AbilityName
from dnd.character.actions._base_action import Action
from dnd.fight._combatant_slot import SlotT
from dnd.fight.fight_character import FightCharacter

if TYPE_CHECKING:
    from dnd.fight.battlemap import Battlemap


class Pass(Action[SlotT], Generic[SlotT]):
    name: Literal[AbilityName.PASS] = AbilityName.PASS
    range_tails: Literal[0] = 0
    actor_slot: SlotT

    @classmethod
    def create(
        cls, actor_slot: SlotT, fighter: FightCharacter, battlemap: Battlemap[SlotT]
    ) -> tuple[Pass[SlotT], ...]:
        if not fighter.has_action:
            return ()
        return (cls(actor_slot=actor_slot),)

    def perform(self, battlemap: Battlemap[SlotT]) -> Battlemap[SlotT]:
        match battlemap.get_combatant(self.actor_slot):
            case FightCharacter() as fighter:
                return battlemap.replace_combatant(
                    self.actor_slot,
                    fighter.model_copy(
                        update={
                            "has_action": False,
                            "has_bonus_action": False,
                            "attacks_remaining": 0,
                        }
                    ),
                )
            case _:
                return battlemap
