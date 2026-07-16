import { useState, useMemo } from "preact/hooks";
import type { BlockInfo } from "../types";
import {
  templateToPipeline,
  getSubclassesForClass,
  getClassUnlockLevel,
} from "../utils/templateToPipeline";

interface ClassEntry {
  cls: string;
  level: number;
  subclass: string | null;
}

interface MagicalItems {
  n_common: number;
  n_uncommon: number;
  n_rare: number;
  n_very_rare: number;
  n_legendary: number;
}

interface Props {
  byType: Map<string, BlockInfo>;
  onGenerate: (entries: { type: string; [k: string]: unknown }[]) => void;
  onClose: () => void;
}

const STAT_LABELS: Record<string, string> = {
  strength: "Strength",
  dexterity: "Dexterity",
  constitution: "Constitution",
  intelligence: "Intelligence",
  wisdom: "Wisdom",
  charisma: "Charisma",
};

const DEFAULT_STATS = [
  "strength",
  "dexterity",
  "constitution",
  "intelligence",
  "wisdom",
  "charisma",
];

const ITEM_RARITIES: { key: keyof MagicalItems; label: string; color: string }[] = [
  { key: "n_common", label: "Common", color: "text-gray-300" },
  { key: "n_uncommon", label: "Uncommon", color: "text-green-400" },
  { key: "n_rare", label: "Rare", color: "text-blue-400" },
  { key: "n_very_rare", label: "Very Rare", color: "text-purple-400" },
  { key: "n_legendary", label: "Legendary", color: "text-orange-400" },
];

const SELECT_CLS =
  "bg-dnd-dark border border-dnd-border rounded px-2 py-1 text-white text-sm focus:outline-none focus:border-dnd-gold w-full";

