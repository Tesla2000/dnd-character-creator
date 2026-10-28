from __future__ import annotations
from typing import Never

from collections.abc import Generator

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from typing import ClassVar
from dnd.character.race import Race
from dnd.character.subrace._base import SubraceModifier


class FirbolgMordenkainenPresentsMonstersoftheMultiverseRace(SubraceModifier):
    race: ClassVar[Race] = Race.FIRBOLG

    def get_modifiers(self) -> Generator[_Modifier[Never] | _ModifierSource]:
        yield from ()


class FirbolgVolosGuidetoMonstersRace(SubraceModifier):
    race: ClassVar[Race] = Race.FIRBOLG

    def get_modifiers(self) -> Generator[_Modifier[Never] | _ModifierSource]:
        yield from ()
