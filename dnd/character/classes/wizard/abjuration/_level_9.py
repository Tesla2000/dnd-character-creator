from __future__ import annotations

from dnd.character.classes.wizard._level_9 import WizardLevelComposer9
from dnd.character.classes.wizard.abjuration._level_8 import AbjurationLevelComposer8


class AbjurationLevelComposer9(WizardLevelComposer9):
    previous: AbjurationLevelComposer8
