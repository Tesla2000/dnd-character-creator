from __future__ import annotations

import logging
from collections.abc import Sequence

from dnd.character.alignment import AlignmentModifier
from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.choices.alignment import Alignment
from dnd.getters._getter import Getter
from dnd.getters._getter import PrioritizedCharacter

logger = logging.getLogger(__name__)


class AlignmentGetter(Getter[PrioritizedCharacter, Alignment]):
    def _get(
        self,
        character: PrioritizedCharacter,
        modifiers: Sequence[_Modifier | _ModifierSource],
    ) -> Alignment:
        values = [
            modifier.apply(character)
            for modifier in modifiers
            if isinstance(modifier, AlignmentModifier)
        ]
        if len(values) > 1:
            logger.warning(
                "Alignment set %d times, using the last value %s",
                len(values),
                values[-1],
            )
        return values[-1] if values else Alignment.UNASSIGNED
