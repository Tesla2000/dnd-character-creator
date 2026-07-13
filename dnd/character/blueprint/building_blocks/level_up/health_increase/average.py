from typing import Generic
from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.health_increase.base import (
    HealthIncrease,
    _DH,
)
from dnd.choices.equipment_creation.weapons import HitDieSize


class HealthIncreaseAverage(HealthIncrease[_DH], Generic[_DH]):
    """Fixed health increase strategy.

    Uses the average value of the hit die (hit_die // 2 + 1) for non-first levels.
    First level always gets the maximum hit die value.
    """

    type: Literal[BuildingBlockType.HEALTH_INCREASE_AVERAGE] = (
        BuildingBlockType.HEALTH_INCREASE_AVERAGE
    )

    def _get_hit_die_value(self, hit_die: HitDieSize) -> int:
        return hit_die.value // 2 + 1
