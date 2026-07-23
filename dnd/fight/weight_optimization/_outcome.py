from __future__ import annotations

from typing import NamedTuple


class FightOutcome(NamedTuple):
    dead_diff: int
    downed_diff: int
    hp_diff: int


class AggregatedOutcome(NamedTuple):
    mean_dead_diff: float
    mean_downed_diff: float
    mean_hp_diff: float

    @classmethod
    def from_outcomes(cls, outcomes: tuple[FightOutcome, ...]) -> AggregatedOutcome:
        count = len(outcomes)
        return cls(
            mean_dead_diff=sum(o.dead_diff for o in outcomes) / count,
            mean_downed_diff=sum(o.downed_diff for o in outcomes) / count,
            mean_hp_diff=sum(o.hp_diff for o in outcomes) / count,
        )

    def beats(self, other: AggregatedOutcome) -> bool:
        if self.mean_dead_diff != other.mean_dead_diff:
            return self.mean_dead_diff > other.mean_dead_diff
        if self.mean_downed_diff != other.mean_downed_diff:
            return self.mean_downed_diff > other.mean_downed_diff
        return self.mean_hp_diff > other.mean_hp_diff
