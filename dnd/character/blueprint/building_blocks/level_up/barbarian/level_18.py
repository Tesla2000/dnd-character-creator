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


class BarbarianLevel18(
    BarbarianSharedLevelBase[
        Literal[ThirdSubclassPostLevel.SEVENTEENTH],
        Literal[ThirdSubclassPostLevel.EIGHTEENTH],
    ]
):
    """Increments barbarian to level 18."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_18] = (
        BuildingBlockType.BARBARIAN_LEVEL_18
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 18}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Indomitable Might",
                        description=(
                            "Beginning at 18th level, if your total for a Strength check is "
                            "less than your Strength score, you can use that score in place "
                            "of the total."
                        ),
                    ),
                ),
            }
        )
