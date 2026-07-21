from __future__ import annotations

from random import randint
from typing import TYPE_CHECKING, Generic, Literal

from dnd.character._ability_name import AbilityName
from dnd.character.actions._base_action import Action
from dnd.fight._combatant_slot import SlotT
from dnd.fight.fight_character import FightCharacter, SpellcasterFightCharacter

if TYPE_CHECKING:
    from dnd.fight.battlemap import Battlemap


class CastMagicMissile(Action[SlotT], Generic[SlotT]):
    name: Literal[AbilityName.MAGIC_MISSILE] = AbilityName.MAGIC_MISSILE
    range_tails: Literal[120] = 120
    actor_slot: SlotT
    target_slot: SlotT

    @classmethod
    def create(
        cls,
        actor_slot: SlotT,
        fighter: FightCharacter,
        battlemap: Battlemap[SlotT],
    ) -> tuple[CastMagicMissile[SlotT], ...]:
        if not isinstance(fighter, SpellcasterFightCharacter):
            return ()
        if not fighter.has_action:
            return ()
        if fighter.remaining_spell_slots.level_1 == 0:
            return ()
        if AbilityName.MAGIC_MISSILE not in fighter.character.actions:
            return ()
        results: list[CastMagicMissile[SlotT]] = []
        for target_slot in battlemap.all_slots():
            if target_slot == actor_slot:
                continue
            results.append(cls(actor_slot=actor_slot, target_slot=target_slot))
        return tuple(results)

    def perform(self, battlemap: Battlemap[SlotT]) -> Battlemap[SlotT]:
        match battlemap.get_combatant(self.actor_slot):
            case SpellcasterFightCharacter() as fighter:
                pass
            case _:
                return battlemap
        battlemap = battlemap.replace_combatant(
            self.actor_slot, fighter.spend_action().spend_level_1_slot()
        )
        match battlemap.get_combatant(self.target_slot):
            case FightCharacter() as target:
                pass
            case _:
                return battlemap
        damage = sum(randint(1, 4) for _ in range(3)) + 3
        return battlemap.replace_combatant(self.target_slot, target.take_damage(damage))
