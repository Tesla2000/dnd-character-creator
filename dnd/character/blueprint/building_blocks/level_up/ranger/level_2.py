from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.ranger.base import (
    RangerSpellcastingLevelBase,
)
from dnd.character.blueprint.sentinels import ClassPreSubclassLevel
from dnd.character.blueprint.sentinels import ThirdSubclassPreLevel
from dnd.character.blueprint.states.state import _BPT
from dnd.choices.abilities.fighting_style import FightingStyle


class RangerLevel2(
    RangerSpellcastingLevelBase[
        ClassPreSubclassLevel[Literal[ThirdSubclassPreLevel.FIRST], None],
        ClassPreSubclassLevel[Literal[ThirdSubclassPreLevel.SECOND], None],
    ]
):
    """Increments ranger to level 2: grants Fighting Style and Spellcasting."""

    type: Literal[BuildingBlockType.RANGER_LEVEL_2] = BuildingBlockType.RANGER_LEVEL_2

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"ranger": 2}),
                "n_fighting_style_choices": blueprint.n_fighting_style_choices + 1,
                "fighting_styles_to_choose_from": frozenset(
                    {
                        FightingStyle.ARCHERY,
                        FightingStyle.DEFENSE,
                        FightingStyle.DUELING,
                    }
                ),
            }
        )
