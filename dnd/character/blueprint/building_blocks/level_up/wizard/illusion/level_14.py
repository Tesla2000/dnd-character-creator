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


class WizardLevel14Illusion(
    WizardSubclassFeatureLevelBase[
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.THIRTEENTH],
            Literal[WizardSubclass.ILLUSION],
        ],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.FOURTEENTH],
            Literal[WizardSubclass.ILLUSION],
        ],
    ]
):
    """Increments wizard to level 14 and grants Illusion subclass feature."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_14_ILLUSION] = (
        BuildingBlockType.WIZARD_LEVEL_14_ILLUSION
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 14}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Illusory Reality",
                        description=(
                            "When you cast an illusion spell of 1st level or higher, choose "
                            "one inanimate non-magical object within the spell. That object "
                            "becomes real for 1 minute. Creatures can interact with it, but "
                            "it cannot deal damage or cause conditions."
                        ),
                    ),
                ),
            }
        )
