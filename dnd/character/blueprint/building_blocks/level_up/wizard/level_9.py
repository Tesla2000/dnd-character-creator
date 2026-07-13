from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.wizard.base import (
    WizardSharedLevelBase,
)
from dnd.character.blueprint.sentinels import SecondSubclassPostLevel
from dnd.character.blueprint.states.state import _BPT


class WizardLevel9(
    WizardSharedLevelBase[
        Literal[SecondSubclassPostLevel.EIGHTH],
        Literal[SecondSubclassPostLevel.NINTH],
    ]
):
    """Increments wizard to level 9."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_9] = BuildingBlockType.WIZARD_LEVEL_9

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 9}),
            }
        )
