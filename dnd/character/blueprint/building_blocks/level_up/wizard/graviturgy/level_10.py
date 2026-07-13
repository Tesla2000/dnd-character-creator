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


class WizardLevel10Graviturgy(
    WizardSubclassFeatureLevelBase[
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.NINTH], Literal[WizardSubclass.GRAVITURGY]
        ],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.TENTH], Literal[WizardSubclass.GRAVITURGY]
        ],
    ]
):
    """Increments wizard to level 10 and grants Graviturgy subclass feature."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_10_GRAVITURGY] = (
        BuildingBlockType.WIZARD_LEVEL_10_GRAVITURGY
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 10}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.REACTION,
                        name="Violent Attraction",
                        description=(
                            "When a creature within 60 feet falls or is moved by a "
                            "non-magical effect, you can increase the damage or force dealt "
                            "by that movement by 2d10. Uses = Intelligence modifier per "
                            "long rest."
                        ),
                    ),
                ),
            }
        )
