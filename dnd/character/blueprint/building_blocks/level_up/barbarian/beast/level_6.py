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


class BarbarianLevel6Beast(
    BarbarianSubclassFeatureLevelBase[
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.FIFTH], BarbarianSubclass],
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.SIXTH], BarbarianSubclass],
    ]
):
    """Grants Beast level 6 subclass feature."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_6_BEAST] = (
        BuildingBlockType.BARBARIAN_LEVEL_6_BEAST
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 6}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Bestial Soul",
                        description=(
                            "Beginning at 6th level, the feral power within you increases, "
                            "causing the natural weapons of your Form of the Beast to count "
                            "as magical for the purpose of overcoming immunity and resistance "
                            "to nonmagical attacks and damage. You can also alter your form "
                            "to help you adapt to your surroundings: a swim speed equal to "
                            "your walking speed and the ability to breathe underwater, or a "
                            "climbing speed equal to your walking speed, or the ability to "
                            "jump three times the normal distance."
                        ),
                    ),
                ),
            }
        )
