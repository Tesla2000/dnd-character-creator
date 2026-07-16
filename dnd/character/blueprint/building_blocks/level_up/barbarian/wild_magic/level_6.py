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


class BarbarianLevel6WildMagic(
    BarbarianSubclassFeatureLevelBase[
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.FIFTH], BarbarianSubclass],
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.SIXTH], BarbarianSubclass],
    ]
):
    """Grants Wild Magic level 6 subclass feature."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_6_WILD_MAGIC] = (
        BuildingBlockType.BARBARIAN_LEVEL_6_WILD_MAGIC
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 6}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.ACTION,
                        name="Bolstering Magic",
                        description=(
                            "Beginning at 6th level, you can harness your wild magic to "
                            "bolster yourself or a companion. As an action, you can touch "
                            "one creature (which can be yourself) and confer one of the "
                            "following benefits of your choice to that creature: for 10 "
                            "minutes, the creature can roll a d3 whenever it makes an attack "
                            "roll or an ability check and add the number rolled to the d20 "
                            "roll; roll a d3, and the creature regains one expended spell "
                            "slot of a level equal to or less than the number rolled. A "
                            "creature can't be under the effect of this feature more than once "
                            "at a time. You can use this feature a number of times equal to "
                            "your proficiency bonus, and you regain all expended uses when "
                            "you finish a long rest."
                        ),
                    ),
                ),
            }
        )
