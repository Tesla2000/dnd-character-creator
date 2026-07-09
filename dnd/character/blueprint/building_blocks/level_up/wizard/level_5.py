from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.wizard.base import (
    WizardSharedLevelBase,
)
from dnd.character.blueprint.sentinels import SecondSubclassPostLevel
from dnd.character.blueprint.state import _BPT


class WizardLevel5(
    WizardSharedLevelBase[
        Literal[SecondSubclassPostLevel.FOURTH],
        Literal[SecondSubclassPostLevel.FIFTH],
    ]
):
    """Increments wizard to level 5."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_5] = BuildingBlockType.WIZARD_LEVEL_5

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 5}),
            }
        )
