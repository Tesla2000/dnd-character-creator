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


class WizardLevel6Scribes(
    WizardSubclassFeatureLevelBase[
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.FIFTH], Literal[WizardSubclass.SCRIBES]
        ],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.SIXTH], Literal[WizardSubclass.SCRIBES]
        ],
    ]
):
    """Increments wizard to level 6 and grants Scribes subclass feature."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_6_SCRIBES] = (
        BuildingBlockType.WIZARD_LEVEL_6_SCRIBES
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 6}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Master Scrivener",
                        description=(
                            "Once per long rest, when you study a spell from your spellbook, "
                            "you can create a magical scroll of it at no material cost. The "
                            "scroll uses your spell save DC and attack bonus, doesn't count "
                            "against prepared spells, and crumbles to dust on your next long "
                            "rest."
                        ),
                    ),
                ),
            }
        )
