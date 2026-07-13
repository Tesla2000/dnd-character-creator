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


class WizardLevel6WarMagic(
    WizardSubclassFeatureLevelBase[
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.FIFTH], Literal[WizardSubclass.WAR_MAGIC]
        ],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.SIXTH], Literal[WizardSubclass.WAR_MAGIC]
        ],
    ]
):
    """Increments wizard to level 6 and grants War Magic subclass feature."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_6_WAR_MAGIC] = (
        BuildingBlockType.WIZARD_LEVEL_6_WAR_MAGIC
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 6}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Power Surge",
                        description=(
                            "Store magical energy through your spells. Once per turn when "
                            "you use Arcane Deflection or counterspell, you gain a power "
                            "surge. When you cast a damage-dealing spell, you can expend one "
                            "power surge to deal extra force damage equal to half your wizard "
                            "level."
                        ),
                    ),
                ),
            }
        )
