from __future__ import annotations

from typing import NamedTuple
from typing import Optional
from typing import Self

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    CombinedBlock,
)
from dnd_character_creator.character.character import Character
from dnd_character_creator.character.checkpoint import Increment
from dnd_character_creator.character.checkpoint import IncrementChain
from dnd_character_creator.character.checkpoint import IncrementStorage
from dnd_character_creator.character.checkpoint import InMemoryIncrementStorage
from dnd_character_creator.character.presentable_character import (
    PresentableCharacter,
)


class BuildResult(NamedTuple):
    """Result of building a character with increment tracking."""

    character: PresentableCharacter
    chain_id: str


class Builder:
    def __init__(
        self,
        building_blocks: tuple[BuildingBlock, ...] = (),
        increment_storage: Optional[IncrementStorage] = None,
    ):
        self._building_blocks = building_blocks
        self._increment_storage = (
            increment_storage or InMemoryIncrementStorage()
        )

    @staticmethod
    def _init_character() -> Blueprint:
        return Blueprint()

    def build(self) -> BuildResult:
        """Build character with automatic increment tracking.

        Returns:
            BuildResult containing the character and chain_id for accessing increments
        """
        blueprint = self._init_character()
        diff_generator = CombinedBlock(
            blocks=tuple(self._building_blocks)
        ).get_change(blueprint)

        increment_chain = IncrementChain()
        building_block_index = 0

        try:
            diff = next(diff_generator)
            while True:
                blueprint = blueprint.add_diff(diff)

                increment = Increment(
                    index=building_block_index,
                    blueprint_state=blueprint,
                    diff=diff,
                )
                increment_chain = increment_chain.add_increment(increment)

                building_block_index += 1
                diff = diff_generator.send(blueprint)
        except StopIteration:
            pass

        chain_id = self._increment_storage.generate_chain_id()
        self._increment_storage.save_chain(chain_id, increment_chain)

        return BuildResult(
            character=self._make_presentable(blueprint), chain_id=chain_id
        )

    def add(self, building_block: BuildingBlock) -> Self:
        return type(self)(
            self._building_blocks + (building_block,), self._increment_storage
        )

    def get_increment_chain(self, chain_id: str) -> IncrementChain:
        """Retrieve an increment chain from storage.

        Args:
            chain_id: ID of the chain to retrieve

        Returns:
            IncrementChain instance

        Raises:
            ValueError: If chain_id not found in storage
        """
        chain = self._increment_storage.load_chain(chain_id)
        if chain is None:
            raise ValueError(
                f"Increment chain {chain_id} not found in storage"
            )
        return chain

    def restore(self, chain_id: str, increment_index: int) -> str:
        """Restore to a specific increment and save as new chain.

        Args:
            chain_id: ID of the chain to restore from
            increment_index: Index of increment to restore to

        Returns:
            New chain_id for the restored state

        Raises:
            ValueError: If chain_id not found
            IndexError: If increment_index out of range
        """
        chain = self.get_increment_chain(chain_id)
        increment = chain.get_increment(increment_index)
        if increment is None:
            raise IndexError(f"Increment index {increment_index} out of range")

        truncated_chain = chain.truncate_to(increment_index)

        new_chain_id = self._increment_storage.generate_chain_id()
        self._increment_storage.save_chain(new_chain_id, truncated_chain)

        return new_chain_id

    def branch_from(
        self,
        chain_id: str,
        increment_index: int,
        new_blocks: tuple[BuildingBlock, ...],
    ) -> str:
        """Create a new build branch from an increment.

        Args:
            chain_id: ID of the chain to branch from
            increment_index: Index of increment to branch from
            new_blocks: New building blocks to apply on the branch

        Returns:
            New chain_id for the branched build

        Raises:
            ValueError: If chain_id not found
            IndexError: If increment_index out of range

        Example:
            >>> branch_id = builder.branch_from(
            ...     chain_id="abc123",
            ...     increment_index=5,
            ...     new_blocks=(LevelUp(class_=Class.ROGUE),),
            ... )
        """
        chain = self.get_increment_chain(chain_id)
        increment = chain.get_increment(increment_index)
        if increment is None:
            raise IndexError(f"Increment index {increment_index} out of range")
        branched_builder = Builder(
            building_blocks=new_blocks,
            increment_storage=self._increment_storage,
        )
        result = branched_builder.build()
        return result.chain_id

    def compare_increments(
        self, chain_id: str, index1: int, index2: int
    ) -> dict[str, tuple]:
        """Compare blueprint states between two increments.

        Args:
            chain_id: ID of the chain
            index1: First increment index
            index2: Second increment index

        Returns:
            Dictionary mapping field names to (value_at_index1, value_at_index2) tuples

        Raises:
            ValueError: If chain_id not found
            IndexError: If indices out of range
        """
        chain = self.get_increment_chain(chain_id)
        increment1 = chain.get_increment(index1)
        increment2 = chain.get_increment(index2)

        if increment1 is None or increment2 is None:
            raise IndexError("One or both increment indices are out of range")

        differences = {}
        all_fields = set(increment1.blueprint_state.model_fields_set) | set(
            increment2.blueprint_state.model_fields_set
        )

        for field_name in all_fields:
            val1 = getattr(increment1.blueprint_state, field_name, None)
            val2 = getattr(increment2.blueprint_state, field_name, None)
            if val1 != val2:
                differences[field_name] = (val1, val2)

        return differences

    @staticmethod
    def _make_presentable(blueprint: Blueprint) -> PresentableCharacter:
        if (
            blueprint.n_stat_choices
            or blueprint.n_skill_choices
            or blueprint.skills_to_choose_from
            or blueprint.equipment_choices
        ):
            raise ValueError("Blueprint still has corresponding choices")
        return PresentableCharacter.model_validate(
            {
                field_name: field_value
                for field_name, field_value in iter(blueprint)
                if field_name in Character.model_fields
            }
        )
