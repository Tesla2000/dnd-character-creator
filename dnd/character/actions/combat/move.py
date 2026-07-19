from __future__ import annotations

from typing import Generic, Literal

from dnd.character._ability_name import AbilityName
from dnd.character.actions._base_action import MovementAction
from dnd._combat_event import OpportunityAttackEvent
from dnd.fight._combatant_slot import SlotT
from dnd.fight.battlemap import Battlemap
from dnd.fight.fight_character import FightCharacter


class Move(MovementAction[SlotT], Generic[SlotT]):
    name: Literal[AbilityName.MOVE] = AbilityName.MOVE
    range_tails: Literal[0] = 0
    to: tuple[int, int]
    mover_slot: SlotT
    triggered_oa_from: tuple[SlotT, ...] = ()

    @classmethod
    def create(
        cls,
        mover_slot: SlotT,
        fighter: FightCharacter,
        battlemap: Battlemap[SlotT],
    ) -> tuple[Move[SlotT], ...]:
        if fighter.movement_remaining < 5:
            return ()
        max_steps = fighter.movement_remaining // 5
        fx, fy = fighter.position
        occupied: frozenset[tuple[int, int]] = frozenset(
            battlemap.get_combatant(s).position
            for s in battlemap.all_slots()
            if s != mover_slot
        )
        results: list[Move[SlotT]] = []
        for dx in range(-max_steps, max_steps + 1):
            for dy in range(-max_steps, max_steps + 1):
                if dx == 0 and dy == 0:
                    continue
                dest = (fx + dx, fy + dy)
                if dest in occupied:
                    continue
                oa_attackers = cls._find_oa_attackers(
                    mover_slot, fighter, dest, battlemap
                )
                results.append(
                    cls(to=dest, mover_slot=mover_slot, triggered_oa_from=oa_attackers)
                )
        return tuple(results)

    @classmethod
    def _find_oa_attackers(
        cls,
        mover_slot: SlotT,
        fighter: FightCharacter,
        dest: tuple[int, int],
        battlemap: Battlemap[SlotT],
    ) -> tuple[SlotT, ...]:
        fx, fy = fighter.position
        tx, ty = dest
        result: list[SlotT] = []
        for slot in battlemap.all_slots():
            if slot == mover_slot:
                continue
            match battlemap.get_combatant(slot):
                case FightCharacter() as c if c.team_id != fighter.team_id and c.has_reaction:
                    cx, cy = c.position
                    was_adjacent = max(abs(cx - fx), abs(cy - fy)) <= 1
                    will_be_adjacent = max(abs(cx - tx), abs(cy - ty)) <= 1
                    if was_adjacent and not will_be_adjacent:
                        result.append(slot)
                case _:
                    pass
        return tuple(result)

    def perform(self, battlemap: Battlemap[SlotT]) -> Battlemap[SlotT]:
        match battlemap.get_combatant(self.mover_slot):
            case FightCharacter() as fighter:
                pass
            case _:
                return battlemap
        fx, fy = fighter.position
        chebyshev = max(abs(self.to[0] - fx), abs(self.to[1] - fy))
        moved = fighter.model_copy(
            update={
                "position": self.to,
                "movement_remaining": fighter.movement_remaining - chebyshev * 5,
            }
        )
        result = battlemap.replace_combatant(self.mover_slot, moved)
        for attacker_slot in self.triggered_oa_from:
            result = result.emit(
                OpportunityAttackEvent(
                    attacker_slot=int(attacker_slot),
                    target_slot=int(self.mover_slot),
                )
            )
        return result
