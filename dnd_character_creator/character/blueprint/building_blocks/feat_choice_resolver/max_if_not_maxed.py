from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks import (
    FeatChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.stats_priority import (
    StatsPriority,
)
from dnd_character_creator.feats import FeatName


class _AlreadyMaxed(Exception):
    pass


class MaxIfNotMaxedResolver(FeatChoiceResolver):
    priority: StatsPriority

    def _select_from_available(
        self, available: list[FeatName], blueprint: Blueprint
    ) -> FeatName:
        highest_priority_stat = self.priority[0]
        if blueprint.stats.get_stat(
            highest_priority_stat
        ) < blueprint.stats_cup.get_stat(highest_priority_stat):
            return FeatName.ABILITY_SCORE_IMPROVEMENT
        raise _AlreadyMaxed()

    def get_change(self, blueprint: Blueprint) -> Blueprint:
        """Replace FeatName.ANY_OF_YOUR_CHOICE placeholders.

        Args:
            blueprint: Current character blueprint.

        Returns:
            Blueprint with feat placeholders replaced and ASI converted
            to n_stat_choices.
        """
        try:
            return super().get_change(blueprint)
        except _AlreadyMaxed:
            return Blueprint()
