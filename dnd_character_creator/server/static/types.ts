/* tslint:disable */
/* eslint-disable */
/**
/* This file was automatically generated from pydantic models by running pydantic2ts.
/* Do not modify it by hand - just update the pydantic models and then re-run the script
*/

/**
 * The character class for which to assign a subclass
 */
export type Class =
  | "Barbarian"
  | "Bard"
  | "Cleric"
  | "Druid"
  | "Fighter"
  | "Monk"
  | "Paladin"
  | "Ranger"
  | "Rogue"
  | "Sorcerer"
  | "Warlock"
  | "Wizard"
  | "Artificer";
export type ArtificerSubclass = "Alchemist" | "Armorer" | "Artillerist" | "Battle Smith";
export type BardSubclass =
  | "College of Creation"
  | "College of Eloquence"
  | "College of Glamour"
  | "College of Lore"
  | "College of Spirits"
  | "College of Swords"
  | "College of Valor"
  | "College of Whispers";
export type BarbarianSubclass =
  | "Path of the Ancestral Guardian"
  | "Path of the Battlerager"
  | "Path of the Beast"
  | "Path of the Berserker"
  | "Path of the Giant"
  | "Path of the Storm Herald"
  | "Path of the Totem Warrior"
  | "Path of Wild Magic"
  | "Path of the Zealot";
export type ClericSubclass =
  | "Arcana Domain"
  | "Death Domain"
  | "Forge Domain"
  | "Grave Domain"
  | "Knowledge Domain"
  | "Life Domain"
  | "Light Domain"
  | "Nature Domain"
  | "Order Domain"
  | "Peace Domain"
  | "Tempest Domain"
  | "Trickery Domain"
  | "Twilight Domain"
  | "War Domain";
export type DruidSubclass =
  | "Circle of Dreams"
  | "Circle of the Land"
  | "Circle of the Moon"
  | "Circle of the Shepherd"
  | "Circle of Spores"
  | "Circle of Stars"
  | "Circle of Wildfire";
export type FighterSubclass =
  | "Arcane Archer"
  | "Banneret"
  | "Battle Master"
  | "Cavalier"
  | "Champion"
  | "Echo Knight"
  | "Eldritch Knight"
  | "Psi Warrior"
  | "Rune Knight"
  | "Samurai";
export type MonkSubclass =
  | "Way of Mercy"
  | "Way of the Ascendant Dragon"
  | "Way of the Astral Self"
  | "Way of the Drunken Master"
  | "Way of the Four Elements"
  | "Way of the Kensei"
  | "Way of the Long Death"
  | "Way of the Open Hand"
  | "Way of Shadow"
  | "Way of the Sun Soul";
export type PaladinSubclass =
  | "Oath of the Ancients"
  | "Oath of Conquest"
  | "Oath of the Crown"
  | "Oath of Devotion"
  | "Oath of Glory"
  | "Oath of Redemption"
  | "Oath of Vengeance"
  | "Oath of the Watchers"
  | "Oathbreaker";
export type RangerSubclass =
  | "Beast Master Conclave"
  | "Drakewarden"
  | "Fey Wanderer"
  | "Gloom Stalker Conclave"
  | "Horizon Walker Conclave"
  | "Hunter Conclave"
  | "Monster Slayer Conclave"
  | "Swarmkeeper";
export type RogueSubclass =
  | "Arcane Trickster"
  | "Assassin"
  | "Inquisitive"
  | "Mastermind"
  | "Phantom"
  | "Scout"
  | "Soulknife"
  | "Swashbuckler"
  | "Thief";
export type SorcererSubclass =
  | "Aberrant Mind"
  | "Clockwork Soul"
  | "Draconic Bloodline"
  | "Divine Soul"
  | "Lunar Sorcery"
  | "Shadow Magic"
  | "Storm Sorcery"
  | "Wild Magic";
export type WarlockSubclass =
  | "Archfey"
  | "Celestial"
  | "Fathomless"
  | "Fiend"
  | "The Genie"
  | "Great Old One"
  | "Hexblade"
  | "Undead"
  | "Undying";
export type WizardSubclass =
  | "School of Abjuration"
  | "School of Bladesinging"
  | "School of Chronurgy"
  | "School of Conjuration"
  | "School of Divination"
  | "School of Enchantment"
  | "School of Evocation"
  | "School of Graviturgy"
  | "School of Illusion"
  | "School of Necromancy"
  | "Order of Scribes"
  | "School of Transmutation"
  | "School of War Magic";
/**
 * Character's moral and ethical alignment
 */
export type Alignment =
  | "lawful_good"
  | "true_lawful"
  | "lawful_neutral"
  | "lawful_evil"
  | "true_good"
  | "neutral_good"
  | "neutral_evil"
  | "true_neutral"
  | "neutral_neutral"
  | "true_evil"
  | "chaotic_good"
  | "true_chaotic"
  | "chaotic_neutral"
  | "chaotic_evil";
/**
 * Character's background story and origin
 */
export type Background =
  | "Acolyte"
  | "Anthropologist"
  | "Archaeologist"
  | "Athlete"
  | "Charlatan"
  | "City Watch"
  | "Clan Crafter"
  | "Cloistered Scholar"
  | "Courtier"
  | "Criminal"
  | "Entertainer"
  | "Faceless"
  | "Faction Agent"
  | "Far Traveler"
  | "Feylost"
  | "Fisher"
  | "Folk Hero"
  | "Giant Foundling"
  | "Gladiator"
  | "Guild Artisan"
  | "Guild Merchant"
  | "Haunted One"
  | "Hermit"
  | "House Agent"
  | "Inheritor"
  | "Investigator"
  | "Knight"
  | "Knight of the Order"
  | "Marine"
  | "Mercenary Veteran"
  | "Noble"
  | "Outlander"
  | "Pirate"
  | "Rewarded"
  | "Ruined"
  | "Rune Carver"
  | "Sage"
  | "Sailor"
  | "Shipwright"
  | "Smuggler"
  | "Soldier"
  | "Spy"
  | "Urban Bounty Hunter"
  | "Urchin"
  | "Uthgardt Tribe Member"
  | "Waterdhavian Noble"
  | "Witchlight Hand";
/**
 * Character's biological sex.
 */
export type Sex = "male" | "female";
/**
 * Character's race. Choose based on character concept and setting.
 */
export type Race =
  | "Human"
  | "Elf"
  | "Dwarf"
  | "Halfling"
  | "Half-Elf"
  | "Half-Orc"
  | "Tiefling"
  | "Dragonborn"
  | "Gnome"
  | "Aasimar"
  | "Genasi-Air"
  | "Genasi-Water"
  | "Genasi-Fire"
  | "Genasi-Earth"
  | "Goliath"
  | "Firbolg"
  | "Tabaxi"
  | "Lizardfolk"
  | "Kenku"
  | "Tortle"
  | "Aarakocra"
  | "Bugbear"
  | "Goblin"
  | "Hobgoblin"
  | "Kobold"
  | "Orc"
  | "Yuan-ti"
  | "Warforged"
  | "Changeling"
  | "Kalashtar"
  | "Shifter"
  | "Minotaur"
  | "Centaur"
  | "Satyr"
  | "Leonin"
  | "Verdan"
  | "Grung";
/**
 * Character's background representing their life before adventuring. Should align with character concept and backstory.
 */
export type Background1 =
  | "Acolyte"
  | "Anthropologist"
  | "Archaeologist"
  | "Athlete"
  | "Charlatan"
  | "City Watch"
  | "Clan Crafter"
  | "Cloistered Scholar"
  | "Courtier"
  | "Criminal"
  | "Entertainer"
  | "Faceless"
  | "Faction Agent"
  | "Far Traveler"
  | "Feylost"
  | "Fisher"
  | "Folk Hero"
  | "Giant Foundling"
  | "Gladiator"
  | "Guild Artisan"
  | "Guild Merchant"
  | "Haunted One"
  | "Hermit"
  | "House Agent"
  | "Inheritor"
  | "Investigator"
  | "Knight"
  | "Knight of the Order"
  | "Marine"
  | "Mercenary Veteran"
  | "Noble"
  | "Outlander"
  | "Pirate"
  | "Rewarded"
  | "Ruined"
  | "Rune Carver"
  | "Sage"
  | "Sailor"
  | "Shipwright"
  | "Smuggler"
  | "Soldier"
  | "Spy"
  | "Urban Bounty Hunter"
  | "Urchin"
  | "Uthgardt Tribe Member"
  | "Waterdhavian Noble"
  | "Witchlight Hand";
/**
 * Character's moral and ethical outlook. Should fit personality and backstory.
 */
export type Alignment1 =
  | "lawful_good"
  | "true_lawful"
  | "lawful_neutral"
  | "lawful_evil"
  | "true_good"
  | "neutral_good"
  | "neutral_evil"
  | "true_neutral"
  | "neutral_neutral"
  | "true_evil"
  | "chaotic_good"
  | "true_chaotic"
  | "chaotic_neutral"
  | "chaotic_evil";
/**
 * Building blocks for level, stats, race, and choices
 *
 * @minItems 4
 * @maxItems 4
 */
export type InitialBuilderBlocks = [unknown, unknown, unknown, unknown];
/**
 * Level increment, health increase, spell assignment, and choice resolution
 *
 * @minItems 4
 * @maxItems 4
 */
export type LevelUpBlocks = [unknown, unknown, unknown, unknown];
/**
 * Feat to add to character's feat list
 */
export type FeatName =
  | "Aberrant Dragonmark"
  | "Actor"
  | "Alert"
  | "Artificer Initiate"
  | "Athlete"
  | "Cartomancer"
  | "Charger"
  | "Chef"
  | "Crossbow Expert"
  | "Crusher"
  | "Defensive Duelist"
  | "Dual Wielder"
  | "Dungeon Delver"
  | "Durable"
  | "Eldritch Adept"
  | "Elemental Adept"
  | "Ember of the Fire Giant"
  | "Fey Touched"
  | "Fighting Initiate"
  | "Fury of the Frost Giant"
  | "Gift of the Chromatic Dragon"
  | "Gift of the Gem Dragon"
  | "Gift of the Metallic Dragon"
  | "Grappler"
  | "Great Weapon Master"
  | "Guile of the Cloud Giant"
  | "Gunner"
  | "Healer"
  | "Heavily Armored"
  | "Heavy Armor Master"
  | "Inspiring Leader"
  | "Keen Mind"
  | "Keenness of the Stone Giant"
  | "Lightly Armored"
  | "Linguist"
  | "Lucky"
  | "Mage Slayer"
  | "Magic Initiate"
  | "Martial Adept"
  | "Medium Armor Master"
  | "Metamagic Adept"
  | "Mobile"
  | "Moderately Armored"
  | "Mounted Combatant"
  | "Observant"
  | "Piercer"
  | "Poisoner"
  | "Polearm Master"
  | "Resilient"
  | "Ritual Caster"
  | "Rune Shaper"
  | "Savage Attacker"
  | "Sentinel"
  | "Shadow Touched"
  | "Sharpshooter"
  | "Shield Master"
  | "Skill Expert"
  | "Skilled"
  | "Skulker"
  | "Slasher"
  | "Soul of the Storm Giant"
  | "Spell Sniper"
  | "Strike of the Giants"
  | "Tavern Brawler"
  | "Telekinetic"
  | "Telepathic"
  | "Tough"
  | "Vigor of the Hill Giant"
  | "War Caster"
  | "Weapon Master"
  | "Ability Score Improvement"
  | "Artisan tool of your choice";
export type Skill =
  | "Any of your choice"
  | "Acrobatics"
  | "Animal Handling"
  | "Arcana"
  | "Athletics"
  | "Deception"
  | "History"
  | "Insight"
  | "Intimidation"
  | "Investigation"
  | "Medicine"
  | "Nature"
  | "Perception"
  | "Performance"
  | "Persuasion"
  | "Religion"
  | "Sleight of Hand"
  | "Stealth"
  | "Survival";
export type ToolProficiency =
  | "Alchemist's supplies"
  | "Brewer's supplies"
  | "Calligrapher's supplies"
  | "Carpenter's tools"
  | "Cartographer's tools"
  | "Cobbler's tools"
  | "Cook's utensils"
  | "Glassblower's tools"
  | "Jeweler's tools"
  | "Leatherworker's tools"
  | "Mason's tools"
  | "Painter's supplies"
  | "Potter's tools"
  | "Smith's tools"
  | "Tinkerer's tools"
  | "Weaver's tools"
  | "Woodcarver's tools"
  | "Disguise kit"
  | "Forgery kit"
  | "Herbalism kit"
  | "Poisoner's kit"
  | "Navigator's tools"
  | "Thieves' tools"
  | "Healer's kit"
  | "Land vehicles"
  | "Water vehicles"
  | "Artisan tool of your choice";
export type MusicalInstrument =
  | "Bagpipes"
  | "Drum"
  | "Dulcimer"
  | "Flute"
  | "Lute"
  | "Lyre"
  | "Horn"
  | "Pan flute"
  | "Shawm"
  | "Viol"
  | "Musical instrument of your choice";
export type GamingSet =
  | "Dice set"
  | "Dragonchess set"
  | "Playing card set"
  | "Three-Dragon Ante set"
  | "Gaming set of your choice";
export type WeaponProficiency =
  | "Simple Weapon"
  | "Martial Weapon"
  | "Club"
  | "Dagger"
  | "Greatclub"
  | "Handaxe"
  | "Javelin"
  | "Light Hammer"
  | "Mace"
  | "Quarterstaff"
  | "Sickle"
  | "Spear"
  | "Light Crossbow"
  | "Dart"
  | "Shortbow"
  | "Sling"
  | "Battleaxe"
  | "Flail"
  | "Glaive"
  | "Greatsword"
  | "Halberd"
  | "Lance"
  | "Firearms"
  | "Longsword"
  | "Maul"
  | "Morningstar"
  | "Pike"
  | "Rapier"
  | "Scimitar"
  | "Shortsword"
  | "Trident"
  | "War Pick"
  | "Warhammer"
  | "Whip"
  | "Blowgun"
  | "Hand Crossbow"
  | "Heavy Crossbow"
  | "Longbow"
  | "Net"
  | "Any of your choice";
export type ArmorProficiency =
  | "Light Armor"
  | "Medium Armor"
  | "Heavy Armor"
  | "Shields"
  | "Any of your choice"
  | "All Armor";
export type StatisticAndAny =
  | "strength"
  | "dexterity"
  | "constitution"
  | "intelligence"
  | "wisdom"
  | "charisma"
  | "any of your choice";
/**
 * The character class to increment level for
 */
export type Class1 =
  | "Barbarian"
  | "Bard"
  | "Cleric"
  | "Druid"
  | "Fighter"
  | "Monk"
  | "Paladin"
  | "Ranger"
  | "Rogue"
  | "Sorcerer"
  | "Warlock"
  | "Wizard"
  | "Artificer";
/**
 * Character's biological sex
 */
export type Sex1 = "male" | "female";
/**
 * Weapon to add to character's inventory
 */
export type WeaponName =
  | "Club"
  | "Dagger"
  | "Greatclub"
  | "Handaxe"
  | "Javelin"
  | "Light hammer"
  | "Mace"
  | "Quarterstaff"
  | "Sickle"
  | "Spear"
  | "Crossbow, light"
  | "Dart"
  | "Shortbow"
  | "Sling"
  | "Battleaxe"
  | "Flail"
  | "Glaive"
  | "Greataxe"
  | "Greatsword"
  | "Halberd"
  | "Lance"
  | "Longsword"
  | "Maul"
  | "Morningstar"
  | "Pike"
  | "Rapier"
  | "Scimitar"
  | "Shortsword"
  | "Trident"
  | "War pick"
  | "Warhammer"
  | "Whip"
  | "Blowgun"
  | "Crossbow, hand"
  | "Crossbow, heavy"
  | "Longbow"
  | "Net";
/**
 * The character class for which to assign a subclass
 */
export type Class2 =
  | "Barbarian"
  | "Bard"
  | "Cleric"
  | "Druid"
  | "Fighter"
  | "Monk"
  | "Paladin"
  | "Ranger"
  | "Rogue"
  | "Sorcerer"
  | "Warlock"
  | "Wizard"
  | "Artificer";
/**
 * The character class for which to assign a subclass
 */
export type Class3 =
  | "Barbarian"
  | "Bard"
  | "Cleric"
  | "Druid"
  | "Fighter"
  | "Monk"
  | "Paladin"
  | "Ranger"
  | "Rogue"
  | "Sorcerer"
  | "Warlock"
  | "Wizard"
  | "Artificer";
/**
 * Character class for spell assignment
 */
export type Class4 =
  | "Barbarian"
  | "Bard"
  | "Cleric"
  | "Druid"
  | "Fighter"
  | "Monk"
  | "Paladin"
  | "Ranger"
  | "Rogue"
  | "Sorcerer"
  | "Warlock"
  | "Wizard"
  | "Artificer";
/**
 * The character class for which spells are being assigned
 */
export type Class5 =
  | "Barbarian"
  | "Bard"
  | "Cleric"
  | "Druid"
  | "Fighter"
  | "Monk"
  | "Paladin"
  | "Ranger"
  | "Rogue"
  | "Sorcerer"
  | "Warlock"
  | "Wizard"
  | "Artificer";
/**
 * The character class for which health is being increased
 */
export type Class6 =
  | "Barbarian"
  | "Bard"
  | "Cleric"
  | "Druid"
  | "Fighter"
  | "Monk"
  | "Paladin"
  | "Ranger"
  | "Rogue"
  | "Sorcerer"
  | "Warlock"
  | "Wizard"
  | "Artificer";
/**
 * The character class for which health is being increased
 */
export type Class7 =
  | "Barbarian"
  | "Bard"
  | "Cleric"
  | "Druid"
  | "Fighter"
  | "Monk"
  | "Paladin"
  | "Ranger"
  | "Rogue"
  | "Sorcerer"
  | "Warlock"
  | "Wizard"
  | "Artificer";
/**
 * The character class for which health is being increased
 */
export type Class8 =
  | "Barbarian"
  | "Bard"
  | "Cleric"
  | "Druid"
  | "Fighter"
  | "Monk"
  | "Paladin"
  | "Ranger"
  | "Rogue"
  | "Sorcerer"
  | "Warlock"
  | "Wizard"
  | "Artificer";
/**
 * The character class for which health is being increased
 */
export type Class9 =
  | "Barbarian"
  | "Bard"
  | "Cleric"
  | "Druid"
  | "Fighter"
  | "Monk"
  | "Paladin"
  | "Ranger"
  | "Rogue"
  | "Sorcerer"
  | "Warlock"
  | "Wizard"
  | "Artificer";
/**
 * Character's race selection
 */
export type Race1 =
  | "Human"
  | "Elf"
  | "Dwarf"
  | "Halfling"
  | "Half-Elf"
  | "Half-Orc"
  | "Tiefling"
  | "Dragonborn"
  | "Gnome"
  | "Aasimar"
  | "Genasi-Air"
  | "Genasi-Water"
  | "Genasi-Fire"
  | "Genasi-Earth"
  | "Goliath"
  | "Firbolg"
  | "Tabaxi"
  | "Lizardfolk"
  | "Kenku"
  | "Tortle"
  | "Aarakocra"
  | "Bugbear"
  | "Goblin"
  | "Hobgoblin"
  | "Kobold"
  | "Orc"
  | "Yuan-ti"
  | "Warforged"
  | "Changeling"
  | "Kalashtar"
  | "Shifter"
  | "Minotaur"
  | "Centaur"
  | "Satyr"
  | "Leonin"
  | "Verdan"
  | "Grung";
/**
 * Enumeration of all available D&D 5e subraces with sources.
 */
