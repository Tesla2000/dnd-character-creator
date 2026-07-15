from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.sorcerer.base import (
    SorcererFeatGrantingLevelBase,
)
from dnd.character.blueprint.sentinels import FirstSubclassPostLevel
from dnd.character.blueprint.states.sorcerer.base import _SBPT


class SorcererLevel16(
    SorcererFeatGrantingLevelBase[
        Literal[FirstSubclassPostLevel.FIFTEENTH],
        Literal[FirstSubclassPostLevel.SIXTEENTH],
    ]
):
    """Increments sorcerer to level 16 and grants a feat or Ability Score Improvement."""

    type: Literal[BuildingBlockType.SORCERER_LEVEL_16] = (
        BuildingBlockType.SORCERER_LEVEL_16
    )

    def _update_blueprint(self, blueprint: _SBPT) -> _SBPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"sorcerer": 16}),
            }
        )
