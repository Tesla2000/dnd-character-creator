from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.base import (
    BarbarianSubclassFeatureLevelBase,
)
from dnd.character.blueprint.sentinels import ClassSubclassLevel
from dnd.character.blueprint.sentinels import ThirdSubclassPostLevel
from dnd.choices.class_creation.character_class import BarbarianSubclass
from dnd.character.blueprint.states.state import _BPT
from dnd.choices.abilities.action import BasicAction
from dnd.choices.abilities.action_type import ActionType


class BarbarianLevel6StormHerald(
    BarbarianSubclassFeatureLevelBase[
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.FIFTH], BarbarianSubclass],
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.SIXTH], BarbarianSubclass],
    ]
):
    """Grants Storm Herald level 6 subclass feature."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_6_STORM_HERALD] = (
        BuildingBlockType.BARBARIAN_LEVEL_6_STORM_HERALD
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 6}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Storm Soul",
                        description=(
                            "At 6th level, the storm grants you benefits even when your aura "
                            "isn't active. The benefits are based on the environment you chose "
                            "at 3rd level: Desert (fire resistance, no harm from extreme heat), "
                            "Sea (lightning resistance, can breathe underwater, swim speed "
                            "equal to walking speed), Tundra (cold resistance, no harm from "
                            "extreme cold, ground within 10 feet is difficult terrain for enemies)."
                        ),
                    ),
                ),
            }
        )
