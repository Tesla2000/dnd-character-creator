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


class BarbarianLevel3StormHerald(
    BarbarianSubclassAssignLevelBase[Literal[BarbarianSubclass.STORM_HERALD]]
):
    """Assigns Path of the Storm Herald subclass at level 3."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_3_STORM_HERALD] = (
        BuildingBlockType.BARBARIAN_LEVEL_3_STORM_HERALD
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 3}),
                "subclasses": blueprint.subclasses + (BarbarianSubclass.STORM_HERALD,),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.BONUS_ACTION,
                        name="Storm Aura",
                        description=(
                            "Starting at 3rd level, you emanate a stormy, magical aura while "
                            "you rage. The aura extends 10 feet from you in every direction, "
                            "but not through total cover. Choose desert, sea, or tundra when "
                            "you adopt this path. Your aura's effects depend on that chosen "
                            "environment: Desert (fire damage to enemies), Sea (lightning and "
                            "thunder damage), or Tundra (temporary hit points to allies). "
                            "You can use a bonus action to cause the effect to activate again."
                        ),
                    ),
                ),
            }
        )