export function TemplateModal({ byType, onGenerate, onClose }: Props) {
  const raceOptions = useMemo(
    () =>
      [...byType.values()]
        .filter((b) => b.type.endsWith("_race_assigner") && b.type !== "race_assigner")
        .sort((a, b) => a.label.localeCompare(b.label)),
    [byType],
  );

  // Detect classes from both `{cls}_level_1` and `{cls}_level_1_{subclass}` patterns
  const classOptions = useMemo(() => {
    const found = new Set<string>();
    for (const key of byType.keys()) {
      const m = key.match(/^([a-z]+)_level_1(?:_|$)/);
      if (m) found.add(m[1]);
    }
    return [...found].sort();
  }, [byType]);

  const defaultRace = raceOptions[0]?.type ?? "";
  const defaultCls = classOptions[0] ?? "wizard";

  const [statDragIdx, setStatDragIdx] = useState<number | null>(null);
  const [statDragOverIdx, setStatDragOverIdx] = useState<number | null>(null);
  const [prompt, setPrompt] = useState("");
  const [race, setRace] = useState<string>(defaultRace);
  const [subrace, setSubrace] = useState<string | null>(null);
  const [statsPriority, setStatsPriority] = useState<string[]>(DEFAULT_STATS);
  const initialSubclass = useMemo(
    () => {
      const unlock = getClassUnlockLevel(defaultCls, byType);
      if (1 >= unlock) return getSubclassesForClass(defaultCls, byType)[0]?.subclass ?? null;
      return null;
    },
    // eslint-disable-next-line react-hooks/exhaustive-deps
    [],
  );
  const [classes, setClasses] = useState<ClassEntry[]>([
    { cls: defaultCls, level: 1, subclass: initialSubclass },
  ]);
  const [magicalItems, setMagicalItems] = useState<MagicalItems>({
    n_common: 0,
    n_uncommon: 0,
    n_rare: 0,
    n_very_rare: 0,
    n_legendary: 0,
  });

  const raceInfo = byType.get(race);
  const subraceEnum = raceInfo?.fields["subrace"]?.enum ?? null;
  const totalLevel = classes.reduce((s, c) => s + c.level, 0);
  const usedClasses = new Set(classes.map((c) => c.cls));

  function handleRaceChange(newRace: string) {
    setRace(newRace);
    setSubrace(null);
  }

  function autoSubclass(cls: string, level: number, current: string | null): string | null {
    const unlock = getClassUnlockLevel(cls, byType);
    if (level < unlock) return current;
    if (current !== null) return current;
    return getSubclassesForClass(cls, byType)[0]?.subclass ?? null;
  }

  function handleClassChange(idx: number, field: keyof ClassEntry, value: unknown) {
    setClasses((prev) => {
      const next = [...prev];
      next[idx] = { ...next[idx], [field]: value } as ClassEntry;
      if (field === "cls") next[idx].subclass = null;
      const { cls, level, subclass } = next[idx];
      next[idx].subclass = autoSubclass(cls, level, field === "cls" ? null : subclass);
      return next;
    });
  }

  function addClassRow() {
    if (totalLevel >= 20 || classes.length >= 4) return;
    const nextCls = classOptions.find((c) => !usedClasses.has(c)) ?? defaultCls;
    const sub = autoSubclass(nextCls, 1, null);
    setClasses((prev) => [...prev, { cls: nextCls, level: 1, subclass: sub }]);
  }

  function removeClassRow(idx: number) {
    setClasses((prev) => prev.filter((_, i) => i !== idx));
  }

  function handleItemChange(key: keyof MagicalItems, val: number) {
    setMagicalItems((prev) => ({ ...prev, [key]: Math.max(0, val) }));
  }

  function handleStatDrop(toIdx: number) {
    if (statDragIdx === null || statDragIdx === toIdx) return;
    setStatsPriority((prev) => {
      const next = [...prev];
      const [item] = next.splice(statDragIdx, 1);
      next.splice(toIdx, 0, item);
      return next;
    });
  }

  function clearStatDrag() {
    setStatDragIdx(null);
    setStatDragOverIdx(null);
  }

  function handleGenerate() {
    onGenerate(
      templateToPipeline({ prompt, race, subrace, statsPriority, classes, magicalItems }, byType),
    );
  }

  const canGenerate =
    prompt.trim() !== "" &&
    race !== "" &&
    classes.length > 0 &&
    classes.every((c) => {
      const unlockLevel = getClassUnlockLevel(c.cls, byType);
      return unlockLevel > c.level || c.subclass !== null;
    });

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center"
      style={{ background: "rgba(0,0,0,0.7)" }}
      onClick={(e) => e.target === e.currentTarget && onClose()}
    >
      <div className="bg-dnd-panel border border-dnd-border rounded-lg shadow-2xl w-full max-w-lg max-h-[90vh] overflow-y-auto">
        {/* Header */}
        <div className="flex items-center justify-between px-5 py-3 border-b border-dnd-border">
          <h2 className="text-base font-bold text-dnd-gold">Character Template</h2>
          <button
            className="text-gray-500 hover:text-white text-xl leading-none"
            onClick={onClose}
          >
            ×
          </button>
        </div>

        <div className="px-5 py-4 flex flex-col gap-5">
          {/* Concept */}
          <section>
            <label className="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1.5">
              Character Concept
            </label>
            <textarea
              className="bg-dnd-dark border border-dnd-border rounded px-2 py-1 text-white text-sm focus:outline-none focus:border-dnd-gold w-full resize-none"
              rows={3}
              placeholder="e.g. A brooding half-elf wizard who seeks forbidden knowledge…"
              value={prompt}
              onInput={(e) => setPrompt((e.target as HTMLTextAreaElement).value)}
            />
            <p className="text-xs text-gray-600 mt-1">
              AI will use this to guide name, background, and personality.
            </p>
          </section>

          {/* Race */}
          <section>
            <label className="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1.5">
              Race
            </label>
            <div className="flex gap-2">
              <select
                className={SELECT_CLS}
                value={race}
                onChange={(e) => handleRaceChange((e.target as HTMLSelectElement).value)}
              >
                {raceOptions.map((b) => (
                  <option key={b.type} value={b.type}>
                    {b.label.replace(" Race Assigner", "")}
                  </option>
                ))}
              </select>
              {subraceEnum && subraceEnum.length > 0 && (
                <select
                  className={SELECT_CLS}
                  value={subrace ?? subraceEnum[0]}
                  onChange={(e) => setSubrace((e.target as HTMLSelectElement).value)}
                >
                  {subraceEnum.map((s) => (
                    <option key={s} value={s}>
                      {s}
                    </option>
                  ))}
                </select>
              )}
            </div>
          </section>

          {/* Stats Priority */}
          <section>
            <label className="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1.5">
              Stats Priority
              <span className="normal-case font-normal text-gray-600 ml-1">
                (highest → lowest)
              </span>
            </label>
            <div className="flex flex-col gap-1">
              {statsPriority.map((stat, idx) => {
                const isDragging = statDragIdx === idx;
                const isTarget = statDragOverIdx === idx && statDragIdx !== idx;
                return (
                  <div
                    key={stat}
                    draggable
                    onDragStart={() => setStatDragIdx(idx)}
                    onDragOver={(e) => { e.preventDefault(); setStatDragOverIdx(idx); }}
                    onDrop={() => { handleStatDrop(idx); clearStatDrag(); }}
                    onDragEnd={clearStatDrag}
                    className={`flex items-center gap-2 bg-dnd-dark border border-dnd-border rounded px-2 py-1 transition-all ${
                      isDragging ? "opacity-30" : ""
                    } ${isTarget ? "border-t-2 border-t-dnd-gold" : ""}`}
                    style={{ cursor: isDragging ? "grabbing" : "grab" }}
                  >
                    <span className="text-gray-600 flex-shrink-0 select-none" style={{ fontSize: "10px", lineHeight: 1, letterSpacing: "-1px" }}>
                      ⠿
                    </span>
                    <span className="text-xs text-gray-600 w-4 text-right flex-shrink-0">
                      {idx + 1}.
                    </span>
                    <span className="text-sm text-white flex-1">{STAT_LABELS[stat]}</span>
                  </div>
                );
              })}
            </div>
          </section>

          {/* Classes */}
          <section>
            <div className="flex items-center justify-between mb-1.5">
              <label className="text-xs font-semibold text-gray-400 uppercase tracking-wider">
                Classes
              </label>
              <span
                className={`text-xs font-mono ${totalLevel >= 20 ? "text-yellow-400" : "text-gray-500"}`}
              >
                Total: {totalLevel} / 20
              </span>
            </div>
            <div className="flex flex-col gap-2">
              {classes.map((entry, idx) => {
                const subclasses = getSubclassesForClass(entry.cls, byType);
                const unlockLevel = getClassUnlockLevel(entry.cls, byType);
                const needsSubclass = unlockLevel <= entry.level;
                const otherTotal = classes.reduce((s, c, i) => (i === idx ? s : s + c.level), 0);
                const maxLevel = 20 - otherTotal;

                return (
                  <div
                    key={idx}
                    className="flex flex-col gap-1.5 bg-dnd-dark rounded p-2 border border-dnd-border"
                  >
                    <div className="flex gap-2 items-center">
                      <select
                        className={`${SELECT_CLS} flex-1`}
                        value={entry.cls}
                        onChange={(e) =>
                          handleClassChange(idx, "cls", (e.target as HTMLSelectElement).value)
                        }
                      >
                        {classOptions.map((c) => (
                          <option
                            key={c}
                            value={c}
                            disabled={c !== entry.cls && usedClasses.has(c)}
                          >
                            {c.charAt(0).toUpperCase() + c.slice(1)}
                            {c !== entry.cls && usedClasses.has(c) ? " (taken)" : ""}
                          </option>
                        ))}
                      </select>

                      <div className="flex items-center gap-1 flex-shrink-0">
                        <span className="text-xs text-gray-500">Lv</span>
                        <input
                          type="number"
                          min={1}
                          max={maxLevel}
                          value={entry.level}
                          className="bg-dnd-dark border border-dnd-border rounded px-2 py-1 text-white text-sm focus:outline-none focus:border-dnd-gold w-14 text-center"
                          onInput={(e) => {
                            const v = parseInt((e.target as HTMLInputElement).value);
                            if (!isNaN(v))
                              handleClassChange(idx, "level", Math.min(maxLevel, Math.max(1, v)));
                          }}
                        />
                      </div>

                      {classes.length > 1 && (
                        <button
                          className="text-gray-500 hover:text-red-400 text-lg leading-none flex-shrink-0"
                          onClick={() => removeClassRow(idx)}
                        >
                          ×
                        </button>
                      )}
                    </div>

                    {subclasses.length > 0 && (
                      <div>
                        <select
                          className={SELECT_CLS}
                          value={entry.subclass ?? ""}
                          onChange={(e) => {
                            const v = (e.target as HTMLSelectElement).value;
                            handleClassChange(idx, "subclass", v || null);
                          }}
                        >
                          <option value="">— Select subclass —</option>
                          {subclasses.map((s) => (
                            <option key={s.subclass} value={s.subclass}>
                              {s.label}
                            </option>
                          ))}
                        </select>
                        {needsSubclass && !entry.subclass && (
                          <p className="text-xs text-yellow-500 mt-0.5">
                            Subclass required at level {unlockLevel} — select one to continue.
                          </p>
                        )}
                        {!needsSubclass && entry.subclass && (
                          <p className="text-xs text-yellow-500 mt-0.5">
                            Subclass unlocks at level {unlockLevel} — will not be applied at level{" "}
                            {entry.level}.
                          </p>
                        )}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>

            {classes.length < 4 && totalLevel < 20 && (
              <button
                className="mt-2 w-full text-xs border border-dnd-border border-dashed rounded px-2 py-1.5 text-gray-500 hover:text-dnd-gold hover:border-dnd-gold transition-colors"
                onClick={addClassRow}
                disabled={usedClasses.size >= classOptions.length}
              >
                + Add class
              </button>
            )}
          </section>

          {/* Magical Items */}
          <section>
            <label className="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1.5">
              Magical Items
            </label>
            <div className="grid grid-cols-5 gap-2">
              {ITEM_RARITIES.map(({ key, label, color }) => (
                <div key={key} className="flex flex-col items-center gap-1">
                  <span className={`text-xs ${color}`}>{label}</span>
                  <input
                    type="number"
                    min={0}
                    value={magicalItems[key]}
                    className="bg-dnd-dark border border-dnd-border rounded px-1 py-1 text-white text-sm focus:outline-none focus:border-dnd-gold w-full text-center"
                    onInput={(e) => {
                      const v = parseInt((e.target as HTMLInputElement).value);
                      if (!isNaN(v)) handleItemChange(key, v);
                    }}
                  />
                </div>
              ))}
            </div>
          </section>
        </div>

        {/* Footer */}
        <div className="flex items-center justify-end gap-3 px-5 py-3 border-t border-dnd-border">
          <button
            className="text-sm text-gray-400 hover:text-white px-3 py-1.5 transition-colors"
            onClick={onClose}
          >
            Cancel
          </button>
          <button
            disabled={!canGenerate}
            className="bg-dnd-red hover:bg-red-700 disabled:opacity-40 disabled:cursor-not-allowed text-white font-semibold px-4 py-1.5 rounded transition-colors text-sm"
            onClick={handleGenerate}
          >
            Generate Pipeline
          </button>
        </div>
      </div>
    </div>
  );
}