export type Subrace =
  | "Aarakocra (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Fallen Aasimar (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Protector Aasimar (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Scourge Aasimar (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Fallen Aasimar (VolosGuidetoMonsters)"
  | "Protector Aasimar (VolosGuidetoMonsters)"
  | "Scourge Aasimar (VolosGuidetoMonsters)"
  | "Bugbear (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Bugbear (VolosGuidetoMonsters)"
  | "Gruul Centaur (GuildmastersGuidetoRavnica)"
  | "Selesnya Centaur (GuildmastersGuidetoRavnica)"
  | "Centaurs (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Lagonna (MythicOdysseysofTheros)"
  | "Pheres (MythicOdysseysofTheros)"
  | "Changeling (EberronRisingfromtheLastWar)"
  | "Changeling (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Changeling (UnearthedArcana)"
  | "Draconblood (ExplorersGuidetoWildemount)"
  | "Ravenite (ExplorersGuidetoWildemount)"
  | "Chromatic (FizbansTreasuryofDragons)"
  | "Gem (FizbansTreasuryofDragons)"
  | "Metallic (FizbansTreasuryofDragons)"
  | "Dragonborn (PlayersHandbook)"
  | "Chromatic (UnearthedArcana)"
  | "Gem (UnearthedArcana)"
  | "Metallic (UnearthedArcana)"
  | "Hill Dwarf (PlayersHandbook)"
  | "Mountain Dwarf (PlayersHandbook)"
  | "Mark of Shadow (EberronRisingfromtheLastWar)"
  | "Pallid Elf (ExplorersGuidetoWildemount)"
  | "Bishtahar Elf (PlaneShiftKaladesh)"
  | "Tirahar Elf (PlaneShiftKaladesh)"
  | "Vahadar Elf (PlaneShiftKaladesh)"
  | "Juraga (PlaneShiftZendikar)"
  | "Mul Daya (PlaneShiftZendikar)"
  | "Tajuru (PlaneShiftZendikar)"
  | "Dark Elf (PlayersHandbook)"
  | "High Elf (PlayersHandbook)"
  | "Wood Elf (PlayersHandbook)"
  | "Astral Elf (SpelljammerAdventuresinSpace)"
  | "Firbolg (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Firbolg (VolosGuidetoMonsters)"
  | "Air Genasi (ElementalEvilPlayersCompanion)"
  | "Air Genasi (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Earth Genasi (ElementalEvilPlayersCompanion)"
  | "Earth Genasi (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Fire Genasi (ElementalEvilPlayersCompanion)"
  | "Fire Genasi (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Water Genasi (ElementalEvilPlayersCompanion)"
  | "Water Genasi (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Mark of Scribing (EberronRisingfromtheLastWar)"
  | "Forest Gnome (PlayersHandbook)"
  | "Rock Gnome (PlayersHandbook)"
  | "Dankwood Goblin (AdventureswithMukDankwood)"
  | "Goblin (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Goblin (PlaneShiftIxalan)"
  | "Goblin (VolosGuidetoMonsters)"
  | "Goliath (ElementalEvilPlayersGuide)"
  | "Goliath (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Grung (PlayersHandbook)"
  | "Aquatic Elf Heritage (PlayersHandbook)"
  | "Dark Elf Heritage (PlayersHandbook)"
  | "High Elf Heritage (PlayersHandbook)"
  | "Wood Elf Heritage (PlayersHandbook)"
  | "Half orc Mark of Finding (EberronRisingfromtheLastWar)"
  | "Half-Orc (PlayersHandbook)"
  | "Mark of Healing (EberronRisingfromtheLastWar)"
  | "Mark of Hospitality (EberronRisingfromtheLastWar)"
  | "Lotusden Halfling (ExplorersGuidetoWildemount)"
  | "Lightfoot (PlayersHandbook)"
  | "Stout (PlayersHandbook)"
  | "Ghostwise (SwordCoastAdventurersGuide)"
  | "Hobgoblin (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Hobgoblin (UnearthedArcana)"
  | "Hobgoblin (VolosGuidetoMonsters)"
  | "Mark of Finding (EberronRisingfromtheLastWar)"
  | "Mark of Handling (EberronRisingfromtheLastWar)"
  | "Mark of Making (EberronRisingfromtheLastWar)"
  | "Mark of Passage (EberronRisingfromtheLastWar)"
  | "Mark of Sentinel (EberronRisingfromtheLastWar)"
  | "Keldon (PlaneShiftDominaria)"
  | "Gavony (PlaneShiftInnistrad)"
  | "Kessig (PlaneShiftInnistrad)"
  | "Nephalia (PlaneShiftInnistrad)"
  | "Stensia (PlaneShiftInnistrad)"
  | "Standard Human (PlayersHandbook)"
  | "Variant Human (PlayersHandbook)"
  | "Kenku (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Kalashtar (EberronRisingfromtheLastWar)"
  | "Kalashtar (UnearthedArcana)"
  | "Kobold (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Kobold (UnearthedArcana)"
  | "Kobold (VolosGuidetoMonsters)"
  | "Leonin (LeoninFeatures)"
  | "Lizardfolk (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Lizardfolk (VolosGuidetoMonsters)"
  | "Minotaur (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Orc (EberronRisingfromtheLastWar)"
  | "Orc (ExplorersGuidetoWildemount)"
  | "Orc (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Orc (PlaneShiftIxalan)"
  | "Orc (VolosGuidetoMonsters)"
  | "Yuan-ti (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Yuan-ti Pureblood (VolosGuidetoMonsters)"
  | "Satyr (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Satyr (MythicOdysseysofTheros)"
  | "Beasthide (EberronRisingfromtheLastWar)"
  | "Longtooth (EberronRisingfromtheLastWar)"
  | "Swiftstride (EberronRisingfromtheLastWar)"
  | "Wildhunt (EberronRisingfromtheLastWar)"
  | "Beasthide (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Longtooth (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Swiftstride (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Wildhunt (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Cliffwalk (UnearthedArcana)"
  | "Razorclaw (UnearthedArcana)"
  | "Tabaxi (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Tabaxi (VolosGuidetoMonsters)"
  | "Bloodline of Baalzebul (MordenkainensTomeofFoes)"
  | "Bloodline of Dispater (MordenkainensTomeofFoes)"
  | "Bloodline of Fierna (MordenkainensTomeofFoes)"
  | "Bloodline of Glasya (MordenkainensTomeofFoes)"
  | "Bloodline of Levistus (MordenkainensTomeofFoes)"
  | "Bloodline of Mammon (MordenkainensTomeofFoes)"
  | "Bloodline of Mephistopheles (MordenkainensTomeofFoes)"
  | "Bloodline of Zariel (MordenkainensTomeofFoes)"
  | "Bloodline of Asmodeus (PlayersHandbook)"
  | "Devil's Tongue(SwordCoastAdventurersGuide)"
  | "Feral (SwordCoastAdventurersGuide)"
  | "Hellfire (SwordCoastAdventurersGuide)"
  | "Winged (SwordCoastAdventurersGuide)"
  | "Abyssal Tiefling (UnearthedArcana)"
  | "Tortle (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Verdan (PlayersHandbook)"
  | "Warforged (EberronRisingfromtheLastWar)"
  | "Envoy (UnearthedArcana)"
  | "Juggernaut (UnearthedArcana)"
  | "Skirmisher (UnearthedArcana)";
export type Sex2 = "male" | "female";
export type Race2 =
  | "Human"
  | "Elf"
  | "Dwarf"
  | "Halfling"
  | "Half-Elf"
  | "Half-Orc"
  | "Tiefling"
  | "Dragonborn"
  | "Gnome"
  | "Aasimar"
  | "Genasi-Air"
  | "Genasi-Water"
  | "Genasi-Fire"
  | "Genasi-Earth"
  | "Goliath"
  | "Firbolg"
  | "Tabaxi"
  | "Lizardfolk"
  | "Kenku"
  | "Tortle"
  | "Aarakocra"
  | "Bugbear"
  | "Goblin"
  | "Hobgoblin"
  | "Kobold"
  | "Orc"
  | "Yuan-ti"
  | "Warforged"
  | "Changeling"
  | "Kalashtar"
  | "Shifter"
  | "Minotaur"
  | "Centaur"
  | "Satyr"
  | "Leonin"
  | "Verdan"
  | "Grung";
/**
 * Enumeration of all available D&D 5e subraces with sources.
 */
export type Subrace1 =
  | "Aarakocra (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Fallen Aasimar (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Protector Aasimar (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Scourge Aasimar (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Fallen Aasimar (VolosGuidetoMonsters)"
  | "Protector Aasimar (VolosGuidetoMonsters)"
  | "Scourge Aasimar (VolosGuidetoMonsters)"
  | "Bugbear (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Bugbear (VolosGuidetoMonsters)"
  | "Gruul Centaur (GuildmastersGuidetoRavnica)"
  | "Selesnya Centaur (GuildmastersGuidetoRavnica)"
  | "Centaurs (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Lagonna (MythicOdysseysofTheros)"
  | "Pheres (MythicOdysseysofTheros)"
  | "Changeling (EberronRisingfromtheLastWar)"
  | "Changeling (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Changeling (UnearthedArcana)"
  | "Draconblood (ExplorersGuidetoWildemount)"
  | "Ravenite (ExplorersGuidetoWildemount)"
  | "Chromatic (FizbansTreasuryofDragons)"
  | "Gem (FizbansTreasuryofDragons)"
  | "Metallic (FizbansTreasuryofDragons)"
  | "Dragonborn (PlayersHandbook)"
  | "Chromatic (UnearthedArcana)"
  | "Gem (UnearthedArcana)"
  | "Metallic (UnearthedArcana)"
  | "Hill Dwarf (PlayersHandbook)"
  | "Mountain Dwarf (PlayersHandbook)"
  | "Mark of Shadow (EberronRisingfromtheLastWar)"
  | "Pallid Elf (ExplorersGuidetoWildemount)"
  | "Bishtahar Elf (PlaneShiftKaladesh)"
  | "Tirahar Elf (PlaneShiftKaladesh)"
  | "Vahadar Elf (PlaneShiftKaladesh)"
  | "Juraga (PlaneShiftZendikar)"
  | "Mul Daya (PlaneShiftZendikar)"
  | "Tajuru (PlaneShiftZendikar)"
  | "Dark Elf (PlayersHandbook)"
  | "High Elf (PlayersHandbook)"
  | "Wood Elf (PlayersHandbook)"
  | "Astral Elf (SpelljammerAdventuresinSpace)"
  | "Firbolg (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Firbolg (VolosGuidetoMonsters)"
  | "Air Genasi (ElementalEvilPlayersCompanion)"
  | "Air Genasi (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Earth Genasi (ElementalEvilPlayersCompanion)"
  | "Earth Genasi (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Fire Genasi (ElementalEvilPlayersCompanion)"
  | "Fire Genasi (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Water Genasi (ElementalEvilPlayersCompanion)"
  | "Water Genasi (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Mark of Scribing (EberronRisingfromtheLastWar)"
  | "Forest Gnome (PlayersHandbook)"
  | "Rock Gnome (PlayersHandbook)"
  | "Dankwood Goblin (AdventureswithMukDankwood)"
  | "Goblin (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Goblin (PlaneShiftIxalan)"
  | "Goblin (VolosGuidetoMonsters)"
  | "Goliath (ElementalEvilPlayersGuide)"
  | "Goliath (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Grung (PlayersHandbook)"
  | "Aquatic Elf Heritage (PlayersHandbook)"
  | "Dark Elf Heritage (PlayersHandbook)"
  | "High Elf Heritage (PlayersHandbook)"
  | "Wood Elf Heritage (PlayersHandbook)"
  | "Half orc Mark of Finding (EberronRisingfromtheLastWar)"
  | "Half-Orc (PlayersHandbook)"
  | "Mark of Healing (EberronRisingfromtheLastWar)"
  | "Mark of Hospitality (EberronRisingfromtheLastWar)"
  | "Lotusden Halfling (ExplorersGuidetoWildemount)"
  | "Lightfoot (PlayersHandbook)"
  | "Stout (PlayersHandbook)"
  | "Ghostwise (SwordCoastAdventurersGuide)"
  | "Hobgoblin (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Hobgoblin (UnearthedArcana)"
  | "Hobgoblin (VolosGuidetoMonsters)"
  | "Mark of Finding (EberronRisingfromtheLastWar)"
  | "Mark of Handling (EberronRisingfromtheLastWar)"
  | "Mark of Making (EberronRisingfromtheLastWar)"
  | "Mark of Passage (EberronRisingfromtheLastWar)"
  | "Mark of Sentinel (EberronRisingfromtheLastWar)"
  | "Keldon (PlaneShiftDominaria)"
  | "Gavony (PlaneShiftInnistrad)"
  | "Kessig (PlaneShiftInnistrad)"
  | "Nephalia (PlaneShiftInnistrad)"
  | "Stensia (PlaneShiftInnistrad)"
  | "Standard Human (PlayersHandbook)"
  | "Variant Human (PlayersHandbook)"
  | "Kenku (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Kalashtar (EberronRisingfromtheLastWar)"
  | "Kalashtar (UnearthedArcana)"
  | "Kobold (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Kobold (UnearthedArcana)"
  | "Kobold (VolosGuidetoMonsters)"
  | "Leonin (LeoninFeatures)"
  | "Lizardfolk (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Lizardfolk (VolosGuidetoMonsters)"
  | "Minotaur (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Orc (EberronRisingfromtheLastWar)"
  | "Orc (ExplorersGuidetoWildemount)"
  | "Orc (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Orc (PlaneShiftIxalan)"
  | "Orc (VolosGuidetoMonsters)"
  | "Yuan-ti (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Yuan-ti Pureblood (VolosGuidetoMonsters)"
  | "Satyr (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Satyr (MythicOdysseysofTheros)"
  | "Beasthide (EberronRisingfromtheLastWar)"
  | "Longtooth (EberronRisingfromtheLastWar)"
  | "Swiftstride (EberronRisingfromtheLastWar)"
  | "Wildhunt (EberronRisingfromtheLastWar)"
  | "Beasthide (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Longtooth (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Swiftstride (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Wildhunt (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Cliffwalk (UnearthedArcana)"
  | "Razorclaw (UnearthedArcana)"
  | "Tabaxi (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Tabaxi (VolosGuidetoMonsters)"
  | "Bloodline of Baalzebul (MordenkainensTomeofFoes)"
  | "Bloodline of Dispater (MordenkainensTomeofFoes)"
  | "Bloodline of Fierna (MordenkainensTomeofFoes)"
  | "Bloodline of Glasya (MordenkainensTomeofFoes)"
  | "Bloodline of Levistus (MordenkainensTomeofFoes)"
  | "Bloodline of Mammon (MordenkainensTomeofFoes)"
  | "Bloodline of Mephistopheles (MordenkainensTomeofFoes)"
  | "Bloodline of Zariel (MordenkainensTomeofFoes)"
  | "Bloodline of Asmodeus (PlayersHandbook)"
  | "Devil's Tongue(SwordCoastAdventurersGuide)"
  | "Feral (SwordCoastAdventurersGuide)"
  | "Hellfire (SwordCoastAdventurersGuide)"
  | "Winged (SwordCoastAdventurersGuide)"
  | "Abyssal Tiefling (UnearthedArcana)"
  | "Tortle (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Verdan (PlayersHandbook)"
  | "Warforged (EberronRisingfromtheLastWar)"
  | "Envoy (UnearthedArcana)"
  | "Juggernaut (UnearthedArcana)"
  | "Skirmisher (UnearthedArcana)";
export type Background2 =
  | "Acolyte"
  | "Anthropologist"
  | "Archaeologist"
  | "Athlete"
  | "Charlatan"
  | "City Watch"
  | "Clan Crafter"
  | "Cloistered Scholar"
  | "Courtier"
  | "Criminal"
  | "Entertainer"
  | "Faceless"
  | "Faction Agent"
  | "Far Traveler"
  | "Feylost"
  | "Fisher"
  | "Folk Hero"
  | "Giant Foundling"
  | "Gladiator"
  | "Guild Artisan"
  | "Guild Merchant"
  | "Haunted One"
  | "Hermit"
  | "House Agent"
  | "Inheritor"
  | "Investigator"
  | "Knight"
  | "Knight of the Order"
  | "Marine"
  | "Mercenary Veteran"
  | "Noble"
  | "Outlander"
  | "Pirate"
  | "Rewarded"
  | "Ruined"
  | "Rune Carver"
  | "Sage"
  | "Sailor"
  | "Shipwright"
  | "Smuggler"
  | "Soldier"
  | "Spy"
  | "Urban Bounty Hunter"
  | "Urchin"
  | "Uthgardt Tribe Member"
  | "Waterdhavian Noble"
  | "Witchlight Hand";
export type Alignment2 =
  | "lawful_good"
  | "true_lawful"
  | "lawful_neutral"
  | "lawful_evil"
  | "true_good"
  | "neutral_good"
  | "neutral_evil"
  | "true_neutral"
  | "neutral_neutral"
  | "true_evil"
  | "chaotic_good"
  | "true_chaotic"
  | "chaotic_neutral"
  | "chaotic_evil";
export type FeatName1 =
  | "Aberrant Dragonmark"
  | "Actor"
  | "Alert"
  | "Artificer Initiate"
  | "Athlete"
  | "Cartomancer"
  | "Charger"
  | "Chef"
  | "Crossbow Expert"
  | "Crusher"
  | "Defensive Duelist"
  | "Dual Wielder"
  | "Dungeon Delver"
  | "Durable"
  | "Eldritch Adept"
  | "Elemental Adept"
  | "Ember of the Fire Giant"
  | "Fey Touched"
  | "Fighting Initiate"
  | "Fury of the Frost Giant"
  | "Gift of the Chromatic Dragon"
  | "Gift of the Gem Dragon"
  | "Gift of the Metallic Dragon"
  | "Grappler"
  | "Great Weapon Master"
  | "Guile of the Cloud Giant"
  | "Gunner"
  | "Healer"
  | "Heavily Armored"
  | "Heavy Armor Master"
  | "Inspiring Leader"
  | "Keen Mind"
  | "Keenness of the Stone Giant"
  | "Lightly Armored"
  | "Linguist"
  | "Lucky"
  | "Mage Slayer"
  | "Magic Initiate"
  | "Martial Adept"
  | "Medium Armor Master"
  | "Metamagic Adept"
  | "Mobile"
  | "Moderately Armored"
  | "Mounted Combatant"
  | "Observant"
  | "Piercer"
  | "Poisoner"
  | "Polearm Master"
  | "Resilient"
  | "Ritual Caster"
  | "Rune Shaper"
  | "Savage Attacker"
  | "Sentinel"
  | "Shadow Touched"
  | "Sharpshooter"
  | "Shield Master"
  | "Skill Expert"
  | "Skilled"
  | "Skulker"
  | "Slasher"
  | "Soul of the Storm Giant"
  | "Spell Sniper"
  | "Strike of the Giants"
  | "Tavern Brawler"
  | "Telekinetic"
  | "Telepathic"
  | "Tough"
  | "Vigor of the Hill Giant"
  | "War Caster"
  | "Weapon Master"
  | "Ability Score Improvement"
  | "Artisan tool of your choice";
export type ArmorName =
  | "Clothes"
  | "Padded"
  | "Leather"
  | "Studded Leather"
  | "Hide"
  | "Chain Shirt"
  | "Scale Male"
  | "Spiked Armor"
  | "Breastplate"
  | "Halfplate"
  | "Ring Mail"
  | "Chain Mail"
  | "Splint"
  | "Plate"
  | "Robe of the Archmagi";
export type WeaponName1 =
  | "Club"
  | "Dagger"
  | "Greatclub"
  | "Handaxe"
  | "Javelin"
  | "Light hammer"
  | "Mace"
  | "Quarterstaff"
  | "Sickle"
  | "Spear"
  | "Crossbow, light"
  | "Dart"
  | "Shortbow"
  | "Sling"
  | "Battleaxe"
  | "Flail"
  | "Glaive"
  | "Greataxe"
  | "Greatsword"
  | "Halberd"
  | "Lance"
  | "Longsword"
  | "Maul"
  | "Morningstar"
  | "Pike"
  | "Rapier"
  | "Scimitar"
  | "Shortsword"
  | "Trident"
  | "War pick"
  | "Warhammer"
  | "Whip"
  | "Blowgun"
  | "Crossbow, hand"
  | "Crossbow, heavy"
  | "Longbow"
  | "Net";
export type Cantrip =
  | "Acid Splash"
  | "Blade Ward"
  | "Booming Blade"
  | "Chill Touch"
  | "Control Flames"
  | "Create Bonfire"
  | "Dancing Lights"
  | "Decompose"
  | "Druidcraft"
  | "Eldritch Blast"
  | "Encode Thoughts"
  | "Fire Bolt"
  | "Friends"
  | "Frostbite"
  | "Green-Flame Blade"
  | "Guidance"
  | "Gust"
  | "Hand of Radiance"
  | "Infestation"
  | "Light"
  | "Lightning Lure"
  | "Mage Hand"
  | "Magic Stone"
  | "Mending"
  | "Message"
  | "Mind Sliver"
  | "Minor Illusion"
  | "Mold Earth"
  | "On-Off"
  | "Poison Spray"
  | "Prestidigitation"
  | "Primal Savagery"
  | "Produce Flame"
  | "Ray of Frost"
  | "Resistance"
  | "Sacred Flame"
  | "Sapping Sting"
  | "Shape Water"
  | "Shillelagh"
  | "Shocking Grasp"
  | "Spare the Dying"
  | "Sword Burst"
  | "Thaumaturgy"
  | "Thorn Whip"
  | "Thunderclap"
  | "Toll the Dead"
  | "True Strike"
  | "Vicious Mockery"
  | "Virtue"
  | "Word of Radiance";
export type FirstLevel =
  | "Absorb Elements"
  | "Acid Stream (UA)"
  | "Alarm"
  | "Animal Friendship"
  | "Arcane Weapon (UA)"
  | "Armor of Agathys"
  | "Arms of Hadar"
  | "Bane"
  | "Beast Bond"
  | "Bless"
  | "Burning Hands"
  | "Catapult"
  | "Cause Fear"
  | "Ceremony"
  | "Chaos Bolt"
  | "Charm Person"
  | "Chromatic Orb"
  | "Color Spray"
  | "Command"
  | "Compelled Duel"
  | "Comprehend Languages"
  | "Create or Destroy Water"
  | "Cure Wounds"
  | "Detect Evil and Good"
  | "Detect Magic"
  | "Detect Poison and Disease"
  | "Disguise Self"
  | "Dissonant Whispers"
  | "Distort Value"
  | "Divine Favor"
  | "Earth Tremor"
  | "Ensnaring Strike"
  | "Entangle"
  | "Expeditious Retreat"
  | "Faerie Fire"
  | "False Life"
  | "Feather Fall"
  | "Find Familiar"
  | "Fog Cloud"
  | "Frost Fingers"
  | "Gift of Alacrity"
  | "Goodberry"
  | "Grease"
  | "Guiding Bolt"
  | "Guiding Hand (UA)"
  | "Hail of Thorns"
  | "Healing Elixir (UA)"
  | "Healing Word"
  | "Hellish Rebuke"
  | "Heroism"
  | "Hex"
  | "Hunter's Mark"
  | "Ice Knife"
  | "Id Insinuation (UA)"
  | "Identify"
  | "Illusory Script"
  | "Infallible Relay (UA)"
  | "Inflict Wounds"
  | "Jim's Magic Missile"
  | "Jump"
  | "Longstrider"
  | "Mage Armor"
  | "Magic Missile"
  | "Magnify Gravity"
  | "Protection from Evil and Good"
  | "Puppet (UA)"
  | "Purify Food and Drink"
  | "Ray of Sickness"
  | "Remote Access (UA)"
  | "Sanctuary"
  | "Searing Smite"
  | "Sense Emotion (UA)"
  | "Shield"
  | "Shield of Faith"
  | "Silent Image"
  | "Silvery Barbs"
  | "Sleep"
  | "Snare"
  | "Speak with Animals"
  | "Sudden Awakening (UA)"
  | "Tasha's Caustic Brew"
  | "Tasha's Hideous Laughter"
  | "Tenser's Floating Disk"
  | "Thunderous Smite"
  | "Thunderwave"
  | "Unearthly Chorus (UA)"
  | "Unseen Servant"
  | "Wild Cunning (UA)"
  | "Witch Bolt"
  | "Wrathful Smite"
  | "Zephyr Strike";
