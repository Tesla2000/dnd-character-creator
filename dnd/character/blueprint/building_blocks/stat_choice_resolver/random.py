import random
from typing import Literal

from dnd.character.blueprint.building_blocks.building_block import _WideBlueprint
from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.stat_choice_resolver.base import (
    StatChoiceResolver,
)
from dnd.choices.stats_creation.statistic import Statistic
from pydantic import ConfigDict
from pydantic import Field


class RandomStatChoiceResolver(StatChoiceResolver):
    """Randomly distributes ability score increases for n_stat_choices."""

    type: Literal[BuildingBlockType.RANDOM_STAT_CHOICE_RESOLVER] = (
        BuildingBlockType.RANDOM_STAT_CHOICE_RESOLVER
    )

    model_config = ConfigDict(frozen=True)

    seed: int | None = Field(default=None)

    def select_stats_to_increase(self, state: _WideBlueprint) -> dict[Statistic, int]:
        assert state.stats is not None
        rng = random.Random(self.seed)
        increases: dict[Statistic, int] = {s: 0 for s in Statistic}
        stats_list = list(Statistic)
        for _ in range(state.n_stat_choices):
            available = [
                s
                for s in stats_list
                if state.stats.get_stat(s) + increases[s] < state.stats_cup.get_stat(s)
            ]
            if available:
                increases[rng.choice(available)] += 1
        return increases
