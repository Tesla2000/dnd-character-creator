from __future__ import annotations

from collections.abc import Generator


from dnd.character.base import ModifiedCharacter
from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.health import HealthModifier
from dnd.character.sight import DarkvisionModifier
from typing import ClassVar
from typing import Protocol
from typing import runtime_checkable
from dnd.character.race import Race
from dnd.character.subrace._base import SubraceModifier
from pydantic import ConfigDict
from pydantic import InstanceOf


@runtime_checkable
class LevelOf[C](Protocol):
    def get(self, character: C) -> int: ...


class DwarvenToughnessModifier(HealthModifier):
    model_config = ConfigDict(frozen=True)

    level_getter: InstanceOf[LevelOf[ModifiedCharacter]]

    def apply(self, character: ModifiedCharacter) -> int:
        return self.level_getter.get(character)


class HillDwarfPlayersHandbookRace(SubraceModifier):
    model_config = ConfigDict(frozen=True)

    race: ClassVar[Race] = Race.DWARF

    level_getter: InstanceOf[LevelOf[ModifiedCharacter]]

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)
        yield DwarvenToughnessModifier(level_getter=self.level_getter)


class MountainDwarfPlayersHandbookRace(SubraceModifier):
    race: ClassVar[Race] = Race.DWARF

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)
