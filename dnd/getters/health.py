from __future__ import annotations

from dnd.getters.getter import Getter
from dnd.character.modifiers.health import DwarvenToughnessModifier
from dnd.character.modifiers.health import MaxHealthModifier
from typing import Self
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dnd.character.character import Character


class MaxHealth(int):
    def __new__(cls, value: int) -> Self:
        if value <= 0:
            raise ValueError(f"MaxHealth must be a positive integer, got {value}")
        return super().__new__(cls, value)


class MaxHealthGetter(Getter):
    def get(self, character: Character) -> MaxHealth:
        return MaxHealth(
            sum(
                modifier.apply(character)
                for modifier in character.modifiers
                if isinstance(modifier, (MaxHealthModifier, DwarvenToughnessModifier))
            )
        )
