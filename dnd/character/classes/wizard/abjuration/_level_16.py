from __future__ import annotations

from dnd.character.classes.wizard._level_16 import WizardLevelComposer16
from dnd.character.classes.wizard.abjuration._level_15 import AbjurationLevelComposer15


class AbjurationLevelComposer16(WizardLevelComposer16):
    previous: AbjurationLevelComposer15
