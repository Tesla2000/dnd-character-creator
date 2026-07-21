from typing import ClassVar

from dnd.character._fight_resource import ResourceName
from dnd.character.blueprint.building_blocks.building_block import BuildingBlock
from dnd.character.blueprint.states.state import _BPT
from dnd.choices.class_creation.character_class import Class


class RageUses(BuildingBlock):
    """Sets the barbarian's max rage uses per rest based on class level."""

    _TABLE: ClassVar[tuple[tuple[int, int], ...]] = (
        (1, 2),
        (3, 3),
        (6, 4),
        (12, 5),
        (17, 6),
        (20, 99),
    )

    def apply(self, blueprint: _BPT) -> _BPT:
        level = blueprint.classes.get_level(Class.BARBARIAN)
        uses = max(t for lvl, t in self._TABLE if lvl <= level)
        return blueprint.with_resource_max_uses(ResourceName.RAGE, uses)
