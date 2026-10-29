from __future__ import annotations

from collections.abc import Sequence

from dnd.character.armor_class import AcModifier
from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.getters._getter import Getter
from dnd.getters._getter import PrioritizedCharacter


class AcGetter(Getter[PrioritizedCharacter, int]):
    base: int = 10

    def _get(
        self,
        character: PrioritizedCharacter,
        modifiers: Sequence[_Modifier | _ModifierSource],
    ) -> int:
        return self.base + sum(
            modifier.apply(character)
            for modifier in modifiers
            if isinstance(modifier, AcModifier)
        )
