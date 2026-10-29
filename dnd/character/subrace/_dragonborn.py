from __future__ import annotations

from collections.abc import Generator

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.sight import DarkvisionModifier
from typing import ClassVar
from dnd.character.race import Race
from dnd.character.subrace._base import SubraceModifier


class DraconbloodExplorersGuidetoWildemountRace(SubraceModifier):
    race: ClassVar[Race] = Race.DRAGONBORN

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class RaveniteExplorersGuidetoWildemountRace(SubraceModifier):
    race: ClassVar[Race] = Race.DRAGONBORN

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class ChromaticFizbansTreasuryofDragonsRace(SubraceModifier):
    race: ClassVar[Race] = Race.DRAGONBORN

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class GemFizbansTreasuryofDragonsRace(SubraceModifier):
    race: ClassVar[Race] = Race.DRAGONBORN

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class MetallicFizbansTreasuryofDragonsRace(SubraceModifier):
    race: ClassVar[Race] = Race.DRAGONBORN

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class DragonbornPlayersHandbookRace(SubraceModifier):
    race: ClassVar[Race] = Race.DRAGONBORN

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()


class ChromaticUnearthedArcanaRace(SubraceModifier):
    race: ClassVar[Race] = Race.DRAGONBORN

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class GemUnearthedArcanaRace(SubraceModifier):
    race: ClassVar[Race] = Race.DRAGONBORN

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class MetallicUnearthedArcanaRace(SubraceModifier):
    race: ClassVar[Race] = Race.DRAGONBORN

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)
