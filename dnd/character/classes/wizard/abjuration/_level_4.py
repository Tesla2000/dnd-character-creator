from __future__ import annotations

from dnd.character.classes.wizard._level_4 import WizardLevelComposer4
from dnd.character.classes.wizard.abjuration._level_3 import AbjurationLevelComposer3


class AbjurationLevelComposer4(WizardLevelComposer4):
    previous: AbjurationLevelComposer3
