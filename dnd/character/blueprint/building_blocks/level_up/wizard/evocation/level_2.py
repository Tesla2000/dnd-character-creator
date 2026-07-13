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


class WizardLevel2Evocation(
    WizardPreSubclassLevelBase[
        WizardPreSubclassLevel[Literal[SecondSubclassPreLevel.FIRST], None],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.SECOND], Literal[WizardSubclass.EVOCATION]
        ],
    ]
):
    """Increments wizard to level 2 and assigns Evocation subclass."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_2_EVOCATION] = (
        BuildingBlockType.WIZARD_LEVEL_2_EVOCATION
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 2}),
                "subclasses": blueprint.subclasses + (WizardSubclass.EVOCATION,),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Evocation Savant",
                        description=(
                            "The gold and time you must spend to copy an evocation spell "
                            "into your spellbook is halved."
                        ),
                    ),
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Sculpt Spells",
                        description=(
                            "When you cast an evocation spell affecting other creatures you "
                            "can see, choose a number of them equal to 1 + the spell's level. "
                            "They automatically succeed on saving throws against the spell "
                            "and take no damage if they would normally take half damage."
                        ),
                    ),
                ),
            }
        )
