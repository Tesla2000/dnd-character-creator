from enum import IntEnum

from dnd.fight.aspect._aoe_vulnerability import (
    _AoeVulnerabilityAspect as AoeVulnerabilityAspect,
)
from dnd.fight.aspect._base import _Aspect as Aspect
from dnd.fight.aspect._type import AspectType

type AnyAspect[SlotT: IntEnum] = AoeVulnerabilityAspect[SlotT]

__all__ = [
    "AnyAspect",
    "Aspect",
    "AoeVulnerabilityAspect",
    "AspectType",
]
