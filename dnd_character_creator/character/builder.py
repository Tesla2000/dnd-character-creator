from __future__ import annotations

from typing import Self

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    CombinedBlock,
)
from dnd_character_creator.character.character import Character


class Builder:
    def __init__(self, building_blocks: tuple[BuildingBlock, ...] = ()):
        self._building_blocks = building_blocks

    @staticmethod
    def _init_character() -> Blueprint:
        return Blueprint()

    def build(self) -> Character:
        blueprint = self._init_character()
        diff_generator = CombinedBlock(
            blocks=tuple(self._building_blocks)
        ).get_change(blueprint)
        try:
            diff = next(diff_generator)  # Get first diff
            while True:
                blueprint = blueprint.model_copy(
                    update={
                        field_name: field_value
                        for field_name, field_value in diff
                        if field_name in diff.model_fields_set
                    }
                )
                diff = diff_generator.send(
                    blueprint
                )  # Send blueprint back and get next diff
        except StopIteration:
            pass
        return self._convert_to_character(blueprint)

    def add(self, building_block: BuildingBlock) -> Self:
        return type(self)(self._building_blocks + (building_block,))

    @staticmethod
    def _convert_to_character(blueprint: Blueprint) -> Character:
        if (
            blueprint.n_stat_choices
            or blueprint.n_skill_choices
            or blueprint.skills_to_choose_from
            or blueprint.equipment_choices
        ):
            raise ValueError("Blueprint still has corresponding choices")
        return Character.model_validate(
            {
                field_name: field_value
                for field_name, field_value in iter(blueprint)
                if field_name in Character.model_fields
            }
        )
