from typing import Literal

from dnd.character._ability_name import AbilityName
from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.ranger.base import (
    RangerSharedLevelBase,
)
from dnd.character.blueprint.sentinels import ClassSubclassLevel
from dnd.character.blueprint.sentinels import ThirdSubclassPostLevel
from dnd.character.blueprint.states.state import _BPT
from dnd.choices.class_creation.character_class import RangerSubclass


class RangerLevel5(
    RangerSharedLevelBase[
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.FOURTH], RangerSubclass],
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.FIFTH], RangerSubclass],
    ]
):
    """Increments ranger to level 5 and grants Extra Attack."""

    type: Literal[BuildingBlockType.RANGER_LEVEL_5] = BuildingBlockType.RANGER_LEVEL_5

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"ranger": 5}),
                "actions": blueprint.actions + (AbilityName.EXTRA_ATTACK,),
            }
        )
