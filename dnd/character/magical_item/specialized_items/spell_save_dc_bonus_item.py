from dnd.character.magical_item.item import MagicalItem


class SpellSaveDcBonusItem(MagicalItem):
    """Generic magical item that provides bonuses to spell save DC and spell attack rolls.

    Examples: Arcane Grimoire (+1 spell save DC and spell attack rolls)
    """

    spell_save_dc_bonus: int
    spell_attack_bonus: int
