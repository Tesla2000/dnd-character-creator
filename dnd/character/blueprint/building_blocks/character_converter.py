from __future__ import annotations

from typing import Literal

from dnd.character.blueprint.building_blocks.building_block import BuildingBlock
from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.character_data import CharacterData
from dnd.character.blueprint.sentinels import AnyClassLevel
from dnd.character.blueprint.sentinels import AnySorcererLevel
from dnd.character.blueprint.sentinels import AnyWizardLevel
from dnd.character.blueprint.state import Blueprint
from dnd.character.presentable_character import PresentableCharacter
from dnd.character.race.race import Race
from dnd.character.stats import Stats
from pydantic import PositiveInt


class CharacterConverter(BuildingBlock):
    """Seals a fully resolved Blueprint into a PresentableCharacter."""

    type: Literal[BuildingBlockType.CHARACTER_CONVERTER] = (
        BuildingBlockType.CHARACTER_CONVERTER
    )

    def apply(
        self,
        blueprint: Blueprint[
            Race,
            Stats,
            PositiveInt,
            Literal[0],
            Literal[0],
            AnyWizardLevel,
            AnySorcererLevel,
            AnyClassLevel,
            AnyClassLevel,
            AnyClassLevel,
            AnyClassLevel,
            AnyClassLevel,
            AnyClassLevel,
            AnyClassLevel,
            AnyClassLevel,
            AnyClassLevel,
            AnyClassLevel,
            AnyClassLevel,
            CharacterData,
        ],
    ) -> PresentableCharacter:
        return PresentableCharacter.model_validate(dict(blueprint))
