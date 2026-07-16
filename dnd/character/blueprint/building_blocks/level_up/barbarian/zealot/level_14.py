from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.base import (
    BarbarianSubclassFeatureLevelBase,
)
from dnd.character.blueprint.sentinels import ClassSubclassLevel
from dnd.character.blueprint.sentinels import ThirdSubclassPostLevel
from dnd.choices.class_creation.character_class import BarbarianSubclass
from dnd.character.blueprint.states.state import _BPT
from dnd.choices.abilities.action import BasicAction
from dnd.choices.abilities.action_type import ActionType


class BarbarianLevel14Zealot(
    BarbarianSubclassFeatureLevelBase[
        ClassSubclassLevel[
            Literal[ThirdSubclassPostLevel.THIRTEENTH], BarbarianSubclass
        ],
        ClassSubclassLevel[
            Literal[ThirdSubclassPostLevel.FOURTEENTH], BarbarianSubclass
        ],
    ]
):
    """Grants Zealot level 14 subclass feature."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_14_ZEALOT] = (
        BuildingBlockType.BARBARIAN_LEVEL_14_ZEALOT
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 14}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Rage Beyond Death",
                        description=(
                            "Beginning at 14th level, the divine power that fuels your rage "
                            "allows you to shrug off fatal blows. While you're raging, having "
                            "0 hit points doesn't knock you unconscious. You still must make "
                            "death saving throws, and you suffer the normal effects of taking "
                            "damage while at 0 hit points. However, if you would die due to "
                            "failing death saving throws, you don't die until your rage ends, "
                            "and you die then only if you still have 0 hit points."
                        ),
                    ),
                ),
            }
        )
