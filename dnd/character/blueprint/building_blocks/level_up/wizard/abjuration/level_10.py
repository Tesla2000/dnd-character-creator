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


class WizardLevel10Abjuration(
    WizardSubclassFeatureLevelBase[
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.NINTH], Literal[WizardSubclass.ABJURATION]
        ],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.TENTH], Literal[WizardSubclass.ABJURATION]
        ],
    ]
):
    """Increments wizard to level 10 and grants Abjuration subclass feature."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_10_ABJURATION] = (
        BuildingBlockType.WIZARD_LEVEL_10_ABJURATION
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 10}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Improved Abjuration",
                        description=(
                            "When you cast an abjuration spell that requires you to make "
                            "an ability check (such as counterspell or dispel magic), add "
                            "your proficiency bonus to that check."
                        ),
                    ),
                ),
            }
        )
