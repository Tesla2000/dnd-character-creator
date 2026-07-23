from __future__ import annotations

from typing import Protocol

from dnd.fight._combatant_slot import SlotT
from dnd.fight._team_id import TeamId
from dnd.fight.aspect import AnyAspect
from dnd.fight.strategy import Strategy
from dnd.fight.weight_optimization._match_runner import MatchRunner


class WeightOptimizer(Protocol[SlotT]):
    def optimize(
        self,
        aspects: tuple[AnyAspect[SlotT], ...],
        evaluator: MatchRunner[SlotT],
        frozen_strategy: Strategy[SlotT],
        optimizing_team: TeamId,
    ) -> tuple[AnyAspect[SlotT], ...]: ...
