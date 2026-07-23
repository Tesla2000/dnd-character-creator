from __future__ import annotations

from dnd.fight._combatant_slot import SlotT
from dnd.fight._team_id import TeamId
from dnd.fight.aspect import AnyAspect
from dnd.fight.strategy import CompositeStrategy, Strategy
from dnd.fight.weight_optimization._match_runner import MatchRunner
from dnd.fight.weight_optimization._outcome import AggregatedOutcome

_CANDIDATE_WEIGHTS: tuple[float, ...] = (0.25, 0.5, 1.0, 2.0, 4.0)
_PASSES = 3


class CoordinateAscentOptimizer:
    def optimize(
        self,
        aspects: tuple[AnyAspect[SlotT], ...],
        evaluator: MatchRunner[SlotT],
        frozen_strategy: Strategy[SlotT],
        optimizing_team: TeamId,
    ) -> tuple[AnyAspect[SlotT], ...]:
        current = tuple(aspect.model_copy(update={"weight": 1.0}) for aspect in aspects)
        best_score = self._evaluate(
            current, evaluator, frozen_strategy, optimizing_team
        )
        for _ in range(_PASSES):
            improved = False
            for index in range(1, len(current)):
                for candidate_weight in _CANDIDATE_WEIGHTS:
                    candidate = self._with_weight(current, index, candidate_weight)
                    score = self._evaluate(
                        candidate, evaluator, frozen_strategy, optimizing_team
                    )
                    if score.beats(best_score):
                        best_score = score
                        current = candidate
                        improved = True
            if not improved:
                break
        return current

    @staticmethod
    def _with_weight(
        aspects: tuple[AnyAspect[SlotT], ...], index: int, weight: float
    ) -> tuple[AnyAspect[SlotT], ...]:
        return tuple(
            aspect.model_copy(update={"weight": weight}) if i == index else aspect
            for i, aspect in enumerate(aspects)
        )

    @staticmethod
    def _evaluate(
        aspects: tuple[AnyAspect[SlotT], ...],
        evaluator: MatchRunner[SlotT],
        frozen_strategy: Strategy[SlotT],
        optimizing_team: TeamId,
    ) -> AggregatedOutcome:
        optimizing_strategy: CompositeStrategy[SlotT] = CompositeStrategy(
            aspects=aspects
        )
        if optimizing_team == TeamId.A:
            return evaluator.run(optimizing_strategy, frozen_strategy, optimizing_team)
        return evaluator.run(frozen_strategy, optimizing_strategy, optimizing_team)
