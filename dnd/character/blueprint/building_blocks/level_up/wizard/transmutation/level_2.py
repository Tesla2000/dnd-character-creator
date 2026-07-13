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


class WizardLevel2Transmutation(
    WizardPreSubclassLevelBase[
        WizardPreSubclassLevel[Literal[SecondSubclassPreLevel.FIRST], None],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.SECOND],
            Literal[WizardSubclass.TRANSMUTATION],
        ],
    ]
):
    """Increments wizard to level 2 and assigns Transmutation subclass."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_2_TRANSMUTATION] = (
        BuildingBlockType.WIZARD_LEVEL_2_TRANSMUTATION
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 2}),
                "subclasses": blueprint.subclasses + (WizardSubclass.TRANSMUTATION,),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Transmutation Savant",
                        description=(
                            "The gold and time you must spend to copy a transmutation spell "
                            "into your spellbook is halved."
                        ),
                    ),
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Minor Alchemy",
                        description=(
                            "Temporarily alter the physical properties of a nonmagical "
                            "object, transforming it into another material. One hour of work "
                            "transforms one cubic foot. The transformation lasts until you "
                            "take a short or long rest."
                        ),
                    ),
                ),
            }
        )
