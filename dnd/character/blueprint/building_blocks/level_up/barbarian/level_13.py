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


class BarbarianLevel13(
    BarbarianSharedLevelBase[
        Literal[ThirdSubclassPostLevel.TWELFTH],
        Literal[ThirdSubclassPostLevel.THIRTEENTH],
    ]
):
    """Increments barbarian to level 13."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_13] = (
        BuildingBlockType.BARBARIAN_LEVEL_13
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 13}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Brutal Critical (2 dice)",
                        description=(
                            "At 13th level, you can roll two additional weapon damage dice "
                            "when determining the extra damage for a critical hit with a "
                            "melee attack."
                        ),
                    ),
                ),
            }
        )
