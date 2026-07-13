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


class WizardLevel2Enchantment(
    WizardPreSubclassLevelBase[
        WizardPreSubclassLevel[Literal[SecondSubclassPreLevel.FIRST], None],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.SECOND], Literal[WizardSubclass.ENCHANTMENT]
        ],
    ]
):
    """Increments wizard to level 2 and assigns Enchantment subclass."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_2_ENCHANTMENT] = (
        BuildingBlockType.WIZARD_LEVEL_2_ENCHANTMENT
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 2}),
                "subclasses": blueprint.subclasses + (WizardSubclass.ENCHANTMENT,),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Enchantment Savant",
                        description=(
                            "The gold and time you must spend to copy an enchantment spell "
                            "into your spellbook is halved."
                        ),
                    ),
                    BasicAction(
                        action_type=ActionType.ACTION,
                        name="Hypnotic Gaze",
                        description=(
                            "Choose a creature within 5 feet. It must succeed on a Wisdom "
                            "save against your spell save DC or be charmed until the end of "
                            "your next turn, its speed drops to 0, and it is incapacitated. "
                            "You can extend this each turn as an action. Creatures that "
                            "succeed are immune for 24 hours."
                        ),
                    ),
                ),
            }
        )
