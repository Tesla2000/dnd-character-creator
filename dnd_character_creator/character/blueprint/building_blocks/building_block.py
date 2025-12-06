from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import Generator

from pydantic import BaseModel, ConfigDict

from dnd_character_creator.character.blueprint.blueprint import Blueprint


class BuildingBlock(BaseModel, ABC):
    model_config = ConfigDict(frozen=True)

    @abstractmethod
    def get_change(
        self, blueprint: Blueprint
    ) -> Generator[Blueprint, Blueprint, None]:
        """Yields Blueprint differences to apply.

        Receives the current blueprint state from yield returns,
        allowing decisions based on current state.
        """

    def __add__(self, other: BuildingBlock) -> CombinedBlock:
        return CombinedBlock(blocks=(self, other))


class CombinedBlock(BuildingBlock):
    """Combines multiple building blocks to apply sequentially."""

    blocks: tuple[BuildingBlock, ...]

    def get_change(
        self, blueprint: Blueprint
    ) -> Generator[Blueprint, Blueprint, None]:
        """Apply all blocks sequentially, yielding differences."""
        for block in self.blocks:
            gen = block.get_change(blueprint)
            try:
                diff = next(gen)
                current = yield diff
                while True:
                    diff = gen.send(current)
                    current = yield diff
            except StopIteration:
                pass