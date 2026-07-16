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


class BarbarianLevel3AncestralGuardian(
    BarbarianSubclassAssignLevelBase[Literal[BarbarianSubclass.ANCESTRAL_GUARDIAN]]
):
    """Assigns Path of the Ancestral Guardian subclass at level 3."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_3_ANCESTRAL_GUARDIAN] = (
        BuildingBlockType.BARBARIAN_LEVEL_3_ANCESTRAL_GUARDIAN
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 3}),
                "subclasses": blueprint.subclasses
                + (BarbarianSubclass.ANCESTRAL_GUARDIAN,),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Ancestral Protectors",
                        description=(
                            "Starting when you choose this path at 3rd level, spectral warriors "
                            "appear when you enter your rage. While you're raging, the first "
                            "creature you hit with an attack on your turn becomes the target of "
                            "the warriors, which hinder its attacks. Until the start of your "
                            "next turn, that target has disadvantage on any attack roll that "
                            "isn't against you, and when the target hits a creature other than "
                            "you with an attack, that creature has resistance to the damage "
                            "dealt by the attack. The effect on the target ends early if your "
                            "rage ends."
                        ),
                    ),
                ),
            }
        )
