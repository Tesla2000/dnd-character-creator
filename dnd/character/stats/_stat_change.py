from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict

from dnd.character.stats._stat import FlooredStat
from dnd.character.stats._stat import StatLike


class StatChange(BaseModel):
    """Adds to or reduces a statistic. Positive amounts add, negative amounts reduce."""

    model_config = ConfigDict(frozen=True)

    amount: int

    def reduce(self, stat: StatLike) -> StatLike:
        return stat.set_value(stat.value + self.amount)


class FloorChange(StatChange):
    """Raises the stat to the minimum, then keeps it from dropping below the minimum."""

    amount: int = 0
    minimum: int

    def reduce(self, stat: StatLike) -> StatLike:
        raised = stat.set_value(max(stat.value, self.minimum))
        return FlooredStat(stat=raised, minimum=self.minimum)
