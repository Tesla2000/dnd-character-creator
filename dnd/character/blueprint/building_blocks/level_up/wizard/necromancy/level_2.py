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


class WizardLevel2Necromancy(
    WizardPreSubclassLevelBase[
        WizardPreSubclassLevel[Literal[SecondSubclassPreLevel.FIRST], None],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.SECOND], Literal[WizardSubclass.NECROMANCY]
        ],
    ]
):
    """Increments wizard to level 2 and assigns Necromancy subclass."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_2_NECROMANCY] = (
        BuildingBlockType.WIZARD_LEVEL_2_NECROMANCY
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 2}),
                "subclasses": blueprint.subclasses + (WizardSubclass.NECROMANCY,),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Necromancy Savant",
                        description=(
                            "The gold and time you must spend to copy a necromancy spell "
                            "into your spellbook is halved."
                        ),
                    ),
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Grim Harvest",
                        description=(
                            "Once per turn when you kill a creature with a spell of 1st "
                            "level or higher, regain HP equal to twice the spell's level, "
                            "or three times its level if the spell is necromancy. Does not "
                            "apply to undead or constructs."
                        ),
                    ),
                ),
            }
        )
