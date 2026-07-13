from dnd.character.armor.armor import Armor
from dnd.character.armor.category import ArmorCategory
from dnd.character.armor.names import ArmorName
from dnd.character.blueprint.sentinels import _ARK
from dnd.character.blueprint.sentinels import _BAK
from dnd.character.blueprint.sentinels import _BDK
from dnd.character.blueprint.sentinels import _CDK
from dnd.character.blueprint.sentinels import _CLK
from dnd.character.blueprint.sentinels import _DRK
from dnd.character.blueprint.sentinels import _FGK
from dnd.character.blueprint.sentinels import _HeK
from dnd.character.blueprint.sentinels import _MOK
from dnd.character.blueprint.sentinels import _PAK
from dnd.character.blueprint.sentinels import _RAK
from dnd.character.blueprint.sentinels import _RK
from dnd.character.blueprint.sentinels import _ROK
from dnd.character.blueprint.sentinels import _SOK
from dnd.character.blueprint.sentinels import _SkCK
from dnd.character.blueprint.sentinels import _StCK
from dnd.character.blueprint.sentinels import _WAK
from dnd.character.blueprint.sentinels import _WZK
from dnd.character.blueprint.states.state import Blueprint
from dnd.character.magical_item.item import MagicalItem
from dnd.character.stats import Stats
from dnd.choices.stats_creation.statistic import Statistic
from pydantic import PositiveInt


class RobeOfTheArchmagi(MagicalItem, Armor):
    """Legendary robe granting +2 spellcasting bonus and 15 + DEX mod AC for arcane casters."""

    name: ArmorName = ArmorName.ROBE_OF_THE_ARCHMAGI
    category: ArmorCategory = ArmorCategory.NONE
    cost: PositiveInt = 15000
    disadvantage_on_stealth: bool = False
    base_ac: int = 15

    def calc_ac(
        self,
        character: Blueprint[
            _RK,
            Stats,
            _HeK,
            _StCK,
            _SkCK,
            _WZK,
            _SOK,
            _FGK,
            _BAK,
            _ROK,
            _CLK,
            _DRK,
            _PAK,
            _RAK,
            _MOK,
            _BDK,
            _WAK,
            _ARK,
            _CDK,
        ],
    ) -> int:
        return self.base_ac + character.stats.get_modifier(Statistic.DEXTERITY)
