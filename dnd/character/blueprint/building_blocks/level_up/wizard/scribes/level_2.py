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


class WizardLevel2Scribes(
    WizardPreSubclassLevelBase[
        WizardPreSubclassLevel[Literal[SecondSubclassPreLevel.FIRST], None],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.SECOND], Literal[WizardSubclass.SCRIBES]
        ],
    ]
):
    """Increments wizard to level 2 and assigns Scribes subclass."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_2_SCRIBES] = (
        BuildingBlockType.WIZARD_LEVEL_2_SCRIBES
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 2}),
                "subclasses": blueprint.subclasses + (WizardSubclass.SCRIBES,),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.FREE_ACTION,
                        name="Wizardly Quill",
                        description=(
                            "Magically create a quill. While holding it you add your "
                            "proficiency bonus to Arcana checks, can use it as a spellcasting "
                            "focus, write twice as fast, and spend 2 minutes to rewrite a "
                            "prepared spell in a different form."
                        ),
                    ),
                    BasicAction(
                        action_type=ActionType.BONUS_ACTION,
                        name="Manifest Mind",
                        description=(
                            "Manifest a spectral presence that can move up to 30 feet as a "
                            "bonus action. You can cast spells as if you were in the "
                            "manifested mind's space. Uses = proficiency bonus per long rest."
                        ),
                    ),
                ),
            }
        )
