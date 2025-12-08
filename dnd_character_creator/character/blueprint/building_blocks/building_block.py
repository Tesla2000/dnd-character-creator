from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from collections.abc import Generator

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from pydantic import BaseModel
from pydantic import ConfigDict


class BuildingBlock(BaseModel, ABC):
    model_config = ConfigDict(frozen=True)

    def get_change(
        self, blueprint: Blueprint
    ) -> Generator[Blueprint, Blueprint, None]:
        """Yields Blueprint differences to apply.

        Receives the current blueprint state from yield returns,
        allowing decisions based on current state.
        """
        yield self._get_change(blueprint)

    @abstractmethod
    def _get_change(self, blueprint: Blueprint) -> Blueprint:
        """Returns Blueprint differences to apply.

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
                blueprint = yield diff
                if not isinstance(blueprint, Blueprint):
                    raise ValueError(
                        f"{blueprint=} sent to {type(self).__name__} should be an instance of {Blueprint.__name__}"
                    )
                while True:
                    diff = gen.send(blueprint)
                    blueprint = yield diff
            except StopIteration:
                pass

    def _get_change(self, blueprint: Blueprint) -> Blueprint:
        raise ValueError(f"{self._get_change.__name__} ")
