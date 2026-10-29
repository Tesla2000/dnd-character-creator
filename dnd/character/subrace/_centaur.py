from __future__ import annotations

from collections.abc import Generator

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from typing import ClassVar
from dnd.character.race import Race
from dnd.character.subrace._base import SubraceModifier


class GruulCentaurGuildmastersGuidetoRavnicaRace(SubraceModifier):
    race: ClassVar[Race] = Race.CENTAUR

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()


class SelesnyaCentaurGuildmastersGuidetoRavnicaRace(SubraceModifier):
    race: ClassVar[Race] = Race.CENTAUR

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()


class CentaursMordenkainenPresentsMonstersoftheMultiverseRace(SubraceModifier):
    race: ClassVar[Race] = Race.CENTAUR

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()


class LagonnaMythicOdysseysofTherosRace(SubraceModifier):
    race: ClassVar[Race] = Race.CENTAUR

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()


class PheresMythicOdysseysofTherosRace(SubraceModifier):
    race: ClassVar[Race] = Race.CENTAUR

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()
