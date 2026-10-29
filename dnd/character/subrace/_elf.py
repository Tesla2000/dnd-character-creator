from __future__ import annotations

from collections.abc import Generator

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.sight import DarkvisionModifier
from typing import ClassVar
from dnd.character.race import Race
from dnd.character.subrace._base import SubraceModifier


class MarkofShadowEberronRisingfromtheLastWarRace(SubraceModifier):
    race: ClassVar[Race] = Race.ELF

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class PallidElfExplorersGuidetoWildemountRace(SubraceModifier):
    race: ClassVar[Race] = Race.ELF

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class BishtaharElfPlaneShiftKaladeshRace(SubraceModifier):
    race: ClassVar[Race] = Race.ELF

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class TiraharElfPlaneShiftKaladeshRace(SubraceModifier):
    race: ClassVar[Race] = Race.ELF

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class VahadarElfPlaneShiftKaladeshRace(SubraceModifier):
    race: ClassVar[Race] = Race.ELF

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class JuragaPlaneShiftZendikarRace(SubraceModifier):
    race: ClassVar[Race] = Race.ELF

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class MulDayaPlaneShiftZendikarRace(SubraceModifier):
    race: ClassVar[Race] = Race.ELF

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=120)


class TajuruPlaneShiftZendikarRace(SubraceModifier):
    race: ClassVar[Race] = Race.ELF

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class DarkElfPlayersHandbookRace(SubraceModifier):
    race: ClassVar[Race] = Race.ELF

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=120)


class HighElfPlayersHandbookRace(SubraceModifier):
    race: ClassVar[Race] = Race.ELF

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class WoodElfPlayersHandbookRace(SubraceModifier):
    race: ClassVar[Race] = Race.ELF

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class AstralElfSpelljammerAdventuresinSpaceRace(SubraceModifier):
    race: ClassVar[Race] = Race.ELF

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)
