from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.base import (
    BarbarianSharedLevelBase,
)
from dnd.character.blueprint.sentinels import ThirdSubclassPostLevel
from dnd.character.blueprint.states.state import _BPT
from dnd.choices.abilities.action import BasicAction
from dnd.choices.abilities.action_type import ActionType


class BarbarianLevel9(
    BarbarianSharedLevelBase[
        Literal[ThirdSubclassPostLevel.EIGHTH],
        Literal[ThirdSubclassPostLevel.NINTH],
    ]
):
    """Increments barbarian to level 9."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_9] = (
        BuildingBlockType.BARBARIAN_LEVEL_9
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 9}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Brutal Critical (1 die)",
                        description=(
                            "Beginning at 9th level, you can roll one additional weapon damage "
                            "die when determining the extra damage for a critical hit with a "
                            "melee attack."
                        ),
                    ),
                ),
            }
        )
