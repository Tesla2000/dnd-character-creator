from __future__ import annotations

from dnd.character.classes.wizard._level_5 import WizardLevelComposer5
from dnd.character.classes.wizard.abjuration._level_4 import AbjurationLevelComposer4


class AbjurationLevelComposer5(WizardLevelComposer5):
    previous: AbjurationLevelComposer4
