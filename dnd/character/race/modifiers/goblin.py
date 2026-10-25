from __future__ import annotations

from collections.abc import Generator

from dnd.character.modifiers.base import _Modifier
from dnd.character.modifiers.source import _ModifierSource
from dnd.character.modifiers.darkvision import DarkvisionModifier
from dnd.character.race.modifiers.base import RaceModifier


class DankwoodGoblinAdventureswithMukDankwoodRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class GoblinMordenkainenPresentsMonstersoftheMultiverseRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class GoblinPlaneShiftIxalanRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class GoblinVolosGuidetoMonstersRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)
