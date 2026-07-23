from __future__ import annotations

from typing import TYPE_CHECKING, Generic, Literal, Self

from dnd.character._ability_name import AbilityName
from dnd.character.actions._base_action import FreeAction
from dnd.character.actions._melee_attack import _MeleeAttackExecutor
from dnd.character.actions.combat.attack_with_wolf_bite import AttackWithWolfBite
from dnd.fight._combatant_slot import SlotT
from dnd.fight.fight_character import FightCharacter

if TYPE_CHECKING:
    from dnd.fight.battlemap import Battlemap


class CommandSummonedBeast(FreeAction[SlotT], Generic[SlotT]):
    name: Literal[AbilityName.CONJURE_ANIMALS] = AbilityName.CONJURE_ANIMALS
    range_tails: Literal[1] = 1
    actor_slot: SlotT
    executor: _MeleeAttackExecutor[SlotT]

    @classmethod
    def create(
        cls,
        actor_slot: SlotT,
        fighter: FightCharacter[SlotT],
        battlemap: Battlemap[SlotT],
    ) -> tuple[Self, ...]:
        results: list[Self] = []
        for beast_slot in battlemap.all_slots():
            match battlemap.get_combatant(beast_slot):
                case FightCharacter() as beast if beast.summoned_by == actor_slot:
                    pass
                case _:
                    continue
            for candidate in AttackWithWolfBite.create(beast_slot, beast, battlemap):
                results.append(
                    cls(actor_slot=actor_slot, executor=candidate.executor)
                )
        return tuple(results)

    def perform(self, battlemap: Battlemap[SlotT]) -> Battlemap[SlotT]:
        return self.executor.attack(battlemap)
