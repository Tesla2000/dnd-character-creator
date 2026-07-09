from dnd.character.armor.category import ArmorCategory
from dnd.character.armor.names import ArmorName
from dnd.character.armor.names import SHIELD
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
from dnd.character.blueprint.sentinels import _ROK
from dnd.character.blueprint.sentinels import _SOK
from dnd.character.blueprint.sentinels import _SkCK
from dnd.character.blueprint.sentinels import _StCK
from dnd.character.blueprint.sentinels import _WAK
from dnd.character.blueprint.sentinels import _WZK
from dnd.character.blueprint.state import Blueprint
from dnd.character.race.race import Race
from dnd.character.stats import Stats
from dnd.choices.class_creation.character_class import Class
from dnd.choices.equipment_creation.item import Item
from dnd.choices.stats_creation.statistic import Statistic
from dnd.other_profficiencies import ArmorProficiency


class Armor(Item):
    name: ArmorName
    category: ArmorCategory
    disadvantage_on_stealth: bool
    base_ac: int

    def calc_ac(
        self,
        character: Blueprint[
            Race,
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
        modifier = character.stats.get_modifier(Statistic.DEXTERITY)
        if self.category == ArmorCategory.HEAVY and (
            ArmorProficiency.ALL_ARMOR in character.armor_proficiencies
            or ArmorProficiency.HEAVY_ARMOR in character.armor_proficiencies
        ):
            bonus = 0
        elif self.category == ArmorCategory.MEDIUM and (
            ArmorProficiency.ALL_ARMOR in character.armor_proficiencies
            or ArmorProficiency.MEDIUM_ARMOR in character.armor_proficiencies
        ):
            bonus = min(2, modifier)
        else:
            bonus = modifier
            if Class.MONK in character.classes:
                bonus += character.stats.get_modifier(Statistic.WISDOM)
            elif Class.BARBARIAN in character.classes:
                bonus += character.stats.get_modifier(Statistic.CONSTITUTION)
        ac = self.base_ac + bonus
        if character.race == Race.LIZARDFOLK:
            ac = max(ac, 13 + modifier)
        return (
            ac
            + 2
            * (
                SHIELD in character.other_equipment
                and ArmorProficiency.SHIELDS in character.armor_proficiencies
            )
            + character.ac_bonus
        )
