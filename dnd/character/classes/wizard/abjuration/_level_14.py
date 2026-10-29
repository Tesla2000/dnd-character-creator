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
from dnd.character.classes.wizard.abjuration._level_13 import AbjurationLevelComposer13
from dnd.character.classes.wizard._level_base import _WizardLevelBase


class AbjurationLevel14Argument(BaseModel):
    model_config = ConfigDict(frozen=True)


class _AbjurationLevel14(_WizardLevelBase):
    class_ = Class.WIZARD

    def _get_level_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()


class _AbjurationLevel14Converter:
    def convert(self, _: AbjurationLevel14Argument) -> _AbjurationLevel14:
        return _AbjurationLevel14()


class AbjurationLevelComposer14(ModifierSource):
    priority: ClassVar[Priority] = Priority.UNORDERED

    new_level: AbjurationLevel14Argument
    previous: AbjurationLevelComposer13

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield self.previous
        yield _AbjurationLevel14Converter().convert(self.new_level)
