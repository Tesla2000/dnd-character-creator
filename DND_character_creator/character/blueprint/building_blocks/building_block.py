from abc import ABC, abstractmethod
from typing import Self

from pydantic import BaseModel

from DND_character_creator.character.blueprint.blueprint import Blueprint
from DND_character_creator.character.character import Character


class BuildingBlock(BaseModel, ABC):
    @abstractmethod
    def apply(self, blueprint: Blueprint) -> None:
        """Modifies character blueprint"""

    def __add__(self, other: Self) -> Self:
        if not isinstance(other, BuildingBlock):
            raise ValueError(f"Only {BuildingBlock.__name__} can be added to another building block. Got {type(other).__name__}")
        class CombinedBlock(BuildingBlock):
            def apply(combined_block, blueprint: Character) -> None:
                self.apply(blueprint)
                other.apply(blueprint)
        return CombinedBlock()