export type SecondLevel =
  | "Aganazzar's Scorcher"
  | "Aid"
  | "Air Bubble"
  | "Alter Self"
  | "Animal Messenger"
  | "Arcane Hacking (UA)"
  | "Arcane Lock"
  | "Augury"
  | "Barkskin"
  | "Beast Sense"
  | "Blindness-Deafness"
  | "Blur"
  | "Borrowed Knowledge"
  | "Branding Smite"
  | "Calm Emotions"
  | "Cloud of Daggers"
  | "Continual Flame"
  | "Cordon of Arrows"
  | "Crown of Madness"
  | "Darkness"
  | "Darkvision"
  | "Detect Thoughts"
  | "Digital Phantom (UA)"
  | "Dragon's Breath"
  | "Dust Devil"
  | "Earthbind"
  | "Enhance Ability"
  | "Enlarge-Reduce"
  | "Enthrall"
  | "Find Steed"
  | "Find Traps"
  | "Find Vehicle (UA)"
  | "Flame Blade"
  | "Flaming Sphere"
  | "Flock of Familiars"
  | "Fortune's Favor"
  | "Gentle Repose"
  | "Gift of Gab"
  | "Gust of Wind"
  | "Healing Spirit"
  | "Heat Metal"
  | "Hold Person"
  | "Immovable Object"
  | "Invisibility"
  | "Jim's Glowing Coin"
  | "Kinetic Jaunt"
  | "Knock"
  | "Lesser Restoration"
  | "Levitate"
  | "Locate Animals or Plants"
  | "Locate Object"
  | "Magic Mouth"
  | "Magic Weapon"
  | "Maximillian's Earthen Grasp"
  | "Melf's Acid Arrow"
  | "Mental Barrier (UA)"
  | "Mind Spike"
  | "Mind Thrust (UA)"
  | "Mirror Image"
  | "Misty Step"
  | "Moonbeam"
  | "Nathair's Mischief"
  | "Nathair's Mischief (UA)"
  | "Nystul's Magic Aura"
  | "Pass Without Trace"
  | "Phantasmal Force"
  | "Prayer of Healing"
  | "Protection from Poison"
  | "Pyrotechnics"
  | "Ray of Enfeeblement"
  | "Rime's Binding Ice"
  | "Rope Trick"
  | "Scorching Ray"
  | "See Invisibility"
  | "Shadow Blade"
  | "Shatter"
  | "Silence"
  | "Skywrite"
  | "Snilloc's Snowball Storm"
  | "Spider Climb"
  | "Spike Growth"
  | "Spiritual Weapon"
  | "Spray Of Cards"
  | "Spray of Cards (UA)"
  | "Suggestion"
  | "Summon Beast"
  | "Tasha's Mind Whip"
  | "Thought Shield (UA)"
  | "Vortex Warp"
  | "Warding Bond"
  | "Warding Wind"
  | "Warp Sense"
  | "Web"
  | "Wither and Bloom"
  | "Wristpocket"
  | "Zone of Truth";
export type ThirdLevel =
  | "Animate Dead"
  | "Antagonize"
  | "Antagonize (UA)"
  | "Ashardalon's Stride"
  | "Aura of Vitality"
  | "Beacon of Hope"
  | "Bestow Curse"
  | "Blinding Smite"
  | "Blink"
  | "Call Lightning"
  | "Catnap"
  | "Clairvoyance"
  | "Conjure Animals"
  | "Conjure Barrage"
  | "Conjure Lesser Demon (UA)"
  | "Counterspell"
  | "Create Food and Water"
  | "Crusader's Mantle"
  | "Daylight"
  | "Dispel Magic"
  | "Elemental Weapon"
  | "Enemies Abound"
  | "Erupting Earth"
  | "Fast Friends"
  | "Fear"
  | "Feign Death"
  | "Fireball"
  | "Flame Arrows"
  | "Flame Stride (UA)"
  | "Fly"
  | "Galder's Tower"
  | "Gaseous Form"
  | "Glyph of Warding"
  | "Haste"
  | "Haywire (UA)"
  | "Hunger Of Hadar"
  | "Hypnotic Pattern"
  | "Incite Greed"
  | "Intellect Fortress"
  | "Invisibility To Cameras (UA)"
  | "Leomund's Tiny Hut"
  | "Life Transference"
  | "Lightning Arrow"
  | "Lightning Bolt"
  | "Magic Circle"
  | "Major Image"
  | "Mass Healing Word"
  | "Meld into Stone"
  | "Melf's Minute Meteors"
  | "Motivational Speech"
  | "Nondetection"
  | "Phantom Steed"
  | "Plant Growth"
  | "Protection from Ballistics (UA)"
  | "Protection from Energy"
  | "Psionic Blast (UA)"
  | "Remove Curse"
  | "Revivify"
  | "Sending"
  | "Sleet Storm"
  | "Slow"
  | "Speak with Dead"
  | "Speak with Plants"
  | "Spirit Guardians"
  | "Spirit Shroud"
  | "Stinking Cloud"
  | "Summon Fey"
  | "Summon Lesser Demons"
  | "Summon Shadowspawn"
  | "Summon Undead"
  | "Summon Warrior Spirit (UA)"
  | "Thunder Step"
  | "Tidal Wave"
  | "Tiny Servant"
  | "Tongues"
  | "Vampiric Touch"
  | "Wall of Sand"
  | "Wall of Water"
  | "Water Breathing"
  | "Water Walk"
  | "Wind Wall";
export type FourthLevel =
  | "Arcane Eye"
  | "Aura of Life"
  | "Aura of Purity"
  | "Banishment"
  | "Blight"
  | "Charm Monster"
  | "Compulsion"
  | "Confusion"
  | "Conjure Barlgura (UA)"
  | "Conjure Knowbot (UA)"
  | "Conjure Minor Elementals"
  | "Conjure Shadow Demon (UA)"
  | "Conjure Woodland Beings"
  | "Control Water"
  | "Death Ward"
  | "Dimension Door"
  | "Divination"
  | "Dominate Beast"
  | "Ego Whip (UA)"
  | "Elemental Bane"
  | "Evard's Black Tentacles"
  | "Fabricate"
  | "Find Greater Steed"
  | "Fire Shield"
  | "Freedom of Movement"
  | "Galder's Speedy Courier"
  | "Gate Seal"
  | "Giant Insect"
  | "Grasping Vine"
  | "Gravity Sinkhole"
  | "Greater Invisibility"
  | "Guardian of Faith"
  | "Guardian of Nature"
  | "Hallucinatory Terrain"
  | "Ice Storm"
  | "Leomund's Secret Chest"
  | "Locate Creature"
  | "Mordenkainen's Faithful Hound"
  | "Mordenkainen's Private Sanctum"
  | "Otiluke's Resilient Sphere"
  | "Phantasmal Killer"
  | "Polymorph"
  | "Raulothim's Psychic Lance"
  | "Raulothim's Psychic Lance (UA)"
  | "Shadow of Moil"
  | "Sickening Radiance"
  | "Spirit of Death"
  | "Spirit of Death (UA)"
  | "Staggering Smite"
  | "Stone Shape"
  | "Stoneskin"
  | "Storm Sphere"
  | "Summon Aberration"
  | "Summon Construct"
  | "Summon Elemental"
  | "Summon Greater Demon"
  | "Synchronicity (UA)"
  | "System Backdoor (UA)"
  | "Vitriolic Sphere"
  | "Wall of Fire"
  | "Watery Sphere"
  | "Widogast's Vault of Amber (HB)"
  | "Widogast's Web of Fire (HB)";
export type FifthLevel =
  | "Animate Objects"
  | "Antilife Shell"
  | "Awaken"
  | "Banishing Smite"
  | "Bigby's Hand"
  | "Circle of Power"
  | "Cloudkill"
  | "Commune"
  | "Commune with City (UA)"
  | "Commune with Nature"
  | "Cone of Cold"
  | "Conjure Elemental"
  | "Conjure Volley"
  | "Conjure Vrock (UA)"
  | "Contact Other Plane"
  | "Contagion"
  | "Control Winds"
  | "Create Spelljamming Helm"
  | "Creation"
  | "Danse Macabre"
  | "Dawn"
  | "Destructive Wave"
  | "Dispel Evil and Good"
  | "Dominate Person"
  | "Dream"
  | "Enervation"
  | "Far Step"
  | "Flame Strike"
  | "Freedom of the Winds (HB)"
  | "Geas"
  | "Greater Restoration"
  | "Hallow"
  | "Hold Monster"
  | "Holy Weapon"
  | "Immolation"
  | "Infernal Calling"
  | "Insect Plague"
  | "Legend Lore"
  | "Maelstrom"
  | "Mass Cure Wounds"
  | "Mislead"
  | "Modify Memory"
  | "Negative Energy Flood"
  | "Passwall"
  | "Planar Binding"
  | "Raise Dead"
  | "Rary's Telepathic Bond"
  | "Reincarnate"
  | "Scrying"
  | "Seeming"
  | "Shutdown (UA)"
  | "Skill Empowerment"
  | "Steel Wind Strike"
  | "Summon Celestial"
  | "Summon Draconic Spirit"
  | "Summon Draconic Spirit (UA)"
  | "Swift Quiver"
  | "Synaptic Static"
  | "Telekinesis"
  | "Teleportation Circle"
  | "Temporal Shunt"
  | "Transmute Rock"
  | "Tree Stride"
  | "Wall of Force"
  | "Wall of Light"
  | "Wall of Stone"
  | "Wrath Of Nature";
export type SixthLevel =
  | "otilukes_freezing_sphere"
  | "true_seeing"
  | "Arcane Gate"
  | "Blade Barrier"
  | "Bones of the Earth"
  | "Chain Lightning"
  | "Circle of Death"
  | "Conjure Fey"
  | "Contingency"
  | "Create Homunculus"
  | "Create Undead"
  | "Disintegrate"
  | "Drawmij's Instant Summons"
  | "Druid Grove"
  | "Eyebite"
  | "Find the Path"
  | "Fizban's Platinum Shield"
  | "Fizban's Platinum Shield (UA)"
  | "Flesh to Stone"
  | "Forbiddance"
  | "Globe of Invulnerability"
  | "Gravity Fissure"
  | "Guards and Wards"
  | "Harm"
  | "Heal"
  | "Heroes' Feast"
  | "Investiture of Flame"
  | "Investiture of Ice"
  | "Investiture of Stone"
  | "Investiture of Wind"
  | "Magic Jar"
  | "Mass Suggestion"
  | "Mental Prison"
  | "Move Earth"
  | "Otherworldly Form (UA)"
  | "Otiluke's Freezing Sphere"
  | "Otto's Irresistible Dance"
  | "Planar Ally"
  | "Primordial Ward"
  | "Programmed Illusion"
  | "Psychic Crush (UA)"
  | "Scatter"
  | "Soul Cage"
  | "Summon Fiend"
  | "Sunbeam"
  | "Tasha's Otherworldly Guise"
  | "Tenser's Transformation"
  | "Transport via Plants"
  | "True Seeing"
  | "Wall of Ice"
  | "Wall of Thorns"
  | "Widogast's Transmogrification (HB)"
  | "Wind Walk"
  | "Word of Recall";
export type SeventhLevel =
  | "Conjure Celestial"
  | "Conjure Hezrou (UA)"
  | "Create Magen"
  | "Crown of Stars"
  | "Delayed Blast Fireball"
  | "Divine Word"
  | "Draconic Transformation"
  | "Draconic Transformation (UA)"
  | "Dream of the Blue Veil"
  | "Etherealness"
  | "Finger of Death"
  | "Fire Storm"
  | "Forcecage"
  | "Mirage Arcane"
  | "Mordenkainen's Magnificent Mansion"
  | "Mordenkainen's Sword"
  | "Plane Shift"
  | "Power Word: Pain"
  | "Prismatic Spray"
  | "Project Image"
  | "Regenerate"
  | "Resurrection"
  | "Reverse Gravity"
  | "Sequester"
  | "Simulacrum"
  | "Symbol"
  | "Teleport"
  | "Temple of the Gods"
  | "Tether Essence"
  | "Whirlwind";
export type EighthLevel =
  | "Abi-Dalzim's Horrid Wilting"
  | "Animal Shapes"
  | "Antimagic Field"
  | "Antipathy/Sympathy"
  | "Clone"
  | "Control Weather"
  | "Dark Star"
  | "Demiplane"
  | "Dominate Monster"
  | "Earthquake"
  | "Feeblemind"
  | "Glibness"
  | "Holy Aura"
  | "Illusory Dragon"
  | "Incendiary Cloud"
  | "Maddening Darkness"
  | "Maze"
  | "Mighty Fortress"
  | "Mind Blank"
  | "Power Word: Stun"
  | "Reality Break"
  | "Sunburst"
  | "Telepathy"
  | "Tsunami";
export type NinthLevel =
  | "Astral Projection"
  | "Blade of Disaster"
  | "Foresight"
  | "Gate"
  | "Imprisonment"
  | "Invulnerability"
  | "Mass Heal"
  | "Mass Polymorph"
  | "Meteor Swarm"
  | "Power Word: Heal"
  | "Power Word: Kill"
  | "Prismatic Wall"
  | "Psychic Scream"
  | "Ravenous Void"
  | "Shapechange"
  | "Storm of Vengeance"
  | "Time Ravage"
  | "Time Stop"
  | "True Polymorph"
  | "True Resurrection"
  | "Weird"
  | "Wish";
export type Language =
  | "Common"
  | "Dwarvish"
  | "Elvish"
  | "Elven"
  | "Giant"
  | "Gnomish"
  | "Goblin"
  | "Halfling"
  | "Orc"
  | "Abyssal"
  | "Celestial"
  | "Draconic"
  | "Deep Speech"
  | "Infernal"
  | "Primordial"
  | "Sylvan"
  | "Undercommon"
  | "Auran"
  | "Aquan"
  | "Terran"
  | "Ignan"
  | "Aarakocra"
  | "Gith"
  | "Quori"
  | "Minotaur"
  | "Leonin"
  | "Thri-kreen"
  | "Lizardfolk"
  | "Kobold"
  | "Troglodyte"
  | "Yuan-ti"
  | "Grung"
  | "Druidic"
  | "Thieves' Cant"
  | "Any of your choice";
export type Level = "common" | "uncommon" | "rare" | "very_rare" | "legendary" | "artifact" | "unique" | "mistery";
export type Source = "dmg" | "phb" | "e_rlw" | "xge" | "wgte" | "scc" | "egw" | "wddm" | "cr_cn" | "homebrew";
export type Statistic = "strength" | "dexterity" | "constitution" | "intelligence" | "wisdom" | "charisma";
/**
 * The character class for which health is being increased
 */
export type Class10 =
  | "Barbarian"
  | "Bard"
  | "Cleric"
  | "Druid"
  | "Fighter"
  | "Monk"
  | "Paladin"
  | "Ranger"
  | "Rogue"
  | "Sorcerer"
  | "Warlock"
  | "Wizard"
  | "Artificer";
/**
 * The character class for which spells are being assigned
 */
export type Class11 =
  | "Barbarian"
  | "Bard"
  | "Cleric"
  | "Druid"
  | "Fighter"
  | "Monk"
  | "Paladin"
  | "Ranger"
  | "Rogue"
  | "Sorcerer"
  | "Warlock"
  | "Wizard"
  | "Artificer";
/**
 * The character's primary race
 */
export type Race3 =
  | "Human"
  | "Elf"
  | "Dwarf"
  | "Halfling"
  | "Half-Elf"
  | "Half-Orc"
  | "Tiefling"
  | "Dragonborn"
  | "Gnome"
  | "Aasimar"
  | "Genasi-Air"
  | "Genasi-Water"
  | "Genasi-Fire"
  | "Genasi-Earth"
  | "Goliath"
  | "Firbolg"
  | "Tabaxi"
  | "Lizardfolk"
  | "Kenku"
  | "Tortle"
  | "Aarakocra"
  | "Bugbear"
  | "Goblin"
  | "Hobgoblin"
  | "Kobold"
  | "Orc"
  | "Yuan-ti"
  | "Warforged"
  | "Changeling"
  | "Kalashtar"
  | "Shifter"
  | "Minotaur"
  | "Centaur"
  | "Satyr"
  | "Leonin"
  | "Verdan"
  | "Grung";
/**
 * Enumeration of all available D&D 5e subraces with sources.
 */
export type Subrace2 =
  | "Aarakocra (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Fallen Aasimar (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Protector Aasimar (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Scourge Aasimar (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Fallen Aasimar (VolosGuidetoMonsters)"
  | "Protector Aasimar (VolosGuidetoMonsters)"
  | "Scourge Aasimar (VolosGuidetoMonsters)"
  | "Bugbear (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Bugbear (VolosGuidetoMonsters)"
  | "Gruul Centaur (GuildmastersGuidetoRavnica)"
  | "Selesnya Centaur (GuildmastersGuidetoRavnica)"
  | "Centaurs (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Lagonna (MythicOdysseysofTheros)"
  | "Pheres (MythicOdysseysofTheros)"
  | "Changeling (EberronRisingfromtheLastWar)"
  | "Changeling (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Changeling (UnearthedArcana)"
  | "Draconblood (ExplorersGuidetoWildemount)"
  | "Ravenite (ExplorersGuidetoWildemount)"
  | "Chromatic (FizbansTreasuryofDragons)"
  | "Gem (FizbansTreasuryofDragons)"
  | "Metallic (FizbansTreasuryofDragons)"
  | "Dragonborn (PlayersHandbook)"
  | "Chromatic (UnearthedArcana)"
  | "Gem (UnearthedArcana)"
  | "Metallic (UnearthedArcana)"
  | "Hill Dwarf (PlayersHandbook)"
  | "Mountain Dwarf (PlayersHandbook)"
  | "Mark of Shadow (EberronRisingfromtheLastWar)"
  | "Pallid Elf (ExplorersGuidetoWildemount)"
  | "Bishtahar Elf (PlaneShiftKaladesh)"
  | "Tirahar Elf (PlaneShiftKaladesh)"
  | "Vahadar Elf (PlaneShiftKaladesh)"
  | "Juraga (PlaneShiftZendikar)"
  | "Mul Daya (PlaneShiftZendikar)"
  | "Tajuru (PlaneShiftZendikar)"
  | "Dark Elf (PlayersHandbook)"
  | "High Elf (PlayersHandbook)"
  | "Wood Elf (PlayersHandbook)"
  | "Astral Elf (SpelljammerAdventuresinSpace)"
  | "Firbolg (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Firbolg (VolosGuidetoMonsters)"
  | "Air Genasi (ElementalEvilPlayersCompanion)"
  | "Air Genasi (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Earth Genasi (ElementalEvilPlayersCompanion)"
  | "Earth Genasi (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Fire Genasi (ElementalEvilPlayersCompanion)"
  | "Fire Genasi (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Water Genasi (ElementalEvilPlayersCompanion)"
  | "Water Genasi (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Mark of Scribing (EberronRisingfromtheLastWar)"
  | "Forest Gnome (PlayersHandbook)"
  | "Rock Gnome (PlayersHandbook)"
  | "Dankwood Goblin (AdventureswithMukDankwood)"
  | "Goblin (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Goblin (PlaneShiftIxalan)"
  | "Goblin (VolosGuidetoMonsters)"
  | "Goliath (ElementalEvilPlayersGuide)"
  | "Goliath (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Grung (PlayersHandbook)"
  | "Aquatic Elf Heritage (PlayersHandbook)"
  | "Dark Elf Heritage (PlayersHandbook)"
  | "High Elf Heritage (PlayersHandbook)"
  | "Wood Elf Heritage (PlayersHandbook)"
  | "Half orc Mark of Finding (EberronRisingfromtheLastWar)"
  | "Half-Orc (PlayersHandbook)"
  | "Mark of Healing (EberronRisingfromtheLastWar)"
  | "Mark of Hospitality (EberronRisingfromtheLastWar)"
  | "Lotusden Halfling (ExplorersGuidetoWildemount)"
  | "Lightfoot (PlayersHandbook)"
  | "Stout (PlayersHandbook)"
  | "Ghostwise (SwordCoastAdventurersGuide)"
  | "Hobgoblin (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Hobgoblin (UnearthedArcana)"
  | "Hobgoblin (VolosGuidetoMonsters)"
  | "Mark of Finding (EberronRisingfromtheLastWar)"
  | "Mark of Handling (EberronRisingfromtheLastWar)"
  | "Mark of Making (EberronRisingfromtheLastWar)"
  | "Mark of Passage (EberronRisingfromtheLastWar)"
  | "Mark of Sentinel (EberronRisingfromtheLastWar)"
  | "Keldon (PlaneShiftDominaria)"
  | "Gavony (PlaneShiftInnistrad)"
  | "Kessig (PlaneShiftInnistrad)"
  | "Nephalia (PlaneShiftInnistrad)"
  | "Stensia (PlaneShiftInnistrad)"
  | "Standard Human (PlayersHandbook)"
  | "Variant Human (PlayersHandbook)"
  | "Kenku (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Kalashtar (EberronRisingfromtheLastWar)"
  | "Kalashtar (UnearthedArcana)"
  | "Kobold (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Kobold (UnearthedArcana)"
  | "Kobold (VolosGuidetoMonsters)"
  | "Leonin (LeoninFeatures)"
  | "Lizardfolk (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Lizardfolk (VolosGuidetoMonsters)"
  | "Minotaur (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Orc (EberronRisingfromtheLastWar)"
  | "Orc (ExplorersGuidetoWildemount)"
  | "Orc (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Orc (PlaneShiftIxalan)"
  | "Orc (VolosGuidetoMonsters)"
  | "Yuan-ti (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Yuan-ti Pureblood (VolosGuidetoMonsters)"
  | "Satyr (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Satyr (MythicOdysseysofTheros)"
  | "Beasthide (EberronRisingfromtheLastWar)"
  | "Longtooth (EberronRisingfromtheLastWar)"
  | "Swiftstride (EberronRisingfromtheLastWar)"
  | "Wildhunt (EberronRisingfromtheLastWar)"
  | "Beasthide (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Longtooth (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Swiftstride (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Wildhunt (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Cliffwalk (UnearthedArcana)"
  | "Razorclaw (UnearthedArcana)"
  | "Tabaxi (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Tabaxi (VolosGuidetoMonsters)"
  | "Bloodline of Baalzebul (MordenkainensTomeofFoes)"
  | "Bloodline of Dispater (MordenkainensTomeofFoes)"
  | "Bloodline of Fierna (MordenkainensTomeofFoes)"
  | "Bloodline of Glasya (MordenkainensTomeofFoes)"
  | "Bloodline of Levistus (MordenkainensTomeofFoes)"
  | "Bloodline of Mammon (MordenkainensTomeofFoes)"
  | "Bloodline of Mephistopheles (MordenkainensTomeofFoes)"
  | "Bloodline of Zariel (MordenkainensTomeofFoes)"
  | "Bloodline of Asmodeus (PlayersHandbook)"
  | "Devil's Tongue(SwordCoastAdventurersGuide)"
  | "Feral (SwordCoastAdventurersGuide)"
  | "Hellfire (SwordCoastAdventurersGuide)"
  | "Winged (SwordCoastAdventurersGuide)"
  | "Abyssal Tiefling (UnearthedArcana)"
  | "Tortle (MordenkainenPresentsMonstersoftheMultiverse)"
  | "Verdan (PlayersHandbook)"
  | "Warforged (EberronRisingfromtheLastWar)"
  | "Envoy (UnearthedArcana)"
  | "Juggernaut (UnearthedArcana)"
  | "Skirmisher (UnearthedArcana)";
