from typing import ClassVar

from pydantic import BaseModel, ConfigDict, NonNegativeInt


class _AttackResult(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)

    first_roll: int | str
    second_roll: int | str
    damage: NonNegativeInt
    crit_damage: NonNegativeInt
    extra_damage: NonNegativeInt = 0
    extra_crit_damage: NonNegativeInt = 0
    extra_damage_type: str = ""

    def __str__(self) -> str:
        first_crit = self.first_roll == "critical"
        second_crit = self.second_roll == "critical"
        base = (
            f"first_roll={self.first_roll!r} second_roll={self.second_roll!r}"
            f" damage={self.damage}"
        )
        if self.extra_damage_type or self.extra_damage:
            base += f" + {self.extra_damage} {self.extra_damage_type}".rstrip()
        if first_crit and second_crit:
            return f"{base} | crit with disadvantage: {self._crit_text}"
        if first_crit:
            return f"{base} | crit: {self._crit_text}"
        if second_crit:
            return f"{base} | crit with adv: {self._crit_text}"
        return base

    @property
    def _crit_text(self) -> str:
        if not (self.extra_damage_type or self.extra_crit_damage):
            return str(self.crit_damage)
        return f"{self.crit_damage} + {self.extra_crit_damage} {self.extra_damage_type}".rstrip()
