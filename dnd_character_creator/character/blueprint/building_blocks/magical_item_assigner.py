from __future__ import annotations

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks import (
    BuildingBlock,
)
from dnd_character_creator.character.magical_item.item import MagicalItem


class MagicalItemAssigner(BuildingBlock):
    magical_item: MagicalItem

    def get_change(self, blueprint: Blueprint) -> Blueprint:
        return self.magical_item.assign_to(blueprint)