/**
 * The character class for which to assign a subclass
 */
export type Class12 =
  | "Barbarian"
  | "Bard"
  | "Cleric"
  | "Druid"
  | "Fighter"
  | "Monk"
  | "Paladin"
  | "Ranger"
  | "Rogue"
  | "Sorcerer"
  | "Warlock"
  | "Wizard"
  | "Artificer";

/**
 * AI-powered resolver that makes all character choices holistically.
 *
 * Unlike the standard AllChoicesResolver which chains individual resolvers,
 * this resolver uses a single LLM call to make all choices simultaneously.
 * This allows the AI to consider the full character concept and make
 * coherent, interconnected decisions across all choice types.
 *
 * Resolves:
 * - Language ANY_OF_YOUR_CHOICE placeholders
 * - Skill proficiency ANY_OF_YOUR_CHOICE placeholders
 * - Feat ANY_OF_YOUR_CHOICE placeholders
 * - Tool proficiency ANY_OF_YOUR_CHOICE placeholders
 * - Stat choices (n_stat_choices distribution)
 * - Skill choices (n_skill_choices from available pool)
 *
 * Note: Initial data (name, backstory) and equipment choices should be
 * handled separately before or after this resolver.
 *
 * Example:
 *     >>> llm = ChatOpenAI(model="gpt-4o", temperature=0.7)
 *     >>> resolver = AIAllChoicesResolver(llm=llm)
 *     >>> builder = Builder().add(resolver)
 */
