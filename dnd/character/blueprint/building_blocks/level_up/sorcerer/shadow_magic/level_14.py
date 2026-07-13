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


class SorcererLevel14ShadowMagic(
    SorcererSubclassFeatureLevelBase[
        SorcererSubclassLevel[
            Literal[FirstSubclassPostLevel.THIRTEENTH],
            Literal[SorcererSubclass.SHADOW_MAGIC],
        ],
        SorcererSubclassLevel[
            Literal[FirstSubclassPostLevel.FOURTEENTH],
            Literal[SorcererSubclass.SHADOW_MAGIC],
        ],
    ]
):
    """Increments sorcerer to level 14 and grants Shadow Magic origin feature."""

    type: Literal[BuildingBlockType.SORCERER_LEVEL_14_SHADOW_MAGIC] = (
        BuildingBlockType.SORCERER_LEVEL_14_SHADOW_MAGIC
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"sorcerer": 14}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.BONUS_ACTION,
                        name="Shadow Walk",
                        description=(
                            "When you are in dim light or darkness, teleport up to 120 feet "
                            "to an unoccupied space you can see that is also in dim light "
                            "or darkness."
                        ),
                    ),
                ),
            }
        )
