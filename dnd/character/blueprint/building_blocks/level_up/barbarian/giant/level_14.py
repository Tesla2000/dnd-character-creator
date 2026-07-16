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


class BarbarianLevel14Giant(
    BarbarianSubclassFeatureLevelBase[
        ClassSubclassLevel[
            Literal[ThirdSubclassPostLevel.THIRTEENTH], BarbarianSubclass
        ],
        ClassSubclassLevel[
            Literal[ThirdSubclassPostLevel.FOURTEENTH], BarbarianSubclass
        ],
    ]
):
    """Grants Giant level 14 subclass feature."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_14_GIANT] = (
        BuildingBlockType.BARBARIAN_LEVEL_14_GIANT
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 14}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Demiurgic Colossus",
                        description=(
                            "At 14th level, the giant power you wield grows beyond measure. "
                            "When you rage, your size can increase to Huge. Your reach "
                            "increases by 10 feet (rather than 5 feet). In addition, the "
                            "die for your Mighty Impel increases to d8, and the range "
                            "increases to 60 feet."
                        ),
                    ),
                ),
            }
        )
