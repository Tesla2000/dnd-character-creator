from typing import Literal

from pydantic import NonNegativeInt

from dnd.character.health_modifier._base import _HealthModifier
from dnd.character.health_modifier._base import _HealthModifierContext
from dnd.character.health_modifier._type import HealthModifierType

_AMULET_CONSTITUTION_MODIFIER = 4


class _AmuletOfHealthModifier(_HealthModifier):
    type: Literal[HealthModifierType.AMULET_OF_HEALTH] = (
        HealthModifierType.AMULET_OF_HEALTH
    )

    def apply(self, context: _HealthModifierContext) -> NonNegativeInt:
        bonus_modifier = max(
            0, _AMULET_CONSTITUTION_MODIFIER - context.constitution_modifier
        )
        return context.level * bonus_modifier
