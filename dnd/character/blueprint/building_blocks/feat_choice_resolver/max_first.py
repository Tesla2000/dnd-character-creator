from __future__ import annotations

from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.feat_choice_resolver.base import (
    FeatChoiceResolver,
)
from dnd.character.blueprint.building_blocks.feat_choice_resolver.random import (
    RandomFeatChoiceResolver,
)
from dnd.character.blueprint.building_blocks.stats_priority import StatsPriority
from dnd.character.blueprint.state import Blueprint
from dnd.character.feature.feats import FeatName
from pydantic import Field


class MaxFirstResolver(FeatChoiceResolver):
    """Prioritizes maxing the highest priority stat before choosing other feats."""

    type: Literal[BuildingBlockType.MAX_FIRST_RESOLVER] = (
        BuildingBlockType.MAX_FIRST_RESOLVER
    )

    priority: StatsPriority = Field(description="Ability score priority order")
    then: RandomFeatChoiceResolver = Field(description="Fallback resolver")

    def _select_from_available(
        self, available: list[FeatName], state: Blueprint
    ) -> FeatName | None:
        highest_priority_stat = self.priority[0]
        if FeatName.ABILITY_SCORE_IMPROVEMENT in available and state.stats.get_stat(
            highest_priority_stat
        ) < state.stats_cup.get_stat(highest_priority_stat):
            return FeatName.ABILITY_SCORE_IMPROVEMENT
        return None

    def apply[_BPT: Blueprint](self, blueprint: _BPT) -> _BPT:
        asi_allowed = blueprint.classes.total_level() != 1
        excluded = [
            *FeatName.not_choosables(),
            *([FeatName.ABILITY_SCORE_IMPROVEMENT] if not asi_allowed else []),
        ]
        available = [f for f in FeatName if f not in excluded]

        if self._select_from_available(available, blueprint) is None:
            return self.then.apply(blueprint)
        return super().apply(blueprint)
