from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.base import (
    BarbarianFeatGrantingLevelBase,
)
from dnd.character.blueprint.sentinels import ThirdSubclassPostLevel
from dnd.character.blueprint.states.state import _BPT


class BarbarianLevel12(
    BarbarianFeatGrantingLevelBase[
        Literal[ThirdSubclassPostLevel.ELEVENTH],
        Literal[ThirdSubclassPostLevel.TWELFTH],
    ]
):
    """Increments barbarian to level 12 (feat-granting level)."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_12] = (
        BuildingBlockType.BARBARIAN_LEVEL_12
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 12}),
            }
        )
