from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dnd_character_creator.character.blueprint.blueprint import Blueprint

from dnd_character_creator.character.feature.feature import Feature
from dnd_character_creator.character.stats import Stats
from dnd_character_creator.choices.stats_creation.statistic import Statistic


class StatBoostFeature(Feature):
    """A feature that increases a specific ability score.

    Examples:
        - Ability Score Improvement feat
        - Racial stat bonuses from certain features
        - Class features that boost stats
    """

    stat: Statistic
    boost_amount: int

    def assign_to(self, blueprint: Blueprint) -> Blueprint:
        """Increase the specified stat by the boost amount.

        Respects the character's stats_cup (maximum stat values).
        Also adds the feature to other_active_abilities.
        """
        stat_name = self.stat.value.lower()

        # Get current stat value and cap
        current_value = getattr(blueprint.stats, stat_name)
        stats_cup_value = getattr(blueprint.stats_cup, stat_name)

        # Calculate new value: add boost, but don't exceed the cap
        new_value = min(current_value + self.boost_amount, stats_cup_value)

        new_stats = Stats(
            **{**blueprint.stats.model_dump(), stat_name: new_value}
        )

        return type(blueprint)(
            stats=new_stats,
            other_active_abilities=blueprint.other_active_abilities
            + (f"{self.name}: {self.description}",),
        )
