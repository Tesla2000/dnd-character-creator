from __future__ import annotations
from typing import Never

from collections.abc import Generator

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.sight import DarkvisionModifier
from typing import ClassVar
from dnd.character.race import Race
from dnd.character.subrace._base import SubraceModifier


class MarkofFindingEberronRisingfromtheLastWarRace(SubraceModifier):
    race: ClassVar[Race] = Race.HUMAN

    def get_modifiers(self) -> Generator[_Modifier[Never] | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class MarkofHandlingEberronRisingfromtheLastWarRace(SubraceModifier):
    race: ClassVar[Race] = Race.HUMAN

    def get_modifiers(self) -> Generator[_Modifier[Never] | _ModifierSource]:
        yield from ()


class MarkofMakingEberronRisingfromtheLastWarRace(SubraceModifier):
    race: ClassVar[Race] = Race.HUMAN

    def get_modifiers(self) -> Generator[_Modifier[Never] | _ModifierSource]:
        yield from ()


class MarkofPassageEberronRisingfromtheLastWarRace(SubraceModifier):
    race: ClassVar[Race] = Race.HUMAN

    def get_modifiers(self) -> Generator[_Modifier[Never] | _ModifierSource]:
        yield from ()


class MarkofSentinelEberronRisingfromtheLastWarRace(SubraceModifier):
    race: ClassVar[Race] = Race.HUMAN

    def get_modifiers(self) -> Generator[_Modifier[Never] | _ModifierSource]:
        yield from ()


class KeldonPlaneShiftDominariaRace(SubraceModifier):
    race: ClassVar[Race] = Race.HUMAN

    def get_modifiers(self) -> Generator[_Modifier[Never] | _ModifierSource]:
        yield from ()


class GavonyPlaneShiftInnistradRace(SubraceModifier):
    race: ClassVar[Race] = Race.HUMAN

    def get_modifiers(self) -> Generator[_Modifier[Never] | _ModifierSource]:
        yield from ()


class KessigPlaneShiftInnistradRace(SubraceModifier):
    race: ClassVar[Race] = Race.HUMAN

    def get_modifiers(self) -> Generator[_Modifier[Never] | _ModifierSource]:
        yield from ()


class NephaliaPlaneShiftInnistradRace(SubraceModifier):
    race: ClassVar[Race] = Race.HUMAN

    def get_modifiers(self) -> Generator[_Modifier[Never] | _ModifierSource]:
        yield from ()


class StensiaPlaneShiftInnistradRace(SubraceModifier):
    race: ClassVar[Race] = Race.HUMAN

    def get_modifiers(self) -> Generator[_Modifier[Never] | _ModifierSource]:
        yield from ()


class StandardHumanPlayersHandbookRace(SubraceModifier):
    race: ClassVar[Race] = Race.HUMAN

    def get_modifiers(self) -> Generator[_Modifier[Never] | _ModifierSource]:
        yield from ()


class VariantHumanPlayersHandbookRace(SubraceModifier):
    race: ClassVar[Race] = Race.HUMAN

    def get_modifiers(self) -> Generator[_Modifier[Never] | _ModifierSource]:
        yield from ()
