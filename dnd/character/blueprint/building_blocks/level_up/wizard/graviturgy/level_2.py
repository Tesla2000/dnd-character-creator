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


class WizardLevel2Graviturgy(
    WizardPreSubclassLevelBase[
        WizardPreSubclassLevel[Literal[SecondSubclassPreLevel.FIRST], None],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.SECOND], Literal[WizardSubclass.GRAVITURGY]
        ],
    ]
):
    """Increments wizard to level 2 and assigns Graviturgy subclass."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_2_GRAVITURGY] = (
        BuildingBlockType.WIZARD_LEVEL_2_GRAVITURGY
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 2}),
                "subclasses": blueprint.subclasses + (WizardSubclass.GRAVITURGY,),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.ACTION,
                        name="Adjust Density",
                        description=(
                            "Alter the weight of one creature or object within 30 feet, "
                            "halving or doubling it for up to 1 minute. Halving causes the "
                            "target's speed to be halved and gives disadvantage on Strength "
                            "checks/saves; doubling halves speed and gives advantage on "
                            "Strength checks/saves. Unwilling creatures can save against "
                            "your spell save DC. Uses = proficiency bonus per long rest."
                        ),
                    ),
                ),
            }
        )
