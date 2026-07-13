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


class WizardLevel10Chronurgy(
    WizardSubclassFeatureLevelBase[
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.NINTH], Literal[WizardSubclass.CHRONURGY]
        ],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.TENTH], Literal[WizardSubclass.CHRONURGY]
        ],
    ]
):
    """Increments wizard to level 10 and grants Chronurgy subclass feature."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_10_CHRONURGY] = (
        BuildingBlockType.WIZARD_LEVEL_10_CHRONURGY
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 10}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Arcane Abeyance",
                        description=(
                            "When you cast a spell using a spell slot of 4th level or lower, "
                            "you can condense it into a mote that one willing creature you "
                            "can see can hold. The mote lasts 1 hour, and the holder can "
                            "cast the spell as a bonus action. Only one mote can exist "
                            "at a time."
                        ),
                    ),
                ),
            }
        )
