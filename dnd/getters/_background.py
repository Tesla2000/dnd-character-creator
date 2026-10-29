from __future__ import annotations

import logging
from collections.abc import Sequence

from dnd.character.background import BackgroundModifier
from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.choices.background_creatrion.background import Background
from dnd.getters._getter import Getter
from dnd.getters._getter import PrioritizedCharacter

logger = logging.getLogger(__name__)


class BackgroundGetter(Getter[PrioritizedCharacter, Background]):
    def _get(
        self,
        character: PrioritizedCharacter,
        modifiers: Sequence[_Modifier | _ModifierSource],
    ) -> Background:
        values = [
            modifier.apply(character)
            for modifier in modifiers
            if isinstance(modifier, BackgroundModifier)
        ]
        if len(values) > 1:
            logger.warning(
                "Background set %d times, using the last value %s",
                len(values),
                values[-1],
            )
        return values[-1] if values else Background.UNASSIGNED
