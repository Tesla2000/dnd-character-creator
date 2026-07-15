import { useState } from "preact/hooks";
import type { BlockInfo } from "../types";

interface Props {
  available: BlockInfo[];
  onSelect: (blockType: string) => void;
  onClose: () => void;
}

const CATEGORY_ORDER = [
  "Leveling",
  "Builders",
  "Stats",
  "Race",
  "Spells",
  "Subclass",
  "Feats",
  "Skills",
  "Languages",
  "Tool Proficiencies",
  "Equipment",
  "Choices",
  "AI",
  "Utility",
  "Other",
  "Identity",
];

export function BlockPicker({ available, onSelect, onClose }: Props) {
  const [search, setSearch] = useState("");

  const filtered = search
    ? available.filter(
        (b) =>
          b.label.toLowerCase().includes(search.toLowerCase()) ||
          b.category.toLowerCase().includes(search.toLowerCase()) ||
          b.description.toLowerCase().includes(search.toLowerCase())
      )
    : available;

  const grouped: Record<string, BlockInfo[]> = {};
  for (const b of filtered) {
    (grouped[b.category] ??= []).push(b);
  }

  const categories = CATEGORY_ORDER.filter((c) => grouped[c]?.length);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60">
      <div className="bg-dnd-panel border border-dnd-border rounded-lg shadow-2xl w-[480px] max-h-[80vh] flex flex-col">
        <div className="p-4 border-b border-dnd-border flex items-center gap-2">
          <input
            autoFocus
            type="text"
            className="flex-1 bg-dnd-dark border border-dnd-border rounded px-3 py-1.5 text-sm text-white focus:outline-none focus:border-dnd-gold"
            placeholder="Search blocks..."
            value={search}
            onInput={(e) => setSearch((e.target as HTMLInputElement).value)}
          />
          <button
            onClick={onClose}
            className="text-gray-400 hover:text-white text-xl leading-none px-1"
          >
            ×
          </button>
        </div>

        <div className="overflow-y-auto flex-1 p-2">
          {categories.length === 0 && (
            <p className="text-center text-gray-500 py-8 text-sm">
              No blocks available at this position
            </p>
          )}
          {categories.map((cat) => (
            <div key={cat} className="mb-3">
              <h3 className="text-xs font-semibold text-dnd-gold uppercase tracking-wider px-2 py-1">
                {cat}
              </h3>
              {grouped[cat].map((b) => (
                <button
                  key={b.type}
                  className="w-full text-left px-3 py-2 rounded hover:bg-dnd-card transition-colors group"
                  onClick={() => {
                    onSelect(b.type);
                    onClose();
                  }}
                >
                  <div className="flex items-center justify-between">
                    <span className="text-sm text-white group-hover:text-dnd-gold">
                      {b.label}
                    </span>
                    {b.is_ai && (
                      <span className="text-xs text-purple-400 bg-purple-900/40 px-1.5 py-0.5 rounded">
                        AI
                      </span>
                    )}
                  </div>
                  {b.description && (
                    <p className="text-xs text-gray-500 mt-0.5 truncate">{b.description}</p>
                  )}
                </button>
              ))}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
