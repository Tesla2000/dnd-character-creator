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


class WizardLevel14Evocation(
    WizardSubclassFeatureLevelBase[
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.THIRTEENTH],
            Literal[WizardSubclass.EVOCATION],
        ],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.FOURTEENTH],
            Literal[WizardSubclass.EVOCATION],
        ],
    ]
):
    """Increments wizard to level 14 and grants Evocation subclass feature."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_14_EVOCATION] = (
        BuildingBlockType.WIZARD_LEVEL_14_EVOCATION
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 14}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Overchannel",
                        description=(
                            "When you cast a wizard spell of 1st–5th level that deals "
                            "damage, you can deal maximum damage. The first time per long "
                            "rest you do so, you suffer no ill effect. Each subsequent time, "
                            "you take 2d12 necrotic damage per spell level. This damage "
                            "cannot be reduced or prevented."
                        ),
                    ),
                ),
            }
        )
