from __future__ import annotations

from collections.abc import Generator

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.sight import DarkvisionModifier
from typing import ClassVar
from dnd.character.race import Race
from dnd.character.subrace._base import SubraceModifier


class BeasthideEberronRisingfromtheLastWarRace(SubraceModifier):
    race: ClassVar[Race] = Race.SHIFTER

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class LongtoothEberronRisingfromtheLastWarRace(SubraceModifier):
    race: ClassVar[Race] = Race.SHIFTER

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class SwiftstrideEberronRisingfromtheLastWarRace(SubraceModifier):
    race: ClassVar[Race] = Race.SHIFTER

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class WildhuntEberronRisingfromtheLastWarRace(SubraceModifier):
    race: ClassVar[Race] = Race.SHIFTER

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class BeasthideMordenkainenPresentsMonstersoftheMultiverseRace(SubraceModifier):
    race: ClassVar[Race] = Race.SHIFTER

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class LongtoothMordenkainenPresentsMonstersoftheMultiverseRace(SubraceModifier):
    race: ClassVar[Race] = Race.SHIFTER

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class SwiftstrideMordenkainenPresentsMonstersoftheMultiverseRace(SubraceModifier):
    race: ClassVar[Race] = Race.SHIFTER

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()


class WildhuntMordenkainenPresentsMonstersoftheMultiverseRace(SubraceModifier):
    race: ClassVar[Race] = Race.SHIFTER

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class CliffwalkUnearthedArcanaRace(SubraceModifier):
    race: ClassVar[Race] = Race.SHIFTER

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()


class RazorclawUnearthedArcanaRace(SubraceModifier):
    race: ClassVar[Race] = Race.SHIFTER

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()
