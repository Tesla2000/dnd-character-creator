from abc import ABC, abstractmethod
from typing import Generic

from pydantic import BaseModel, ConfigDict

from dnd.fight._combatant_slot import SlotT
from dnd.fight.battlemap import Battlemap


class _Aspect(BaseModel, Generic[SlotT], ABC):
    """value() must return higher-is-better for actor_slot's team; weight
    scales magnitude but must never flip that sign convention."""

    model_config = ConfigDict(frozen=True)

    weight: float = 1.0

    @abstractmethod
    def value(
        self,
        before: Battlemap[SlotT],
        after: Battlemap[SlotT],
        actor_slot: SlotT,
    ) -> float: ...
