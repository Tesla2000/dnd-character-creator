from typing import Annotated
from typing import Union

from pydantic import Field

from dnd.character.health_modifier._base import _HealthModifier as HealthModifier
from dnd.character.health_modifier._base import (
    _HealthModifierContext as HealthModifierContext,
)
from dnd.character.health_modifier._dwarf import (
    _DwarfHealthModifier as DwarfHealthModifier,
)
from dnd.character.health_modifier._tough import (
    _ToughHealthModifier as ToughHealthModifier,
)
from dnd.character.health_modifier._type import HealthModifierType

AnyHealthModifier = Annotated[
    Union[DwarfHealthModifier, ToughHealthModifier],
    Field(discriminator="type"),
]

__all__ = [
    "AnyHealthModifier",
    "DwarfHealthModifier",
    "HealthModifier",
    "HealthModifierContext",
    "HealthModifierType",
    "ToughHealthModifier",
]
