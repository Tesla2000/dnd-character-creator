from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.wizard.base import (
    WizardSubclassFeatureLevelBase,
)
from dnd.character.blueprint.sentinels import SecondSubclassPostLevel
from dnd.character.blueprint.sentinels import WizardSubclassLevel
from dnd.character.blueprint.states.state import _BPT
from dnd.choices.abilities.action import BasicAction
from dnd.choices.abilities.action_type import ActionType
from dnd.choices.class_creation.character_class import WizardSubclass


class WizardLevel10Divination(
    WizardSubclassFeatureLevelBase[
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.NINTH], Literal[WizardSubclass.DIVINATION]
        ],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.TENTH], Literal[WizardSubclass.DIVINATION]
        ],
    ]
):
    """Increments wizard to level 10 and grants Divination subclass feature."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_10_DIVINATION] = (
        BuildingBlockType.WIZARD_LEVEL_10_DIVINATION
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 10}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.ACTION,
                        name="Third Eye",
                        description=(
                            "Gain one benefit until incapacitated: darkvision 60 ft, see "
                            "invisible creatures and objects within 10 ft, read any written "
                            "language, or see into the Ethereal Plane up to 60 ft. "
                            "Recharge: short rest."
                        ),
                    ),
                ),
            }
        )
