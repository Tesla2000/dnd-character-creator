from __future__ import annotations

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)


class EquipmentAdder(BuildingBlock):
    """Adds an item to the character's other equipment list.

    Appends to existing equipment. Allows duplicates.

    Example:
        >>> builder = Builder([
        ...     EquipmentAdder(item="Rope, hempen (50 feet)"),
        ...     EquipmentAdder(item="Torch"),
        ...     EquipmentAdder(item="Torch"),  # Second torch
        ...     EquipmentAdder(item="Healing potion"),
        ... ])
    """

    item: str

    def _get_change(self, blueprint: Blueprint) -> Blueprint:
        """Add the item to the existing equipment tuple.

        Args:
            blueprint: The current blueprint state.

        Yields:
            Blueprint with the item added.
        """
        existing_equipment = blueprint.other_equipment
        new_equipment = existing_equipment + (self.item,)
        return Blueprint(other_equipment=new_equipment)
