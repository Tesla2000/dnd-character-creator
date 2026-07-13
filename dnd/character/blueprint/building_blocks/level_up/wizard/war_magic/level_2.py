from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.wizard.base import (
    WizardPreSubclassLevelBase,
)
from dnd.character.blueprint.sentinels import SecondSubclassPostLevel
from dnd.character.blueprint.sentinels import SecondSubclassPreLevel
from dnd.character.blueprint.sentinels import WizardPreSubclassLevel
from dnd.character.blueprint.sentinels import WizardSubclassLevel
from dnd.character.blueprint.states.state import _BPT
from dnd.choices.abilities.action import BasicAction
from dnd.choices.abilities.action_type import ActionType
from dnd.choices.class_creation.character_class import WizardSubclass


class WizardLevel2WarMagic(
    WizardPreSubclassLevelBase[
        WizardPreSubclassLevel[Literal[SecondSubclassPreLevel.FIRST], None],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.SECOND], Literal[WizardSubclass.WAR_MAGIC]
        ],
    ]
):
    """Increments wizard to level 2 and assigns War Magic subclass."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_2_WAR_MAGIC] = (
        BuildingBlockType.WIZARD_LEVEL_2_WAR_MAGIC
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 2}),
                "subclasses": blueprint.subclasses + (WizardSubclass.WAR_MAGIC,),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.REACTION,
                        name="Arcane Deflection",
                        description=(
                            "When hit by an attack or you fail a saving throw, gain +2 AC "
                            "against that attack or +4 to that save. If you do, you can only "
                            "cast cantrips until your next turn."
                        ),
                    ),
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Tactical Wit",
                        description=(
                            "Add your Intelligence modifier to your initiative rolls."
                        ),
                    ),
                ),
            }
        )
