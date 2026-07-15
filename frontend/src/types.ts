export interface SubBlockTypeInfo {
  type_value: string;
  label: string;
  fields: Record<string, FieldSchema>;
}

export interface FieldSchema {
  type: string;
  description?: string;
  enum?: string[];
  default?: unknown;
  required?: boolean;
  note?: string;
  properties?: Record<string, FieldSchema>;
  items?: { type?: string; enum?: string[] };
  sub_block_types?: SubBlockTypeInfo[];
}

export type ArgSpec =
  | { kind: "free" }
  | { kind: "none" }
  | { kind: "type"; name: string }
  | { kind: "literal"; values: (string | number)[] }
  | { kind: "generic"; origin: string; args: ArgSpec[] }
  | { kind: "union"; members: ArgSpec[] };

export interface BlueprintSig {
  origin: string;
  args: ArgSpec[];
}

export interface BlueprintState {
  origin: string;
  args: ArgSpec[];
}

export interface BlockInfo {
  type: string;
  type_name: string;
  label: string;
  class_name: string;
  category: string;
  description: string;
  is_ai: boolean;
  fields: Record<string, FieldSchema>;
  default_config?: Record<string, unknown>;
  blueprint_sig?: { input: BlueprintSig | null; output: BlueprintSig | null } | null;
}

export interface PipelineBlock {
  id: string;
  blockType: string;
  config: Record<string, unknown>;
}

export interface CharacterStats {
  strength: number;
  dexterity: number;
  constitution: number;
  intelligence: number;
  wisdom: number;
  charisma: number;
}

export interface CharacterSpells {
  cantrips: string[];
  first_level_spells: string[];
  second_level_spells: string[];
  third_level_spells: string[];
  fourth_level_spells: string[];
  fifth_level_spells: string[];
  sixth_level_spells: string[];
  seventh_level_spells: string[];
  eighth_level_spells: string[];
  ninth_level_spells: string[];
}

export interface CharacterResult {
  // Blueprint base fields
  race: string | null;
  subrace: string | null;
  speed: number | null;
  dark_vision_range: number | null;
  stats: CharacterStats | null;
  health_base: number | null;
  classes: Record<string, number>;
  feats: string[];
  subclasses: string[];
  armors: string[];
  weapons: string[];
  other_equipment: string[];
  spells: CharacterSpells;
  languages: string[];
  skill_proficiencies: string[];
  tool_proficiencies: string[];
  weapon_proficiencies: string[];
  armor_proficiencies: string[];
  saving_throw_proficiencies: string[];
  actions: unknown[];
  character_data: {
    name: string | null;
    age: number | null;
    sex: string | null;
    alignment: string | null;
    background: string | null;
  } | null;
  // Computed fields
  level: number;
  abilities: Record<string, number>;
  initiative: number;
  passive_perception: number;
  proficiency_bonus: number;
  saving_throw_modifiers: Record<string, number>;
  ac: number;
  capacity: number;
  health: number;
  spellcasting_ability: string | null;
  spell_save_dc: number | null;
  spell_attack_bonus: number | null;
  n_prepared_spells: number;
}

export interface BuildResult {
  character: CharacterResult | null;
  error: string | null;
}
