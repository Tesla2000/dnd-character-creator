from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.druid.base import (
    DruidSharedLevelBase,
)
from dnd.character.blueprint.sentinels import SecondSubclassPostLevel
from dnd.character.blueprint.states.state import _BPT


class DruidLevel5(
    DruidSharedLevelBase[
        Literal[SecondSubclassPostLevel.FOURTH],
        Literal[SecondSubclassPostLevel.FIFTH],
    ]
):
    """Increments druid to level 5."""

    type: Literal[BuildingBlockType.DRUID_LEVEL_5] = BuildingBlockType.DRUID_LEVEL_5

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"druid": 5}),
            }
        )
