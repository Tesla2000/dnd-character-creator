from __future__ import annotations

from abc import ABC, abstractmethod
from typing import ClassVar, Generic, Self, cast

from pydantic import BaseModel, ConfigDict, Field

from dnd._position import Position
from dnd.fight._combat_event import (
    AnyCombatEvent,
    RoundEndEvent,
    RoundStartEvent,
    TurnEndEvent,
    TurnStartEvent,
)
from dnd.fight._combatant_slot import SlotT
from dnd.fight._terrain_type import TerrainType
from dnd.fight.fight_character import AnyActiveCombatant
from dnd.fight.terrain_modifier import AnyTerrainModifier


class Battlemap(BaseModel, Generic[SlotT], ABC):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)
    event_log: tuple[AnyCombatEvent[SlotT], ...] = ()
    terrain_height: dict[tuple[int, int], int] = Field(default_factory=dict)
    terrain: dict[Position, tuple[AnyTerrainModifier[SlotT], ...]] = Field(
        default_factory=dict
    )

    def terrain_height_at(self, x: int, y: int) -> int:
        return self.terrain_height.get((x, y), 0)

    def relative_height_at(self, position: Position) -> int:
        return position.height - self.terrain_height_at(position.x, position.y)

    def terrain_at(self, position: Position) -> TerrainType:
        if self.relative_height_at(position) != 0:
            return TerrainType.NORMAL
        ground = Position(x=position.x, y=position.y)
        for modifier in self.terrain.get(ground, ()):
            if modifier.terrain_type() is TerrainType.DIFFICULT:
                return TerrainType.DIFFICULT
        return TerrainType.NORMAL

    def all_slots(self) -> tuple[SlotT, ...]:
        for base in type(self).__mro__:
            if (
                issubclass(base, Battlemap)
                and base.__pydantic_generic_metadata__["args"]
            ):
                slot_type = cast(
                    type[SlotT], base.__pydantic_generic_metadata__["args"][0]
                )
                return tuple(slot_type)
        return ()

    @abstractmethod
    def get_combatant(self, slot: SlotT) -> AnyActiveCombatant: ...

    @abstractmethod
    def replace_combatant(self, slot: SlotT, updated: AnyActiveCombatant) -> Self: ...

    def emit(self, event: AnyCombatEvent[SlotT]) -> Self:
        result: Self = self
        pending: list[AnyCombatEvent[SlotT]] = []
        for slot in result.all_slots():
            combatant = result.get_combatant(slot)
            updated, emitted = combatant.on_event(event)
            result = result.replace_combatant(slot, updated)
            pending.extend(emitted)

        distinct: dict[int, AnyTerrainModifier[SlotT]] = {
            id(modifier): modifier
            for modifiers in result.terrain.values()
            for modifier in modifiers
        }
        survivors: dict[int, AnyTerrainModifier[SlotT] | None] = {}
        for modifier_id, modifier in distinct.items():
            updated_modifier, emitted = modifier.on_event(event)
            pending.extend(emitted)
            survivors[modifier_id] = updated_modifier

        new_terrain: dict[Position, tuple[AnyTerrainModifier[SlotT], ...]] = {}
        for position, modifiers in result.terrain.items():
            surviving = tuple(
                survivor
                for modifier in modifiers
                if (survivor := survivors[id(modifier)]) is not None
            )
            if surviving:
                new_terrain[position] = surviving

        result = result.model_copy(
            update={"terrain": new_terrain, "event_log": result.event_log + (event,)}
        )
        for next_event in pending:
            result = result.emit(next_event)
        return result

    def has_progress_since(self, index: int) -> bool:
        bookkeeping = (TurnStartEvent, TurnEndEvent, RoundStartEvent, RoundEndEvent)
        return any(
            not isinstance(event, bookkeeping) for event in self.event_log[index:]
        )
