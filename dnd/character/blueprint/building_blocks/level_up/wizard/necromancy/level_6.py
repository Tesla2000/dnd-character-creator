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


class WizardLevel6Necromancy(
    WizardSubclassFeatureLevelBase[
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.FIFTH], Literal[WizardSubclass.NECROMANCY]
        ],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.SIXTH], Literal[WizardSubclass.NECROMANCY]
        ],
    ]
):
    """Increments wizard to level 6 and grants Necromancy subclass feature."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_6_NECROMANCY] = (
        BuildingBlockType.WIZARD_LEVEL_6_NECROMANCY
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 6}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Undead Thralls",
                        description=(
                            "Animate dead can target one additional corpse or pile of bones. "
                            "Animated undead gain a bonus to damage rolls equal to your "
                            "proficiency bonus and their HP maximum increases by your wizard "
                            "level."
                        ),
                    ),
                ),
            }
        )
