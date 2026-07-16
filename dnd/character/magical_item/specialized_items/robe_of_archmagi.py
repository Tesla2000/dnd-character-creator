from typing import ClassVar
from typing import Literal

from pydantic import ConfigDict
from pydantic import PositiveInt

from dnd.character.ac_modifier._base import _AcModifierContext
from dnd.character.ac_modifier._type import AcModifierType
from dnd.character.armor.armor import Armor
from dnd.character.armor.category import ArmorCategory
from dnd.character.armor.names import ArmorName
from dnd.character.magical_item.item import MagicalItem
from dnd.choices.stats_creation.statistic import Statistic


class RobeOfTheArchmagi(MagicalItem, Armor):
    """Legendary robe granting +2 spellcasting bonus and 15 + DEX mod AC for arcane casters."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)

    type: Literal[AcModifierType.ARMOR] = AcModifierType.ARMOR
    name: ArmorName = ArmorName.ROBE_OF_THE_ARCHMAGI
    category: ArmorCategory = ArmorCategory.NONE
    cost: PositiveInt = 15000
    disadvantage_on_stealth: bool = False
    base_ac: int = 15

    def apply(self, context: _AcModifierContext) -> int:
        return self.base_ac + context.stats.get_modifier(Statistic.DEXTERITY)
