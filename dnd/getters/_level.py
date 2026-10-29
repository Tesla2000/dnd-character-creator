from __future__ import annotations

from collections.abc import Sequence

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.classes import ClassLevelBase
from dnd.getters._getter import Getter
from dnd.getters._getter import PrioritizedCharacter


class LevelGetter(Getter[PrioritizedCharacter, int]):
    def _get(
        self,
        character: PrioritizedCharacter,
        modifiers: Sequence[_Modifier | _ModifierSource],
    ) -> int:
        return sum(1 for modifier in modifiers if isinstance(modifier, ClassLevelBase))
