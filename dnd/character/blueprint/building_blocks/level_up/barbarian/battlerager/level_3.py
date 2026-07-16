from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.base import (
    BarbarianSubclassAssignLevelBase,
)
from dnd.character.blueprint.states.state import _BPT
from dnd.choices.abilities.action import BasicAction
from dnd.choices.abilities.action_type import ActionType
from dnd.choices.class_creation.character_class import BarbarianSubclass


class BarbarianLevel3Battlerager(
    BarbarianSubclassAssignLevelBase[Literal[BarbarianSubclass.BATTLERAGER]]
):
    """Assigns Path of the Battlerager subclass at level 3."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_3_BATTLERAGER] = (
        BuildingBlockType.BARBARIAN_LEVEL_3_BATTLERAGER
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 3}),
                "subclasses": blueprint.subclasses + (BarbarianSubclass.BATTLERAGER,),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Battlerager Armor",
                        description=(
                            "When you choose this path at 3rd level, you gain the ability to "
                            "use spiked armor as a weapon. While you are wearing spiked armor "
                            "and are raging, you can use a bonus action to make one melee "
                            "weapon attack with the armor spikes against a target within 5 "
                            "feet of you. If the attack hits, the spikes deal 1d4 piercing "
                            "damage. You are proficient with your armor spikes."
                        ),
                    ),
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Spiked Retribution",
                        description=(
                            "Starting at 3rd level, when a creature within 5 feet of you hits "
                            "you with a melee attack, the attacker takes 3 piercing damage if "
                            "you are wearing spiked armor and are raging."
                        ),
                    ),
                ),
            }
        )
