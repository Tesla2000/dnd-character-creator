from __future__ import annotations

from collections.abc import Generator

from dnd.character.modifiers.base import _Modifier
from dnd.character.modifiers.source import _ModifierSource
from dnd.character.modifiers.darkvision import DarkvisionModifier
from dnd.character.race.modifiers.base import RaceModifier


class DraconbloodExplorersGuidetoWildemountRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class RaveniteExplorersGuidetoWildemountRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class ChromaticFizbansTreasuryofDragonsRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class GemFizbansTreasuryofDragonsRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class MetallicFizbansTreasuryofDragonsRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class DragonbornPlayersHandbookRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=0)


class ChromaticUnearthedArcanaRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class GemUnearthedArcanaRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class MetallicUnearthedArcanaRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)
