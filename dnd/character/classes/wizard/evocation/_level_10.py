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
from dnd.character.classes.wizard.evocation._level_9 import EvocationLevelComposer9
from dnd.character.classes.wizard._level_base import _WizardLevelBase


class EvocationLevel10Argument(BaseModel):
    model_config = ConfigDict(frozen=True)


class _EvocationLevel10(_WizardLevelBase):
    class_ = Class.WIZARD

    def _get_level_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()


class _EvocationLevel10Converter:
    def convert(self, _: EvocationLevel10Argument) -> _EvocationLevel10:
        return _EvocationLevel10()


class EvocationLevelComposer10(ModifierSource):
    priority: ClassVar[Priority] = Priority.UNORDERED

    new_level: EvocationLevel10Argument
    previous: EvocationLevelComposer9

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield self.previous
        yield _EvocationLevel10Converter().convert(self.new_level)
