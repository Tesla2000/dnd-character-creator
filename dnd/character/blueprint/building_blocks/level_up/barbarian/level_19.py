from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.base import (
    BarbarianFeatGrantingLevelBase,
)
from dnd.character.blueprint.sentinels import ThirdSubclassPostLevel
from dnd.character.blueprint.states.state import _BPT


class BarbarianLevel19(
    BarbarianFeatGrantingLevelBase[
        Literal[ThirdSubclassPostLevel.EIGHTEENTH],
        Literal[ThirdSubclassPostLevel.NINETEENTH],
    ]
):
    """Increments barbarian to level 19 (feat-granting level)."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_19] = (
        BuildingBlockType.BARBARIAN_LEVEL_19
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 19}),
            }
        )
