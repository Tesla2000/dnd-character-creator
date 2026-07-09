from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.wizard.base import (
    WizardSubclassFeatureLevelBase,
)
from dnd.character.blueprint.sentinels import SecondSubclassPostLevel
from dnd.character.blueprint.sentinels import WizardSubclassLevel
from dnd.character.blueprint.state import _BPT
from dnd.choices.class_creation.character_class import WizardSubclass


class WizardLevel14Necromancy(
    WizardSubclassFeatureLevelBase[
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.THIRTEENTH],
            Literal[WizardSubclass.NECROMANCY],
        ],
        WizardSubclassLevel[
            Literal[SecondSubclassPostLevel.FOURTEENTH],
            Literal[WizardSubclass.NECROMANCY],
        ],
    ]
):
    """Increments wizard to level 14 and grants Necromancy subclass feature."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_14_NECROMANCY] = (
        BuildingBlockType.WIZARD_LEVEL_14_NECROMANCY
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 14}),
                # TODO: add Necromancy level-14 subclass feature
            }
        )
