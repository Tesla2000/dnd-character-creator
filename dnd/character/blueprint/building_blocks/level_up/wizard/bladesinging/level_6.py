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


class WizardLevel6Bladesinging(
    WizardSubclassFeatureLevelBase[
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.FIFTH], Literal[WizardSubclass.BLADESINGING]
        ],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.SIXTH], Literal[WizardSubclass.BLADESINGING]
        ],
    ]
):
    """Increments wizard to level 6 and grants Bladesinging subclass feature."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_6_BLADESINGING] = (
        BuildingBlockType.WIZARD_LEVEL_6_BLADESINGING
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 6}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Extra Attack",
                        description=(
                            "You can attack twice instead of once when you take the Attack "
                            "action. While your Bladesong is active, one of these attacks "
                            "can be replaced with casting a cantrip."
                        ),
                    ),
                ),
            }
        )
