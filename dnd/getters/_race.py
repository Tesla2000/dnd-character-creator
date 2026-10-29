from __future__ import annotations

from collections.abc import Sequence

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.race import Race
from dnd.getters._getter import Getter
from dnd.getters._getter import PrioritizedCharacter
from dnd.getters._subrace import SubraceGetter


class RaceGetter(Getter[PrioritizedCharacter, Race | None]):
    def _get(
        self,
        character: PrioritizedCharacter,
        modifiers: Sequence[_Modifier | _ModifierSource],
    ) -> Race | None:
        subrace = SubraceGetter().get(character)
        return subrace.race if subrace is not None else None
