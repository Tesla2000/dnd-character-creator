from typing import ClassVar
from typing import Literal

from pydantic import ConfigDict

from dnd.character.ac_modifier._base import _AcModifierContext
from dnd.character.ac_modifier._base import _CompetingAcModifier
from dnd.character.ac_modifier._type import AcModifierType
from dnd.character.armor.category import ArmorCategory
from dnd.character.armor.names import ArmorName
from dnd.character.armor.names import SHIELD
from dnd.character.race.race import Race
from dnd.choices.stats_creation.statistic import Statistic
from dnd.other_profficiencies import ArmorProficiency


class Armor(_CompetingAcModifier):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)

    type: Literal[AcModifierType.ARMOR] = AcModifierType.ARMOR
    name: ArmorName
    category: ArmorCategory
    disadvantage_on_stealth: bool
    base_ac: int
    cost: float = 0
    weight: float = 0

    def apply(self, context: _AcModifierContext) -> int:
        modifier = context.stats.get_modifier(Statistic.DEXTERITY)
        if self.category == ArmorCategory.HEAVY and (
            ArmorProficiency.ALL_ARMOR in context.armor_proficiencies
            or ArmorProficiency.HEAVY_ARMOR in context.armor_proficiencies
        ):
            bonus = 0
        elif self.category == ArmorCategory.MEDIUM and (
            ArmorProficiency.ALL_ARMOR in context.armor_proficiencies
            or ArmorProficiency.MEDIUM_ARMOR in context.armor_proficiencies
        ):
            bonus = min(2, modifier)
        else:
            bonus = modifier
        ac = self.base_ac + bonus
        if context.race == Race.LIZARDFOLK:
            ac = max(ac, 13 + modifier)
        return ac + 2 * (
            SHIELD in context.other_equipment
            and ArmorProficiency.SHIELDS in context.armor_proficiencies
        )
