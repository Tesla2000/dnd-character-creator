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


class WizardLevel2Conjuration(
    WizardPreSubclassLevelBase[
        WizardPreSubclassLevel[Literal[SecondSubclassPreLevel.FIRST], None],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.SECOND], Literal[WizardSubclass.CONJURATION]
        ],
    ]
):
    """Increments wizard to level 2 and assigns Conjuration subclass."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_2_CONJURATION] = (
        BuildingBlockType.WIZARD_LEVEL_2_CONJURATION
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 2}),
                "subclasses": blueprint.subclasses + (WizardSubclass.CONJURATION,),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Conjuration Savant",
                        description=(
                            "The gold and time you must spend to copy a conjuration spell "
                            "into your spellbook is halved."
                        ),
                    ),
                    BasicAction(
                        action_type=ActionType.ACTION,
                        name="Minor Conjuration",
                        description=(
                            "Conjure a Small or smaller inanimate object you have seen. "
                            "It appears in an unoccupied space within 10 feet, lasts 1 hour, "
                            "weighs no more than 10 lbs, and disappears if it takes any "
                            "damage or if you use this feature again."
                        ),
                    ),
                ),
            }
        )
