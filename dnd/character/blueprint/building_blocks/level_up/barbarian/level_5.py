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


class BarbarianLevel5(
    BarbarianSharedLevelBase[
        Literal[ThirdSubclassPostLevel.FOURTH],
        Literal[ThirdSubclassPostLevel.FIFTH],
    ]
):
    """Increments barbarian to level 5."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_5] = (
        BuildingBlockType.BARBARIAN_LEVEL_5
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 5}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Extra Attack",
                        description=(
                            "You can attack twice, instead of once, whenever you take the "
                            "Attack action on your turn."
                        ),
                    ),
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Fast Movement",
                        description=(
                            "Your speed increases by 10 feet while you aren't wearing heavy armor."
                        ),
                    ),
                ),
            }
        )
