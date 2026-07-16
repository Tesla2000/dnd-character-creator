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


class BarbarianLevel17(
    BarbarianSharedLevelBase[
        Literal[ThirdSubclassPostLevel.SIXTEENTH],
        Literal[ThirdSubclassPostLevel.SEVENTEENTH],
    ]
):
    """Increments barbarian to level 17."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_17] = (
        BuildingBlockType.BARBARIAN_LEVEL_17
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 17}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Brutal Critical (3 dice)",
                        description=(
                            "At 17th level, you can roll three additional weapon damage dice "
                            "when determining the extra damage for a critical hit with a "
                            "melee attack."
                        ),
                    ),
                ),
            }
        )
