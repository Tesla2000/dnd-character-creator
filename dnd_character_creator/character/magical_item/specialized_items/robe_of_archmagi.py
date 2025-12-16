from dnd_character_creator.character.armor.armor import Armor
from dnd_character_creator.character.armor.category import ArmorCategory
from dnd_character_creator.character.armor.names import ArmorName
from dnd_character_creator.character.character import Character
from dnd_character_creator.character.magical_item.item import BlueprintType
from dnd_character_creator.character.magical_item.item import MagicalItem
from dnd_character_creator.choices.class_creation.character_class import Class
from dnd_character_creator.choices.stats_creation.statistic import Statistic
from pydantic import PositiveInt


class RobeOfTheArchmagi(MagicalItem, Armor):
    name: ArmorName = ArmorName.ROBE_OF_THE_ARCHMAGI
    category: ArmorCategory = ArmorCategory.NONE
    cost: PositiveInt = 15000
    disadvantage_on_stealth: bool = False
    base_ac: int = 15

    def assign_to(self, blueprint: BlueprintType) -> BlueprintType:
        if not any(
            map(
                blueprint.classes.__contains__,
                (Class.SORCERER, Class.WIZARD, Class.WARLOCK),
            )
        ):
            return type(blueprint)(
                magical_items=blueprint.magical_items + (self,),
            )
        return type(blueprint)(
            magical_items=blueprint.magical_items + (self,),
            armors=blueprint.armors + (self.name,),
            spellcasting_ability_bonus=2,
            spell_save_dc_bonus=2,
        )

    def calc_ac(self, character: Character) -> int:
        return self.base_ac + character.stats.get_modifier(Statistic.DEXTERITY)
