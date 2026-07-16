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


class BarbarianLevel3Berserker(
    BarbarianSubclassAssignLevelBase[Literal[BarbarianSubclass.BERSERKER]]
):
    """Assigns Path of the Berserker subclass at level 3."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_3_BERSERKER] = (
        BuildingBlockType.BARBARIAN_LEVEL_3_BERSERKER
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 3}),
                "subclasses": blueprint.subclasses + (BarbarianSubclass.BERSERKER,),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.BONUS_ACTION,
                        name="Frenzy",
                        description=(
                            "Starting when you choose this path at 3rd level, you can go into "
                            "a frenzy when you rage. If you do so, for the duration of your "
                            "rage you can make a single melee weapon attack as a bonus action "
                            "on each of your turns after this one. When your rage ends, you "
                            "suffer one level of exhaustion."
                        ),
                    ),
                ),
            }
        )
