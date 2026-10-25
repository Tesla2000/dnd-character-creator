from __future__ import annotations

from collections.abc import Generator

from dnd.character.modifiers.base import _Modifier
from dnd.character.modifiers.source import _ModifierSource
from dnd.character.modifiers.darkvision import DarkvisionModifier
from dnd.character.race.modifiers.base import RaceModifier


class WarforgedEberronRisingfromtheLastWarRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=0)


class EnvoyUnearthedArcanaRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=0)


class JuggernautUnearthedArcanaRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=0)


class SkirmisherUnearthedArcanaRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=0)
