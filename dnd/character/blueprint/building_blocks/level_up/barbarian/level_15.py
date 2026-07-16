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


class BarbarianLevel15(
    BarbarianSharedLevelBase[
        Literal[ThirdSubclassPostLevel.FOURTEENTH],
        Literal[ThirdSubclassPostLevel.FIFTEENTH],
    ]
):
    """Increments barbarian to level 15."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_15] = (
        BuildingBlockType.BARBARIAN_LEVEL_15
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 15}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Persistent Rage",
                        description=(
                            "Beginning at 15th level, your rage is so fierce that it ends "
                            "early only if you fall unconscious or if you choose to end it."
                        ),
                    ),
                ),
            }
        )
