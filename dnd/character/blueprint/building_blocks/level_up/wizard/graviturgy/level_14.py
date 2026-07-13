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


class WizardLevel14Graviturgy(
    WizardSubclassFeatureLevelBase[
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.THIRTEENTH],
            Literal[WizardSubclass.GRAVITURGY],
        ],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.FOURTEENTH],
            Literal[WizardSubclass.GRAVITURGY],
        ],
    ]
):
    """Increments wizard to level 14 and grants Graviturgy subclass feature."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_14_GRAVITURGY] = (
        BuildingBlockType.WIZARD_LEVEL_14_GRAVITURGY
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 14}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Event Horizon",
                        description=(
                            "As a reaction when a creature within 60 feet starts its turn, "
                            "emit a field of gravitic attraction until the start of your next "
                            "turn. Creatures starting their turn within 30 feet must make a "
                            "Strength save or have their speed reduced to 0. Creatures spend "
                            "2 feet of movement per foot moved away from you. "
                            "Recharge: long rest."
                        ),
                    ),
                ),
            }
        )
