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


class SorcererLevel19(
    SorcererSharedLevelBase[
        Literal[FirstSubclassPostLevel.EIGHTEENTH],
        Literal[FirstSubclassPostLevel.NINETEENTH],
    ]
):
    """Increments sorcerer to level 19 and grants an Ability Score Improvement."""

    type: Literal[BuildingBlockType.SORCERER_LEVEL_19] = (
        BuildingBlockType.SORCERER_LEVEL_19
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"sorcerer": 19}),
                "feats": blueprint.feats
                + (FeatName.ANY_EXCEPT_ABILITY_SCORE_IMPROVEMENT,),
            }
        )
