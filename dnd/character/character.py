from __future__ import annotations

from collections.abc import Generator

from dnd.character.base import PrioritizedNode
from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource


class Character:
    def __init__(self, *, modifier_sources: tuple[_ModifierSource, ...] = ()) -> None:
        self._modifier_sources = modifier_sources

    @property
    def modifiers(self) -> tuple[_Modifier | _ModifierSource, ...]:
        """Every modifier and source, ordered by the priority of the source it came from."""
        prioritized = [
            PrioritizedNode(source.priority, found)
            for source in self._modifier_sources
            for found in self._flatten(source)
        ]
        return tuple(found.node for found in sorted(prioritized))

    @classmethod
    def _flatten(
        cls, node: _Modifier | _ModifierSource
    ) -> Generator[_Modifier | _ModifierSource]:
        yield node
        if isinstance(node, _ModifierSource):
            for child in node.get_modifiers():
                yield from cls._flatten(child)
