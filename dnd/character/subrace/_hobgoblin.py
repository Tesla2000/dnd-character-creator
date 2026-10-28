from __future__ import annotations
from typing import Never

from collections.abc import Generator

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.sight import DarkvisionModifier
from typing import ClassVar
from dnd.character.race import Race
from dnd.character.subrace._base import SubraceModifier


class HobgoblinMordenkainenPresentsMonstersoftheMultiverseRace(SubraceModifier):
    race: ClassVar[Race] = Race.HOBGOBLIN

    def get_modifiers(self) -> Generator[_Modifier[Never] | _ModifierSource]:
        yield from ()


class HobgoblinUnearthedArcanaRace(SubraceModifier):
    race: ClassVar[Race] = Race.HOBGOBLIN

    def get_modifiers(self) -> Generator[_Modifier[Never] | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class HobgoblinVolosGuidetoMonstersRace(SubraceModifier):
    race: ClassVar[Race] = Race.HOBGOBLIN

    def get_modifiers(self) -> Generator[_Modifier[Never] | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)
