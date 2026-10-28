from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict

from dnd.choices.stats_creation.statistic import Statistic


class StatValue(BaseModel):
    """Read-only result of reading a statistic."""

    model_config = ConfigDict(frozen=True)

    statistic: Statistic
    value: int

    @property
    def modifier(self) -> int:
        return self.value // 2 - 5


class Stat(BaseModel):
    """A statistic being changed. Changes call set_value to store their result."""

    model_config = ConfigDict(frozen=True)

    statistic: Statistic
    value: int

    def set_value(self, value: int) -> Stat:
        return self.model_copy(update={"value": value})


class FlooredStat(BaseModel):
    """Wraps a stat so that set_value never stores a value below the minimum."""

    model_config = ConfigDict(frozen=True)

    stat: Stat | FlooredStat
    minimum: int

    @property
    def value(self) -> int:
        return self.stat.value

    def set_value(self, value: int) -> FlooredStat:
        return FlooredStat(
            stat=self.stat.set_value(max(self.minimum, value)),
            minimum=self.minimum,
        )


type StatLike = Stat | FlooredStat
