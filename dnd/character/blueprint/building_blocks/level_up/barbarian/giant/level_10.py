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


class BarbarianLevel10Giant(
    BarbarianSubclassFeatureLevelBase[
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.NINTH], BarbarianSubclass],
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.TENTH], BarbarianSubclass],
    ]
):
    """Grants Giant level 10 subclass feature."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_10_GIANT] = (
        BuildingBlockType.BARBARIAN_LEVEL_10_GIANT
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 10}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.BONUS_ACTION,
                        name="Mighty Impel",
                        description=(
                            "At 10th level, your connection to giant power allows you to hurl "
                            "both allies and enemies on the battlefield. As a bonus action "
                            "while raging, you can choose one Medium or smaller creature "
                            "within your reach and move it to an unoccupied space you can "
                            "see within 30 feet of you. An unwilling creature must succeed "
                            "on a Strength saving throw (DC equal to 8 + your Strength "
                            "modifier + your proficiency bonus) to avoid the effect. If the "
                            "creature would be thrown into a space occupied by another creature "
                            "or an object, both take 2d6 bludgeoning damage."
                        ),
                    ),
                ),
            }
        )
