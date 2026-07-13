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


class WizardLevel14Transmutation(
    WizardSubclassFeatureLevelBase[
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.THIRTEENTH],
            Literal[WizardSubclass.TRANSMUTATION],
        ],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.FOURTEENTH],
            Literal[WizardSubclass.TRANSMUTATION],
        ],
    ]
):
    """Increments wizard to level 14 and grants Transmutation subclass feature."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_14_TRANSMUTATION] = (
        BuildingBlockType.WIZARD_LEVEL_14_TRANSMUTATION
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 14}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.ACTION,
                        name="Master Transmuter",
                        description=(
                            "Consume your transmuter's stone to cast one of: major image, "
                            "passwall, move earth, or polymorph (on a willing target as a "
                            "true polymorph effect), without expending a spell slot."
                        ),
                    ),
                ),
            }
        )
