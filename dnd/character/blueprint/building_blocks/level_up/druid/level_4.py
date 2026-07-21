from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.druid.base import (
    DruidFeatGrantingLevelBase,
)
from dnd.character.blueprint.sentinels import SecondSubclassPostLevel
from dnd.character.blueprint.states.state import _BPT


class DruidLevel4(
    DruidFeatGrantingLevelBase[
        Literal[SecondSubclassPostLevel.THIRD],
        Literal[SecondSubclassPostLevel.FOURTH],
    ]
):
    """Increments druid to level 4 and grants a feat or Ability Score Improvement."""

    type: Literal[BuildingBlockType.DRUID_LEVEL_4] = BuildingBlockType.DRUID_LEVEL_4

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"druid": 4}),
            }
        )
