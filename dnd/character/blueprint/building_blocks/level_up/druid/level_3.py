from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.druid.base import (
    DruidSharedLevelBase,
)
from dnd.character.blueprint.sentinels import SecondSubclassPostLevel
from dnd.character.blueprint.states.state import _BPT


class DruidLevel3(
    DruidSharedLevelBase[
        Literal[SecondSubclassPostLevel.SECOND],
        Literal[SecondSubclassPostLevel.THIRD],
    ]
):
    """Increments druid to level 3."""

    type: Literal[BuildingBlockType.DRUID_LEVEL_3] = BuildingBlockType.DRUID_LEVEL_3

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"druid": 3}),
            }
        )
