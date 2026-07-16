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


class BarbarianLevel7(
    BarbarianSharedLevelBase[
        Literal[ThirdSubclassPostLevel.SIXTH],
        Literal[ThirdSubclassPostLevel.SEVENTH],
    ]
):
    """Increments barbarian to level 7."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_7] = (
        BuildingBlockType.BARBARIAN_LEVEL_7
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 7}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Feral Instinct",
                        description=(
                            "Your instincts are so honed that you have advantage on initiative "
                            "rolls. Additionally, if you are surprised at the beginning of "
                            "combat and aren't incapacitated, you can act normally on your "
                            "first turn, but only if you enter your rage before doing anything else."
                        ),
                    ),
                ),
            }
        )
