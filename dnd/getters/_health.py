from __future__ import annotations

from collections.abc import Sequence
from typing import Never
from typing import Self

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.classes import HitDieModifier
from dnd.character.health import HealthModifier
from dnd.getters._getter import Getter
from dnd.getters._getter import PrioritizedCharacter
from dnd.getters._stat import ConstitutionGetter


class MaxHealth(int):
    def __new__(cls, value: int) -> Self:
        if value <= 0:
            raise ValueError(f"MaxHealth must be a positive integer, got {value}")
        return super().__new__(cls, value)


class MaxHealthGetter(Getter[PrioritizedCharacter, MaxHealth]):
    def _get(
        self,
        character: PrioritizedCharacter,
        modifiers: Sequence[_Modifier[Never] | _ModifierSource],
    ) -> MaxHealth:
        constitution = ConstitutionGetter().get(character).modifier
        hit_dice = [
            modifier for modifier in modifiers if isinstance(modifier, HitDieModifier)
        ]
        levels = 0
        for index, hit_die in enumerate(hit_dice):
            die_hit_points = hit_die.die if index == 0 else hit_die.die // 2 + 1
            levels += die_hit_points + constitution
        bonuses = sum(
            modifier.apply(character)
            for modifier in modifiers
            if isinstance(modifier, HealthModifier)
        )
        return MaxHealth(levels + bonuses)
