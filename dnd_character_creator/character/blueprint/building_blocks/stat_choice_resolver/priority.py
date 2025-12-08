from __future__ import annotations

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks.stat_choice_resolver.base import (
    StatChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.stats_priority import (
    StatsPriority,
)
from dnd_character_creator.choices.stats_creation.statistic import Statistic
from pydantic import ConfigDict


class PriorityStatChoiceResolver(StatChoiceResolver):
    """Resolves stat choices based on a priority order with even distribution.

    Distributes increases as evenly as possible across stats in priority order.

    Example:
        >>> resolver = PriorityStatChoiceResolver(
        ...     priority=(
        ...         Statistic.STRENGTH,
        ...         Statistic.CONSTITUTION,
        ...         Statistic.DEXTERITY,
        ...         Statistic.WISDOM,
        ...         Statistic.INTELLIGENCE,
        ...         Statistic.CHARISMA,
        ...     )
        ... )
        >>> # For n_stat_choices=2, will increase STR +1, CON +1
        >>> # For n_stat_choices=3, will increase STR +2, CON +1
        >>> # For n_stat_choices=5, will increase STR +2, CON +2, DEX +1
        >>> # For n_stat_choices=7, will increase STR +2, CON +2, DEX +2, WIS +1
    """

    model_config = ConfigDict(frozen=True)

    priority: StatsPriority

    def _select_stats_to_increase(
        self, blueprint: Blueprint
    ) -> dict[Statistic, int]:
        """Select stats to increase based on priority order.

        Args:
            blueprint: Current character blueprint.

        Returns:
            Dictionary mapping the highest priority stat to all increases.
        """
        return {self.priority[0]: blueprint.n_stat_choices}
