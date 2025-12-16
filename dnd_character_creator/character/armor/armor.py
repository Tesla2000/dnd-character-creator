from __future__ import annotations

from dnd_character_creator.character.armor.category import ArmorCategory
from dnd_character_creator.character.armor.names import SHIELD
from dnd_character_creator.character.character import Character
from dnd_character_creator.character.race.race import Race
from dnd_character_creator.choices.class_creation.character_class import Class
from dnd_character_creator.choices.equipment_creation.item import Item
from dnd_character_creator.choices.stats_creation.statistic import Statistic
from dnd_character_creator.other_profficiencies import ArmorProficiency


class Armor(Item):
    name: str
    category: ArmorCategory
    disadvantage_on_stealth: bool
    base_ac: int

    def calc_ac(self, character: Character) -> int:
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
