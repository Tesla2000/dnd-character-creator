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


class WizardLevel14Necromancy(
    WizardSubclassFeatureLevelBase[
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.THIRTEENTH],
            Literal[WizardSubclass.NECROMANCY],
        ],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.FOURTEENTH],
            Literal[WizardSubclass.NECROMANCY],
        ],
    ]
):
    """Increments wizard to level 14 and grants Necromancy subclass feature."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_14_NECROMANCY] = (
        BuildingBlockType.WIZARD_LEVEL_14_NECROMANCY
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 14}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.ACTION,
                        name="Command Undead",
                        description=(
                            "Choose one undead within 60 feet. If its Intelligence is 8 or "
                            "lower, it must succeed on a Charisma save vs your spell save DC "
                            "or obey your commands for 24 hours. If Intelligence 9+, it has "
                            "advantage on the save. Undead you created automatically fail."
                        ),
                    ),
                ),
            }
        )
