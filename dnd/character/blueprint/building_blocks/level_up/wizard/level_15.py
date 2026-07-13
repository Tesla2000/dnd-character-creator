from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.wizard.base import (
    WizardSharedLevelBase,
)
from dnd.character.blueprint.sentinels import SecondSubclassPostLevel
from dnd.character.blueprint.states.state import _BPT


class WizardLevel15(
    WizardSharedLevelBase[
        Literal[SecondSubclassPostLevel.FOURTEENTH],
        Literal[SecondSubclassPostLevel.FIFTEENTH],
    ]
):
    """Increments wizard to level 15."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_15] = BuildingBlockType.WIZARD_LEVEL_15

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 15}),
            }
        )
