from abc import ABC
from typing import Annotated

from pydantic import AfterValidator

from dnd_character_creator.character.blueprint.building_blocks import \
    BuildingBlock
from dnd_character_creator.choices.stats_creation.statistic import Statistic

StatsPriority = tuple[Statistic, Statistic, Statistic, Statistic, Statistic, Statistic]
def _validate_uniqueness(stats_priority: StatsPriority) -> StatsPriority:
    if len(stats_priority) != len(set(stats_priority)):
        raise ValueError(f"Elements of {stats_priority=} are not unique")
    return stats_priority


class StatsBuilder(BuildingBlock, ABC):
    stats_priority: Annotated[StatsPriority, AfterValidator(_validate_uniqueness)]