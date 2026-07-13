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


class SorcererLevel18WildMagic(
    SorcererSubclassFeatureLevelBase[
        SorcererSubclassLevel[
            Literal[FirstSubclassPostLevel.SEVENTEENTH],
            Literal[SorcererSubclass.WILD_MAGIC],
        ],
        SorcererSubclassLevel[
            Literal[FirstSubclassPostLevel.EIGHTEENTH],
            Literal[SorcererSubclass.WILD_MAGIC],
        ],
    ]
):
    """Increments sorcerer to level 18 and grants Wild Magic origin feature."""

    type: Literal[BuildingBlockType.SORCERER_LEVEL_18_WILD_MAGIC] = (
        BuildingBlockType.SORCERER_LEVEL_18_WILD_MAGIC
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"sorcerer": 18}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Spell Bombardment",
                        description=(
                            "When you roll damage for a spell and roll the highest number "
                            "possible on any damage die, choose another die of the same type "
                            "and add its result to the damage. You can do this only once "
                            "per turn."
                        ),
                    ),
                ),
            }
        )
