from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.sorcerer.base import (
    SorcererSharedLevelBase,
)
from dnd.character.blueprint.sentinels import FirstSubclassPostLevel
from dnd.character.blueprint.states.sorcerer.base import _SBPT
from dnd.choices.abilities.action import BasicAction
from dnd.choices.abilities.action_type import ActionType


class SorcererLevel2(
    SorcererSharedLevelBase[
        Literal[FirstSubclassPostLevel.FIRST],
        Literal[FirstSubclassPostLevel.SECOND],
    ]
):
    """Increments sorcerer to level 2."""

    type: Literal[BuildingBlockType.SORCERER_LEVEL_2] = (
        BuildingBlockType.SORCERER_LEVEL_2
    )

    def _update_blueprint(self, blueprint: _SBPT) -> _SBPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"sorcerer": 2}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Font of Magic",
                        description=(
                            "You have a pool of sorcery points equal to your sorcerer level. "
                            "You can spend sorcery points to create spell slots or convert "
                            "spent spell slots to sorcery points. You regain all sorcery "
                            "points on a long rest."
                        ),
                    ),
                    BasicAction(
                        action_type=ActionType.ACTION,
                        name="Flexible Casting",
                        description=(
                            "You can use your action to convert sorcery points into spell "
                            "slots (2 points = 1st-level, 3 = 2nd, 5 = 3rd, 6 = 4th, "
                            "7 = 5th), or convert an unexpended spell slot into sorcery "
                            "points equal to the slot's level."
                        ),
                    ),
                ),
            }
        )
