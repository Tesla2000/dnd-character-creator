from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.wizard.base import (
    WizardSharedLevelBase,
)
from dnd.character.blueprint.sentinels import SecondSubclassPostLevel
from dnd.character.blueprint.state import _BPT


class WizardLevel11(
    WizardSharedLevelBase[
        Literal[SecondSubclassPostLevel.TENTH],
        Literal[SecondSubclassPostLevel.ELEVENTH],
    ]
):
    """Increments wizard to level 11."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_11] = BuildingBlockType.WIZARD_LEVEL_11

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 11}),
            }
        )
