from __future__ import annotations

from collections.abc import Generator
from typing import ClassVar

from pydantic import BaseModel
from pydantic import ConfigDict

from dnd.character.base import ModifierSource
from dnd.character.base import Priority
from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.classes._enums import Class
from dnd.character.classes.wizard.evocation._level_13 import EvocationLevelComposer13
from dnd.character.classes.wizard._level_base import _WizardLevelBase


class EvocationLevel14Argument(BaseModel):
    model_config = ConfigDict(frozen=True)


class _EvocationLevel14(_WizardLevelBase):
    class_ = Class.WIZARD

    def _get_level_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()


class _EvocationLevel14Converter:
    def convert(self, _: EvocationLevel14Argument) -> _EvocationLevel14:
        return _EvocationLevel14()


class EvocationLevelComposer14(ModifierSource):
    priority: ClassVar[Priority] = Priority.UNORDERED

    new_level: EvocationLevel14Argument
    previous: EvocationLevelComposer13

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield self.previous
        yield _EvocationLevel14Converter().convert(self.new_level)
