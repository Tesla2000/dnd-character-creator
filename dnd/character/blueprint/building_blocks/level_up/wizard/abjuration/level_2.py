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


class WizardLevel2Abjuration(
    WizardPreSubclassLevelBase[
        WizardPreSubclassLevel[Literal[SecondSubclassPreLevel.FIRST], None],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.SECOND], Literal[WizardSubclass.ABJURATION]
        ],
    ]
):
    """Increments wizard to level 2 and assigns Abjuration subclass."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_2_ABJURATION] = (
        BuildingBlockType.WIZARD_LEVEL_2_ABJURATION
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 2}),
                "subclasses": blueprint.subclasses + (WizardSubclass.ABJURATION,),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Abjuration Savant",
                        description=(
                            "The gold and time you must spend to copy an abjuration spell "
                            "into your spellbook is halved."
                        ),
                    ),
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Arcane Ward",
                        description=(
                            "When you cast an abjuration spell of 1st level or higher, you "
                            "create a ward with HP = twice your wizard level + your "
                            "Intelligence modifier. The ward absorbs damage you take first. "
                            "Casting abjuration spells restores the ward."
                        ),
                    ),
                ),
            }
        )
