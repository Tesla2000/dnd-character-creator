from typing import Literal

from dnd.character.health_modifier._base import _HealthModifier
from dnd.character.health_modifier._base import _HealthModifierContext
from dnd.character.health_modifier._type import HealthModifierType
from pydantic import PositiveInt


class _DwarfHealthModifier(_HealthModifier):
    type: Literal[HealthModifierType.DWARF] = HealthModifierType.DWARF

    def apply(self, context: _HealthModifierContext) -> PositiveInt:
        return context.level
