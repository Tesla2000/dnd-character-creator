from enum import IntEnum
from typing import Literal, Self

from dnd._combat_event import AnyCombatEvent, RageEndsEvent, TurnStartEvent
from dnd.character.actions.duration_modifier._base import _DurationModifier
from dnd.character.actions.duration_modifier._type import DurationModifierType


class _RageRoundCounterModifier(_DurationModifier):
    type: Literal[DurationModifierType.RAGE_ROUND_COUNTER] = (
        DurationModifierType.RAGE_ROUND_COUNTER
    )
    rounds_remaining: int = 10

    def on_event[T: IntEnum](
        self, event: AnyCombatEvent[T]
    ) -> tuple[Self | None, tuple[AnyCombatEvent[T], ...]]:
        match event:
            case RageEndsEvent() if event.target_id == self.owner_id:
                return None, ()
            case TurnStartEvent() if event.target_id == self.owner_id:
                remaining = self.rounds_remaining - 1
                if remaining <= 0:
                    return None, (RageEndsEvent(target_id=self.owner_id),)
                return self.model_copy(update={"rounds_remaining": remaining}), ()
            case _:
                return self, ()
