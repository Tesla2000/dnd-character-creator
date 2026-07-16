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


class BarbarianLevel10Zealot(
    BarbarianSubclassFeatureLevelBase[
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.NINTH], BarbarianSubclass],
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.TENTH], BarbarianSubclass],
    ]
):
    """Grants Zealot level 10 subclass feature."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_10_ZEALOT] = (
        BuildingBlockType.BARBARIAN_LEVEL_10_ZEALOT
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 10}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.BONUS_ACTION,
                        name="Zealous Presence",
                        description=(
                            "At 10th level, you learn to channel divine power to inspire "
                            "zealotry in others. As a bonus action, you unleash a battle cry "
                            "infused with divine energy. Up to ten other creatures of your "
                            "choice within 60 feet of you that can hear you gain advantage on "
                            "attack rolls and saving throws until the start of your next turn. "
                            "Once you use this feature, you can't use it again until you "
                            "finish a long rest."
                        ),
                    ),
                ),
            }
        )
