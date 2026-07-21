from typing import Literal

from dnd.character._ability_name import AbilityName
from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.druid.base import (
    DruidSubclassFeatureLevelBase,
)
from dnd.character.blueprint.sentinels import DruidSubclassLevel
from dnd.character.blueprint.sentinels import SecondSubclassPostLevel
from dnd.character.blueprint.states.state import _BPT
from dnd.choices.class_creation.character_class import DruidSubclass


class DruidLevel6Moon(
    DruidSubclassFeatureLevelBase[
        DruidSubclassLevel[
            Literal[SecondSubclassPostLevel.FIFTH], Literal[DruidSubclass.MOON]
        ],
        DruidSubclassLevel[
            Literal[SecondSubclassPostLevel.SIXTH], Literal[DruidSubclass.MOON]
        ],
    ]
):
    """Increments druid to level 6 and grants Circle of the Moon's Primal Strike."""

    type: Literal[BuildingBlockType.DRUID_LEVEL_6_MOON] = (
        BuildingBlockType.DRUID_LEVEL_6_MOON
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"druid": 6}),
                "actions": blueprint.actions + (AbilityName.PRIMAL_STRIKE,),
            }
        )
