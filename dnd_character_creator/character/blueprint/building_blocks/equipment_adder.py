from __future__ import annotations

from typing import Generator

from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd_character_creator.character.blueprint.blueprint import Blueprint


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

    def get_change(
        self, blueprint: Blueprint
    ) -> Generator[Blueprint, Blueprint, None]:
        """Add the item to the existing equipment tuple.

        Args:
            blueprint: The current blueprint state.

        Yields:
            Blueprint with the item added.
        """
        existing_equipment = blueprint.other_equipment
        new_equipment = existing_equipment + (self.item,)
        yield Blueprint(other_equipment=new_equipment)
