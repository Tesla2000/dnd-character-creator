from __future__ import annotations

from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.building_block import _WideBlueprint
from dnd.character.blueprint.building_blocks.stat_choice_resolver.base import (
    StatChoiceResolver,
)
from dnd.choices.stats_creation.statistic import Statistic


class MaxStatChoiceResolver(StatChoiceResolver):
    """Puts each stat point into whichever stat currently has the highest value below its cap."""

    type: Literal[BuildingBlockType.MAX_STAT_CHOICE_RESOLVER] = (
        BuildingBlockType.MAX_STAT_CHOICE_RESOLVER
    )

    def select_stats_to_increase(self, state: _WideBlueprint) -> dict[Statistic, int]:
        stats = state.stats
        if stats is None:
            return {s: 0 for s in Statistic}
        increases: dict[Statistic, int] = {s: 0 for s in Statistic}
        n = state.n_stat_choices
        while n > 0:
            top = max(
                (
                    s
                    for s in Statistic
                    if stats.get_stat(s) + increases[s] < state.stats_cup.get_stat(s)
                ),
                key=lambda s: stats.get_stat(s) + increases[s],
                default=None,
            )
            if top is None:
                break
            increases[top] += 1
            n -= 1
        return increases
