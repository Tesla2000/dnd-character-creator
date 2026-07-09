from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.sorcerer.base import (
    SorcererSubclassFeatureLevelBase,
)
from dnd.character.blueprint.sentinels import FirstSubclassPostLevel
from dnd.character.blueprint.sentinels import SorcererSubclassLevel
from dnd.character.blueprint.state import _BPT
from dnd.choices.class_creation.character_class import SorcererSubclass


class SorcererLevel14StormSorcery(
    SorcererSubclassFeatureLevelBase[
        SorcererSubclassLevel[
            Literal[FirstSubclassPostLevel.THIRTEENTH],
            Literal[SorcererSubclass.STORM_SORCERY],
        ],
        SorcererSubclassLevel[
            Literal[FirstSubclassPostLevel.FOURTEENTH],
            Literal[SorcererSubclass.STORM_SORCERY],
        ],
    ]
):
    """Increments sorcerer to level 14 and grants Storm Sorcery origin feature."""

    type: Literal[BuildingBlockType.SORCERER_LEVEL_14_STORM_SORCERY] = (
        BuildingBlockType.SORCERER_LEVEL_14_STORM_SORCERY
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"sorcerer": 14}),
                # TODO: add Storm Sorcery level-14 origin feature
            }
        )
