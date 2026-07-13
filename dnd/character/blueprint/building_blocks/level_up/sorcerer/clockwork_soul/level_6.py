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


class SorcererLevel6ClockworkSoul(
    SorcererSubclassFeatureLevelBase[
        SorcererSubclassLevel[
            Literal[FirstSubclassPostLevel.FIFTH],
            Literal[SorcererSubclass.CLOCKWORK_SOUL],
        ],
        SorcererSubclassLevel[
            Literal[FirstSubclassPostLevel.SIXTH],
            Literal[SorcererSubclass.CLOCKWORK_SOUL],
        ],
    ]
):
    """Increments sorcerer to level 6 and grants Clockwork Soul origin feature."""

    type: Literal[BuildingBlockType.SORCERER_LEVEL_6_CLOCKWORK_SOUL] = (
        BuildingBlockType.SORCERER_LEVEL_6_CLOCKWORK_SOUL
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"sorcerer": 6}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Bulwark of Law",
                        description=(
                            "You can imbue a creature with a protective field of d8s equal "
                            "to your proficiency bonus. The creature can expend those dice to "
                            "reduce incoming damage. Recharge: long rest."
                        ),
                    ),
                ),
            }
        )
