from typing import Optional

from DND_character_creator.character.blueprint.blueprint import Blueprint
from DND_character_creator.character.blueprint.building_blocks.building_block import \
    BuildingBlock
from DND_character_creator.character.character import Character


class Builder:
    def __init__(self, building_blocks: Optional[list[BuildingBlock]]):
        self._building_blocks = building_blocks or []
    
    def _init_character(self) -> Blueprint:
        return Blueprint()

    def build(self) -> Character:
        blueprint = self._init_character()
        for block in self._building_blocks:
            block.apply(blueprint)
        return self._convert_to_character(blueprint)
    
    def add(self, building_block: BuildingBlock):
        self._building_blocks.append(building_block)

    @staticmethod
    def _convert_to_character(blueprint: Blueprint) -> Character:
        return Character.model_validate(dict(blueprint))
