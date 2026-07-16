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


class BarbarianLevel3Beast(
    BarbarianSubclassAssignLevelBase[Literal[BarbarianSubclass.BEAST]]
):
    """Assigns Path of the Beast subclass at level 3."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_3_BEAST] = (
        BuildingBlockType.BARBARIAN_LEVEL_3_BEAST
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 3}),
                "subclasses": blueprint.subclasses + (BarbarianSubclass.BEAST,),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.BONUS_ACTION,
                        name="Form of the Beast",
                        description=(
                            "Starting at 3rd level, when you enter your rage, you can "
                            "transform, revealing the bestial power within you. Until the "
                            "rage ends, you manifest a natural weapon. Choose one: Bite "
                            "(1d8 piercing, you can regain HP equal to the damage on one "
                            "hit per rage), Claws (two attacks when you use the Attack "
                            "action, 1d6 slashing each), or Tail (1d8 piercing, reaction "
                            "to add +1d8 to AC against one attack)."
                        ),
                    ),
                ),
            }
        )
