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


class BarbarianLevel3Giant(
    BarbarianSubclassAssignLevelBase[Literal[BarbarianSubclass.GIANT]]
):
    """Assigns Path of the Giant subclass at level 3."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_3_GIANT] = (
        BuildingBlockType.BARBARIAN_LEVEL_3_GIANT
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 3}),
                "subclasses": blueprint.subclasses + (BarbarianSubclass.GIANT,),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.BONUS_ACTION,
                        name="Giant's Power",
                        description=(
                            "At 3rd level, you learn the Giant language. You also learn a "
                            "minor magical trick tied to Giant magic: you learn one cantrip of "
                            "your choice from the druid or sorcerer spell list, using "
                            "Constitution as your spellcasting ability."
                        ),
                    ),
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Giant's Havoc",
                        description=(
                            "Also at 3rd level, your rage imbues you with the might of a "
                            "giant. While raging, you gain the following benefits: your reach "
                            "increases by 5 feet, and your size increases by one category "
                            "(from Medium to Large, for example)."
                        ),
                    ),
                ),
            }
        )
