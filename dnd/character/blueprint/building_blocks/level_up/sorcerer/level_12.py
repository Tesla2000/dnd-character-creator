from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.sorcerer.base import (
    SorcererFeatGrantingLevelBase,
)
from dnd.character.blueprint.sentinels import FirstSubclassPostLevel
from dnd.character.blueprint.states.sorcerer.base import _SBPT


class SorcererLevel12(
    SorcererFeatGrantingLevelBase[
        Literal[FirstSubclassPostLevel.ELEVENTH],
        Literal[FirstSubclassPostLevel.TWELFTH],
    ]
):
    """Increments sorcerer to level 12 and grants a feat or Ability Score Improvement."""

    type: Literal[BuildingBlockType.SORCERER_LEVEL_12] = (
        BuildingBlockType.SORCERER_LEVEL_12
    )

    def _update_blueprint(self, blueprint: _SBPT) -> _SBPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"sorcerer": 12}),
            }
        )
