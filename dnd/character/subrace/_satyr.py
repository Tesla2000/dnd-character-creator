from __future__ import annotations

from collections.abc import Generator

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from typing import ClassVar
from dnd.character.race import Race
from dnd.character.subrace._base import SubraceModifier


class SatyrMordenkainenPresentsMonstersoftheMultiverseRace(SubraceModifier):
    race: ClassVar[Race] = Race.SATYR

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()


class SatyrMythicOdysseysofTherosRace(SubraceModifier):
    race: ClassVar[Race] = Race.SATYR

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()
