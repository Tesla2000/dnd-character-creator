from typing import Generator, ClassVar

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks.stats_builder.stats_builder import \
    StatsBuilder
from dnd_character_creator.character.stats import Stats


class StandardArray(StatsBuilder):
    _standard_array_descending: ClassVar[tuple[int, int, int, int, int, int]] = (15, 14, 13, 12, 10, 8)
    def _get_change(self, blueprint: Blueprint) -> Blueprint:
        return Blueprint(stats=Stats.from_mapping(dict(zip(self.stats_priority, self._standard_array_descending))))