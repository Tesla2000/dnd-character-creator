from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.sorcerer.base import (
    SorcererSubclassFeatureLevelBase,
)
from dnd.character.blueprint.sentinels import FirstSubclassPostLevel
from dnd.character.blueprint.sentinels import SorcererSubclassLevel
from dnd.character.blueprint.states.state import _BPT
from dnd.choices.abilities.action import BasicAction
from dnd.choices.abilities.action_type import ActionType
from dnd.choices.class_creation.character_class import SorcererSubclass


class SorcererLevel14DraconicBloodline(
    SorcererSubclassFeatureLevelBase[
        SorcererSubclassLevel[
            Literal[FirstSubclassPostLevel.THIRTEENTH],
            Literal[SorcererSubclass.DRACONIC_BLOODLINE],
        ],
        SorcererSubclassLevel[
            Literal[FirstSubclassPostLevel.FOURTEENTH],
            Literal[SorcererSubclass.DRACONIC_BLOODLINE],
        ],
    ]
):
    """Increments sorcerer to level 14 and grants Draconic Bloodline origin feature."""

    type: Literal[BuildingBlockType.SORCERER_LEVEL_14_DRACONIC_BLOODLINE] = (
        BuildingBlockType.SORCERER_LEVEL_14_DRACONIC_BLOODLINE
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"sorcerer": 14}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.FREE_ACTION,
                        name="Dragon Wings",
                        description=(
                            "Sprout a pair of dragon wings granting a fly speed of 60 feet "
                            "while not wearing armor. You can dismiss the wings as a bonus "
                            "action."
                        ),
                    ),
                ),
            }
        )
