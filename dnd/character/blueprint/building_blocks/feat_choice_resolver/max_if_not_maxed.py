from __future__ import annotations

from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.feat_choice_resolver.base import (
    FeatChoiceResolver,
)
from dnd.character.blueprint.building_blocks.stats_priority import StatsPriority
from dnd.character.blueprint.state import Blueprint
from dnd.character.feature.feats import FeatName
from pydantic import Field


class MaxIfNotMaxedResolver(FeatChoiceResolver):
    """Chooses ASI only if the highest priority stat is not maxed; otherwise no-op."""

    type: Literal[BuildingBlockType.MAX_IF_NOT_MAXED_RESOLVER] = (
        BuildingBlockType.MAX_IF_NOT_MAXED_RESOLVER
    )

    priority: StatsPriority = Field(description="Ability score priority order")

    def _select_from_available(
        self, available: list[FeatName], state: Blueprint
    ) -> FeatName | None:
        highest_priority_stat = self.priority[0]
        if state.stats.get_stat(highest_priority_stat) < state.stats_cup.get_stat(
            highest_priority_stat
        ):
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
            return blueprint.model_copy(
                update={
                    "feats": blueprint.feats,
                    "n_stat_choices": blueprint.n_stat_choices,
                }
            )
        return super().apply(blueprint)
