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


class BarbarianLevel6Zealot(
    BarbarianSubclassFeatureLevelBase[
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.FIFTH], BarbarianSubclass],
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.SIXTH], BarbarianSubclass],
    ]
):
    """Grants Zealot level 6 subclass feature."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_6_ZEALOT] = (
        BuildingBlockType.BARBARIAN_LEVEL_6_ZEALOT
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 6}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.FREE_ACTION,
                        name="Fanatical Focus",
                        description=(
                            "Starting at 6th level, the divine power that fuels your rage "
                            "can protect you. If you fail a saving throw while you're raging, "
                            "you can reroll it, and you must use the new roll. You can use "
                            "this feature only once per rage."
                        ),
                    ),
                ),
            }
        )
