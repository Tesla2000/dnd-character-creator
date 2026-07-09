from typing import Literal

from dnd.character.feature.feats import FeatName
from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.sorcerer.base import (
    SorcererSharedLevelBase,
)
from dnd.character.blueprint.sentinels import FirstSubclassPostLevel
from dnd.character.blueprint.state import _BPT


class SorcererLevel16(
    SorcererSharedLevelBase[
        Literal[FirstSubclassPostLevel.FIFTEENTH],
        Literal[FirstSubclassPostLevel.SIXTEENTH],
    ]
):
    """Increments sorcerer to level 16 and grants an Ability Score Improvement."""

    type: Literal[BuildingBlockType.SORCERER_LEVEL_16] = (
        BuildingBlockType.SORCERER_LEVEL_16
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"sorcerer": 16}),
                "feats": blueprint.feats
                + (FeatName.ANY_EXCEPT_ABILITY_SCORE_IMPROVEMENT,),
            }
        )
