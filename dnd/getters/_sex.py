from __future__ import annotations

import logging
from collections.abc import Sequence

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.sex import SexModifier
from dnd.choices.sex import Sex
from dnd.getters._getter import Getter
from dnd.getters._getter import PrioritizedCharacter

logger = logging.getLogger(__name__)


class SexGetter(Getter[PrioritizedCharacter, Sex]):
    def _get(
        self,
        character: PrioritizedCharacter,
        modifiers: Sequence[_Modifier | _ModifierSource],
    ) -> Sex:
        values = [
            modifier.apply(character)
            for modifier in modifiers
            if isinstance(modifier, SexModifier)
        ]
        if len(values) > 1:
            logger.warning(
                "Sex set %d times, using the last value %s",
                len(values),
                values[-1],
            )
        return values[-1] if values else Sex.UNASSIGNED
