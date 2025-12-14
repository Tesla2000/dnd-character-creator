from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path
from typing import Annotated
from typing import Optional

from dnd_character_creator.character.checkpoint.increment import Increment
from pydantic import AfterValidator
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


def _validate_sequential_indices(
    increments: tuple[Increment, ...],
) -> tuple[Increment, ...]:
    """Ensure increments have sequential indices starting from 0."""
    for i, increment in enumerate(increments):
        if increment.index != i:
            raise ValueError(
                f"Increment at position {i} has index {increment.index}, expected {i}"
            )
    return increments


SequentialIncrements = Annotated[
    tuple[Increment, ...], AfterValidator(_validate_sequential_indices)
]


class IncrementChain(BaseModel):
    """Ordered sequence of increments representing a build process.

    Maintains a linear history of the character build, enabling
    restoration to any point and branching from increments.
    """

    model_config = ConfigDict(frozen=True)

    increments: SequentialIncrements = Field(
        default_factory=tuple,
        description="Ordered sequence of build increments",
    )

    def get_increment(self, index: int) -> Optional[Increment]:
        """Get increment at specific index.

        Args:
            index: Increment index (0-based)

        Returns:
            Increment or None if index out of range
        """
        if 0 <= index < len(self.increments):
            return self.increments[index]
        return None

    def get_latest(self) -> Optional[Increment]:
        """Get the most recent increment."""
        if self.increments:
            return self.increments[-1]
        return None

    def add_increment(self, increment: Increment) -> IncrementChain:
        """Add a new increment to the chain (returns new instance).

        Args:
            increment: New increment to append

        Returns:
            New IncrementChain with increment added
        """
        expected_index = len(self.increments)
        if increment.index != expected_index:
            increment = increment.model_copy(update={"index": expected_index})

        return IncrementChain(increments=self.increments + (increment,))

    def truncate_to(self, index: int) -> IncrementChain:
        """Create new chain containing only increments up to (and including) index.

        Args:
            index: Last increment index to keep (inclusive)

        Returns:
            New IncrementChain with truncated history
        """
        if index < 0 or index >= len(self.increments):
            raise IndexError(f"Increment index {index} out of range")
        return IncrementChain(increments=self.increments[: index + 1])

    def __len__(self) -> int:
        """Return number of increments in chain."""
        return len(self.increments)

    def __iter__(self) -> Iterator[Increment]:
        """Iterate over increments in order."""
        return iter(self.increments)

    def save_to_json(self, filepath: str) -> None:
        """Save increment chain to JSON file.

        Args:
            filepath: Path to save the JSON file
        """
        Path(filepath).write_text(self.model_dump_json(indent=2))

    @classmethod
    def load_from_json(cls, filepath: str) -> IncrementChain:
        """Load increment chain from JSON file.

        Args:
            filepath: Path to the JSON file

        Returns:
            IncrementChain instance
        """
        return cls.model_validate_json(Path(filepath).read_text())
