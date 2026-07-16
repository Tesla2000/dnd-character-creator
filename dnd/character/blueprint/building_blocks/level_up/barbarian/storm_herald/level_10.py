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


class BarbarianLevel10StormHerald(
    BarbarianSubclassFeatureLevelBase[
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.NINTH], BarbarianSubclass],
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.TENTH], BarbarianSubclass],
    ]
):
    """Grants Storm Herald level 10 subclass feature."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_10_STORM_HERALD] = (
        BuildingBlockType.BARBARIAN_LEVEL_10_STORM_HERALD
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 10}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Shielding Storm",
                        description=(
                            "At 10th level, you learn to use your mastery of the storm to "
                            "protect others. Each creature of your choice has the damage "
                            "resistance you gained from the Storm Soul feature while the "
                            "creature is in your Storm Aura."
                        ),
                    ),
                ),
            }
        )
