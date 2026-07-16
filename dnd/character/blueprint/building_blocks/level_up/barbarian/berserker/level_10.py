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


class BarbarianLevel10Berserker(
    BarbarianSubclassFeatureLevelBase[
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.NINTH], BarbarianSubclass],
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.TENTH], BarbarianSubclass],
    ]
):
    """Grants Berserker level 10 subclass feature."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_10_BERSERKER] = (
        BuildingBlockType.BARBARIAN_LEVEL_10_BERSERKER
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 10}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.ACTION,
                        name="Intimidating Presence",
                        description=(
                            "Beginning at 10th level, you can use your action to frighten "
                            "someone with your menacing presence. When you do so, choose one "
                            "creature that you can see within 30 feet of you. If the creature "
                            "can see or hear you, it must succeed on a Wisdom saving throw "
                            "(DC equal to 8 + your proficiency bonus + your Charisma modifier) "
                            "or be frightened of you until the end of your next turn. On "
                            "subsequent turns, you can use your action to extend the duration "
                            "of this effect on the frightened creature until the end of your "
                            "next turn. This effect ends if the creature ends its turn out of "
                            "line of sight or more than 60 feet away from you."
                        ),
                    ),
                ),
            }
        )
