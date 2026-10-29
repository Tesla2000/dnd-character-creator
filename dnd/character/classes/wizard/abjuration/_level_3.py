from __future__ import annotations

from dnd.character.classes.wizard._level_3 import WizardLevelComposer3
from dnd.character.classes.wizard.abjuration._level_2 import AbjurationLevelComposer2


class AbjurationLevelComposer3(WizardLevelComposer3):
    previous: AbjurationLevelComposer2
