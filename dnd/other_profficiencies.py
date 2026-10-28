from enum import StrEnum


class ToolProficiency(StrEnum):
    ALCHEMISTS_SUPPLIES = "Alchemist's supplies"
    BREWERS_SUPPLIES = "Brewer's supplies"
    CALLIGRAPHERS_SUPPLIES = "Calligrapher's supplies"
    CARPENTERS_TOOLS = "Carpenter's tools"
    CARTOGRAPHERS_TOOLS = "Cartographer's tools"
    COBBLERS_TOOLS = "Cobbler's tools"
    COOKS_UTENSILS = "Cook's utensils"
    GLASSBLOWERS_TOOLS = "Glassblower's tools"
    JEWELERS_TOOLS = "Jeweler's tools"
    LEATHERWORKERS_TOOLS = "Leatherworker's tools"
    MASONS_TOOLS = "Mason's tools"
    PAINTERS_SUPPLIES = "Painter's supplies"
    POTTERS_TOOLS = "Potter's tools"
    SMITHS_TOOLS = "Smith's tools"
    TINKERS_TOOLS = "Tinkerer's tools"
    WEAVERS_TOOLS = "Weaver's tools"
    WOODCARVERS_TOOLS = "Woodcarver's tools"
    DISGUISE_KIT = "Disguise kit"
    FORGERY_KIT = "Forgery kit"
    HERBALISM_KIT = "Herbalism kit"
    POISONERS_KIT = "Poisoner's kit"
    NAVIGATORS_TOOLS = "Navigator's tools"
    THIEVES_TOOLS = "Thieves' tools"
    HEALERS_KIT = "Healer's kit"
    LAND_VEHICLES = "Land vehicles"
    WATER_VEHICLES = "Water vehicles"
    ANY_OF_YOUR_CHOICE = "Any of your choice"


class GamingSet(StrEnum):
    DICE_SET = "Dice set"
    DRAGONCHESS_SET = "Dragonchess set"
    PLAYING_CARD_SET = "Playing card set"
    THREE_DRAGON_ANTE_SET = "Three-Dragon Ante set"
    ANY_OF_YOUR_CHOICE = "Gaming set of your choice"


class MusicalInstrument(StrEnum):
    BAGPIPES = "Bagpipes"
    DRUM = "Drum"
    DULCIMER = "Dulcimer"
    FLUTE = "Flute"
    LUTE = "Lute"
    LYRE = "Lyre"
    HORN = "Horn"
    PAN_FLUTE = "Pan flute"
    SHAWM = "Shawm"
    VIOL = "Viol"
    ANY_OF_YOUR_CHOICE = "Musical instrument of your choice"


class ArmorProficiency(StrEnum):
    LIGHT_ARMOR = "Light Armor"
    MEDIUM_ARMOR = "Medium Armor"
    HEAVY_ARMOR = "Heavy Armor"
    SHIELDS = "Shields"
    ANY_OF_YOUR_CHOICE = "Any of your choice"
    ALL_ARMOR = "All Armor"
