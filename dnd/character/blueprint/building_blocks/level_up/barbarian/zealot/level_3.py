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


class BarbarianLevel3Zealot(
    BarbarianSubclassAssignLevelBase[Literal[BarbarianSubclass.ZEALOT]]
):
    """Assigns Path of the Zealot subclass at level 3."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_3_ZEALOT] = (
        BuildingBlockType.BARBARIAN_LEVEL_3_ZEALOT
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 3}),
                "subclasses": blueprint.subclasses + (BarbarianSubclass.ZEALOT,),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Divine Fury",
                        description=(
                            "Starting when you choose this path at 3rd level, you can channel "
                            "divine fury into your weapon strikes. While you're raging, the "
                            "first creature you hit on each of your turns with a weapon attack "
                            "takes extra necrotic or radiant damage (your choice when you gain "
                            "this feature) equal to 1d6 + half your barbarian level."
                        ),
                    ),
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Warrior of the Gods",
                        description=(
                            "At 3rd level, your soul is marked for endless battle. If a spell, "
                            "such as raise dead, has the sole effect of restoring you to life "
                            "(but not undeath), the caster doesn't need material components to "
                            "cast the spell on you."
                        ),
                    ),
                ),
            }
        )
