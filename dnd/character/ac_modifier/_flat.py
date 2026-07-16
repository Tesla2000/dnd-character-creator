from typing import Literal

from dnd.character.ac_modifier._base import _AcModifierContext
from dnd.character.ac_modifier._base import _AdditiveAcModifier
from dnd.character.ac_modifier._type import AcModifierType


class _FlatAcModifier(_AdditiveAcModifier):
    type: Literal[AcModifierType.FLAT] = AcModifierType.FLAT
    amount: int

    def apply(self, context: _AcModifierContext) -> int:
        return self.amount
