from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Self

from pydantic import BaseModel, ConfigDict

from dnd._combat_event import AnyCombatEvent
from dnd.fight._combatant_slot import SlotT
from dnd.fight._terrain_type import TerrainType


class _TerrainModifier(BaseModel, Generic[SlotT], ABC):
    model_config = ConfigDict(frozen=True)

    @abstractmethod
    def terrain_type(self) -> TerrainType: ...

    def on_event(
        self, event: AnyCombatEvent[SlotT]
    ) -> tuple[Self | None, tuple[AnyCombatEvent[SlotT], ...]]:
        return self, ()
