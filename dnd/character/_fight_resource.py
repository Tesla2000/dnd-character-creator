from enum import StrEnum, auto
from typing import ClassVar

from pydantic import BaseModel, ConfigDict, PositiveInt


class ResourceName(StrEnum):
    RAGE = auto()
    KI_POINTS = auto()
    BARDIC_INSPIRATION = auto()
    LAY_ON_HANDS = auto()
    ACTION_SURGE = auto()
    SECOND_WIND = auto()
    WILD_SHAPE = auto()
    CHANNEL_DIVINITY = auto()
    SORCERY_POINTS = auto()
    SUPERIORITY_DICE = auto()
    SNEAK_ATTACK = auto()


class ResourceAllotment(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)

    name: ResourceName
    max_uses: PositiveInt
