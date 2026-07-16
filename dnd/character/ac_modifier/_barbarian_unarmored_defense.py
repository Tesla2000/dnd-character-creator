from typing import Literal

from dnd.character.ac_modifier._base import _AcModifierContext
from dnd.character.ac_modifier._base import _CompetingAcModifier
from dnd.character.ac_modifier._type import AcModifierType
from dnd.character.armor.names import SHIELD
from dnd.choices.stats_creation.statistic import Statistic
from dnd.other_profficiencies import ArmorProficiency


class _BarbarianUnarmoredDefenseAcModifier(_CompetingAcModifier):
    type: Literal[AcModifierType.BARBARIAN_UNARMORED_DEFENSE] = (
        AcModifierType.BARBARIAN_UNARMORED_DEFENSE
    )

    def apply(self, context: _AcModifierContext) -> int:
        dex = context.stats.get_modifier(Statistic.DEXTERITY)
        con = context.stats.get_modifier(Statistic.CONSTITUTION)
        shield = 2 * (
            SHIELD in context.other_equipment
            and ArmorProficiency.SHIELDS in context.armor_proficiencies
        )
        return 10 + dex + con + shield
