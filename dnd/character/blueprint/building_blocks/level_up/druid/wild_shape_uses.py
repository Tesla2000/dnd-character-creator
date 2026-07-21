from typing import ClassVar

from dnd.character._fight_resource import ResourceName
from dnd.character.blueprint.building_blocks.building_block import BuildingBlock
from dnd.character.blueprint.states.state import _BPT
from dnd.choices.class_creation.character_class import Class


class WildShapeUses(BuildingBlock):
    """Sets the druid's max Wild Shape uses per rest based on class level."""

    _TABLE: ClassVar[tuple[tuple[int, int], ...]] = (
        (2, 2),
        (20, 99),
    )

    def apply(self, blueprint: _BPT) -> _BPT:
        level = blueprint.classes.get_level(Class.DRUID)
        uses = max(t for lvl, t in self._TABLE if lvl <= level)
        return blueprint.with_resource_max_uses(ResourceName.WILD_SHAPE, uses)
