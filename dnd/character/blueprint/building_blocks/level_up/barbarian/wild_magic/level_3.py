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


class BarbarianLevel3WildMagic(
    BarbarianSubclassAssignLevelBase[Literal[BarbarianSubclass.WILD_MAGIC]]
):
    """Assigns Path of Wild Magic subclass at level 3."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_3_WILD_MAGIC] = (
        BuildingBlockType.BARBARIAN_LEVEL_3_WILD_MAGIC
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 3}),
                "subclasses": blueprint.subclasses + (BarbarianSubclass.WILD_MAGIC,),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.ACTION,
                        name="Magic Awareness",
                        description=(
                            "As an action, you can open your awareness to the presence of "
                            "concentrated magic. Until the end of your next turn, you know "
                            "the location of any spell, magic item, or other magical phenomenon "
                            "within 60 feet of you that isn't behind total cover. When you "
                            "sense a spell, you learn which school of magic it belongs to. "
                            "You can use this feature a number of times equal to your "
                            "proficiency bonus, and you regain all expended uses when you "
                            "finish a long rest."
                        ),
                    ),
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Wild Surge",
                        description=(
                            "Also at 3rd level, the magical energy roiling inside you "
                            "sometimes erupts from you. Immediately after you enter your "
                            "rage, roll on the Wild Magic table to determine the magical "
                            "effect produced. If the effect requires a saving throw, the DC "
                            "equals 8 + your proficiency bonus + your Constitution modifier."
                        ),
                    ),
                ),
            }
        )
