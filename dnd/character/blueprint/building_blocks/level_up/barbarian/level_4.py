from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.base import (
    BarbarianFeatGrantingLevelBase,
)
from dnd.character.blueprint.sentinels import ThirdSubclassPostLevel
from dnd.character.blueprint.states.state import _BPT


class BarbarianLevel4(
    BarbarianFeatGrantingLevelBase[
        Literal[ThirdSubclassPostLevel.THIRD],
        Literal[ThirdSubclassPostLevel.FOURTH],
    ]
):
    """Increments barbarian to level 4 (feat-granting level)."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_4] = (
        BuildingBlockType.BARBARIAN_LEVEL_4
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 4}),
            }
        )
