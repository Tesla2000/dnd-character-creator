export interface FieldSchema {
  type: string;
  description?: string;
  enum?: string[];
  default?: unknown;
  required?: boolean;
  note?: string;
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
  requires: string[];
  provides: string[];
  conflicts: string[];
}

export interface PipelineBlock {
  id: string;
  blockType: string;
  config: Record<string, unknown>;
}

export interface CharacterResult {
  name?: string;
  age?: number;
  sex?: string;
  alignment?: string;
  background?: string;
  race?: string;
  level?: number;
  classes?: Record<string, number>;
  stats?: Record<string, number>;
  health_base?: number;
  feats?: string[];
  weapons?: string[];
  spells?: Record<string, string[]>;
  subclasses?: string[];
  skill_proficiencies?: string[];
  languages?: string[];
  [key: string]: unknown;
}

export interface BuildResult {
  character: CharacterResult | null;
  error: string | null;
}
