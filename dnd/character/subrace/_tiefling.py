from __future__ import annotations

from collections.abc import Generator

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.sight import DarkvisionModifier
from typing import ClassVar
from dnd.character.race import Race
from dnd.character.subrace._base import SubraceModifier


class BloodlineofBaalzebulMordenkainensTomeofFoesRace(SubraceModifier):
    race: ClassVar[Race] = Race.TIEFLING

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class BloodlineofDispaterMordenkainensTomeofFoesRace(SubraceModifier):
    race: ClassVar[Race] = Race.TIEFLING

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class BloodlineofFiernaMordenkainensTomeofFoesRace(SubraceModifier):
    race: ClassVar[Race] = Race.TIEFLING

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class BloodlineofGlasyaMordenkainensTomeofFoesRace(SubraceModifier):
    race: ClassVar[Race] = Race.TIEFLING

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class BloodlineofLevistusMordenkainensTomeofFoesRace(SubraceModifier):
    race: ClassVar[Race] = Race.TIEFLING

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class BloodlineofMammonMordenkainensTomeofFoesRace(SubraceModifier):
    race: ClassVar[Race] = Race.TIEFLING

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class BloodlineofMephistophelesMordenkainensTomeofFoesRace(SubraceModifier):
    race: ClassVar[Race] = Race.TIEFLING

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class BloodlineofZarielMordenkainensTomeofFoesRace(SubraceModifier):
    race: ClassVar[Race] = Race.TIEFLING

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class BloodlineofAsmodeusPlayersHandbookRace(SubraceModifier):
    race: ClassVar[Race] = Race.TIEFLING

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class DevilsTongueSwordCoastAdventurersGuideRace(SubraceModifier):
    race: ClassVar[Race] = Race.TIEFLING

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class FeralSwordCoastAdventurersGuideRace(SubraceModifier):
    race: ClassVar[Race] = Race.TIEFLING

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class HellfireSwordCoastAdventurersGuideRace(SubraceModifier):
    race: ClassVar[Race] = Race.TIEFLING

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class WingedSwordCoastAdventurersGuideRace(SubraceModifier):
    race: ClassVar[Race] = Race.TIEFLING

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class AbyssalTieflingUnearthedArcanaRace(SubraceModifier):
    race: ClassVar[Race] = Race.TIEFLING

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)
