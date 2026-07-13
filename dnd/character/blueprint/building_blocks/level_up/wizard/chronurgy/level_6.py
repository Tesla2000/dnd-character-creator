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


class WizardLevel6Chronurgy(
    WizardSubclassFeatureLevelBase[
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.FIFTH], Literal[WizardSubclass.CHRONURGY]
        ],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.SIXTH], Literal[WizardSubclass.CHRONURGY]
        ],
    ]
):
    """Increments wizard to level 6 and grants Chronurgy subclass feature."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_6_CHRONURGY] = (
        BuildingBlockType.WIZARD_LEVEL_6_CHRONURGY
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 6}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.ACTION,
                        name="Momentary Stasis",
                        description=(
                            "When a Large or smaller creature ends its turn within 60 feet, "
                            "you can force it to make a Constitution save vs your spell save "
                            "DC. On failure, it is incapacitated and its speed becomes 0 "
                            "until the start of your next turn. Uses = Intelligence modifier "
                            "per long rest."
                        ),
                    ),
                ),
            }
        )
