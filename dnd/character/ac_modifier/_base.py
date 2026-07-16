from abc import ABC
from abc import abstractmethod
from typing import Protocol

from pydantic import BaseModel
from pydantic import ConfigDict

from dnd.character.race.race import Race
from dnd.character.stats import Stats
from dnd.other_profficiencies import ArmorProficiency


class _AcModifierContext(Protocol):
    @property
    def race(self) -> Race | None: ...

    @property
    def stats(self) -> Stats: ...

    @property
    def other_equipment(self) -> tuple[str, ...]: ...

    @property
    def armor_proficiencies(self) -> frozenset[ArmorProficiency]: ...


class _AcModifier(BaseModel, ABC):
    model_config = ConfigDict(frozen=True)

    @abstractmethod
    def apply(self, context: _AcModifierContext) -> int: ...


class _CompetingAcModifier(_AcModifier, ABC):
    """Returns a full AC value; the highest among all competing modifiers wins."""


class _AdditiveAcModifier(_AcModifier, ABC):
    """Returns a flat bonus applied on top of the winning competing value."""
