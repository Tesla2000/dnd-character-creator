from __future__ import annotations

from collections.abc import Generator
from dnd.character.classes.modifier import ClassModifier
from dnd.character.equipment.cloak import CloakModifier
from dnd.character.equipment.cloak import NoCloak
from dnd.character.equipment.helmet import HelmetModifier
from dnd.character.equipment.helmet import NoHelmet
from dnd.character.modifiers.base import _Modifier
from dnd.character.modifiers.source import _ModifierSource
from dnd.character.race.modifiers.base import RaceModifier
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import InstanceOf


class Character(BaseModel):
    model_config = ConfigDict(frozen=True)

    class_modifier: InstanceOf[ClassModifier]
    race_modifier: RaceModifier
    helmet_modifier: HelmetModifier = NoHelmet()
    cloak_modifier: CloakModifier = NoCloak()

    @property
    def level(self) -> int:
        return self.class_modifier.total_level()

    @property
    def modifiers(self) -> tuple[_Modifier, ...]:
        roots = (
            self.class_modifier,
            self.race_modifier,
            self.helmet_modifier,
            self.cloak_modifier,
        )
        return tuple(found for root in roots for found in self._walk(root))

    @classmethod
    def _walk(cls, source: _ModifierSource) -> Generator[_Modifier]:
        for child in source.get_modifiers():
            if isinstance(child, _ModifierSource):
                yield from cls._walk(child)
            else:
                yield child
