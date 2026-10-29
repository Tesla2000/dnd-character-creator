from __future__ import annotations

from dnd.character.classes.wizard._level_4 import WizardLevelComposer4
from dnd.character.classes.wizard.evocation._level_3 import EvocationLevelComposer3


class EvocationLevelComposer4(WizardLevelComposer4):
    previous: EvocationLevelComposer3
