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


class WizardLevel10Enchantment(
    WizardSubclassFeatureLevelBase[
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.NINTH], Literal[WizardSubclass.ENCHANTMENT]
        ],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.TENTH], Literal[WizardSubclass.ENCHANTMENT]
        ],
    ]
):
    """Increments wizard to level 10 and grants Enchantment subclass feature."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_10_ENCHANTMENT] = (
        BuildingBlockType.WIZARD_LEVEL_10_ENCHANTMENT
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 10}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Split Enchantment",
                        description=(
                            "When you cast an enchantment spell of 1st level or higher "
                            "that targets only one creature, you can have it target a "
                            "second creature."
                        ),
                    ),
                ),
            }
        )
