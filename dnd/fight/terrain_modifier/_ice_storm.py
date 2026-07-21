from __future__ import annotations

from typing import Generic, Literal, Self

from dnd._combat_event import AnyCombatEvent, TurnEndEvent
from dnd._position import Position
from dnd.fight._combatant_slot import SlotT
from dnd.fight._terrain_type import TerrainType
from dnd.fight.terrain_modifier._base import _TerrainModifier
from dnd.fight.terrain_modifier._type import TerrainModifierType


class _IceStormTerrainModifier(_TerrainModifier[SlotT], Generic[SlotT]):
    type: Literal[TerrainModifierType.ICE_STORM] = TerrainModifierType.ICE_STORM
    caster_slot: SlotT
    turn_ends_remaining: int = 2

    def terrain_type(self) -> TerrainType:
        return TerrainType.DIFFICULT

    def on_event(
        self, event: AnyCombatEvent[SlotT]
    ) -> tuple[Self | None, tuple[AnyCombatEvent[SlotT], ...]]:
        match event:
            case TurnEndEvent() as e if e.actor_slot == self.caster_slot:
                remaining = self.turn_ends_remaining - 1
                if remaining <= 0:
                    return None, ()
                return self.model_copy(update={"turn_ends_remaining": remaining}), ()
            case _:
                return self, ()

    @classmethod
    def sphere(
        cls, center: Position, radius_tails: int, caster_slot: SlotT
    ) -> dict[Position, Self]:
        modifier = cls(caster_slot=caster_slot)
        return {
            Position(x=center.x + dx, y=center.y + dy): modifier
            for dx in range(-radius_tails, radius_tails + 1)
            for dy in range(-radius_tails, radius_tails + 1)
            if max(abs(dx), abs(dy)) <= radius_tails
        }
