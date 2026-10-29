from __future__ import annotations

from collections.abc import Generator

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.sight import DarkvisionModifier
from typing import ClassVar
from dnd.character.race import Race
from dnd.character.subrace._base import SubraceModifier


class HalforcMarkofFindingEberronRisingfromtheLastWarRace(SubraceModifier):
    race: ClassVar[Race] = Race.HALF_ORC

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class HalfOrcPlayersHandbookRace(SubraceModifier):
    race: ClassVar[Race] = Race.HALF_ORC

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)
