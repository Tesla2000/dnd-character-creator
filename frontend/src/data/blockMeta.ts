/**
 * Precondition metadata for each block type.
 * Derived from inspecting `get_change()` type guards in the block implementations.
 *
 * INITIAL_PROTOCOLS: protocols satisfied by Blueprint before any blocks are applied.
 */

export const INITIAL_PROTOCOLS = new Set([
  "HasNStatChoices",
  "HasNSkillChoices",
  "HasSkillsToChooseFrom",
  "HasStatsCup",
  "HasFeats",
  "HasWeapons",
  "HasLanguages",
  "HasSubclasses",
  "HasClasses",
  "HasSpells",
  "HasSkillProficiencies",
  "HasToolProficiencies",
  "HasArmors",
  "HasOtherEquipment",
  "HasEquipmentChoices",
  "HasMagicalItems",
]);

export interface BlockPreconditions {
  requires: string[];
  provides: string[];
  conflicts: string[];
}

type BlockMetaMap = Record<string, BlockPreconditions>;

const RACE_PROVIDES = ["HasRace", "HasLanguages", "HasSkillProficiencies", "HasNStatChoices"];

const SUBCLASS_REQUIRES = ["HasClasses", "HasSubclasses"];
const SUBCLASS_PROVIDES = ["HasSubclasses"];

