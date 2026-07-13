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


class SorcererLevel6StormSorcery(
    SorcererSubclassFeatureLevelBase[
        SorcererSubclassLevel[
            Literal[FirstSubclassPostLevel.FIFTH],
            Literal[SorcererSubclass.STORM_SORCERY],
        ],
        SorcererSubclassLevel[
            Literal[FirstSubclassPostLevel.SIXTH],
            Literal[SorcererSubclass.STORM_SORCERY],
        ],
    ]
):
    """Increments sorcerer to level 6 and grants Storm Sorcery origin feature."""

    type: Literal[BuildingBlockType.SORCERER_LEVEL_6_STORM_SORCERY] = (
        BuildingBlockType.SORCERER_LEVEL_6_STORM_SORCERY
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"sorcerer": 6}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Heart of the Storm",
                        description=(
                            "You gain resistance to lightning and thunder damage. When you "
                            "cast a spell of 1st level or higher dealing lightning or thunder "
                            "damage, each creature within 10 feet takes lightning or thunder "
                            "damage (your choice) equal to half your sorcerer level."
                        ),
                    ),
                ),
            }
        )
