from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.ranger.base import (
    RangerFeatGrantingLevelBase,
)
from dnd.character.blueprint.sentinels import ClassSubclassLevel
from dnd.character.blueprint.sentinels import ThirdSubclassPostLevel
from dnd.character.blueprint.states.state import _BPT
from dnd.choices.class_creation.character_class import RangerSubclass


class RangerLevel4(
    RangerFeatGrantingLevelBase[
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.THIRD], RangerSubclass],
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.FOURTH], RangerSubclass],
    ]
):
    """Increments ranger to level 4 and grants an Ability Score Improvement."""

    type: Literal[BuildingBlockType.RANGER_LEVEL_4] = BuildingBlockType.RANGER_LEVEL_4

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"ranger": 4}),
            }
        )