export interface AIAllChoicesResolver {
  /**
   * Ordered building blocks: stat resolver, equipment chooser, optional feat resolver, and non-stat choices resolver
   *
   * @minItems 4
   * @maxItems 4
   */
  blocks: [unknown, unknown, unknown, unknown];
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Uses AI to assign all basic character parameters based on a description.
 *
 * This building block leverages LLM structured output to generate coherent
 * character parameters (name, sex, age, race, background, alignment, level,
 * backstory, physical attributes, and personality traits) from a natural
 * language description. Always generates all fields regardless of what's
 * already set.
 *
 * Example:
 *     >>> from langchain_openai import ChatOpenAI
 *     >>> assigner = AIBaseBuilderAssigner(
 *     ...     description="A wise elderly elven wizard who studies ancient magic",
 *     ...     llm=ChatOpenAI(model="gpt-4o", temperature=0.7)
 *     ... )
 *     >>> builder = Builder([assigner])
 *     >>> character = builder.build()
 */
export interface AIBaseBuilderAssigner {
  /**
   * Natural language description of the character to generate
   */
  description: string;
  llm: ChatOpenAI;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Language model for making AI-powered decisions
 */
export interface ChatOpenAI {
  name?: string | null;
  disable_streaming?: boolean | "tool_calling";
  output_version?: string | null;
  model?: string;
  temperature?: number | null;
  model_kwargs?: {
    [k: string]: unknown;
  };
  api_key?: string | null;
  base_url?: string | null;
  organization?: string | null;
  openai_proxy?: string | null;
  timeout?: unknown;
  stream_usage?: boolean | null;
  max_retries?: number | null;
  presence_penalty?: number | null;
  frequency_penalty?: number | null;
  seed?: number | null;
  logprobs?: boolean | null;
  top_logprobs?: number | null;
  logit_bias?: {
    [k: string]: number;
  } | null;
  streaming?: boolean;
  n?: number | null;
  top_p?: number | null;
  max_completion_tokens?: number | null;
  reasoning_effort?: string | null;
  reasoning?: {
    [k: string]: unknown;
  } | null;
  verbosity?: string | null;
  tiktoken_model_name?: string | null;
  default_headers?: {
    [k: string]: string;
  } | null;
  default_query?: {
    [k: string]: unknown;
  } | null;
  stop_sequences?: string[] | string | null;
  extra_body?: {
    [k: string]: unknown;
  } | null;
  include_response_headers?: boolean;
  disabled_params?: {
    [k: string]: unknown;
  } | null;
  include?: string[] | null;
  service_tier?: string | null;
  store?: boolean | null;
  truncation?: string | null;
  use_previous_response_id?: boolean;
  use_responses_api?: boolean | null;
}
/**
 * AI-powered equipment chooser that selects equipment based on character context.
 *
 * Uses an LLM to make intelligent equipment choices based on the character's
 * class, background, stats, and overall concept. The AI receives a formatted
 * description of the character and selects the most appropriate equipment
 * from available options.
 *
 * Example:
 *     >>> from langchain_openai import ChatOpenAI
 *     >>> chooser = AIEquipmentChooser(
 *     ...     llm=ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
 *     ... )
 *     >>> builder = Builder().add(chooser)
 */
export interface AIEquipmentChooser {
  llm: ChatOpenAI1;
  formatter?: BlueprintFormatter;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Language model for making AI-powered decisions
 */
export interface ChatOpenAI1 {
  name?: string | null;
  disable_streaming?: boolean | "tool_calling";
  output_version?: string | null;
  model?: string;
  temperature?: number | null;
  model_kwargs?: {
    [k: string]: unknown;
  };
  api_key?: string | null;
  base_url?: string | null;
  organization?: string | null;
  openai_proxy?: string | null;
  timeout?: number | [unknown, unknown] | unknown | null;
  stream_usage?: boolean | null;
  max_retries?: number | null;
  presence_penalty?: number | null;
  frequency_penalty?: number | null;
  seed?: number | null;
  logprobs?: boolean | null;
  top_logprobs?: number | null;
  logit_bias?: {
    [k: string]: number;
  } | null;
  streaming?: boolean;
  n?: number | null;
  top_p?: number | null;
  max_completion_tokens?: number | null;
  reasoning_effort?: string | null;
  reasoning?: {
    [k: string]: unknown;
  } | null;
  verbosity?: string | null;
  tiktoken_model_name?: string | null;
  default_headers?: {
    [k: string]: string;
  } | null;
  default_query?: {
    [k: string]: unknown;
  } | null;
  stop_sequences?: string[] | string | null;
  extra_body?: {
    [k: string]: unknown;
  } | null;
  include_response_headers?: boolean;
  disabled_params?: {
    [k: string]: unknown;
  } | null;
  include?: string[] | null;
  service_tier?: string | null;
  store?: boolean | null;
  truncation?: string | null;
  use_previous_response_id?: boolean;
  use_responses_api?: boolean | null;
}
/**
 * Blueprint formatter for creating AI prompts
 */
export interface BlueprintFormatter {
  /**
   * Include character name
   */
  include_name?: boolean;
  /**
   * Include character sex
   */
  include_sex?: boolean;
  /**
   * Include character age
   */
  include_age?: boolean;
  /**
   * Include race and subrace
   */
  include_race?: boolean;
  /**
   * Include class and level information
   */
  include_classes?: boolean;
  /**
   * Include character background
   */
  include_background?: boolean;
  /**
   * Include character alignment
   */
  include_alignment?: boolean;
  /**
   * Include character backstory
   */
  include_backstory?: boolean;
  /**
   * Include ability scores
   */
  include_stats?: boolean;
  /**
   * Include skill proficiencies
   */
  include_skills?: boolean;
  /**
   * Include current equipment
   */
  include_equipment?: boolean;
  /**
   * Include spell information
   */
  include_spells?: boolean;
  /**
   * Include feats
   */
  include_feats?: boolean;
  /**
   * Output format style (plain text or markdown)
   */
  format_style?: "plain" | "markdown";
  /**
   * Optional custom system prompt to prepend to the formatted output
   */
  system_prompt?: string;
}
/**
 * AI-powered resolver for FeatName.ANY_OF_YOUR_CHOICE placeholders.
 *
 * Uses an LLM to make intelligent feat selections based on
 * character context (race, class, stats, etc.).
 *
 * Example:
 *     >>> resolver = AIFeatChoiceResolver(
 *     ...     llm=ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
 *     ... )
 */
export interface AIFeatChoiceResolver {
  llm: ChatOpenAI2;
  formatter?: BlueprintFormatter1;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Language model for making AI-powered decisions
 */
export interface ChatOpenAI2 {
  name?: string | null;
  disable_streaming?: boolean | "tool_calling";
  output_version?: string | null;
  model?: string;
  temperature?: number | null;
  model_kwargs?: {
    [k: string]: unknown;
  };
  api_key?: string | null;
  base_url?: string | null;
  organization?: string | null;
  openai_proxy?: string | null;
  timeout?: number | [unknown, unknown] | unknown | null;
  stream_usage?: boolean | null;
  max_retries?: number | null;
  presence_penalty?: number | null;
  frequency_penalty?: number | null;
  seed?: number | null;
  logprobs?: boolean | null;
  top_logprobs?: number | null;
  logit_bias?: {
    [k: string]: number;
  } | null;
  streaming?: boolean;
  n?: number | null;
  top_p?: number | null;
  max_completion_tokens?: number | null;
  reasoning_effort?: string | null;
  reasoning?: {
    [k: string]: unknown;
  } | null;
  verbosity?: string | null;
  tiktoken_model_name?: string | null;
  default_headers?: {
    [k: string]: string;
  } | null;
  default_query?: {
    [k: string]: unknown;
  } | null;
  stop_sequences?: string[] | string | null;
  extra_body?: {
    [k: string]: unknown;
  } | null;
  include_response_headers?: boolean;
  disabled_params?: {
    [k: string]: unknown;
  } | null;
  include?: string[] | null;
  service_tier?: string | null;
  store?: boolean | null;
  truncation?: string | null;
  use_previous_response_id?: boolean;
  use_responses_api?: boolean | null;
}
/**
 * Blueprint formatter for creating AI prompts
 */
export interface BlueprintFormatter1 {
  /**
   * Include character name
   */
  include_name?: boolean;
  /**
   * Include character sex
   */
  include_sex?: boolean;
  /**
   * Include character age
   */
  include_age?: boolean;
  /**
   * Include race and subrace
   */
  include_race?: boolean;
  /**
   * Include class and level information
   */
  include_classes?: boolean;
  /**
   * Include character background
   */
  include_background?: boolean;
  /**
   * Include character alignment
   */
  include_alignment?: boolean;
  /**
   * Include character backstory
   */
  include_backstory?: boolean;
  /**
   * Include ability scores
   */
  include_stats?: boolean;
  /**
   * Include skill proficiencies
   */
  include_skills?: boolean;
  /**
   * Include current equipment
   */
  include_equipment?: boolean;
  /**
   * Include spell information
   */
  include_spells?: boolean;
  /**
   * Include feats
   */
  include_feats?: boolean;
  /**
   * Output format style (plain text or markdown)
   */
  format_style?: "plain" | "markdown";
  /**
   * Optional custom system prompt to prepend to the formatted output
   */
  system_prompt?: string;
}
/**
 * AI-powered resolver for Language.ANY_OF_YOUR_CHOICE placeholders.
 *
 * Uses an LLM to make intelligent language selections based on
 * character context (race, background, class, etc.).
 *
 * Example:
 *     >>> resolver = AILanguageChoiceResolver(
 *     ...     llm=ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
 *     ...  )
 */
export interface AILanguageChoiceResolver {
  llm: ChatOpenAI3;
  formatter?: BlueprintFormatter2;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Language model for making AI-powered decisions
 */
export interface ChatOpenAI3 {
  name?: string | null;
  disable_streaming?: boolean | "tool_calling";
  output_version?: string | null;
  model?: string;
  temperature?: number | null;
  model_kwargs?: {
    [k: string]: unknown;
  };
  api_key?: string | null;
  base_url?: string | null;
  organization?: string | null;
  openai_proxy?: string | null;
  timeout?: number | [unknown, unknown] | unknown | null;
  stream_usage?: boolean | null;
  max_retries?: number | null;
  presence_penalty?: number | null;
  frequency_penalty?: number | null;
  seed?: number | null;
  logprobs?: boolean | null;
  top_logprobs?: number | null;
  logit_bias?: {
    [k: string]: number;
  } | null;
  streaming?: boolean;
  n?: number | null;
  top_p?: number | null;
  max_completion_tokens?: number | null;
  reasoning_effort?: string | null;
  reasoning?: {
    [k: string]: unknown;
  } | null;
  verbosity?: string | null;
  tiktoken_model_name?: string | null;
  default_headers?: {
    [k: string]: string;
  } | null;
  default_query?: {
    [k: string]: unknown;
  } | null;
  stop_sequences?: string[] | string | null;
  extra_body?: {
    [k: string]: unknown;
  } | null;
  include_response_headers?: boolean;
  disabled_params?: {
    [k: string]: unknown;
  } | null;
  include?: string[] | null;
  service_tier?: string | null;
  store?: boolean | null;
  truncation?: string | null;
  use_previous_response_id?: boolean;
  use_responses_api?: boolean | null;
}
/**
 * Blueprint formatter for creating AI prompts
 */
export interface BlueprintFormatter2 {
  /**
   * Include character name
   */
  include_name?: boolean;
  /**
   * Include character sex
   */
  include_sex?: boolean;
  /**
   * Include character age
   */
  include_age?: boolean;
  /**
   * Include race and subrace
   */
  include_race?: boolean;
  /**
   * Include class and level information
   */
  include_classes?: boolean;
  /**
   * Include character background
   */
  include_background?: boolean;
  /**
   * Include character alignment
   */
  include_alignment?: boolean;
  /**
   * Include character backstory
   */
  include_backstory?: boolean;
  /**
   * Include ability scores
   */
  include_stats?: boolean;
  /**
   * Include skill proficiencies
   */
  include_skills?: boolean;
  /**
   * Include current equipment
   */
  include_equipment?: boolean;
  /**
   * Include spell information
   */
  include_spells?: boolean;
  /**
   * Include feats
   */
  include_feats?: boolean;
  /**
   * Output format style (plain text or markdown)
   */
  format_style?: "plain" | "markdown";
  /**
   * Optional custom system prompt to prepend to the formatted output
   */
  system_prompt?: string;
}
/**
 * AI-powered magical item chooser that makes all selections holistically.
 *
 * Unlike the standard MagicalItemChooser which selects items per rarity level,
 * this chooser uses a single LLM call to select all items simultaneously.
 * This allows the AI to consider the full character concept and make
 * coherent, synergistic decisions across all item selections.
 *
 * Example:
 *     >>> llm = ChatOpenAI(model="gpt-4o", temperature=0.7)
 *     >>> chooser = AIMagicalItemChooser(
 *     ...     llm=llm,
 *     ...     n_uncommon=2,
 *     ...     n_rare=1,
 *     ... )
 *     >>> builder = Builder().add(chooser)
 */
export interface AIMagicalItemChooser {
  /**
   * Number of common magical items to select
   */
  n_common?: number;
  /**
   * Number of uncommon magical items to select
   */
  n_uncommon?: number;
  /**
   * Number of rare magical items to select
   */
  n_rare?: number;
  /**
   * Number of very rare magical items to select
   */
  n_very_rare?: number;
  /**
   * Number of legendary magical items to select
   */
  n_legendary?: number;
  /**
   * Number of artifact magical items to select
   */
  n_artifact?: number;
  /**
   * Number of unique magical items to select
   */
  n_unique?: number;
  /**
   * Number of mystery magical items to select
   */
  n_mistery?: number;
  llm: ChatOpenAI4;
  formatter?: BlueprintFormatter3;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Language model for making AI-powered decisions
 */
export interface ChatOpenAI4 {
  name?: string | null;
  disable_streaming?: boolean | "tool_calling";
  output_version?: string | null;
  model?: string;
  temperature?: number | null;
  model_kwargs?: {
    [k: string]: unknown;
  };
  api_key?: string | null;
  base_url?: string | null;
  organization?: string | null;
  openai_proxy?: string | null;
  timeout?: number | [unknown, unknown] | unknown | null;
  stream_usage?: boolean | null;
  max_retries?: number | null;
  presence_penalty?: number | null;
  frequency_penalty?: number | null;
  seed?: number | null;
  logprobs?: boolean | null;
  top_logprobs?: number | null;
  logit_bias?: {
    [k: string]: number;
  } | null;
  streaming?: boolean;
  n?: number | null;
  top_p?: number | null;
  max_completion_tokens?: number | null;
  reasoning_effort?: string | null;
  reasoning?: {
    [k: string]: unknown;
  } | null;
  verbosity?: string | null;
  tiktoken_model_name?: string | null;
  default_headers?: {
    [k: string]: string;
  } | null;
  default_query?: {
    [k: string]: unknown;
  } | null;
  stop_sequences?: string[] | string | null;
  extra_body?: {
    [k: string]: unknown;
  } | null;
  include_response_headers?: boolean;
  disabled_params?: {
    [k: string]: unknown;
  } | null;
  include?: string[] | null;
  service_tier?: string | null;
  store?: boolean | null;
  truncation?: string | null;
  use_previous_response_id?: boolean;
  use_responses_api?: boolean | null;
}
/**
 * Blueprint formatter for creating AI prompts
 */
export interface BlueprintFormatter3 {
  /**
   * Include character name
   */
  include_name?: boolean;
  /**
   * Include character sex
   */
  include_sex?: boolean;
  /**
   * Include character age
   */
  include_age?: boolean;
  /**
   * Include race and subrace
   */
  include_race?: boolean;
  /**
   * Include class and level information
   */
  include_classes?: boolean;
  /**
   * Include character background
   */
  include_background?: boolean;
  /**
   * Include character alignment
   */
  include_alignment?: boolean;
  /**
   * Include character backstory
   */
  include_backstory?: boolean;
  /**
   * Include ability scores
   */
  include_stats?: boolean;
  /**
   * Include skill proficiencies
   */
  include_skills?: boolean;
  /**
   * Include current equipment
   */
  include_equipment?: boolean;
  /**
   * Include spell information
   */
  include_spells?: boolean;
  /**
   * Include feats
   */
  include_feats?: boolean;
  /**
   * Output format style (plain text or markdown)
   */
  format_style?: "plain" | "markdown";
  /**
   * Optional custom system prompt to prepend to the formatted output
   */
  system_prompt?: string;
}
/**
 * Uses AI to fill only unset basic character parameters.
 *
 * This building block leverages LLM structured output to generate values
 * only for fields that are currently unset in the blueprint. Already set
 * fields are preserved and passed to the AI as context.
 *
 * Example:
 *     >>> from langchain_openai import ChatOpenAI
 *     >>> builder = Builder([
 *     ...     RaceAssigner(race=Race.ELF),  # Set race first
 *     ...     AIPartialBuilderAssigner(
 *     ...         description="A wise wizard",
 *     ...         llm=ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
 *     ...     ),  # AI fills other fields, respects race=ELF
 *     ... ])
 *     >>> character = builder.build()
 */
export interface AIPartialBuilderAssigner {
  /**
   * Natural language description of the character to generate
   */
  description: string;
  llm: ChatOpenAI5;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Language model for making AI-powered decisions
 */
export interface ChatOpenAI5 {
  name?: string | null;
  disable_streaming?: boolean | "tool_calling";
  output_version?: string | null;
  model?: string;
  temperature?: number | null;
  model_kwargs?: {
    [k: string]: unknown;
  };
  api_key?: string | null;
  base_url?: string | null;
  organization?: string | null;
  openai_proxy?: string | null;
  timeout?: number | [unknown, unknown] | unknown | null;
  stream_usage?: boolean | null;
  max_retries?: number | null;
  presence_penalty?: number | null;
  frequency_penalty?: number | null;
  seed?: number | null;
  logprobs?: boolean | null;
  top_logprobs?: number | null;
  logit_bias?: {
    [k: string]: number;
  } | null;
  streaming?: boolean;
  n?: number | null;
  top_p?: number | null;
  max_completion_tokens?: number | null;
  reasoning_effort?: string | null;
  reasoning?: {
    [k: string]: unknown;
  } | null;
  verbosity?: string | null;
  tiktoken_model_name?: string | null;
  default_headers?: {
    [k: string]: string;
  } | null;
  default_query?: {
    [k: string]: unknown;
  } | null;
  stop_sequences?: string[] | string | null;
  extra_body?: {
    [k: string]: unknown;
  } | null;
  include_response_headers?: boolean;
  disabled_params?: {
    [k: string]: unknown;
  } | null;
  include?: string[] | null;
  service_tier?: string | null;
  store?: boolean | null;
  truncation?: string | null;
  use_previous_response_id?: boolean;
  use_responses_api?: boolean | null;
}
/**
 * AI-powered skill choice resolver that selects skills based on character context.
 *
 * Uses an LLM to make intelligent skill selections based on the character's
 * class, background, stats, and overall concept. The AI considers which skills
 * best fit the character's role and abilities.
 *
 * Example:
 *     >>> from langchain_openai import ChatOpenAI
 *     >>> resolver = AISkillChoiceResolver(
 *     ...     llm=ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
 *     ... )
 *     >>> builder = Builder().add(resolver)
 */
export interface AISkillChoiceResolver {
  llm: ChatOpenAI6;
  formatter?: BlueprintFormatter4;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Language model for making AI-powered decisions
 */
export interface ChatOpenAI6 {
  name?: string | null;
  disable_streaming?: boolean | "tool_calling";
  output_version?: string | null;
  model?: string;
  temperature?: number | null;
  model_kwargs?: {
    [k: string]: unknown;
  };
  api_key?: string | null;
  base_url?: string | null;
  organization?: string | null;
  openai_proxy?: string | null;
  timeout?: number | [unknown, unknown] | unknown | null;
  stream_usage?: boolean | null;
  max_retries?: number | null;
  presence_penalty?: number | null;
  frequency_penalty?: number | null;
  seed?: number | null;
  logprobs?: boolean | null;
  top_logprobs?: number | null;
  logit_bias?: {
    [k: string]: number;
  } | null;
  streaming?: boolean;
  n?: number | null;
  top_p?: number | null;
  max_completion_tokens?: number | null;
  reasoning_effort?: string | null;
  reasoning?: {
    [k: string]: unknown;
  } | null;
  verbosity?: string | null;
  tiktoken_model_name?: string | null;
  default_headers?: {
    [k: string]: string;
  } | null;
  default_query?: {
    [k: string]: unknown;
  } | null;
  stop_sequences?: string[] | string | null;
  extra_body?: {
    [k: string]: unknown;
  } | null;
  include_response_headers?: boolean;
  disabled_params?: {
    [k: string]: unknown;
  } | null;
  include?: string[] | null;
  service_tier?: string | null;
  store?: boolean | null;
  truncation?: string | null;
  use_previous_response_id?: boolean;
  use_responses_api?: boolean | null;
}
/**
 * Blueprint formatter for creating AI prompts
 */
export interface BlueprintFormatter4 {
  /**
   * Include character name
   */
  include_name?: boolean;
  /**
   * Include character sex
   */
  include_sex?: boolean;
  /**
   * Include character age
   */
  include_age?: boolean;
  /**
   * Include race and subrace
   */
  include_race?: boolean;
  /**
   * Include class and level information
   */
  include_classes?: boolean;
  /**
   * Include character background
   */
  include_background?: boolean;
  /**
   * Include character alignment
   */
  include_alignment?: boolean;
  /**
   * Include character backstory
   */
  include_backstory?: boolean;
  /**
   * Include ability scores
   */
  include_stats?: boolean;
  /**
   * Include skill proficiencies
   */
  include_skills?: boolean;
  /**
   * Include current equipment
   */
  include_equipment?: boolean;
  /**
   * Include spell information
   */
  include_spells?: boolean;
  /**
   * Include feats
   */
  include_feats?: boolean;
  /**
   * Output format style (plain text or markdown)
   */
  format_style?: "plain" | "markdown";
  /**
   * Optional custom system prompt to prepend to the formatted output
   */
  system_prompt?: string;
}
/**
 * AI-powered stat choice resolver that selects stat increases based on character context.
 *
 * Uses an LLM to make intelligent decisions about which ability scores to increase
 * based on the character's class, current stats, and overall build strategy.
 *
 * Example:
 *     >>> from langchain_openai import ChatOpenAI
 *     >>> resolver = AIStatChoiceResolver(
 *     ...     llm=ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
 *     ... )
 *     >>> builder = Builder().add(resolver)
 */
export interface AIStatChoiceResolver {
  llm: ChatOpenAI7;
  formatter?: BlueprintFormatter5;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Language model for making AI-powered decisions
 */
export interface ChatOpenAI7 {
  name?: string | null;
  disable_streaming?: boolean | "tool_calling";
  output_version?: string | null;
  model?: string;
  temperature?: number | null;
  model_kwargs?: {
    [k: string]: unknown;
  };
  api_key?: string | null;
  base_url?: string | null;
  organization?: string | null;
  openai_proxy?: string | null;
  timeout?: number | [unknown, unknown] | unknown | null;
  stream_usage?: boolean | null;
  max_retries?: number | null;
  presence_penalty?: number | null;
  frequency_penalty?: number | null;
  seed?: number | null;
  logprobs?: boolean | null;
  top_logprobs?: number | null;
  logit_bias?: {
    [k: string]: number;
  } | null;
  streaming?: boolean;
  n?: number | null;
  top_p?: number | null;
  max_completion_tokens?: number | null;
  reasoning_effort?: string | null;
  reasoning?: {
    [k: string]: unknown;
  } | null;
  verbosity?: string | null;
  tiktoken_model_name?: string | null;
  default_headers?: {
    [k: string]: string;
  } | null;
  default_query?: {
    [k: string]: unknown;
  } | null;
  stop_sequences?: string[] | string | null;
  extra_body?: {
    [k: string]: unknown;
  } | null;
  include_response_headers?: boolean;
  disabled_params?: {
    [k: string]: unknown;
  } | null;
  include?: string[] | null;
  service_tier?: string | null;
  store?: boolean | null;
  truncation?: string | null;
  use_previous_response_id?: boolean;
  use_responses_api?: boolean | null;
}
/**
 * Blueprint formatter for creating AI prompts
 */
export interface BlueprintFormatter5 {
  /**
   * Include character name
   */
  include_name?: boolean;
  /**
   * Include character sex
   */
  include_sex?: boolean;
  /**
   * Include character age
   */
  include_age?: boolean;
  /**
   * Include race and subrace
   */
  include_race?: boolean;
  /**
   * Include class and level information
   */
  include_classes?: boolean;
  /**
   * Include character background
   */
  include_background?: boolean;
  /**
   * Include character alignment
   */
  include_alignment?: boolean;
  /**
   * Include character backstory
   */
  include_backstory?: boolean;
  /**
   * Include ability scores
   */
  include_stats?: boolean;
  /**
   * Include skill proficiencies
   */
  include_skills?: boolean;
  /**
   * Include current equipment
   */
  include_equipment?: boolean;
  /**
   * Include spell information
   */
  include_spells?: boolean;
  /**
   * Include feats
   */
  include_feats?: boolean;
  /**
   * Output format style (plain text or markdown)
   */
  format_style?: "plain" | "markdown";
  /**
   * Optional custom system prompt to prepend to the formatted output
   */
  system_prompt?: string;
}
/**
 * AI-powered subclass assigner that selects subclasses based on character context.
 *
 * Uses an LLM to make intelligent subclass selections based on the character's
 * background, stats, personality, and overall concept. The AI considers which
 * subclass best fits the character's thematic and mechanical direction.
 *
 * Example:
 *     >>> from dnd_character_creator.choices.class_creation.character_class import Class
 *     >>> from langchain_openai import ChatOpenAI
 *     >>> assigner = AISubclassAssigner(
 *     ...     class_=Class.WIZARD,
 *     ...     llm=ChatOpenAI(model="gpt-4o-mini", temperature=0.4)
 *     ... )
 *     >>> builder = Builder().add(assigner)
 */
export interface AISubclassAssigner {
  class_: Class;
  /**
   * Tuple of subclasses available for selection (defaults to all valid subclasses)
   */
  available_subclasses?: (
    | ArtificerSubclass
    | BardSubclass
    | BarbarianSubclass
    | ClericSubclass
    | DruidSubclass
    | FighterSubclass
    | MonkSubclass
    | PaladinSubclass
    | RangerSubclass
    | RogueSubclass
    | SorcererSubclass
    | WarlockSubclass
    | WizardSubclass
  )[];
  llm: ChatOpenAI8;
  formatter?: BlueprintFormatter6;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Language model for making AI-powered decisions
 */
export interface ChatOpenAI8 {
  name?: string | null;
  disable_streaming?: boolean | "tool_calling";
  output_version?: string | null;
  model?: string;
  temperature?: number | null;
  model_kwargs?: {
    [k: string]: unknown;
  };
  api_key?: string | null;
  base_url?: string | null;
  organization?: string | null;
  openai_proxy?: string | null;
  timeout?: number | [unknown, unknown] | unknown | null;
  stream_usage?: boolean | null;
  max_retries?: number | null;
  presence_penalty?: number | null;
  frequency_penalty?: number | null;
  seed?: number | null;
  logprobs?: boolean | null;
  top_logprobs?: number | null;
  logit_bias?: {
    [k: string]: number;
  } | null;
  streaming?: boolean;
  n?: number | null;
  top_p?: number | null;
  max_completion_tokens?: number | null;
  reasoning_effort?: string | null;
  reasoning?: {
    [k: string]: unknown;
  } | null;
  verbosity?: string | null;
  tiktoken_model_name?: string | null;
  default_headers?: {
    [k: string]: string;
  } | null;
  default_query?: {
    [k: string]: unknown;
  } | null;
  stop_sequences?: string[] | string | null;
  extra_body?: {
    [k: string]: unknown;
  } | null;
  include_response_headers?: boolean;
  disabled_params?: {
    [k: string]: unknown;
  } | null;
  include?: string[] | null;
  service_tier?: string | null;
  store?: boolean | null;
  truncation?: string | null;
  use_previous_response_id?: boolean;
  use_responses_api?: boolean | null;
}
/**
 * Blueprint formatter for creating AI prompts
 */
export interface BlueprintFormatter6 {
  /**
   * Include character name
   */
  include_name?: boolean;
  /**
   * Include character sex
   */
  include_sex?: boolean;
  /**
   * Include character age
   */
  include_age?: boolean;
  /**
   * Include race and subrace
   */
  include_race?: boolean;
  /**
   * Include class and level information
   */
  include_classes?: boolean;
  /**
   * Include character background
   */
  include_background?: boolean;
  /**
   * Include character alignment
   */
  include_alignment?: boolean;
  /**
   * Include character backstory
   */
  include_backstory?: boolean;
  /**
   * Include ability scores
   */
  include_stats?: boolean;
  /**
   * Include skill proficiencies
   */
  include_skills?: boolean;
  /**
   * Include current equipment
   */
  include_equipment?: boolean;
  /**
   * Include spell information
   */
  include_spells?: boolean;
  /**
   * Include feats
   */
  include_feats?: boolean;
  /**
   * Output format style (plain text or markdown)
   */
  format_style?: "plain" | "markdown";
  /**
   * Optional custom system prompt to prepend to the formatted output
   */
  system_prompt?: string;
}
/**
 * AI-powered resolver for tool proficiency ANY_OF_YOUR_CHOICE placeholders.
 *
 * Uses an LLM to make intelligent tool selections based on
 * character context (race, class, background, etc.).
 *
 * Example:
 *     >>> resolver = AIToolProficiencyChoiceResolver(
 *     ...     llm=ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
 *     ... )
 */
export interface AIToolProficiencyChoiceResolver {
  llm: ChatOpenAI9;
  formatter?: BlueprintFormatter7;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Language model for making AI-powered decisions
 */
export interface ChatOpenAI9 {
  name?: string | null;
  disable_streaming?: boolean | "tool_calling";
  output_version?: string | null;
  model?: string;
  temperature?: number | null;
  model_kwargs?: {
    [k: string]: unknown;
  };
  api_key?: string | null;
  base_url?: string | null;
  organization?: string | null;
  openai_proxy?: string | null;
  timeout?: number | [unknown, unknown] | unknown | null;
  stream_usage?: boolean | null;
  max_retries?: number | null;
  presence_penalty?: number | null;
  frequency_penalty?: number | null;
  seed?: number | null;
  logprobs?: boolean | null;
  top_logprobs?: number | null;
  logit_bias?: {
    [k: string]: number;
  } | null;
  streaming?: boolean;
  n?: number | null;
  top_p?: number | null;
  max_completion_tokens?: number | null;
  reasoning_effort?: string | null;
  reasoning?: {
    [k: string]: unknown;
  } | null;
  verbosity?: string | null;
  tiktoken_model_name?: string | null;
  default_headers?: {
    [k: string]: string;
  } | null;
  default_query?: {
    [k: string]: unknown;
  } | null;
  stop_sequences?: string[] | string | null;
  extra_body?: {
    [k: string]: unknown;
  } | null;
  include_response_headers?: boolean;
  disabled_params?: {
    [k: string]: unknown;
  } | null;
  include?: string[] | null;
  service_tier?: string | null;
  store?: boolean | null;
  truncation?: string | null;
  use_previous_response_id?: boolean;
  use_responses_api?: boolean | null;
}
/**
 * Blueprint formatter for creating AI prompts
 */
export interface BlueprintFormatter7 {
  /**
   * Include character name
   */
  include_name?: boolean;
  /**
   * Include character sex
   */
  include_sex?: boolean;
  /**
   * Include character age
   */
  include_age?: boolean;
  /**
   * Include race and subrace
   */
  include_race?: boolean;
  /**
   * Include class and level information
   */
  include_classes?: boolean;
  /**
   * Include character background
   */
  include_background?: boolean;
  /**
   * Include character alignment
   */
  include_alignment?: boolean;
  /**
   * Include character backstory
   */
  include_backstory?: boolean;
  /**
   * Include ability scores
   */
  include_stats?: boolean;
  /**
   * Include skill proficiencies
   */
  include_skills?: boolean;
  /**
   * Include current equipment
   */
  include_equipment?: boolean;
  /**
   * Include spell information
   */
  include_spells?: boolean;
  /**
   * Include feats
   */
  include_feats?: boolean;
  /**
   * Output format style (plain text or markdown)
   */
  format_style?: "plain" | "markdown";
  /**
   * Optional custom system prompt to prepend to the formatted output
   */
  system_prompt?: string;
}
/**
 * Assigns an age to the character.
 */
export interface AgeAssigner {
  /**
   * Character's age in years
   */
  age: number;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Assigns an alignment to the character.
 */
export interface AlignmentAssigner {
  alignment: Alignment;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Resolves all character choices by chaining individual resolvers sequentially.
 *
 * Combines language, skill, feat, tool, stat, and equipment resolvers into a
 * single pipeline that processes all character choices in order. Each resolver
 * handles its specific choice type independently.
 *
 * Example:
 *     >>> resolver = AllChoicesResolver(blocks=(
 *     ...     RandomLanguageChoiceResolver(),
 *     ...     RandomSkillChoiceResolver(),
 *     ...     RandomFeatChoiceResolver(),
 *     ...     RandomToolProficiencyChoiceResolver(),
 *     ...     PriorityStatChoiceResolver(priority=stats_priority),
 *     ...     RandomEquipmentChooser(),
 *     ... ))
 */
export interface AllChoicesResolver {
  /**
   * Ordered sequence of choice resolvers: language, skill, feat, tool, stat, and equipment
   *
   * @minItems 6
   * @maxItems 6
   */
  blocks: [unknown, unknown, unknown, unknown, unknown, unknown];
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Assigns a background to the character.
 */
export interface BackgroundAssigner {
  background: Background;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Template for AI-generated basic character parameters.
 *
 * This model defines the structure for generating core character attributes
 * using LLM structured output. All fields have descriptions to guide the AI
 * in making appropriate choices.
 */
export interface CharacterBaseTemplate {
  /**
   * Character's full name, appropriate for their race and background.
   */
  name: string;
  sex: Sex;
  /**
   * Character's age in years, appropriate for their race. Consider racial lifespans: elves live centuries, humans decades.
   */
  age: number;
  race: Race;
  background: Background1;
  alignment: Alignment1;
  /**
   * Character's personal history, motivations, and life story before adventuring.
   */
  backstory: string;
  /**
   * Character's height in inches. Should be appropriate for their race and sex.
   */
  height: number;
  /**
   * Character's weight in pounds. Should be appropriate for their race and sex.
   */
  weight: number;
  /**
   * Color of character's eyes. Can be typical or exotic based on race.
   */
  eye_color: string;
  /**
   * Character's skin tone or color. Should be appropriate for their race.
   */
  skin_color: string;
  /**
   * Description of character's hairstyle and hair color.
   */
  hairstyle: string;
  /**
   * Overall physical description of the character, including distinctive features.
   */
  appearance: string;
  /**
   * Personality traits that define how the character behaves and interacts.
   */
  character_traits: string;
  /**
   * Core beliefs and principles that guide the character's actions.
   */
  ideals: string;
  /**
   * Connections to people, places, or things that the character cares about.
   */
  bonds: string;
  /**
   * Flaws or weaknesses in the character's personality or past.
   */
  weaknesses: string;
}
/**
 * Combines multiple building blocks to apply sequentially.
 */
export interface CombinedBlock {
  /**
   * Tuple of building blocks to apply in order
   */
  blocks: (
    | (
        | CombinedBlock
        | AIAllChoicesResolver
        | AllChoicesResolver
        | InitialBuilder
        | LevelUp
        | LevelUpMultiple
        | AgeAssigner
        | AlignmentAssigner
        | NullBlock
        | AIAllNonStatChoicesResolver
        | BackgroundAssigner
        | EquipmentAdder
        | FeatAdder
        | FeatureAssigner
        | LevelAssigner
        | LevelIncrementer
        | NameAssigner
        | SexAssigner
        | WeaponAdder
        | AISubclassAssigner
        | RandomSubclassAssigner
        | OptionalSubclassAssigner
        | AIMagicalItemChooser
        | RandomMagicalItemChooser
        | LLMSpellAssigner
        | RandomSpellAssigner
        | HealthIncreaseAverage
        | HealthIncreaseRandom
        | HealthIncreaseRandomMinTwo
        | HealthIncreaseRandomRerollOnes
        | RandomInitialDataFiller
        | AIBaseBuilderAssigner
        | AIPartialBuilderAssigner
        | StandardArray
        | RaceAssigner
        | RandomRaceAssigner
        | AIToolProficiencyChoiceResolver
        | RandomToolProficiencyChoiceResolver
        | AISkillChoiceResolver
        | RandomSkillChoiceResolver
        | AILanguageChoiceResolver
        | RandomLanguageChoiceResolver
        | AIStatChoiceResolver
        | PriorityStatChoiceResolver
        | AIFeatChoiceResolver
        | RandomFeatChoiceResolver
        | MaxFirstResolver
        | MaxIfNotMaxedResolver
        | AIEquipmentChooser
        | RandomEquipmentChooser
      )
    | CombinedBlock
    | BuildingBlock
  )[];
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Building block that performs initial character generation.
 *
 * Combines level assignment, ability score building, race selection,
 * and choice resolution into a single orchestrated process.
 */
export interface InitialBuilder {
  blocks: InitialBuilderBlocks;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Adds one level to a specific class.
 *
 * Increments the level for the specified class by 1. Validates that total
 * character level doesn't exceed the blueprint's level field.
 *
 * Accepts any implementation of AllChoicesResolverBase, allowing
 * flexibility between sequential resolvers (AllChoicesResolver) and
 * holistic AI resolvers (AIAllChoicesResolver).
 *
 * Example:
 *     >>> builder = Builder([
 *     ...     LevelAssigner(level=10),
 *     ...     LevelUp(class_=Class.FIGHTER),  # +1 level
 *     ...     LevelUp(class_=Class.FIGHTER),  # +1 level
 *     ...     LevelUp(class_=Class.WIZARD),   # +1 level
 *     ... ])  # Character at level 10 with 2 Fighter / 1 Wizard (7 unused levels)
 */
export interface LevelUp {
  blocks: LevelUpBlocks;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Container for multiple level up operations.
 *
 * Combines multiple LevelUp building blocks to apply sequential level ups
 * for different classes.
 */
export interface LevelUpMultiple {
  /**
   * Tuple of LevelUp blocks to apply sequentially
   */
  blocks: LevelUp[];
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * A building block that applies no changes to the blueprint.
 *
 * Useful as a placeholder or default no-op building block when
 * a block is required but no modification is needed.
 */
export interface NullBlock {
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * AI-powered resolver for non-stat character choices (languages, skills, feats, tools).
 *
 * Handles all non-stat character choices in a single AI call, making coherent
 * decisions across languages, skill proficiencies, feats, and tool proficiencies.
 * Used internally by AIAllChoicesResolver after stat choices are handled separately.
 *
 * Example:
 *     >>> llm = ChatOpenAI(model="gpt-4o", temperature=0.7)
 *     >>> resolver = AIAllNonStatChoicesResolver(llm=llm)
 */
export interface AIAllNonStatChoicesResolver {
  llm: ChatOpenAI10;
  formatter?: BlueprintFormatter8;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Language model for making AI-powered decisions
 */
export interface ChatOpenAI10 {
  name?: string | null;
  disable_streaming?: boolean | "tool_calling";
  output_version?: string | null;
  model?: string;
  temperature?: number | null;
  model_kwargs?: {
    [k: string]: unknown;
  };
  api_key?: string | null;
  base_url?: string | null;
  organization?: string | null;
  openai_proxy?: string | null;
  timeout?: number | [unknown, unknown] | unknown | null;
  stream_usage?: boolean | null;
  max_retries?: number | null;
  presence_penalty?: number | null;
  frequency_penalty?: number | null;
  seed?: number | null;
  logprobs?: boolean | null;
  top_logprobs?: number | null;
  logit_bias?: {
    [k: string]: number;
  } | null;
  streaming?: boolean;
  n?: number | null;
  top_p?: number | null;
  max_completion_tokens?: number | null;
  reasoning_effort?: string | null;
  reasoning?: {
    [k: string]: unknown;
  } | null;
  verbosity?: string | null;
  tiktoken_model_name?: string | null;
  default_headers?: {
    [k: string]: string;
  } | null;
  default_query?: {
    [k: string]: unknown;
  } | null;
  stop_sequences?: string[] | string | null;
  extra_body?: {
    [k: string]: unknown;
  } | null;
  include_response_headers?: boolean;
  disabled_params?: {
    [k: string]: unknown;
  } | null;
  include?: string[] | null;
  service_tier?: string | null;
  store?: boolean | null;
  truncation?: string | null;
  use_previous_response_id?: boolean;
  use_responses_api?: boolean | null;
}
/**
 * Blueprint formatter for creating AI prompts
 */
export interface BlueprintFormatter8 {
  /**
   * Include character name
   */
  include_name?: boolean;
  /**
   * Include character sex
   */
  include_sex?: boolean;
  /**
   * Include character age
   */
  include_age?: boolean;
  /**
   * Include race and subrace
   */
  include_race?: boolean;
  /**
   * Include class and level information
   */
  include_classes?: boolean;
  /**
   * Include character background
   */
  include_background?: boolean;
  /**
   * Include character alignment
   */
  include_alignment?: boolean;
  /**
   * Include character backstory
   */
  include_backstory?: boolean;
  /**
   * Include ability scores
   */
  include_stats?: boolean;
  /**
   * Include skill proficiencies
   */
  include_skills?: boolean;
  /**
   * Include current equipment
   */
  include_equipment?: boolean;
  /**
   * Include spell information
   */
  include_spells?: boolean;
  /**
   * Include feats
   */
  include_feats?: boolean;
  /**
   * Output format style (plain text or markdown)
   */
  format_style?: "plain" | "markdown";
  /**
   * Optional custom system prompt to prepend to the formatted output
   */
  system_prompt?: string;
}
/**
 * Adds an item to the character's other equipment list.
 *
 * Appends to existing equipment. Allows duplicates.
 *
 * Example:
 *     >>> builder = Builder([
 *     ...     EquipmentAdder(item="Rope, hempen (50 feet)"),
 *     ...     EquipmentAdder(item="Torch"),
 *     ...     EquipmentAdder(item="Torch"),  # Second torch
 *     ...     EquipmentAdder(item="Healing potion"),
 *     ... ])
 */
export interface EquipmentAdder {
  /**
   * Equipment item to add to character's inventory
   */
  item: string;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Adds a feat to the character's feat list.
 *
 * Appends to existing feats, allowing incremental feat additions.
 * Raises error if feat already exists.
 *
 * Example:
 *     >>> builder = Builder([
 *     ...     FeatAdder(feat=FeatName.TOUGH),
 *     ...     FeatAdder(feat=FeatName.ALERT),
 *     ...     FeatAdder(feat=FeatName.LUCKY),
 *     ... ])  # Character will have all three feats
 */
export interface FeatAdder {
  feat: FeatName;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Building block that assigns a feature to a character blueprint.
 *
 * Similar to MagicalItemAssigner, this wraps a Feature object and applies
 * it to the blueprint. The Feature's assign_to method determines what
 * changes are made to the blueprint.
 *
 * Example:
 *     >>> from character.feature import Feature
 *     >>> from character.feature.specialized_features import StatBoostFeature
 *     >>> from choices.stats_creation.statistic import Statistic
 *     >>>
 *     >>> # Simple descriptive feature
 *     >>> trance = Feature(
 *     ...     name="Trance",
 *     ...     description="Elves don't need to sleep. Instead, they meditate deeply for 4 hours a day."
 *     ... )
 *     >>> trance_assigner = FeatureAssigner(feature=trance)
 *     >>>
 *     >>> # Feature that boosts a stat
 *     >>> asi = StatBoostFeature(
 *     ...     name="Ability Score Improvement",
 *     ...     description="Increase one ability score by 2",
 *     ...     stat=Statistic.STRENGTH,
 *     ...     boost_amount=2
 *     ... )
 *     >>> asi_assigner = FeatureAssigner(feature=asi)
 */
export interface FeatureAssigner {
  feature: Feature;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Character feature to assign (ability, trait, or stat boost)
 */
export interface Feature {
  source: string | null;
  ability: Ability | null;
  skill_proficiency_gain: Skill | null;
  /**
   * The same as double proficiency.
   */
  skill_expertise_gain: Skill | null;
  tool_proficiency_gain: ToolProficiency | null;
  instrument_proficiency_gain: MusicalInstrument | null;
  gaming_set_proficiency_gain: GamingSet | null;
  /**
   * Must remain empty if nothing is provided.
   */
  weapon_proficiencies_gain: WeaponProficiency[];
  /**
   * Must remain empty if nothing is provided.
   */
  armor_proficiencies_gain: ArmorProficiency[];
  attribute_increase: StatisticAndAny | null;
}
export interface Ability {
  name?: string;
  /**
   * Does this ability posses utility in combat. Mostly yes, the exceptions are improvements to skills parameters, and abilities such as trans or increased carrying capacity. Examples pack tactics, sunlite sensitivity.
   */
  combat_related?: boolean;
  description: string;
  [k: string]: unknown;
}
/**
 * Assigns a level to the character.
 */
export interface LevelAssigner {
  /**
   * Character's level (1-20)
   */
  level: number;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Building block that increments a character's level in a specific class.
 *
 * Handles multiclass level progression with validation that total class levels
 * don't exceed character level, and automatically grants ability score improvements
 * at appropriate levels (4, 8, 12, 16, 19 for wizards/sorcerers).
 */
export interface LevelIncrementer {
  class_: Class1;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Assigns a name to the character.
 */
export interface NameAssigner {
  /**
   * Character's full name
   */
  name: string;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Assigns a sex to the character.
 */
export interface SexAssigner {
  sex: Sex1;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Adds a weapon to the character's weapons list.
 *
 * Appends to existing weapons. Allows duplicates (e.g., multiple daggers).
 *
 * Example:
 *     >>> builder = Builder([
 *     ...     WeaponAdder(weapon=WeaponName.LONGSWORD),
 *     ...     WeaponAdder(weapon=WeaponName.DAGGER),
 *     ...     WeaponAdder(weapon=WeaponName.DAGGER),  # Second dagger
 *     ... ])  # Character will have longsword and 2 daggers
 */
export interface WeaponAdder {
  weapon: WeaponName;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Randomly selects a subclass from available options.
 *
 * Provides deterministic randomness when seed is set, useful for
 * reproducible character generation.
 *
 * Example:
 *     >>> from dnd_character_creator.choices.class_creation.character_class import Class
 *     >>> assigner = RandomSubclassAssigner(
 *     ...     class_=Class.WIZARD,
 *     ...     seed=42  # Reproducible
 *     ... )
 *     >>> # or
 *     >>> assigner = RandomSubclassAssigner(class_=Class.WIZARD)  # Truly random
 */
export interface RandomSubclassAssigner {
  class_: Class2;
  /**
   * Tuple of subclasses available for selection (defaults to all valid subclasses)
   */
  available_subclasses?: (
    | ArtificerSubclass
    | BardSubclass
    | BarbarianSubclass
    | ClericSubclass
    | DruidSubclass
    | FighterSubclass
    | MonkSubclass
    | PaladinSubclass
    | RangerSubclass
    | RogueSubclass
    | SorcererSubclass
    | WarlockSubclass
    | WizardSubclass
  )[];
  /**
   * Optional seed for reproducible random selection
   */
  seed?: number | null;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Optionally assigns a subclass, gracefully handling cases where assignment is not possible.
 *
 * Wraps another subclass assigner and silently succeeds if the assignment would fail
 * (e.g., character not high enough level for subclass selection).
 */
export interface OptionalSubclassAssigner {
  class_: Class3;
  /**
   * Tuple of subclasses available for selection (defaults to all valid subclasses)
   */
  available_subclasses?: (
    | ArtificerSubclass
    | BardSubclass
    | BarbarianSubclass
    | ClericSubclass
    | DruidSubclass
    | FighterSubclass
    | MonkSubclass
    | PaladinSubclass
    | RangerSubclass
    | RogueSubclass
    | SorcererSubclass
    | WarlockSubclass
    | WizardSubclass
  )[];
  /**
   * The subclass assigner strategy to use (random or AI)
   */
  assigner: RandomSubclassAssigner | AISubclassAssigner;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Randomly selects magical items by rarity level.
 *
 * Selects items level-by-level using random.choices(), allowing duplicates.
 * Optionally accepts a seed for reproducible selection.
 *
 * Example:
 *     >>> chooser = RandomMagicalItemChooser(
 *     ...     n_uncommon=2,
 *     ...     n_rare=1,
 *     ...     seed=42,
 *     ... )
 *     >>> builder = Builder().add(chooser)
 */
export interface RandomMagicalItemChooser {
  /**
   * Number of common magical items to select
   */
  n_common?: number;
  /**
   * Number of uncommon magical items to select
   */
  n_uncommon?: number;
  /**
   * Number of rare magical items to select
   */
  n_rare?: number;
  /**
   * Number of very rare magical items to select
   */
  n_very_rare?: number;
  /**
   * Number of legendary magical items to select
   */
  n_legendary?: number;
  /**
   * Number of artifact magical items to select
   */
  n_artifact?: number;
  /**
   * Number of unique magical items to select
   */
  n_unique?: number;
  /**
   * Number of mystery magical items to select
   */
  n_mistery?: number;
  /**
   * Optional seed for reproducible random selection
   */
  seed?: number | null;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Uses LLM to select thematically appropriate spells.
 *
 * Selects spells based on character background, personality, and theme
 * using an LLM to make intelligent choices that fit the character concept.
 *
 * Example:
 *     >>> from langchain_openai import ChatOpenAI
 *     >>> assigner = LLMSpellAssigner(
 *     ...     class_=Class.WIZARD,
 *     ...     llm=ChatOpenAI(model="gpt-4o-mini", temperature=0.7),
 *     ...     character_description="Fire-focused evocation specialist",
 *     ... )
 */
export interface LLMSpellAssigner {
  class_: Class4;
  llm: ChatOpenAI11;
  /**
   * Additional character context for AI spell selection
   */
  character_description?: string | null;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Language model for making AI-powered decisions
 */
export interface ChatOpenAI11 {
  name?: string | null;
  disable_streaming?: boolean | "tool_calling";
  output_version?: string | null;
  model?: string;
  temperature?: number | null;
  model_kwargs?: {
    [k: string]: unknown;
  };
  api_key?: string | null;
  base_url?: string | null;
  organization?: string | null;
  openai_proxy?: string | null;
  timeout?: number | [unknown, unknown] | unknown | null;
  stream_usage?: boolean | null;
  max_retries?: number | null;
  presence_penalty?: number | null;
  frequency_penalty?: number | null;
  seed?: number | null;
  logprobs?: boolean | null;
  top_logprobs?: number | null;
  logit_bias?: {
    [k: string]: number;
  } | null;
  streaming?: boolean;
  n?: number | null;
  top_p?: number | null;
  max_completion_tokens?: number | null;
  reasoning_effort?: string | null;
  reasoning?: {
    [k: string]: unknown;
  } | null;
  verbosity?: string | null;
  tiktoken_model_name?: string | null;
  default_headers?: {
    [k: string]: string;
  } | null;
  default_query?: {
    [k: string]: unknown;
  } | null;
  stop_sequences?: string[] | string | null;
  extra_body?: {
    [k: string]: unknown;
  } | null;
  include_response_headers?: boolean;
  disabled_params?: {
    [k: string]: unknown;
  } | null;
  include?: string[] | null;
  service_tier?: string | null;
  store?: boolean | null;
  truncation?: string | null;
  use_previous_response_id?: boolean;
  use_responses_api?: boolean | null;
}
/**
 * Randomly selects spells from available class spell list.
 *
 * Provides deterministic randomness when seed is set, useful for
 * reproducible character generation.
 *
 * Example:
 *     >>> assigner = RandomSpellAssigner(
 *     ...     class_=Class.WIZARD,
 *     ...     seed=42,  # Reproducible
 *     ... )
 */
export interface RandomSpellAssigner {
  class_: Class5;
  /**
   * Optional seed for reproducible random selection
   */
  seed?: number | null;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Fixed health increase strategy.
 *
 * Uses the average value of the hit die (hit_die // 2 + 1) for non-first levels.
 * First level always gets the maximum hit die value.
 *
 * Example:
 *     - d6 hit die: +4 health per level (after first)
 *     - d8 hit die: +5 health per level (after first)
 *     - d10 hit die: +6 health per level (after first)
 *     - d12 hit die: +7 health per level (after first)
 */
export interface HealthIncreaseAverage {
  class_: Class6;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Random health increase strategy.
 *
 * Rolls a random value between 1 and the hit die size for non-first levels.
 * First level always gets the maximum hit die value.
 *
 * Example:
 *     - d6 hit die: random 1-6 health per level (after first)
 *     - d8 hit die: random 1-8 health per level (after first)
 *     - d10 hit die: random 1-10 health per level (after first)
 *     - d12 hit die: random 1-12 health per level (after first)
 */
export interface HealthIncreaseRandom {
  class_: Class7;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Random health increase strategy with minimum value of 2.
 *
 * Rolls a random value between 2 and the hit die size.
 * First level always gets the maximum hit die value.
 *
 * Example:
 *     - d6 hit die: random 2-6
 *     - d8 hit die: random 2-8
 *     - d10 hit die: random 2-10
 *     - d12 hit die: random 2-12
 */
export interface HealthIncreaseRandomMinTwo {
  class_: Class8;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Random health increase strategy with reroll on 1.
 *
 * Rolls a random value between 1 and the hit die size.
 * If a 1 is rolled, reroll once and take the new value.
 * First level always gets the maximum hit die value.
 *
 * Example:
 *     - d6 hit die: random 1-6, reroll if 1
 *     - d8 hit die: random 1-8, reroll if 1
 *     - d10 hit die: random 1-10, reroll if 1
 *     - d12 hit die: random 1-12, reroll if 1
 */
export interface HealthIncreaseRandomRerollOnes {
  class_: Class9;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Fills missing required Character fields with random mock data.
 *
 * Only fills fields that are currently None. Does not overwrite existing values.
 *
 * Example:
 *     >>> filler = RandomInitialDataFiller(seed=42)  # Reproducible
 *     >>> # or
 *     >>> filler = RandomInitialDataFiller()  # Truly random
 */
export interface RandomInitialDataFiller {
  /**
   * Optional seed for reproducible random selection
   */
  seed?: number | null;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Assigns ability scores using the standard array method (15, 14, 13, 12, 10, 8).
 *
 * Distributes the standard D&D 5e ability score array to the six ability scores
 * based on the provided stats priority, assigning higher values to more important stats.
 *
 * Example:
 *     >>> stats_priority = StatsPriority((Statistic.STR, Statistic.CON, ...))
 *     >>> builder = StandardArray(stats_priority=stats_priority)
 *     >>> # Will assign 15 to STR, 14 to CON, etc.
 */
export interface StandardArray {
  /**
   * Ability scores ranked by priority for stat assignment
   *
   * @minItems 6
   * @maxItems 6
   */
  stats_priority: [unknown, unknown, unknown, unknown, unknown, unknown];
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Assigns a race to the character.
 */
export interface RaceAssigner {
  race: Race1;
  subrace: Subrace;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Building block that randomly assigns a race and subrace to a character.
 */
export interface RandomRaceAssigner {
  /**
   * Optional seed for reproducible random selection
   */
  seed?: number | null;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Randomly selects tool proficiencies for ANY_OF_YOUR_CHOICE placeholders.
 *
 * Provides deterministic randomness when seed is set, useful for
 * reproducible character generation.
 *
 * Example:
 *     >>> resolver = RandomToolProficiencyChoiceResolver(seed=42)
 *     >>> # or
 *     >>> resolver = RandomToolProficiencyChoiceResolver()  # Truly random
 */
export interface RandomToolProficiencyChoiceResolver {
  /**
   * Optional seed for reproducible random selection
   */
  seed?: number | null;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Randomly selects skills from available options.
 *
 * Provides deterministic randomness when seed is set, useful for
 * reproducible character generation.
 *
 * Example:
 *     >>> resolver = RandomSkillChoiceResolver(seed=42)  # Reproducible
 *     >>> # or
 *     >>> resolver = RandomSkillChoiceResolver()  # Truly random
 */
export interface RandomSkillChoiceResolver {
  /**
   * Optional seed for reproducible random selection
   */
  seed?: number | null;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Randomly selects languages for ANY_OF_YOUR_CHOICE placeholders.
 *
 * Provides deterministic randomness when seed is set, useful for
 * reproducible character generation.
 *
 * Example:
 *     >>> resolver = RandomLanguageChoiceResolver(seed=42)
 *     >>> # or
 *     >>> resolver = RandomLanguageChoiceResolver()  # Truly random
 */
export interface RandomLanguageChoiceResolver {
  /**
   * Optional seed for reproducible random selection
   */
  seed?: number | null;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Resolves stat choices based on a priority order.
 *
 * Uses logic similar to ability score improvements: prioritizes making odd
 * stats even (for better modifier bonuses) while respecting priority order.
 *
 * In D&D 5e, ability modifiers are calculated as (stat - 10) / 2 rounded down.
 * This means increasing an odd stat to even provides a modifier improvement,
 * while increasing an even stat by just 1 doesn't help. This resolver optimizes
 * stat distribution by preferring odd stats when possible.
 *
 * Example:
 *     >>> resolver = PriorityStatChoiceResolver(
 *     ...     priority=(
 *     ...         Statistic.STRENGTH,
 *     ...         Statistic.CONSTITUTION,
 *     ...         Statistic.DEXTERITY,
 *     ...         Statistic.WISDOM,
 *     ...         Statistic.INTELLIGENCE,
 *     ...         Statistic.CHARISMA,
 *     ...     )
 *     ... )
 *     >>> # Distributes points intelligently based on current stat values
 *     >>> # Prioritizes odd stats to maximize modifier improvements
 */
export interface PriorityStatChoiceResolver {
  /**
   * Ability scores ranked by priority for stat increase allocation
   *
   * @minItems 6
   * @maxItems 6
   */
  priority: [unknown, unknown, unknown, unknown, unknown, unknown];
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Randomly selects feats for ANY_OF_YOUR_CHOICE placeholders.
 *
 * Provides deterministic randomness when seed is set, useful for
 * reproducible character generation.
 *
 * Example:
 *     >>> resolver = RandomFeatChoiceResolver(seed=42)
 *     >>> # or
 *     >>> resolver = RandomFeatChoiceResolver()  # Truly random
 */
export interface RandomFeatChoiceResolver {
  /**
   * Optional seed for reproducible random selection
   */
  seed?: number | null;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Prioritizes maxing the highest priority stat before choosing other feats.
 *
 * Checks if the highest priority stat is below its cap and selects Ability Score
 * Improvement if so. Otherwise, delegates to the fallback resolver (random or AI).
 *
 * Example:
 *     >>> resolver = MaxFirstResolver(
 *     ...     priority=StatsPriority((Statistic.STR, ...)),
 *     ...     then=RandomFeatChoiceResolver()
 *     ... )
 *     >>> # Will choose ASI if STR < cap, otherwise random feat
 */
export interface MaxFirstResolver {
  /**
   * Ability score priority order for determining which stat to max
   *
   * @minItems 6
   * @maxItems 6
   */
  priority: [unknown, unknown, unknown, unknown, unknown, unknown];
  /**
   * Fallback resolver to use when highest priority stat is already maxed
   */
  then: RandomFeatChoiceResolver | AIFeatChoiceResolver;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Chooses Ability Score Improvement only if the highest priority stat is not maxed.
 *
 * If the highest priority stat is already at its cap, returns an empty blueprint
 * instead of choosing a feat. Useful for builds that want ASI when possible but
 * skip the feat choice entirely when not needed.
 *
 * Example:
 *     >>> resolver = MaxIfNotMaxedResolver(
 *     ...     priority=StatsPriority((Statistic.DEX, ...))
 *     ... )
 *     >>> # Chooses ASI if DEX < cap, otherwise returns empty blueprint
 */
export interface MaxIfNotMaxedResolver {
  /**
   * Ability score priority order for determining which stat to check
   *
   * @minItems 6
   * @maxItems 6
   */
  priority: [unknown, unknown, unknown, unknown, unknown, unknown];
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Randomly selects equipment from available choices.
 *
 * For each equipment choice in the blueprint, randomly selects one option
 * and categorizes it as a weapon, armor, or other equipment. Clears all
 * equipment choices after selection.
 *
 * Example:
 *     >>> chooser = RandomEquipmentChooser()
 *     >>> # Randomly picks from equipment_choices and categorizes them
 */
export interface RandomEquipmentChooser {
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
export interface BuildingBlock {
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Base model for serializable building blocks with polymorphic type discrimination.
 *
 * Provides functionality for serializing building blocks to JSON/dict format
 * with a computed 'block_type' field for polymorphic deserialization.
 */
export interface SerializableBlock {
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Blueprint for building a Character with optional fields.
 *
 * All required fields from Character are optional in Blueprint, allowing
 * incremental character construction through building blocks.
 */
export interface Blueprint {
  sex?: Sex2 | null;
  backstory?: string | null;
  level?: number | null;
  age?: number | null;
  classes?: {
    [k: string]: number;
  };
  race?: Race2 | null;
  subrace?: Subrace1 | null;
  name?: string | null;
  background?: Background2 | null;
  alignment?: Alignment2 | null;
  stats?: Stats | null;
  health_base?: number | null;
  height?: number | null;
  weight?: number | null;
  eye_color?: string | null;
  skin_color?: string | null;
  hairstyle?: string | null;
  appearance?: string | null;
  character_traits?: string | null;
  ideals?: string | null;
  bonds?: string | null;
  weaknesses?: string | null;
  dark_vision_range?: number | null;
  base_description?: string | null;
  /**
   * Feats from a list fitting description of the character if race is variant human at least one must be different than ability score improvement
   */
  feats?: FeatName1[];
  subclasses?: (
    | ArtificerSubclass
    | BardSubclass
    | BarbarianSubclass
    | ClericSubclass
    | DruidSubclass
    | FighterSubclass
    | MonkSubclass
    | PaladinSubclass
    | RangerSubclass
    | RogueSubclass
    | SorcererSubclass
    | WarlockSubclass
    | WizardSubclass
  )[];
  /**
   * You would typically have clothes for spell casters. You have a total of 'amount_of_gold_for_equipment' to spend for both armor and weapons. Barbarians and Monks usually don't use armor either.
   */
  armors?: ArmorName[];
  /**
   * You would typically leave it empty for spell casters. You have a total of 'amount_of_gold_for_equipment' to spend for both armor and weapons.
   */
  weapons?: WeaponName1[];
  /**
   * All alchemical supplies, medicines, potions etc.
   */
  other_equipment?: string[];
  spells?: Spells;
  languages?: Language[];
  /**
   * Skills the character is proficient in
   */
  skill_proficiencies?: Skill[];
  /**
   * Tool proficiencies
   */
  tool_proficiencies?: (ToolProficiency | GamingSet | MusicalInstrument)[];
  /**
   * Weapon proficiencies
   */
  weapon_proficiencies?: WeaponProficiency[];
  /**
   * Armor proficiencies
   */
  armor_proficiencies?: ArmorProficiency[];
  speed?: number | null;
  magical_items?: MagicalItem[];
  saving_throw_proficiencies?: Statistic[];
  other_active_abilities?: string[];
  n_stat_choices?: number;
  n_skill_choices?: number;
  /**
   * Skills from which n_skill_choices can be chosen
   */
  skills_to_choose_from?: Skill[];
  equipment_choices?: (WeaponName1 | ArmorName | string)[][];
}
/**
 * D&D character statistics.
 *
 * All stats are positive integers representing the character's ability scores.
 * Typical range is 1-20 for standard characters, with racial bonuses and
 * magical items potentially exceeding this.
 */
export interface Stats {
  strength: number;
  dexterity: number;
  constitution: number;
  intelligence: number;
  wisdom: number;
  charisma: number;
}
export interface Spells {
  cantrips?: Cantrip[];
  first_level_spells?: FirstLevel[];
  second_level_spells?: SecondLevel[];
  third_level_spells?: ThirdLevel[];
  fourth_level_spells?: FourthLevel[];
  fifth_level_spells?: FifthLevel[];
  sixth_level_spells?: SixthLevel[];
  seventh_level_spells?: SeventhLevel[];
  eighth_level_spells?: EighthLevel[];
  ninth_level_spells?: NinthLevel[];
  [k: string]: unknown;
}
export interface MagicalItem {
  name: string;
  description: string;
  level: Level;
  source: Source;
  attuned: boolean;
}
/**
 * Complete package of all choices to be made for a character.
 *
 * This schema is used by AI to make all character choices holistically
 * in a single LLM call, allowing for more coherent and context-aware
 * selections across all choice types.
 */
export interface ChoicePackage {
  /**
   * Languages to replace ANY_OF_YOUR_CHOICE placeholders
   */
  languages?: Language[];
  /**
   * Skills to replace ANY_OF_YOUR_CHOICE placeholders
   */
  skill_proficiencies?: Skill[];
  /**
   * Feats to replace ANY_OF_YOUR_CHOICE placeholders (excluding ABILITY_SCORE_IMPROVEMENT)
   */
  feats?: FeatName1[];
  /**
   * Tool proficiencies to replace ANY_OF_YOUR_CHOICE placeholders
   */
  tool_proficiencies?: (ToolProficiency | GamingSet | MusicalInstrument)[];
  /**
   * Skills selected from skills_to_choose_from pool
   */
  selected_skills?: Skill[];
}
/**
 * Abstract base class for resolvers that handle all character choices.
 *
 * Implementations must resolve:
 * - Language choices (ANY_OF_YOUR_CHOICE placeholders)
 * - Skill proficiency choices (ANY_OF_YOUR_CHOICE placeholders)
 * - Feat choices (ANY_OF_YOUR_CHOICE placeholders)
 * - Tool proficiency choices (ANY_OF_YOUR_CHOICE placeholders)
 * - Stat choices (n_stat_choices distribution)
 * - Skill choices (n_skill_choices from available pool)
 * - Initial data (name, backstory, etc.)
 * - Equipment choices
 *
 * This base class provides a common type for both sequential resolvers
 * (AllChoicesResolver via CombinedBlock) and holistic AI resolvers
 * (AIAllChoicesResolver).
 *
 * Subclasses implement _get_change() to define resolution logic.
 * The apply() method is inherited from BuildingBlock.
 */
export interface AllChoicesResolverBase {}
/**
 * Formats Blueprint data into structured text suitable for AI prompts.
 *
 * This component provides a standardized way to present character information
 * to AI models, with configurable sections and formatting options.
 *
 * Example:
 *     >>> formatter = BlueprintFormatter(
 *     ...     include_backstory=True,
 *     ...     include_stats=True,
 *     ...     format_style="markdown"
 *     ... )
 *     >>> prompt_text = formatter.format(blueprint)
 */
export interface BlueprintFormatter9 {
  /**
   * Include character name
   */
  include_name?: boolean;
  /**
   * Include character sex
   */
  include_sex?: boolean;
  /**
   * Include character age
   */
  include_age?: boolean;
  /**
   * Include race and subrace
   */
  include_race?: boolean;
  /**
   * Include class and level information
   */
  include_classes?: boolean;
  /**
   * Include character background
   */
  include_background?: boolean;
  /**
   * Include character alignment
   */
  include_alignment?: boolean;
  /**
   * Include character backstory
   */
  include_backstory?: boolean;
  /**
   * Include ability scores
   */
  include_stats?: boolean;
  /**
   * Include skill proficiencies
   */
  include_skills?: boolean;
  /**
   * Include current equipment
   */
  include_equipment?: boolean;
  /**
   * Include spell information
   */
  include_spells?: boolean;
  /**
   * Include feats
   */
  include_feats?: boolean;
  /**
   * Output format style (plain text or markdown)
   */
  format_style?: "plain" | "markdown";
  /**
   * Optional custom system prompt to prepend to the formatted output
   */
  system_prompt?: string;
}
/**
 * Interface to OpenAI chat model APIs.
 *
 * ???+ info "Setup"
 *
 *     Install `langchain-openai` and set environment variable `OPENAI_API_KEY`.
 *
 *     ```bash
 *     pip install -U langchain-openai
 *
 *     # or using uv
 *     uv add langchain-openai
 *     ```
 *
 *     ```bash
 *     export OPENAI_API_KEY="your-api-key"
 *     ```
 *
 * ??? info "Key init args — completion params"
 *
 *     | Param               | Type          | Description                                                                                                 |
 *     | ------------------- | ------------- | ----------------------------------------------------------------------------------------------------------- |
 *     | `model`             | `str`         | Name of OpenAI model to use.                                                                                |
 *     | `temperature`       | `float`       | Sampling temperature.                                                                                       |
 *     | `max_tokens`        | `int | None`  | Max number of tokens to generate.                                                                           |
 *     | `logprobs`          | `bool | None` | Whether to return logprobs.                                                                                 |
 *     | `stream_options`    | `dict`        | Configure streaming outputs, like whether to return token usage when streaming (`{"include_usage": True}`). |
 *     | `use_responses_api` | `bool | None` | Whether to use the responses API.                                                                           |
 *
 *     See full list of supported init args and their descriptions below.
 *
 * ??? info "Key init args — client params"
 *
 *     | Param          | Type                                       | Description                                                                         |
 *     | -------------- | ------------------------------------------ | ----------------------------------------------------------------------------------- |
 *     | `timeout`      | `float | Tuple[float, float] | Any | None` | Timeout for requests.                                                               |
 *     | `max_retries`  | `int | None`                               | Max number of retries.                                                              |
 *     | `api_key`      | `str | None`                               | OpenAI API key. If not passed in will be read from env var `OPENAI_API_KEY`.        |
 *     | `base_url`     | `str | None`                               | Base URL for API requests. Only specify if using a proxy or service emulator.       |
 *     | `organization` | `str | None`                               | OpenAI organization ID. If not passed in will be read from env var `OPENAI_ORG_ID`. |
 *
 *     See full list of supported init args and their descriptions below.
 *
 * ??? info "Instantiate"
 *
 *     Create a model instance with desired params. For example:
 *
 *     ```python
 *     from langchain_openai import ChatOpenAI
 *
 *     model = ChatOpenAI(
 *         model="...",
 *         temperature=0,
 *         max_tokens=None,
 *         timeout=None,
 *         max_retries=2,
 *         # api_key="...",
 *         # base_url="...",
 *         # organization="...",
 *         # other params...
 *     )
 *     ```
 *
 *     See all available params below.
 *
 *     !!! tip "Preserved params"
 *         Any param which is not explicitly supported will be passed directly to
 *         [`openai.OpenAI.chat.completions.create(...)`](https://platform.openai.com/docs/api-reference/chat/create)
 *         every time to the model is invoked. For example:
 *
 *         ```python
 *         from langchain_openai import ChatOpenAI
 *         import openai
 *
 *         ChatOpenAI(..., frequency_penalty=0.2).invoke(...)
 *
 *         # Results in underlying API call of:
 *
 *         openai.OpenAI(..).chat.completions.create(..., frequency_penalty=0.2)
 *
 *         # Which is also equivalent to:
 *
 *         ChatOpenAI(...).invoke(..., frequency_penalty=0.2)
 *         ```
 *
 * ??? info "Invoke"
 *
 *     Generate a response from the model:
 *
 *     ```python
 *     messages = [
 *         (
 *             "system",
 *             "You are a helpful translator. Translate the user sentence to French.",
 *         ),
 *         ("human", "I love programming."),
 *     ]
 *     model.invoke(messages)
 *     ```
 *
 *     Results in an `AIMessage` response:
 *
 *     ```python
 *     AIMessage(
 *         content="J'adore la programmation.",
 *         response_metadata={
 *             "token_usage": {
 *                 "completion_tokens": 5,
 *                 "prompt_tokens": 31,
 *                 "total_tokens": 36,
 *             },
 *             "model_name": "gpt-4o",
 *             "system_fingerprint": "fp_43dfabdef1",
 *             "finish_reason": "stop",
 *             "logprobs": None,
 *         },
 *         id="run-012cffe2-5d3d-424d-83b5-51c6d4a593d1-0",
 *         usage_metadata={"input_tokens": 31, "output_tokens": 5, "total_tokens": 36},
 *     )
 *     ```
 *
 * ??? info "Stream"
 *
 *     Stream a response from the model:
 *
 *     ```python
 *     for chunk in model.stream(messages):
 *         print(chunk.text, end="")
 *     ```
 *
 *     Results in a sequence of `AIMessageChunk` objects with partial content:
 *
 *     ```python
 *     AIMessageChunk(content="", id="run-9e1517e3-12bf-48f2-bb1b-2e824f7cd7b0")
 *     AIMessageChunk(content="J", id="run-9e1517e3-12bf-48f2-bb1b-2e824f7cd7b0")
 *     AIMessageChunk(content="'adore", id="run-9e1517e3-12bf-48f2-bb1b-2e824f7cd7b0")
 *     AIMessageChunk(content=" la", id="run-9e1517e3-12bf-48f2-bb1b-2e824f7cd7b0")
 *     AIMessageChunk(
 *         content=" programmation", id="run-9e1517e3-12bf-48f2-bb1b-2e824f7cd7b0"
 *     )
 *     AIMessageChunk(content=".", id="run-9e1517e3-12bf-48f2-bb1b-2e824f7cd7b0")
 *     AIMessageChunk(
 *         content="",
 *         response_metadata={"finish_reason": "stop"},
 *         id="run-9e1517e3-12bf-48f2-bb1b-2e824f7cd7b0",
 *     )
 *     ```
 *
 *     To collect the full message, you can concatenate the chunks:
 *
 *     ```python
 *     stream = model.stream(messages)
 *     full = next(stream)
 *     for chunk in stream:
 *         full += chunk
 *     ```
 *
 *     ```python
 *     full = AIMessageChunk(
 *         content="J'adore la programmation.",
 *         response_metadata={"finish_reason": "stop"},
 *         id="run-bf917526-7f58-4683-84f7-36a6b671d140",
 *     )
 *     ```
 *
 * ??? info "Async"
 *
 *     Asynchronous equivalents of `invoke`, `stream`, and `batch` are also available:
 *
 *     ```python
 *     # Invoke
 *     await model.ainvoke(messages)
 *
 *     # Stream
 *     async for chunk in (await model.astream(messages))
 *
 *     # Batch
 *     await model.abatch([messages])
 *     ```
 *
 *     Results in an `AIMessage` response:
 *
 *     ```python
 *     AIMessage(
 *         content="J'adore la programmation.",
 *         response_metadata={
 *             "token_usage": {
 *                 "completion_tokens": 5,
 *                 "prompt_tokens": 31,
 *                 "total_tokens": 36,
 *             },
 *             "model_name": "gpt-4o",
 *             "system_fingerprint": "fp_43dfabdef1",
 *             "finish_reason": "stop",
 *             "logprobs": None,
 *         },
 *         id="run-012cffe2-5d3d-424d-83b5-51c6d4a593d1-0",
 *         usage_metadata={
 *             "input_tokens": 31,
 *             "output_tokens": 5,
 *             "total_tokens": 36,
 *         },
 *     )
 *     ```
 *
 *     For batched calls, results in a `list[AIMessage]`.
 *
 * ??? info "Tool calling"
 *
 *     ```python
 *     from pydantic import BaseModel, Field
 *
 *
 *     class GetWeather(BaseModel):
 *         '''Get the current weather in a given location'''
 *
 *         location: str = Field(
 *             ..., description="The city and state, e.g. San Francisco, CA"
 *         )
 *
 *
 *     class GetPopulation(BaseModel):
 *         '''Get the current population in a given location'''
 *
 *         location: str = Field(
 *             ..., description="The city and state, e.g. San Francisco, CA"
 *         )
 *
 *
 *     model_with_tools = model.bind_tools(
 *         [GetWeather, GetPopulation]
 *         # strict = True  # Enforce tool args schema is respected
 *     )
 *     ai_msg = model_with_tools.invoke(
 *         "Which city is hotter today and which is bigger: LA or NY?"
 *     )
 *     ai_msg.tool_calls
 *     ```
 *
 *     ```python
 *     [
 *         {
 *             "name": "GetWeather",
 *             "args": {"location": "Los Angeles, CA"},
 *             "id": "call_6XswGD5Pqk8Tt5atYr7tfenU",
 *         },
 *         {
 *             "name": "GetWeather",
 *             "args": {"location": "New York, NY"},
 *             "id": "call_ZVL15vA8Y7kXqOy3dtmQgeCi",
 *         },
 *         {
 *             "name": "GetPopulation",
 *             "args": {"location": "Los Angeles, CA"},
 *             "id": "call_49CFW8zqC9W7mh7hbMLSIrXw",
 *         },
 *         {
 *             "name": "GetPopulation",
 *             "args": {"location": "New York, NY"},
 *             "id": "call_6ghfKxV264jEfe1mRIkS3PE7",
 *         },
 *     ]
 *     ```
 *
 *     !!! note "Parallel tool calls"
 *         [`openai >= 1.32`](https://pypi.org/project/openai/) supports a
 *         `parallel_tool_calls` parameter that defaults to `True`. This parameter can
 *         be set to `False` to disable parallel tool calls:
 *
 *         ```python
 *         ai_msg = model_with_tools.invoke(
 *             "What is the weather in LA and NY?", parallel_tool_calls=False
 *         )
 *         ai_msg.tool_calls
 *         ```
 *
 *         ```python
 *         [
 *             {
 *                 "name": "GetWeather",
 *                 "args": {"location": "Los Angeles, CA"},
 *                 "id": "call_4OoY0ZR99iEvC7fevsH8Uhtz",
 *             }
 *         ]
 *         ```
 *
 *     Like other runtime parameters, `parallel_tool_calls` can be bound to a model
 *     using `model.bind(parallel_tool_calls=False)` or during instantiation by
 *     setting `model_kwargs`.
 *
 *     See `bind_tools` for more.
 *
 * ??? info "Built-in (server-side) tools"
 *
 *     You can access [built-in tools](https://platform.openai.com/docs/guides/tools?api-mode=responses)
 *     supported by the OpenAI Responses API. See [LangChain docs](https://docs.langchain.com/oss/python/integrations/chat/openai#responses-api)
 *     for more detail.
 *
 *     ```python
 *     from langchain_openai import ChatOpenAI
 *
 *     model = ChatOpenAI(model="...", output_version="responses/v1")
 *
 *     tool = {"type": "web_search"}
 *     model_with_tools = model.bind_tools([tool])
 *
 *     response = model_with_tools.invoke("What was a positive news story from today?")
 *     response.content
 *     ```
 *
 *     ```python
 *     [
 *         {
 *             "type": "text",
 *             "text": "Today, a heartwarming story emerged from ...",
 *             "annotations": [
 *                 {
 *                     "end_index": 778,
 *                     "start_index": 682,
 *                     "title": "Title of story",
 *                     "type": "url_citation",
 *                     "url": "<url of story>",
 *                 }
 *             ],
 *         }
 *     ]
 *     ```
 *
 *     !!! version-added "Added in `langchain-openai` 0.3.9"
 *
 *     !!! version-added "Added in `langchain-openai` 0.3.26: Updated `AIMessage` format"
 *         [`langchain-openai >= 0.3.26`](https://pypi.org/project/langchain-openai/#history)
 *         allows users to opt-in to an updated `AIMessage` format when using the
 *         Responses API. Setting `ChatOpenAI(..., output_version="responses/v1")` will
 *         format output from reasoning summaries, built-in tool invocations, and other
 *         response items into the message's `content` field, rather than
 *         `additional_kwargs`. We recommend this format for new applications.
 *
 * ??? info "Managing conversation state"
 *
 *     OpenAI's Responses API supports management of [conversation state](https://platform.openai.com/docs/guides/conversation-state?api-mode=responses).
 *     Passing in response IDs from previous messages will continue a conversational
 *     thread.
 *
 *     ```python
 *     from langchain_openai import ChatOpenAI
 *
 *     model = ChatOpenAI(
 *         model="...",
 *         use_responses_api=True,
 *         output_version="responses/v1",
 *     )
 *     response = model.invoke("Hi, I'm Bob.")
 *     response.text
 *     ```
 *
 *     ```txt
 *     "Hi Bob! How can I assist you today?"
 *     ```
 *
 *     ```python
 *     second_response = model.invoke(
 *         "What is my name?",
 *         previous_response_id=response.response_metadata["id"],
 *     )
 *     second_response.text
 *     ```
 *
 *     ```txt
 *     "Your name is Bob. How can I help you today, Bob?"
 *     ```
 *
 *     !!! version-added "Added in `langchain-openai` 0.3.9"
 *
 *     !!! version-added "Added in `langchain-openai` 0.3.26"
 *         You can also initialize `ChatOpenAI` with `use_previous_response_id`.
 *         Input messages up to the most recent response will then be dropped from request
 *         payloads, and `previous_response_id` will be set using the ID of the most
 *         recent response.
 *
 *         ```python
 *         model = ChatOpenAI(model="...", use_previous_response_id=True)
 *         ```
 *
 * ??? info "Reasoning output"
 *
 *     OpenAI's Responses API supports [reasoning models](https://platform.openai.com/docs/guides/reasoning?api-mode=responses)
 *     that expose a summary of internal reasoning processes.
 *
 *     ```python
 *     from langchain_openai import ChatOpenAI
 *
 *     reasoning = {
 *         "effort": "medium",  # 'low', 'medium', or 'high'
 *         "summary": "auto",  # 'detailed', 'auto', or None
 *     }
 *
 *     model = ChatOpenAI(
 *         model="...", reasoning=reasoning, output_version="responses/v1"
 *     )
 *     response = model.invoke("What is 3^3?")
 *
 *     # Response text
 *     print(f"Output: {response.text}")
 *
 *     # Reasoning summaries
 *     for block in response.content:
 *         if block["type"] == "reasoning":
 *             for summary in block["summary"]:
 *                 print(summary["text"])
 *     ```
 *
 *     ```txt
 *     Output: 3³ = 27
 *     Reasoning: The user wants to know...
 *     ```
 *
 *     !!! version-added "Added in `langchain-openai` 0.3.26: Updated `AIMessage` format"
 *         [`langchain-openai >= 0.3.26`](https://pypi.org/project/langchain-openai/#history)
 *         allows users to opt-in to an updated `AIMessage` format when using the
 *         Responses API. Setting `ChatOpenAI(..., output_version="responses/v1")` will
 *         format output from reasoning summaries, built-in tool invocations, and other
 *         response items into the message's `content` field, rather than
 *         `additional_kwargs`. We recommend this format for new applications.
 *
 * ??? info "Structured output"
 *
 *     ```python
 *     from pydantic import BaseModel, Field
 *
 *
 *     class Joke(BaseModel):
 *         '''Joke to tell user.'''
 *
 *         setup: str = Field(description="The setup of the joke")
 *         punchline: str = Field(description="The punchline to the joke")
 *         rating: int | None = Field(
 *             description="How funny the joke is, from 1 to 10"
 *         )
 *
 *
 *     structured_model = model.with_structured_output(Joke)
 *     structured_model.invoke("Tell me a joke about cats")
 *     ```
 *
 *     ```python
 *     Joke(
 *         setup="Why was the cat sitting on the computer?",
 *         punchline="To keep an eye on the mouse!",
 *         rating=None,
 *     )
 *     ```
 *
 *     See `with_structured_output` for more info.
 *
 * ??? info "JSON mode"
 *
 *     ```python
 *     json_model = model.bind(response_format={"type": "json_object"})
 *     ai_msg = json_model.invoke(
 *         "Return a JSON object with key 'random_ints' and a value of 10 random ints in [0-99]"
 *     )
 *     ai_msg.content
 *     ```
 *
 *     ```txt
 *     '\\n{\\n  "random_ints": [23, 87, 45, 12, 78, 34, 56, 90, 11, 67]\\n}'
 *     ```
 *
 * ??? info "Image input"
 *
 *     ```python
 *     import base64
 *     import httpx
 *     from langchain.messages import HumanMessage
 *
 *     image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
 *     image_data = base64.b64encode(httpx.get(image_url).content).decode("utf-8")
 *     message = HumanMessage(
 *         content=[
 *             {"type": "text", "text": "describe the weather in this image"},
 *             {
 *                 "type": "image_url",
 *                 "image_url": {"url": f"data:image/jpeg;base64,{image_data}"},
 *             },
 *         ]
 *     )
 *
 *     ai_msg = model.invoke([message])
 *     ai_msg.content
 *     ```
 *
 *     ```txt
 *     "The weather in the image appears to be clear and pleasant. The sky is mostly blue with scattered, light clouds, suggesting a sunny day with minimal cloud cover. There is no indication of rain or strong winds, and the overall scene looks bright and calm. The lush green grass and clear visibility further indicate good weather conditions."
 *     ```
 *
 * ??? info "Token usage"
 *
 *     ```python
 *     ai_msg = model.invoke(messages)
 *     ai_msg.usage_metadata
 *
 *     ```txt
 *     {"input_tokens": 28, "output_tokens": 5, "total_tokens": 33}
 *     ```
 *
 *     When streaming, set the `stream_usage` kwarg:
 *
 *     ```python
 *     stream = model.stream(messages, stream_usage=True)
 *     full = next(stream)
 *     for chunk in stream:
 *         full += chunk
 *     full.usage_metadata
 *     ```
 *
 *     ```txt
 *     {"input_tokens": 28, "output_tokens": 5, "total_tokens": 33}
 *     ```
 *
 * ??? info "Logprobs"
 *
 *     ```python
 *     logprobs_model = model.bind(logprobs=True)
 *     ai_msg = logprobs_model.invoke(messages)
 *     ai_msg.response_metadata["logprobs"]
 *     ```
 *
 *     ```txt
 *     {
 *         "content": [
 *             {
 *                 "token": "J",
 *                 "bytes": [74],
 *                 "logprob": -4.9617593e-06,
 *                 "top_logprobs": [],
 *             },
 *             {
 *                 "token": "'adore",
 *                 "bytes": [39, 97, 100, 111, 114, 101],
 *                 "logprob": -0.25202933,
 *                 "top_logprobs": [],
 *             },
 *             {
 *                 "token": " la",
 *                 "bytes": [32, 108, 97],
 *                 "logprob": -0.20141791,
 *                 "top_logprobs": [],
 *             },
 *             {
 *                 "token": " programmation",
 *                 "bytes": [
 *                     32,
 *                     112,
 *                     114,
 *                     111,
 *                     103,
 *                     114,
 *                     97,
 *                     109,
 *                     109,
 *                     97,
 *                     116,
 *                     105,
 *                     111,
 *                     110,
 *                 ],
 *                 "logprob": -1.9361265e-07,
 *                 "top_logprobs": [],
 *             },
 *             {
 *                 "token": ".",
 *                 "bytes": [46],
 *                 "logprob": -1.2233183e-05,
 *                 "top_logprobs": [],
 *             },
 *         ]
 *     }
 *     ```
 *
 * ??? info "Response metadata"
 *
 *     ```python
 *     ai_msg = model.invoke(messages)
 *     ai_msg.response_metadata
 *     ```
 *
 *     ```txt
 *     {
 *         "token_usage": {
 *             "completion_tokens": 5,
 *             "prompt_tokens": 28,
 *             "total_tokens": 33,
 *         },
 *         "model_name": "gpt-4o",
 *         "system_fingerprint": "fp_319be4768e",
 *         "finish_reason": "stop",
 *         "logprobs": None,
 *     }
 *     ```
 *
 * ??? info "Flex processing"
 *
 *     OpenAI offers a variety of [service tiers](https://platform.openai.com/docs/guides/flex-processing?api-mode=responses).
 *     The "flex" tier offers cheaper pricing for requests, with the trade-off that
 *     responses may take longer and resources might not always be available.
 *     This approach is best suited for non-critical tasks, including model testing,
 *     data enhancement, or jobs that can be run asynchronously.
 *
 *     To use it, initialize the model with `service_tier="flex"`:
 *
 *     ```python
 *     from langchain_openai import ChatOpenAI
 *
 *     model = ChatOpenAI(model="...", service_tier="flex")
 *     ```
 *
 *     Note that this is a beta feature that is only available for a subset of models.
 *     See OpenAI [flex processing docs](https://platform.openai.com/docs/guides/flex-processing?api-mode=responses)
 *     for more detail.
 *
 * ??? info "OpenAI-compatible APIs"
 *
 *     `ChatOpenAI` can be used with OpenAI-compatible APIs like
 *     [LM Studio](https://lmstudio.ai/), [vLLM](https://github.com/vllm-project/vllm),
 *     [Ollama](https://ollama.com/), and others.
 *
 *     To use custom parameters specific to these providers, use the `extra_body` parameter.
 *
 *     !!! example "LM Studio example with TTL (auto-eviction)"
 *
 *         ```python
 *         from langchain_openai import ChatOpenAI
 *
 *         model = ChatOpenAI(
 *             base_url="http://localhost:1234/v1",
 *             api_key="lm-studio",  # Can be any string
 *             model="mlx-community/QwQ-32B-4bit",
 *             temperature=0,
 *             extra_body={
 *                 "ttl": 300
 *             },  # Auto-evict model after 5 minutes of inactivity
 *         )
 *         ```
 *
 *     !!! example "vLLM example with custom parameters"
 *
 *         ```python
 *         model = ChatOpenAI(
 *             base_url="http://localhost:8000/v1",
 *             api_key="EMPTY",
 *             model="meta-llama/Llama-2-7b-chat-hf",
 *             extra_body={"use_beam_search": True, "best_of": 4},
 *         )
 *         ```
 *
 * ??? info "`model_kwargs` vs `extra_body`"
 *
 *     Use the correct parameter for different types of API arguments:
 *
 *     **Use `model_kwargs` for:**
 *
 *     - Standard OpenAI API parameters not explicitly defined as class parameters
 *     - Parameters that should be flattened into the top-level request payload
 *     - Examples: `max_completion_tokens`, `stream_options`, `modalities`, `audio`
 *
 *     ```python
 *     # Standard OpenAI parameters
 *     model = ChatOpenAI(
 *         model="...",
 *         model_kwargs={
 *             "stream_options": {"include_usage": True},
 *             "max_completion_tokens": 300,
 *             "modalities": ["text", "audio"],
 *             "audio": {"voice": "alloy", "format": "wav"},
 *         },
 *     )
 *     ```
 *
 *     **Use `extra_body` for:**
 *
 *     - Custom parameters specific to OpenAI-compatible providers (vLLM, LM Studio,
 *         OpenRouter, etc.)
 *     - Parameters that need to be nested under `extra_body` in the request
 *     - Any non-standard OpenAI API parameters
 *
 *     ```python
 *     # Custom provider parameters
 *     model = ChatOpenAI(
 *         base_url="http://localhost:8000/v1",
 *         model="custom-model",
 *         extra_body={
 *             "use_beam_search": True,  # vLLM parameter
 *             "best_of": 4,  # vLLM parameter
 *             "ttl": 300,  # LM Studio parameter
 *         },
 *     )
 *     ```
 *
 *     **Key Differences:**
 *
 *     - `model_kwargs`: Parameters are **merged into top-level** request payload
 *     - `extra_body`: Parameters are **nested under `extra_body`** key in request
 *
 *     !!! warning
 *         Always use `extra_body` for custom parameters, **not** `model_kwargs`.
 *         Using `model_kwargs` for non-OpenAI parameters will cause API errors.
 *
 * ??? info "Prompt caching optimization"
 *
 *     For high-volume applications with repetitive prompts, use `prompt_cache_key`
 *     per-invocation to improve cache hit rates and reduce costs:
 *
 *     ```python
 *     model = ChatOpenAI(model="...")
 *
 *     response = model.invoke(
 *         messages,
 *         prompt_cache_key="example-key-a",  # Routes to same machine for cache hits
 *     )
 *
 *     customer_response = model.invoke(messages, prompt_cache_key="example-key-b")
 *     support_response = model.invoke(messages, prompt_cache_key="example-key-c")
 *
 *     # Dynamic cache keys based on context
 *     cache_key = f"example-key-{dynamic_suffix}"
 *     response = model.invoke(messages, prompt_cache_key=cache_key)
 *     ```
 *
 *     Cache keys help ensure requests with the same prompt prefix are routed to
 *     machines with existing cache, providing cost reduction and latency improvement on
 *     cached tokens.
 */
export interface ChatOpenAI12 {
  name?: string | null;
  disable_streaming?: boolean | "tool_calling";
  output_version?: string | null;
  model?: string;
  temperature?: number | null;
  model_kwargs?: {
    [k: string]: unknown;
  };
  api_key?: string | null;
  base_url?: string | null;
  organization?: string | null;
  openai_proxy?: string | null;
  timeout?: number | [unknown, unknown] | unknown | null;
  stream_usage?: boolean | null;
  max_retries?: number | null;
  presence_penalty?: number | null;
  frequency_penalty?: number | null;
  seed?: number | null;
  logprobs?: boolean | null;
  top_logprobs?: number | null;
  logit_bias?: {
    [k: string]: number;
  } | null;
  streaming?: boolean;
  n?: number | null;
  top_p?: number | null;
  max_completion_tokens?: number | null;
  reasoning_effort?: string | null;
  reasoning?: {
    [k: string]: unknown;
  } | null;
  verbosity?: string | null;
  tiktoken_model_name?: string | null;
  default_headers?: {
    [k: string]: string;
  } | null;
  default_query?: {
    [k: string]: unknown;
  } | null;
  stop_sequences?: string[] | string | null;
  extra_body?: {
    [k: string]: unknown;
  } | null;
  include_response_headers?: boolean;
  disabled_params?: {
    [k: string]: unknown;
  } | null;
  include?: string[] | null;
  service_tier?: string | null;
  store?: boolean | null;
  truncation?: string | null;
  use_previous_response_id?: boolean;
  use_responses_api?: boolean | null;
}
/**
 * Schema for AI to select equipment from choices.
 */
export interface EquipmentChoiceSelection {
  /**
   * Index of selected item from each equipment choice (0-indexed)
   */
  selected_indices: number[];
}
export interface EquipmentChooser {
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Resolves FeatName.ANY_OF_YOUR_CHOICE placeholders.
 *
 * This resolver replaces ANY_OF_YOUR_CHOICE placeholders in the
 * blueprint's feats set with concrete FeatName choices.
 *
 * Handles special logic for ABILITY_SCORE_IMPROVEMENT:
 * - Excluded from choices if character is level 1
 * - Converted to n_stat_choices for StatChoiceResolver
 * - Filtered out from final feats tuple
 */
export interface FeatChoiceResolver {
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Schema for AI to select feat replacements.
 */
export interface FeatSelection {
  feats?: FeatName1[];
}
export interface Feature1 {
  source: string | null;
  ability: Ability | null;
  skill_proficiency_gain: Skill | null;
  /**
   * The same as double proficiency.
   */
  skill_expertise_gain: Skill | null;
  tool_proficiency_gain: ToolProficiency | null;
  instrument_proficiency_gain: MusicalInstrument | null;
  gaming_set_proficiency_gain: GamingSet | null;
  /**
   * Must remain empty if nothing is provided.
   */
  weapon_proficiencies_gain: WeaponProficiency[];
  /**
   * Must remain empty if nothing is provided.
   */
  armor_proficiencies_gain: ArmorProficiency[];
  attribute_increase: StatisticAndAny | null;
}
/**
 * Base class for AI-powered character builders.
 *
 * Provides common functionality for AI building blocks that use LLM
 * structured output to generate character parameters from descriptions.
 */
export interface AIBuilderBase {
  /**
   * Natural language description of the character to generate
   */
  description: string;
  llm: ChatOpenAI13;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Language model for making AI-powered decisions
 */
export interface ChatOpenAI13 {
  name?: string | null;
  disable_streaming?: boolean | "tool_calling";
  output_version?: string | null;
  model?: string;
  temperature?: number | null;
  model_kwargs?: {
    [k: string]: unknown;
  };
  api_key?: string | null;
  base_url?: string | null;
  organization?: string | null;
  openai_proxy?: string | null;
  timeout?: number | [unknown, unknown] | unknown | null;
  stream_usage?: boolean | null;
  max_retries?: number | null;
  presence_penalty?: number | null;
  frequency_penalty?: number | null;
  seed?: number | null;
  logprobs?: boolean | null;
  top_logprobs?: number | null;
  logit_bias?: {
    [k: string]: number;
  } | null;
  streaming?: boolean;
  n?: number | null;
  top_p?: number | null;
  max_completion_tokens?: number | null;
  reasoning_effort?: string | null;
  reasoning?: {
    [k: string]: unknown;
  } | null;
  verbosity?: string | null;
  tiktoken_model_name?: string | null;
  default_headers?: {
    [k: string]: string;
  } | null;
  default_query?: {
    [k: string]: unknown;
  } | null;
  stop_sequences?: string[] | string | null;
  extra_body?: {
    [k: string]: unknown;
  } | null;
  include_response_headers?: boolean;
  disabled_params?: {
    [k: string]: unknown;
  } | null;
  include?: string[] | null;
  service_tier?: string | null;
  store?: boolean | null;
  truncation?: string | null;
  use_previous_response_id?: boolean;
  use_responses_api?: boolean | null;
}
export interface InitialDataFiller {
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Resolves Language.ANY_OF_YOUR_CHOICE placeholders.
 *
 * This resolver replaces ANY_OF_YOUR_CHOICE placeholders in the
 * blueprint's languages set with concrete Language choices.
 */
export interface LanguageChoiceResolver {
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Schema for AI to select language replacements.
 */
export interface LanguageSelection {
  languages?: Language[];
}
/**
 * Abstract base class for health increase strategies when leveling up.
 *
 * Subclasses must implement _get_hit_die_value to determine how much
 * health to gain from the hit die (fixed value, random roll, etc.).
 */
export interface HealthIncrease {
  class_: Class10;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Abstract base class for spell assignment strategies.
 *
 * Subclasses must implement get_change to determine how spells are selected
 * and assigned to the character.
 */
export interface SpellAssigner {
  class_: Class11;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Abstract base class for choosers that select magical items.
 *
 * Implementations must select magical items based on rarity counts:
 * - n_common, n_uncommon, n_rare, etc.
 *
 * This base class provides a common type for both random choosers
 * (RandomMagicalItemChooser) and holistic AI choosers (AIMagicalItemChooser).
 *
 * - RandomMagicalItemChooser: Selects items level-by-level
 * - AIMagicalItemChooser: Selects all items in a single holistic LLM call
 *
 * Subclasses implement _get_change() to define selection logic.
 */
export interface MagicalItemChooserBase {
  /**
   * Number of common magical items to select
   */
  n_common?: number;
  /**
   * Number of uncommon magical items to select
   */
  n_uncommon?: number;
  /**
   * Number of rare magical items to select
   */
  n_rare?: number;
  /**
   * Number of very rare magical items to select
   */
  n_very_rare?: number;
  /**
   * Number of legendary magical items to select
   */
  n_legendary?: number;
  /**
   * Number of artifact magical items to select
   */
  n_artifact?: number;
  /**
   * Number of unique magical items to select
   */
  n_unique?: number;
  /**
   * Number of mystery magical items to select
   */
  n_mistery?: number;
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Package of magical item selections.
 */
export interface MagicalItemSelection {
  /**
   * List of selected magical item names
   */
  selected_items?: string[];
}
export interface BaseRaceAssigner {
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Represents a valid combination of race and subrace for character creation.
 *
 * Ensures that the selected subrace belongs to the selected race through validation.
 */
export interface RaceSubracePair {
  race: Race3;
  subrace: Subrace2;
}
/**
 * Abstract base class for resolving n_skill_choices.
 *
 * When a race/class grants skill proficiencies of the player's choice
 * (n_skill_choices > 0), this component determines which skills to select
 * from the available skills_to_choose_from.
 *
 * Subclasses must implement _select_skills to determine the
 * selection strategy.
 */
export interface SkillChoiceResolver {
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Schema for AI to select skills.
 */
export interface SkillSelection {
  /**
   * Selected skill proficiencies
   */
  selected_skills: Skill[];
}
/**
 * Abstract base class for resolving n_stat_choices.
 *
 * When a race/subrace grants ability score increases of the player's choice
 * (n_stat_choices > 0), this component determines which stats to increase.
 *
 * Subclasses must implement _select_stats_to_increase to determine the
 * selection strategy.
 */
export interface StatChoiceResolver {
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Schema for AI to select stat increases.
 */
export interface StatIncreaseSelection {
  /**
   * Dictionary mapping statistics to their increase amounts
   */
  stat_increases: {
    [k: string]: number;
  };
}
/**
 * Abstract base class for building character ability scores.
 *
 * Subclasses implement different methods of generating stats (standard array,
 * rolling, point buy, etc.) based on a priority order.
 */
export interface StatsBuilder {
  /**
   * Ability scores ranked by priority for stat assignment
   *
   * @minItems 6
   * @maxItems 6
   */
  stats_priority: [unknown, unknown, unknown, unknown, unknown, unknown];
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Abstract base class for assigning subclasses to characters.
 *
 * Subclasses must implement _select_subclass to determine which subclass
 * to assign based on the character's class and context.
 *
 * Example:
 *     >>> from dnd_character_creator.choices.class_creation.character_class import Class
 *     >>> assigner = SomeSubclassAssigner(class_=Class.WIZARD)
 *     >>> builder = Builder().add(assigner)
 */
export interface SubclassAssigner {
  class_: Class12;
  /**
   * Tuple of subclasses available for selection (defaults to all valid subclasses)
   */
  available_subclasses?: (
    | ArtificerSubclass
    | BardSubclass
    | BarbarianSubclass
    | ClericSubclass
    | DruidSubclass
    | FighterSubclass
    | MonkSubclass
    | PaladinSubclass
    | RangerSubclass
    | RogueSubclass
    | SorcererSubclass
    | WarlockSubclass
    | WizardSubclass
  )[];
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Resolves ANY_OF_YOUR_CHOICE placeholders in tool proficiencies.
 *
 * This resolver handles the union type:
 * ToolProficiency | GamingSet | MusicalInstrument
 *
 * Each placeholder is replaced based on its specific type.
 */
export interface ToolProficiencyChoiceResolver {
  /**
   * Return the class name as the block type for polymorphic serialization.
   */
  block_type: string;
}
/**
 * Schema for AI to select tool proficiency replacements.
 */
export interface ToolProficiencySelection {
  tool_proficiencies?: (ToolProficiency | GamingSet | MusicalInstrument)[];
}
