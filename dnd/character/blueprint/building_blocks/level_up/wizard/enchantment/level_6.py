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


class WizardLevel6Enchantment(
    WizardSubclassFeatureLevelBase[
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.FIFTH], Literal[WizardSubclass.ENCHANTMENT]
        ],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.SIXTH], Literal[WizardSubclass.ENCHANTMENT]
        ],
    ]
):
    """Increments wizard to level 6 and grants Enchantment subclass feature."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_6_ENCHANTMENT] = (
        BuildingBlockType.WIZARD_LEVEL_6_ENCHANTMENT
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 6}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.REACTION,
                        name="Instinctive Charm",
                        description=(
                            "When a creature within 30 feet attacks you, force it to make a "
                            "Wisdom save vs your spell save DC. On failure, it must attack "
                            "another creature of your choice, or if none is available, it "
                            "doesn't attack. On success, it's immune for 24 hours."
                        ),
                    ),
                ),
            }
        )
