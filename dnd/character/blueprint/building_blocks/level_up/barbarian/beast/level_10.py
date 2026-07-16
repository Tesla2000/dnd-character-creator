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


class BarbarianLevel10Beast(
    BarbarianSubclassFeatureLevelBase[
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.NINTH], BarbarianSubclass],
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.TENTH], BarbarianSubclass],
    ]
):
    """Grants Beast level 10 subclass feature."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_10_BEAST] = (
        BuildingBlockType.BARBARIAN_LEVEL_10_BEAST
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 10}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Infectious Fury",
                        description=(
                            "At 10th level, when you hit a creature with your natural weapons "
                            "while in your Form of the Beast, the bestial spirit within you "
                            "can curse your target with rabid fury. The target must succeed on "
                            "a Wisdom saving throw (DC equal to 8 + your Constitution modifier "
                            "+ your proficiency bonus) or suffer one of the following effects "
                            "(your choice): the target must use its reaction to make a melee "
                            "attack against another creature of your choice that you can see, "
                            "or the target takes 2d12 psychic damage. You can use this feature "
                            "a number of times equal to your proficiency bonus, and you regain "
                            "all expended uses when you finish a long rest."
                        ),
                    ),
                ),
            }
        )
