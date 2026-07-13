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


class WizardLevel6Divination(
    WizardSubclassFeatureLevelBase[
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.FIFTH], Literal[WizardSubclass.DIVINATION]
        ],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.SIXTH], Literal[WizardSubclass.DIVINATION]
        ],
    ]
):
    """Increments wizard to level 6 and grants Divination subclass feature."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_6_DIVINATION] = (
        BuildingBlockType.WIZARD_LEVEL_6_DIVINATION
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 6}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Expert Divination",
                        description=(
                            "When you cast a divination spell of 2nd level or higher using "
                            "a spell slot, you regain one expended spell slot. The recovered "
                            "slot must be of lower level than the spell and can be no higher "
                            "than 5th level."
                        ),
                    ),
                ),
            }
        )
