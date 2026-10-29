from __future__ import annotations

from dnd.character.classes.wizard._level_3 import WizardLevelComposer3
from dnd.character.classes.wizard.evocation._level_2 import EvocationLevelComposer2


class EvocationLevelComposer3(WizardLevelComposer3):
    previous: EvocationLevelComposer2
