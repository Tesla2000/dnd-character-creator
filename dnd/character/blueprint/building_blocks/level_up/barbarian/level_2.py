from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.base import (
    BarbarianPreSubclassLevelBase,
)
from dnd.character.blueprint.sentinels import ThirdSubclassPreLevel
from dnd.character.blueprint.states.state import _BPT
from dnd.choices.abilities.action import BasicAction
from dnd.choices.abilities.action_type import ActionType


class BarbarianLevel2(
    BarbarianPreSubclassLevelBase[
        Literal[ThirdSubclassPreLevel.FIRST],
        Literal[ThirdSubclassPreLevel.SECOND],
    ]
):
    """Increments barbarian to level 2."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_2] = (
        BuildingBlockType.BARBARIAN_LEVEL_2
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 2}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Reckless Attack",
                        description=(
                            "When you make your first attack on your turn, you can decide to "
                            "attack recklessly. Doing so gives you advantage on melee weapon "
                            "attack rolls using Strength during this turn, but attack rolls "
                            "against you have advantage until your next turn."
                        ),
                    ),
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Danger Sense",
                        description=(
                            "You have advantage on Dexterity saving throws against effects "
                            "that you can see, such as traps and spells. To gain this benefit, "
                            "you cannot be blinded, deafened, or incapacitated."
                        ),
                    ),
                ),
            }
        )
