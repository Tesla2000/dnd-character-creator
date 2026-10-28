from __future__ import annotations
from typing import Never

from collections.abc import Generator

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.base import PrioritizedNode
from dnd.character.classes import Class
from dnd.character.classes import ClassModifier
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import InstanceOf


class Character(BaseModel):
    model_config = ConfigDict(frozen=True)

    class_modifier: InstanceOf[ClassModifier]
    modifier_sources: tuple[InstanceOf[_ModifierSource], ...] = ()

    @property
    def level(self) -> int:
        return self.class_modifier.get_total_level()

    @property
    def prioritized_modifiers(self) -> tuple[PrioritizedNode, ...]:
        """Every modifier and source with the priority of the source it came from.

        Getters sort these by priority before reading them.
        """
        roots = (self.class_modifier, *self.modifier_sources)
        return tuple(
            PrioritizedNode(root.priority, found)
            for root in roots
            for found in self._flatten(root)
        )

    def level_up(self, class_: Class) -> None:
        self.class_modifier.level_up(class_)

    @classmethod
    def _flatten(
        cls, node: _Modifier[Never] | _ModifierSource
    ) -> Generator[_Modifier[Never] | _ModifierSource]:
        yield node
        if isinstance(node, _ModifierSource):
            for child in node.get_modifiers():
                yield from cls._flatten(child)
