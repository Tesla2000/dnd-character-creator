from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks import (
    BuildingBlock,
)


class NullBlock(BuildingBlock):
    def _get_change(self, blueprint: Blueprint) -> Blueprint:
        return Blueprint()
