from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.sorcerer.base import (
    SorcererSharedLevelBase,
)
from dnd.character.blueprint.sentinels import FirstSubclassPostLevel
from dnd.character.blueprint.state import _BPT


class SorcererLevel2(
    SorcererSharedLevelBase[
        Literal[FirstSubclassPostLevel.FIRST],
        Literal[FirstSubclassPostLevel.SECOND],
    ]
):
    """Increments sorcerer to level 2."""

    type: Literal[BuildingBlockType.SORCERER_LEVEL_2] = (
        BuildingBlockType.SORCERER_LEVEL_2
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"sorcerer": 2}),
            }
        )
