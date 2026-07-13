from typing import Literal

from dnd.character.feature.feats import FeatName
from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.sorcerer.base import (
    SorcererSharedLevelBase,
)
from dnd.character.blueprint.sentinels import FirstSubclassPostLevel
from dnd.character.blueprint.states.sorcerer.base import _SBPT


class SorcererLevel4(
    SorcererSharedLevelBase[
        Literal[FirstSubclassPostLevel.THIRD],
        Literal[FirstSubclassPostLevel.FOURTH],
    ]
):
    """Increments sorcerer to level 4 and grants an Ability Score Improvement."""

    type: Literal[BuildingBlockType.SORCERER_LEVEL_4] = (
        BuildingBlockType.SORCERER_LEVEL_4
    )

    def _update_blueprint(self, blueprint: _SBPT) -> _SBPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"sorcerer": 4}),
                "feats": blueprint.feats
                + (FeatName.ANY_EXCEPT_ABILITY_SCORE_IMPROVEMENT,),
            }
        )
