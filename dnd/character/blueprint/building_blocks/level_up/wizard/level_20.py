from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.wizard.base import (
    WizardLevel20UpgradeLevelBase,
)
from dnd.character.blueprint.sentinels import SecondSubclassPostLevel
from dnd.character.blueprint.states.state import _BPT


class WizardLevel20(
    WizardLevel20UpgradeLevelBase[
        Literal[SecondSubclassPostLevel.NINETEENTH],
        Literal[SecondSubclassPostLevel.TWENTIETH],
    ]
):
    """Increments wizard to level 20 and transitions to WizardLevel20Blueprint."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_20] = BuildingBlockType.WIZARD_LEVEL_20

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 20}),
            }
        )
