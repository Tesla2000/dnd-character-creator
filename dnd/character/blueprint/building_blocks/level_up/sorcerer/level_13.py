from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.sorcerer.base import (
    SorcererSharedLevelBase,
)
from dnd.character.blueprint.sentinels import FirstSubclassPostLevel
from dnd.character.blueprint.states.sorcerer.base import _SBPT


class SorcererLevel13(
    SorcererSharedLevelBase[
        Literal[FirstSubclassPostLevel.TWELFTH],
        Literal[FirstSubclassPostLevel.THIRTEENTH],
    ]
):
    """Increments sorcerer to level 13."""

    type: Literal[BuildingBlockType.SORCERER_LEVEL_13] = (
        BuildingBlockType.SORCERER_LEVEL_13
    )

    def _update_blueprint(self, blueprint: _SBPT) -> _SBPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"sorcerer": 13}),
            }
        )
