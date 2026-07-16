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


class BarbarianLevel14Battlerager(
    BarbarianSubclassFeatureLevelBase[
        ClassSubclassLevel[
            Literal[ThirdSubclassPostLevel.THIRTEENTH], BarbarianSubclass
        ],
        ClassSubclassLevel[
            Literal[ThirdSubclassPostLevel.FOURTEENTH], BarbarianSubclass
        ],
    ]
):
    """Grants Battlerager level 14 subclass feature."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_14_BATTLERAGER] = (
        BuildingBlockType.BARBARIAN_LEVEL_14_BATTLERAGER
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 14}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Spiked Retribution (Improved)",
                        description=(
                            "Starting at 14th level, when a creature within 5 feet of you "
                            "hits you with a melee attack, the attacker takes 3 piercing "
                            "damage if you are wearing spiked armor and are raging. In "
                            "addition, the spiked armor bonus action attack now deals 2d4 "
                            "piercing damage instead of 1d4."
                        ),
                    ),
                ),
            }
        )
