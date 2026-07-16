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


class BarbarianLevel11(
    BarbarianSharedLevelBase[
        Literal[ThirdSubclassPostLevel.TENTH],
        Literal[ThirdSubclassPostLevel.ELEVENTH],
    ]
):
    """Increments barbarian to level 11."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_11] = (
        BuildingBlockType.BARBARIAN_LEVEL_11
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 11}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Relentless Rage",
                        description=(
                            "Starting at 11th level, your rage can keep you fighting despite "
                            "grievous wounds. If you drop to 0 hit points while you're raging "
                            "and don't die outright, you can make a DC 10 Constitution saving "
                            "throw. If you succeed, you drop to 1 hit point instead. Each time "
                            "you use this feature after the first, the DC increases by 5. When "
                            "you finish a short or long rest, the DC resets to 10."
                        ),
                    ),
                ),
            }
        )
