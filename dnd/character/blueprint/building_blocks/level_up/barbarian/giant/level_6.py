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


class BarbarianLevel6Giant(
    BarbarianSubclassFeatureLevelBase[
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.FIFTH], BarbarianSubclass],
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.SIXTH], BarbarianSubclass],
    ]
):
    """Grants Giant level 6 subclass feature."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_6_GIANT] = (
        BuildingBlockType.BARBARIAN_LEVEL_6_GIANT
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 6}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.BONUS_ACTION,
                        name="Elemental Cleaver",
                        description=(
                            "At 6th level, your bond with the elemental might of giants "
                            "grows, and you learn to infuse weapons with elemental energy. "
                            "When you enter your rage, you can choose one weapon you are "
                            "holding and imbue it with one of the following damage types: "
                            "acid, cold, fire, thunder, or lightning. While raging, the "
                            "chosen weapon deals an extra 1d6 damage of the chosen type on "
                            "a hit. The extra damage is elemental and bypasses resistance "
                            "and immunity to nonmagical damage."
                        ),
                    ),
                ),
            }
        )