export const BLOCK_META: BlockMetaMap = {
  // --- Identity ---
  name_assigner: { requires: [], provides: ["HasName"], conflicts: [] },
  age_assigner: { requires: [], provides: ["HasAge"], conflicts: [] },
  sex_assigner: { requires: [], provides: ["HasSex"], conflicts: [] },
  alignment_assigner: { requires: [], provides: ["HasAlignment"], conflicts: [] },
  background_assigner: { requires: [], provides: ["HasBackground"], conflicts: [] },
  level_assigner: { requires: [], provides: ["HasLevel"], conflicts: [] },

  // --- Stats ---
  standard_array: { requires: [], provides: ["HasStats", "HasStatsCup"], conflicts: [] },

  // --- Race assigners (all 39 concrete races + random) ---
  ...Object.fromEntries(
    [
      "aarakocra_race_assigner",
      "aasimar_race_assigner",
      "bugbear_race_assigner",
      "centaur_race_assigner",
      "changeling_race_assigner",
      "dragonborn_race_assigner",
      "dwarf_race_assigner",
      "elf_race_assigner",
      "firbolg_race_assigner",
      "genasi_air_race_assigner",
      "genasi_earth_race_assigner",
      "genasi_fire_race_assigner",
      "genasi_water_race_assigner",
      "gnome_race_assigner",
      "goblin_race_assigner",
      "goliath_race_assigner",
      "grung_race_assigner",
      "half_elf_race_assigner",
      "halfling_race_assigner",
      "half_orc_race_assigner",
      "hobgoblin_race_assigner",
      "human_race_assigner",
      "kalashtar_race_assigner",
      "kenku_race_assigner",
      "kobold_race_assigner",
      "leonin_race_assigner",
      "lizardfolk_race_assigner",
      "minotaur_race_assigner",
      "orc_race_assigner",
      "satyr_race_assigner",
      "shifter_race_assigner",
      "tabaxi_race_assigner",
      "tiefling_race_assigner",
      "tortle_race_assigner",
      "verdan_race_assigner",
      "warforged_race_assigner",
      "yuan_ti_pureblood_race_assigner",
      "random_race_assigner",
      "race_assigner",
    ].map((t) => [
      t,
      { requires: ["HasStats"], provides: RACE_PROVIDES, conflicts: ["HasRace"] },
    ])
  ),

  // --- Level-Up ---
  level_up: {
    requires: ["HasRace", "HasLevel"],
    provides: ["HasClasses", "HasHealthBase"],
    conflicts: [],
  },
  level_up_multiple: {
    requires: ["HasRace", "HasLevel"],
    provides: ["HasClasses", "HasHealthBase", "HasWizardLevel", "HasSorcererLevel"],
    conflicts: [],
  },
  health_increase_average: { requires: ["HasClasses"], provides: ["HasHealthBase"], conflicts: [] },
  health_increase_random: { requires: ["HasClasses"], provides: ["HasHealthBase"], conflicts: [] },
  health_increase_random_min_two: {
    requires: ["HasClasses"],
    provides: ["HasHealthBase"],
    conflicts: [],
  },
  health_increase_random_reroll_ones: {
    requires: ["HasClasses"],
    provides: ["HasHealthBase"],
    conflicts: [],
  },
  wizard_level_incrementer: {
    requires: ["HasLevel", "HasClasses"],
    provides: ["HasWizardLevel"],
    conflicts: [],
  },
  sorcerer_level_incrementer: {
    requires: ["HasLevel", "HasClasses"],
    provides: ["HasSorcererLevel"],
    conflicts: [],
  },

  // --- Spells ---
  wizard_random_spell_assigner: {
    requires: ["HasWizardLevel"],
    provides: ["HasSpells"],
    conflicts: [],
  },
  sorcerer_random_spell_assigner: {
    requires: ["HasSorcererLevel"],
    provides: ["HasSpells"],
    conflicts: [],
  },
  wizard_llm_spell_assigner: {
    requires: ["HasWizardLevel"],
    provides: ["HasSpells"],
    conflicts: [],
  },
  sorcerer_llm_spell_assigner: {
    requires: ["HasSorcererLevel"],
    provides: ["HasSpells"],
    conflicts: [],
  },

  // --- Subclasses ---
  artificer_subclass_assigner: {
    requires: SUBCLASS_REQUIRES,
    provides: SUBCLASS_PROVIDES,
    conflicts: [],
  },
  barbarian_subclass_assigner: {
    requires: SUBCLASS_REQUIRES,
    provides: SUBCLASS_PROVIDES,
    conflicts: [],
  },
  bard_subclass_assigner: {
    requires: SUBCLASS_REQUIRES,
    provides: SUBCLASS_PROVIDES,
    conflicts: [],
  },
  cleric_subclass_assigner: {
    requires: SUBCLASS_REQUIRES,
    provides: SUBCLASS_PROVIDES,
    conflicts: [],
  },
  druid_subclass_assigner: {
    requires: SUBCLASS_REQUIRES,
    provides: SUBCLASS_PROVIDES,
    conflicts: [],
  },
  fighter_subclass_assigner: {
    requires: SUBCLASS_REQUIRES,
    provides: SUBCLASS_PROVIDES,
    conflicts: [],
  },
  monk_subclass_assigner: {
    requires: SUBCLASS_REQUIRES,
    provides: SUBCLASS_PROVIDES,
    conflicts: [],
  },
  paladin_subclass_assigner: {
    requires: SUBCLASS_REQUIRES,
    provides: SUBCLASS_PROVIDES,
    conflicts: [],
  },
  ranger_subclass_assigner: {
    requires: SUBCLASS_REQUIRES,
    provides: SUBCLASS_PROVIDES,
    conflicts: [],
  },
  rogue_subclass_assigner: {
    requires: SUBCLASS_REQUIRES,
    provides: SUBCLASS_PROVIDES,
    conflicts: [],
  },
  sorcerer_subclass_assigner: {
    requires: SUBCLASS_REQUIRES,
    provides: SUBCLASS_PROVIDES,
    conflicts: [],
  },
  warlock_subclass_assigner: {
    requires: SUBCLASS_REQUIRES,
    provides: SUBCLASS_PROVIDES,
    conflicts: [],
  },
  wizard_subclass_assigner: {
    requires: SUBCLASS_REQUIRES,
    provides: SUBCLASS_PROVIDES,
    conflicts: [],
  },
  random_subclass_assigner: {
    requires: SUBCLASS_REQUIRES,
    provides: SUBCLASS_PROVIDES,
    conflicts: [],
  },
  optional_subclass_assigner: {
    requires: SUBCLASS_REQUIRES,
    provides: SUBCLASS_PROVIDES,
    conflicts: [],
  },

  // --- Feats ---
  feat_adder: { requires: ["HasFeats"], provides: ["HasFeats"], conflicts: [] },
  random_feat_choice_resolver: {
    requires: ["HasFeats", "HasStats"],
    provides: ["HasFeats"],
    conflicts: [],
  },
  max_first_resolver: {
    requires: ["HasFeats", "HasStats", "HasStatsCup"],
    provides: ["HasFeats"],
    conflicts: [],
  },
  max_if_not_maxed_resolver: {
    requires: ["HasFeats", "HasStats", "HasStatsCup"],
    provides: ["HasFeats"],
    conflicts: [],
  },

  // --- Skills ---
  random_skill_choice_resolver: {
    requires: ["HasNSkillChoices", "HasSkillsToChooseFrom", "HasSkillProficiencies"],
    provides: ["HasSkillProficiencies"],
    conflicts: [],
  },

  // --- Languages ---
  random_language_choice_resolver: {
    requires: ["HasLanguages"],
    provides: ["HasLanguages"],
    conflicts: [],
  },

  // --- Tool Proficiencies ---
  random_tool_proficiency_choice_resolver: {
    requires: ["HasToolProficiencies"],
    provides: ["HasToolProficiencies"],
    conflicts: [],
  },

  // --- Stats ---
  priority_stat_choice_resolver: {
    requires: ["HasStats", "HasNStatChoices"],
    provides: ["HasStats"],
    conflicts: [],
  },

  // --- Equipment ---
  weapon_adder: { requires: ["HasWeapons"], provides: ["HasWeapons"], conflicts: [] },
  equipment_adder: {
    requires: ["HasOtherEquipment"],
    provides: ["HasOtherEquipment"],
    conflicts: [],
  },
  random_equipment_chooser: {
    requires: ["HasEquipmentChoices"],
    provides: ["HasWeapons", "HasArmors", "HasOtherEquipment"],
    conflicts: [],
  },
  random_magical_item_chooser: {
    requires: [],
    provides: ["HasMagicalItems"],
    conflicts: [],
  },

  // --- Builders / Compound ---
  initial_builder: {
    requires: [],
    provides: ["HasLevel", "HasStats", "HasRace", "HasLanguages", "HasSkillProficiencies"],
    conflicts: [],
  },
  initial_data_filler: {
    requires: [],
    provides: ["HasName", "HasAge", "HasSex", "HasAlignment", "HasBackground", "HasInitialData"],
    conflicts: [],
  },

  // --- Choices (compound) ---
  all_choices_resolver: {
    requires: ["HasRace"],
    provides: [
      "HasLanguages",
      "HasSkillProficiencies",
      "HasToolProficiencies",
      "HasFeats",
      "HasStats",
      "HasWeapons",
      "HasArmors",
      "HasOtherEquipment",
    ],
    conflicts: [],
  },

  // --- AI blocks ---
  ai_all_choices_resolver: {
    requires: ["HasRace"],
    provides: [
      "HasLanguages",
      "HasSkillProficiencies",
      "HasToolProficiencies",
      "HasFeats",
      "HasStats",
      "HasWeapons",
      "HasArmors",
      "HasOtherEquipment",
    ],
    conflicts: [],
  },
  ai_all_non_stat_choices_resolver: {
    requires: ["HasRace"],
    provides: [
      "HasLanguages",
      "HasSkillProficiencies",
      "HasToolProficiencies",
      "HasFeats",
      "HasWeapons",
      "HasArmors",
      "HasOtherEquipment",
    ],
    conflicts: [],
  },
  ai_base_builder_assigner: {
    requires: [],
    provides: ["HasLevel", "HasStats", "HasRace", "HasLanguages", "HasSkillProficiencies"],
    conflicts: [],
  },
  ai_partial_builder_assigner: {
    requires: [],
    provides: ["HasLevel", "HasStats", "HasRace"],
    conflicts: [],
  },
  ai_equipment_chooser: {
    requires: ["HasEquipmentChoices"],
    provides: ["HasWeapons", "HasArmors", "HasOtherEquipment"],
    conflicts: [],
  },
  ai_feat_choice_resolver: {
    requires: ["HasFeats", "HasStats"],
    provides: ["HasFeats"],
    conflicts: [],
  },
  ai_language_choice_resolver: {
    requires: ["HasLanguages"],
    provides: ["HasLanguages"],
    conflicts: [],
  },
  ai_magical_item_chooser: { requires: [], provides: ["HasMagicalItems"], conflicts: [] },
  ai_skill_choice_resolver: {
    requires: ["HasNSkillChoices", "HasSkillsToChooseFrom", "HasSkillProficiencies"],
    provides: ["HasSkillProficiencies"],
    conflicts: [],
  },
  ai_stat_choice_resolver: {
    requires: ["HasStats", "HasNStatChoices"],
    provides: ["HasStats"],
    conflicts: [],
  },
  ai_subclass_assigner: {
    requires: SUBCLASS_REQUIRES,
    provides: SUBCLASS_PROVIDES,
    conflicts: [],
  },
  ai_tool_proficiency_choice_resolver: {
    requires: ["HasToolProficiencies"],
    provides: ["HasToolProficiencies"],
    conflicts: [],
  },

  // --- Utility ---
  null_block: { requires: [], provides: [], conflicts: [] },
};

export function getPreconditions(blockType: string): BlockPreconditions {
  return BLOCK_META[blockType] ?? { requires: [], provides: [], conflicts: [] };
}
