from __future__ import annotations

import heapq
from typing import Generic, Literal

from dnd._position import Position
from dnd.character._ability_name import AbilityName
from dnd.character.actions._base_action import MovementAction
from dnd._combat_event import MovementEvent, OpportunityAttackEvent
from dnd.fight._combatant_slot import SlotT
from dnd.fight._terrain_type import TerrainType
from dnd.fight.battlemap import Battlemap
from dnd.fight.fight_character import FightCharacter

_NORMAL_STEP_COST = 5
_DIFFICULT_STEP_COST = 10


class Move(MovementAction[SlotT], Generic[SlotT]):
    name: Literal[AbilityName.MOVE] = AbilityName.MOVE
    range_tails: Literal[0] = 0
    to: Position
    mover_slot: SlotT
    movement_cost: int
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
        start = fighter.position
        blocked: frozenset[tuple[int, int]] = frozenset(
            (p.x, p.y)
            for p in (
                battlemap.get_combatant(s).position
                for s in battlemap.all_slots()
                if s != mover_slot
            )
        )
        cost_map = cls._cost_map(start, max_steps, battlemap, blocked)
        results: list[Move[SlotT]] = []
        for (x, y), cost in cost_map.items():
            if cost > fighter.movement_remaining:
                continue
            dest = Position(x=x, y=y, height=start.height)
            oa_attackers = cls._find_oa_attackers(
                mover_slot, fighter, dest, battlemap
            )
            results.append(
                cls(
                    to=dest,
                    mover_slot=mover_slot,
                    movement_cost=cost,
                    triggered_oa_from=oa_attackers,
                )
            )
        return tuple(results)

    @staticmethod
    def _cost_map(
        start: Position,
        max_steps: int,
        battlemap: Battlemap[SlotT],
        blocked: frozenset[tuple[int, int]],
    ) -> dict[tuple[int, int], int]:
        best: dict[tuple[int, int], int] = {(start.x, start.y): 0}
        heap: list[tuple[int, int, int]] = [(0, start.x, start.y)]
        while heap:
            cost, x, y = heapq.heappop(heap)
            if cost > best[(x, y)]:
                continue
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if max(abs(nx - start.x), abs(ny - start.y)) > max_steps:
                        continue
                    if (nx, ny) in blocked:
                        continue
                    neighbor = Position(x=nx, y=ny, height=start.height)
                    step_cost = (
                        _DIFFICULT_STEP_COST
                        if battlemap.terrain_at(neighbor) is TerrainType.DIFFICULT
                        else _NORMAL_STEP_COST
                    )
                    new_cost = cost + step_cost
                    if new_cost < best.get((nx, ny), new_cost + 1):
                        best[(nx, ny)] = new_cost
                        heapq.heappush(heap, (new_cost, nx, ny))
        del best[(start.x, start.y)]
        return best

    @classmethod
    def _find_oa_attackers(
        cls,
        mover_slot: SlotT,
        fighter: FightCharacter,
        dest: Position,
        battlemap: Battlemap[SlotT],
    ) -> tuple[SlotT, ...]:
        fx, fy = fighter.position.x, fighter.position.y
        tx, ty = dest.x, dest.y
        result: list[SlotT] = []
        for slot in battlemap.all_slots():
            if slot == mover_slot:
                continue
            match battlemap.get_combatant(slot):
                case FightCharacter() as c if (
                    c.team_id != fighter.team_id and c.has_reaction
                ):
                    cx, cy = c.position.x, c.position.y
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
        moved = fighter.model_copy(
            update={
                "position": self.to,
                "movement_remaining": fighter.movement_remaining - self.movement_cost,
            }
        )
        result = battlemap.replace_combatant(self.mover_slot, moved)
        result = result.emit(MovementEvent(mover_slot=self.mover_slot, to=self.to))
        for attacker_slot in self.triggered_oa_from:
            result = result.emit(
                OpportunityAttackEvent(
                    attacker_slot=attacker_slot,
                    target_slot=self.mover_slot,
                )
            )
        return result
