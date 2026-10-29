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
from dnd.character.classes.wizard.abjuration._level_5 import AbjurationLevelComposer5
from dnd.character.classes.wizard._level_base import _WizardLevelBase


class AbjurationLevel6Argument(BaseModel):
    model_config = ConfigDict(frozen=True)


class _AbjurationLevel6(_WizardLevelBase):
    class_ = Class.WIZARD

    def _get_level_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()


class _AbjurationLevel6Converter:
    def convert(self, _: AbjurationLevel6Argument) -> _AbjurationLevel6:
        return _AbjurationLevel6()


class AbjurationLevelComposer6(ModifierSource):
    priority: ClassVar[Priority] = Priority.UNORDERED

    new_level: AbjurationLevel6Argument
    previous: AbjurationLevelComposer5

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield self.previous
        yield _AbjurationLevel6Converter().convert(self.new_level)
