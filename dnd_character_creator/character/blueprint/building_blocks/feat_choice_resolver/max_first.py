from typing import Union

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks.feat_choice_resolver.ai import (
    AIFeatChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.feat_choice_resolver.base import (
    FeatChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.feat_choice_resolver.random import (
    RandomFeatChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.stats_priority import (
    StatsPriority,
)
from dnd_character_creator.character.feature.feats import FeatName


class MaxFirstResolver(FeatChoiceResolver):
    priority: StatsPriority
    then: Union[RandomFeatChoiceResolver, AIFeatChoiceResolver]

    def _select_from_available(
        self, available: list[FeatName], blueprint: Blueprint
    ) -> FeatName:
        highest_priority_stat = self.priority[0]
        if blueprint.stats.get_stat(
            highest_priority_stat
        ) < blueprint.stats_cup.get_stat(highest_priority_stat):
            return FeatName.ABILITY_SCORE_IMPROVEMENT
        return self.then._select_from_available(available, blueprint)
