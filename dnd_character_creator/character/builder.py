from __future__ import annotations

from typing import Optional

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock, CombinedBlock,
)
from dnd_character_creator.character.character import Character


class Builder:
    def __init__(self, building_blocks: Optional[list[BuildingBlock]] = None):
        self._building_blocks = building_blocks or []

    def _init_character(self) -> Blueprint:
        return Blueprint()

    def build(self) -> Character:
        blueprint = self._init_character()
        for diff in CombinedBlock(blocks=tuple(self._building_blocks)).get_change(blueprint):
            blueprint = blueprint.model_copy(
                update=diff.model_dump(exclude_unset=True)
            )
        return self._convert_to_character(blueprint)

    def add(self, building_block: BuildingBlock):
        self._building_blocks.append(building_block)

    @staticmethod
    def _convert_to_character(blueprint: Blueprint) -> Character:
        return Character.model_validate(dict(blueprint))
