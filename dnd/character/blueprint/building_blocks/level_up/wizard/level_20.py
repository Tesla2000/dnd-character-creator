from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.wizard.base import (
    WizardSharedLevelBase,
)
from dnd.character.blueprint.sentinels import SecondSubclassPostLevel
from dnd.character.blueprint.state import _BPT


class WizardLevel20(
    WizardSharedLevelBase[
        Literal[SecondSubclassPostLevel.NINETEENTH],
        Literal[SecondSubclassPostLevel.TWENTIETH],
    ]
):
    """Increments wizard to level 20."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_20] = BuildingBlockType.WIZARD_LEVEL_20

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 20}),
            }
        )
