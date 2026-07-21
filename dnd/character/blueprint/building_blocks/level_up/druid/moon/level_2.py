from typing import Literal

from pydantic import Field

from dnd.character._ability_name import AbilityName
from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.druid.base import (
    DruidPreSubclassLevelBase,
)
from dnd.character.blueprint.building_blocks.level_up.druid.wild_shape_uses import (
    WildShapeUses,
)
from dnd.character.blueprint.sentinels import DruidPreSubclassLevel
from dnd.character.blueprint.sentinels import DruidSubclassLevel
from dnd.character.blueprint.sentinels import SecondSubclassPostLevel
from dnd.character.blueprint.sentinels import SecondSubclassPreLevel
from dnd.character.blueprint.states.state import _BPT
from dnd.choices.class_creation.character_class import DruidSubclass


class DruidLevel2Moon(
    DruidPreSubclassLevelBase[
        DruidPreSubclassLevel[Literal[SecondSubclassPreLevel.FIRST], None],
        DruidSubclassLevel[
            Literal[SecondSubclassPostLevel.SECOND], Literal[DruidSubclass.MOON]
        ],
    ]
):
    """Increments druid to level 2 and assigns Circle of the Moon subclass."""

    type: Literal[BuildingBlockType.DRUID_LEVEL_2_MOON] = (
        BuildingBlockType.DRUID_LEVEL_2_MOON
    )
    wild_shape_uses: WildShapeUses = Field(default_factory=WildShapeUses)

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        result = blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"druid": 2}),
                "subclasses": blueprint.subclasses + (DruidSubclass.MOON,),
                "actions": blueprint.actions
                + (AbilityName.WILD_SHAPE, AbilityName.BEAST_ATTACK),
            }
        )
        return self.wild_shape_uses.apply(result)
