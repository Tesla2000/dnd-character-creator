from __future__ import annotations

from collections.abc import Sequence
from typing import Never

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.sight import DarkvisionModifier
from dnd.getters._getter import Getter
from dnd.getters._getter import PrioritizedCharacter


class DarkvisionGetter(Getter[PrioritizedCharacter, int]):
    def _get(
        self,
        character: PrioritizedCharacter,
        modifiers: Sequence[_Modifier[Never] | _ModifierSource],
    ) -> int:
        return max(
            (
                modifier.apply(character)
                for modifier in modifiers
                if isinstance(modifier, DarkvisionModifier)
            ),
            default=0,
        )
