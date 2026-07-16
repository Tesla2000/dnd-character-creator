import type { BlockInfo, FieldSchema } from "../types";

export interface TemplateData {
  prompt: string;
  race: string;
  subrace: string | null;
  statsPriority: string[];
  classes: Array<{ cls: string; level: number; subclass: string | null }>;
  magicalItems: {
    n_common: number;
    n_uncommon: number;
    n_rare: number;
    n_very_rare: number;
    n_legendary: number;
  };
}

function preferAiSubType(types: string[]): string | null {
  return (
    types.find((t) => t.startsWith("ai_") || t.includes("_ai_")) ??
    types.find((t) => t.includes("llm")) ??
    null
  );
}

function toAiConfig(
  config: Record<string, unknown>,
  fields: Record<string, FieldSchema>,
): Record<string, unknown> {
  const result: Record<string, unknown> = {};
  for (const [key, value] of Object.entries(config)) {
    const field = fields[key];
    if (
      field?.type === "sub_block" &&
      field.sub_block_types &&
      value !== null &&
      typeof value === "object"
    ) {
      const aiType = preferAiSubType(field.sub_block_types.map((s) => s.type_value));
      if (aiType) {
        result[key] = { type: aiType };
        continue;
      }
    }
    result[key] = value;
  }
  return result;
}

export function templateToPipeline(
  template: TemplateData,
  byType: Map<string, BlockInfo>,
): { type: string; [k: string]: unknown }[] {
  const entries: { type: string; [k: string]: unknown }[] = [];

  if (template.prompt.trim()) {
    entries.push({ type: "ai_base_builder_assigner", description: template.prompt });
  } else {
    entries.push({ type: "random_initial_data_filler" });
  }

  entries.push({
    type: "standard_array",
    stats_priority: template.statsPriority,
  });

  const raceInfo = byType.get(template.race);
  if (raceInfo) {
    const config = toAiConfig(raceInfo.default_config ?? {}, raceInfo.fields);
    if (template.subrace !== null) config["subrace"] = template.subrace;
    entries.push({ type: template.race, ...config });
  }

  for (const { cls, level, subclass } of template.classes) {
    for (let n = 1; n <= level; n++) {
      const subclassType = subclass ? `${cls}_level_${n}_${subclass}` : null;
      let blockType =
        subclassType && byType.has(subclassType)
          ? subclassType
          : `${cls}_level_${n}`;

      if (!byType.has(blockType)) {
        const fallback = [...byType.keys()].find((t) =>
          t.startsWith(`${cls}_level_${n}_`),
        );
        if (fallback) blockType = fallback;
      }

      const info = byType.get(blockType);
      if (info) {
        const config = toAiConfig(info.default_config ?? {}, info.fields);
        entries.push({ type: blockType, ...config });
      }
    }
  }

  const { n_common, n_uncommon, n_rare, n_very_rare, n_legendary } =
    template.magicalItems;
  if (n_common + n_uncommon + n_rare + n_very_rare + n_legendary > 0) {
    entries.push({
      type: "ai_magical_item_chooser",
      n_common,
      n_uncommon,
      n_rare,
      n_very_rare,
      n_legendary,
      n_artifact: 0,
      n_unique: 0,
      n_mistery: 0,
    });
  }

  return entries;
}

export function getSubclassesForClass(
  cls: string,
  byType: Map<string, BlockInfo>,
): { subclass: string; label: string; unlockLevel: number }[] {
  const subclassPattern = new RegExp(`^${cls}_level_(\\d+)_(.+)$`);
  const seen = new Map<string, number>();

  for (const key of byType.keys()) {
    const m = key.match(subclassPattern);
    if (!m) continue;
    const lvl = parseInt(m[1]);
    const sub = m[2];
    if (!seen.has(sub) || lvl < seen.get(sub)!) seen.set(sub, lvl);
  }

  return [...seen.entries()].map(([subclass, unlockLevel]) => ({
    subclass,
    label: subclass
      .split("_")
      .map((w) => w.charAt(0).toUpperCase() + w.slice(1))
      .join(" "),
    unlockLevel,
  })).sort((a, b) => a.label.localeCompare(b.label));
}

export function getClassUnlockLevel(cls: string, byType: Map<string, BlockInfo>): number {
  const subclasses = getSubclassesForClass(cls, byType);
  if (subclasses.length === 0) return Infinity;
  return Math.min(...subclasses.map((s) => s.unlockLevel));
}
