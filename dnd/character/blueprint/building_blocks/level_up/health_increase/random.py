import random as _random
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


class HealthIncreaseRandom(HealthIncrease[_DH], Generic[_DH]):
    """Random health increase strategy.

    Rolls a random value between 1 and the hit die size for non-first levels.
    First level always gets the maximum hit die value.
    """

    type: Literal[BuildingBlockType.HEALTH_INCREASE_RANDOM] = (
        BuildingBlockType.HEALTH_INCREASE_RANDOM
    )

    def _get_hit_die_value(self, hit_die: HitDieSize) -> int:
        return _random.randint(1, hit_die.value)
