from __future__ import annotations

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks import (
    BuildingBlock,
)
from dnd_character_creator.character.feature.feature import Feature


class FeatureAssigner(BuildingBlock):
    """Building block that assigns a feature to a character blueprint.

    Similar to MagicalItemAssigner, this wraps a Feature object and applies
    it to the blueprint. The Feature's assign_to method determines what
    changes are made to the blueprint.

    Example:
        >>> from character.feature import Feature
        >>> from character.feature.specialized_features import StatBoostFeature
        >>> from choices.stats_creation.statistic import Statistic
        >>>
        >>> # Simple descriptive feature
        >>> trance = Feature(
        ...     name="Trance",
        ...     description="Elves don't need to sleep. Instead, they meditate deeply for 4 hours a day."
        ... )
        >>> trance_assigner = FeatureAssigner(feature=trance)
        >>>
        >>> # Feature that boosts a stat
        >>> asi = StatBoostFeature(
        ...     name="Ability Score Improvement",
        ...     description="Increase one ability score by 2",
        ...     stat=Statistic.STRENGTH,
        ...     boost_amount=2
        ... )
        >>> asi_assigner = FeatureAssigner(feature=asi)
    """

    feature: Feature

    def _get_change(self, blueprint: Blueprint) -> Blueprint:
        """Apply the feature to the blueprint.

        Delegates to the feature's assign_to method, which determines
        what modifications are made to the blueprint.
        """
        return self.feature.assign_to(blueprint)
