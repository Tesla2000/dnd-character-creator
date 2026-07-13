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


class WizardLevel10Scribes(
    WizardSubclassFeatureLevelBase[
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.NINTH], Literal[WizardSubclass.SCRIBES]
        ],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.TENTH], Literal[WizardSubclass.SCRIBES]
        ],
    ]
):
    """Increments wizard to level 10 and grants Scribes subclass feature."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_10_SCRIBES] = (
        BuildingBlockType.WIZARD_LEVEL_10_SCRIBES
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 10}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Awakened Spellbook",
                        description=(
                            "Your spellbook becomes a living tome. Once per long rest when "
                            "casting a spell using a spell slot, you can replace its damage "
                            "type with one from another spell in your spellbook. Once per "
                            "turn when casting a 1st-level-or-higher spell, you can add a "
                            "ritual tag for that casting only."
                        ),
                    ),
                ),
            }
        )
