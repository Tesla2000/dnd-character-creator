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


class WizardLevel14Enchantment(
    WizardSubclassFeatureLevelBase[
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.THIRTEENTH],
            Literal[WizardSubclass.ENCHANTMENT],
        ],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.FOURTEENTH],
            Literal[WizardSubclass.ENCHANTMENT],
        ],
    ]
):
    """Increments wizard to level 14 and grants Enchantment subclass feature."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_14_ENCHANTMENT] = (
        BuildingBlockType.WIZARD_LEVEL_14_ENCHANTMENT
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 14}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Alter Memories",
                        description=(
                            "When you cast an enchantment spell to charm a humanoid, you "
                            "can make it unaware of your spell. Before the spell ends, you "
                            "can use your action to try to make the target forget part of "
                            "its memories; it forgets up to 1 hour per wizard level on a "
                            "failed Intelligence save."
                        ),
                    ),
                ),
            }
        )
