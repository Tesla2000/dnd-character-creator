from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.wizard.base import (
    WizardPostLevel18FeatGrantingLevelBase,
)
from dnd.character.blueprint.sentinels import SecondSubclassPostLevel
from dnd.character.blueprint.states.state import _BPT


class WizardLevel19(
    WizardPostLevel18FeatGrantingLevelBase[
        Literal[SecondSubclassPostLevel.EIGHTEENTH],
        Literal[SecondSubclassPostLevel.NINETEENTH],
    ]
):
    """Increments wizard to level 19 and grants a feat or Ability Score Improvement."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_19] = BuildingBlockType.WIZARD_LEVEL_19

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 19}),
            }
        )
