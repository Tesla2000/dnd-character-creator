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


class BarbarianLevel14Beast(
    BarbarianSubclassFeatureLevelBase[
        ClassSubclassLevel[
            Literal[ThirdSubclassPostLevel.THIRTEENTH], BarbarianSubclass
        ],
        ClassSubclassLevel[
            Literal[ThirdSubclassPostLevel.FOURTEENTH], BarbarianSubclass
        ],
    ]
):
    """Grants Beast level 14 subclass feature."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_14_BEAST] = (
        BuildingBlockType.BARBARIAN_LEVEL_14_BEAST
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 14}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.BONUS_ACTION,
                        name="Call the Hunt",
                        description=(
                            "At 14th level, the beast within you grows so powerful that you "
                            "can spread its ferocity to others. When you enter your rage, you "
                            "can choose a number of other willing creatures you can see within "
                            "30 feet of you, up to a number equal to your Constitution modifier "
                            "(minimum of one creature). Until the rage ends, each chosen creature "
                            "can add your Rage Damage bonus to their damage rolls with weapons. "
                            "In addition, when you enter your rage, you gain 5 temporary hit "
                            "points for each creature that gains this benefit. You can use this "
                            "feature a number of times equal to your proficiency bonus, and "
                            "you regain all expended uses when you finish a long rest."
                        ),
                    ),
                ),
            }
        )
