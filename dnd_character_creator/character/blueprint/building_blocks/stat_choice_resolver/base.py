from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from pydantic import ConfigDict

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd_character_creator.character.stats import Stats
from dnd_character_creator.choices.stats_creation.statistic import Statistic


class StatChoiceResolver(BuildingBlock, ABC):
    """Abstract base class for resolving n_stat_choices.

    When a race/subrace grants ability score increases of the player's choice
    (n_stat_choices > 0), this component determines which stats to increase.

    Subclasses must implement _select_stats_to_increase to determine the
    selection strategy.
    """

    model_config = ConfigDict(frozen=True)

    @abstractmethod
    def _select_stats_to_increase(
        self, n: int, current_stats: Stats
    ) -> dict[Statistic, int]:
        pass

    def _get_change(self, blueprint: Blueprint) -> Blueprint:
        """Apply stat increases based on n_stat_choices."""
        if blueprint.n_stat_choices == 0:
            # No stat choices to resolve, yield empty
            return Blueprint()
            return

        if not blueprint.stats:
            raise ValueError(
                "Stats must be set before stat choices can be resolved"
            )

        # Select which stats to increase
        stat_increases = self._select_stats_to_increase(
            blueprint.n_stat_choices, blueprint.stats
        )

        # Apply increases to current stats
        new_stats = Stats(
            strength=blueprint.stats.strength
            + stat_increases.get(Statistic.STRENGTH, 0),
            dexterity=blueprint.stats.dexterity
            + stat_increases.get(Statistic.DEXTERITY, 0),
            constitution=blueprint.stats.constitution
            + stat_increases.get(Statistic.CONSTITUTION, 0),
            intelligence=blueprint.stats.intelligence
            + stat_increases.get(Statistic.INTELLIGENCE, 0),
            wisdom=blueprint.stats.wisdom
            + stat_increases.get(Statistic.WISDOM, 0),
            charisma=blueprint.stats.charisma
            + stat_increases.get(Statistic.CHARISMA, 0),
        )

        return Blueprint(stats=new_stats, n_stat_choices=0)
