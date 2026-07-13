from typing import Literal

from dnd.character.feature.feats import FeatName
from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.wizard.base import (
    WizardSharedLevelBase,
)
from dnd.character.blueprint.sentinels import SecondSubclassPostLevel
from dnd.character.blueprint.states.state import _BPT


class WizardLevel8(
    WizardSharedLevelBase[
        Literal[SecondSubclassPostLevel.SEVENTH],
        Literal[SecondSubclassPostLevel.EIGHTH],
    ]
):
    """Increments wizard to level 8 and grants an Ability Score Improvement."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_8] = BuildingBlockType.WIZARD_LEVEL_8

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 8}),
                "feats": blueprint.feats
                + (FeatName.ANY_EXCEPT_ABILITY_SCORE_IMPROVEMENT,),
            }
        )
