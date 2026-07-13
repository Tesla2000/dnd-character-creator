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


class WizardLevel14Chronurgy(
    WizardSubclassFeatureLevelBase[
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.THIRTEENTH],
            Literal[WizardSubclass.CHRONURGY],
        ],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.FOURTEENTH],
            Literal[WizardSubclass.CHRONURGY],
        ],
    ]
):
    """Increments wizard to level 14 and grants Chronurgy subclass feature."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_14_CHRONURGY] = (
        BuildingBlockType.WIZARD_LEVEL_14_CHRONURGY
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 14}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.REACTION,
                        name="Convergent Future",
                        description=(
                            "When you or a creature you can see makes an attack, check, or "
                            "save, you can force a reroll. You choose which result to keep. "
                            "Each use gives you one level of exhaustion, which goes away "
                            "when you finish a long rest."
                        ),
                    ),
                ),
            }
        )
