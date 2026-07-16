from typing import Literal

from dnd.character.health_modifier._base import _HealthModifier
from dnd.character.health_modifier._base import _HealthModifierContext
from dnd.character.health_modifier._type import HealthModifierType
from pydantic import PositiveInt


class _ToughHealthModifier(_HealthModifier):
    type: Literal[HealthModifierType.TOUGH] = HealthModifierType.TOUGH

    def apply(self, context: _HealthModifierContext) -> PositiveInt:
        return context.level * 2
