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


class SorcererLevel14AberrantMind(
    SorcererSubclassFeatureLevelBase[
        SorcererSubclassLevel[
            Literal[FirstSubclassPostLevel.THIRTEENTH],
            Literal[SorcererSubclass.ABERRANT_MIND],
        ],
        SorcererSubclassLevel[
            Literal[FirstSubclassPostLevel.FOURTEENTH],
            Literal[SorcererSubclass.ABERRANT_MIND],
        ],
    ]
):
    """Increments sorcerer to level 14 and grants Aberrant Mind origin feature."""

    type: Literal[BuildingBlockType.SORCERER_LEVEL_14_ABERRANT_MIND] = (
        BuildingBlockType.SORCERER_LEVEL_14_ABERRANT_MIND
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"sorcerer": 14}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.BONUS_ACTION,
                        name="Revelation in Flesh",
                        description=(
                            "Spend 1 or more sorcery points (up to your proficiency bonus) "
                            "to gain benefits for 10 minutes: fly speed 40 ft, swim speed "
                            "equal to walk speed and water breathing, blindsight 30 ft, or "
                            "move through objects and creatures as difficult terrain."
                        ),
                    ),
                ),
            }
        )
