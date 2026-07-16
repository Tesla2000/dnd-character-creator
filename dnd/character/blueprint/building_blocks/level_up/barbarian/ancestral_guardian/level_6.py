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


class BarbarianLevel6AncestralGuardian(
    BarbarianSubclassFeatureLevelBase[
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.FIFTH], BarbarianSubclass],
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.SIXTH], BarbarianSubclass],
    ]
):
    """Grants Ancestral Guardian level 6 subclass feature."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_6_ANCESTRAL_GUARDIAN] = (
        BuildingBlockType.BARBARIAN_LEVEL_6_ANCESTRAL_GUARDIAN
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 6}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.REACTION,
                        name="Spirit Shield",
                        description=(
                            "Beginning at 6th level, the guardian spirits that aid you can "
                            "provide supernatural protection to those you defend. If you are "
                            "raging and another creature you can see within 30 feet of you "
                            "takes damage, you can use your reaction to reduce that damage by "
                            "2d6. When you reach certain levels in this class, you can reduce "
                            "the damage by more: 3d6 at 10th level and 4d6 at 14th level."
                        ),
                    ),
                ),
            }
        )
