from __future__ import annotations

import logging
from collections.abc import Sequence
from typing import Never

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.subrace import SubraceModifier
from dnd.getters._getter import Getter
from dnd.getters._getter import PrioritizedCharacter

logger = logging.getLogger(__name__)


class SubraceGetter(Getter[PrioritizedCharacter, SubraceModifier | None]):
    def _get(
        self,
        character: PrioritizedCharacter,
        modifiers: Sequence[_Modifier[Never] | _ModifierSource],
    ) -> SubraceModifier | None:
        values = [
            modifier for modifier in modifiers if isinstance(modifier, SubraceModifier)
        ]
        if len(values) > 1:
            logger.warning(
                "Subrace set %d times, using the last value %s",
                len(values),
                values[-1],
            )
        return values[-1] if values else None
