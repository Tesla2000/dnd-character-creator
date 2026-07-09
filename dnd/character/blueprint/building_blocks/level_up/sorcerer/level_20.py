from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.sorcerer.base import (
    SorcererSharedLevelBase,
)
from dnd.character.blueprint.sentinels import FirstSubclassPostLevel
from dnd.character.blueprint.state import _BPT


class SorcererLevel20(
    SorcererSharedLevelBase[
        Literal[FirstSubclassPostLevel.NINETEENTH],
        Literal[FirstSubclassPostLevel.TWENTIETH],
    ]
):
    """Increments sorcerer to level 20."""

    type: Literal[BuildingBlockType.SORCERER_LEVEL_20] = (
        BuildingBlockType.SORCERER_LEVEL_20
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"sorcerer": 20}),
            }
        )
