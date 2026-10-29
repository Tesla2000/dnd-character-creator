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
from dnd.character.classes.wizard._level_1 import WizardLevelComposer1
from dnd.character.classes.wizard._level_base import _WizardLevelBase


class AbjurationLevel2Argument(BaseModel):
    model_config = ConfigDict(frozen=True)


class _AbjurationLevel2(_WizardLevelBase):
    class_ = Class.WIZARD

    def _get_level_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()


class _AbjurationLevel2Converter:
    def convert(self, _: AbjurationLevel2Argument) -> _AbjurationLevel2:
        return _AbjurationLevel2()


class AbjurationLevelComposer2(ModifierSource):
    priority: ClassVar[Priority] = Priority.UNORDERED

    new_level: AbjurationLevel2Argument
    previous: WizardLevelComposer1

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield self.previous
        yield _AbjurationLevel2Converter().convert(self.new_level)
