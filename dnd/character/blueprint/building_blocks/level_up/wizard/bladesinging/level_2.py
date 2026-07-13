from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.wizard.base import (
    WizardPreSubclassLevelBase,
)
from dnd.character.blueprint.sentinels import SecondSubclassPostLevel
from dnd.character.blueprint.sentinels import SecondSubclassPreLevel
from dnd.character.blueprint.sentinels import WizardPreSubclassLevel
from dnd.character.blueprint.sentinels import WizardSubclassLevel
from dnd.character.blueprint.states.state import _BPT
from dnd.choices.abilities.action import BasicAction
from dnd.choices.abilities.action_type import ActionType
from dnd.choices.class_creation.character_class import WizardSubclass


class WizardLevel2Bladesinging(
    WizardPreSubclassLevelBase[
        WizardPreSubclassLevel[Literal[SecondSubclassPreLevel.FIRST], None],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.SECOND],
            Literal[WizardSubclass.BLADESINGING],
        ],
    ]
):
    """Increments wizard to level 2 and assigns Bladesinging subclass."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_2_BLADESINGING] = (
        BuildingBlockType.WIZARD_LEVEL_2_BLADESINGING
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 2}),
                "subclasses": blueprint.subclasses + (WizardSubclass.BLADESINGING,),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Training in War and Song",
                        description=(
                            "You gain proficiency with light armor and one one-handed melee "
                            "weapon of your choice."
                        ),
                    ),
                    BasicAction(
                        action_type=ActionType.BONUS_ACTION,
                        name="Bladesong",
                        description=(
                            "Invoke the bladesong for 1 minute: AC bonus = INT modifier, "
                            "+10 ft walking speed, advantage on Dexterity (Acrobatics) "
                            "checks, and bonus to concentration checks = INT modifier. "
                            "Ends if you wear medium/heavy armor or shield, are incapacitated, "
                            "or use two hands to attack. Uses = proficiency bonus per long rest."
                        ),
                    ),
                ),
            }
        )
