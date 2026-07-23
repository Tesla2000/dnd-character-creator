from dnd.character.actions.duration_modifier._base import _DurationModifier as DurationModifier
from dnd.character.actions.duration_modifier._rage_round_counter import (
    _RageRoundCounterModifier as RageRoundCounterModifier,
)
from dnd.character.actions.duration_modifier._type import DurationModifierType

AnyDurationModifier = RageRoundCounterModifier

__all__ = [
    "AnyDurationModifier",
    "DurationModifier",
    "DurationModifierType",
    "RageRoundCounterModifier",
]
