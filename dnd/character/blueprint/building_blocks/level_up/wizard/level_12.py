from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.wizard.base import (
    WizardFeatGrantingLevelBase,
)
from dnd.character.blueprint.sentinels import SecondSubclassPostLevel
from dnd.character.blueprint.states.state import _BPT


class WizardLevel12(
    WizardFeatGrantingLevelBase[
        Literal[SecondSubclassPostLevel.ELEVENTH],
        Literal[SecondSubclassPostLevel.TWELFTH],
    ]
):
    """Increments wizard to level 12 and grants a feat or Ability Score Improvement."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_12] = BuildingBlockType.WIZARD_LEVEL_12

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 12}),
            }
        )
