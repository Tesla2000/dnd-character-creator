from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Generic, Self

from dnd._position import Position
from dnd.character.actions._base_action import Action
from dnd.fight._combatant_slot import SlotT
from dnd.fight.fight_character import FightCharacter

if TYPE_CHECKING:
    from dnd.fight.battlemap import Battlemap


class NegativeAoeAction(Action[SlotT], Generic[SlotT], ABC):
    actor_slot: SlotT
    spell_save_dc: int

    @abstractmethod
    def hit_slots(self, battlemap: Battlemap[SlotT]) -> frozenset[SlotT]:
        """Slots caught in this candidate's area, excluding the caster."""
        ...

    @classmethod
    @abstractmethod
    def _for_position(
        cls, actor_slot: SlotT, position: Position, spell_save_dc: int
    ) -> Self: ...

    @classmethod
    def create_candidates(
        cls, actor_slot: SlotT, battlemap: Battlemap[SlotT], spell_save_dc: int
    ) -> tuple[Self, ...]:
        match battlemap.get_combatant(actor_slot):
            case FightCharacter() as actor:
                pass
            case _:
                return ()
        raw: list[tuple[Self, frozenset[SlotT], frozenset[SlotT]]] = []
        for target_slot in battlemap.all_slots():
            if target_slot == actor_slot:
                continue
            match battlemap.get_combatant(target_slot):
                case FightCharacter() as target:
                    pass
                case _:
                    continue
            candidate = cls._for_position(actor_slot, target.position, spell_save_dc)
            enemies: set[SlotT] = set()
            allies: set[SlotT] = set()
            for slot in candidate.hit_slots(battlemap):
                match battlemap.get_combatant(slot):
                    case FightCharacter() as combatant:
                        group = (
                            allies if combatant.team_id == actor.team_id else enemies
                        )
                        group.add(slot)
                    case _:
                        pass
            raw.append((candidate, frozenset(enemies), frozenset(allies)))

        dominated: set[int] = set()
        for i, (_, enemies_i, allies_i) in enumerate(raw):
            for j, (_, enemies_j, allies_j) in enumerate(raw):
                if (
                    i != j
                    and enemies_j <= enemies_i
                    and allies_i <= allies_j
                    and (enemies_i, allies_i) != (enemies_j, allies_j)
                ):
                    dominated.add(j)
        return tuple(
            candidate
            for idx, (candidate, _, _) in enumerate(raw)
            if idx not in dominated
        )
