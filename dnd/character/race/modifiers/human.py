from __future__ import annotations

from collections.abc import Generator

from dnd.character.modifiers.base import _Modifier
from dnd.character.modifiers.source import _ModifierSource
from dnd.character.modifiers.darkvision import DarkvisionModifier
from dnd.character.race.modifiers.base import RaceModifier


class MarkofFindingEberronRisingfromtheLastWarRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class MarkofHandlingEberronRisingfromtheLastWarRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=0)


class MarkofMakingEberronRisingfromtheLastWarRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=0)


class MarkofPassageEberronRisingfromtheLastWarRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=0)


class MarkofSentinelEberronRisingfromtheLastWarRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=0)


class KeldonPlaneShiftDominariaRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=0)


class GavonyPlaneShiftInnistradRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=0)


class KessigPlaneShiftInnistradRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=0)


class NephaliaPlaneShiftInnistradRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=0)


class StensiaPlaneShiftInnistradRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=0)


class StandardHumanPlayersHandbookRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=0)


class VariantHumanPlayersHandbookRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=0)
