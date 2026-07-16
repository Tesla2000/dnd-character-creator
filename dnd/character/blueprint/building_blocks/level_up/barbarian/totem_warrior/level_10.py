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


class BarbarianLevel10TotemWarrior(
    BarbarianSubclassFeatureLevelBase[
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.NINTH], BarbarianSubclass],
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.TENTH], BarbarianSubclass],
    ]
):
    """Grants Totem Warrior level 10 subclass feature."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_10_TOTEM_WARRIOR] = (
        BuildingBlockType.BARBARIAN_LEVEL_10_TOTEM_WARRIOR
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 10}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.ACTION,
                        name="Spirit Walker",
                        description=(
                            "At 10th level, you can cast the commune with nature spell, but "
                            "only as a ritual. When you do so, a spiritual version of one of "
                            "the animals you chose for Totem Spirit or Aspect of the Beast "
                            "appears to you to convey the information you seek."
                        ),
                    ),
                ),
            }
        )
