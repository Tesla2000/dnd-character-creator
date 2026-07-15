import type { CharacterResult } from "../types";

interface Props {
  character: CharacterResult;
}

function Section({ title, children }: { title: string; children: preact.ComponentChildren }) {
  return (
    <div className="mb-4">
      <h3 className="text-xs font-semibold text-dnd-gold uppercase tracking-wider mb-2">
        {title}
      </h3>
      <div className="text-sm text-gray-300">{children}</div>
    </div>
  );
}

function Stat({ label, value }: { label: string; value: unknown }) {
  if (value === undefined || value === null) return null;
  return (
    <div className="flex justify-between py-0.5">
      <span className="text-gray-500">{label}</span>
      <span className="text-white font-medium">{String(value)}</span>
    </div>
  );
}

export function CharacterPreview({ character }: Props) {
  const cd = character.character_data;
  const stats = character.stats;
  const spells = character.spells;

  return (
    <div className="overflow-y-auto">
      {Object.keys(character.classes).length > 0 && (
        <Section title="Leveling">
          {Object.entries(character.classes).map(([cls, lvl]) => (
            <div key={cls} className="flex justify-between py-0.5">
              <span className="text-gray-500">{cls}</span>
              <span className="text-white">Lv {lvl}</span>
            </div>
          ))}
        </Section>
      )}

      {stats && (
        <Section title="Stats">
          <div className="grid grid-cols-3 gap-1">
            {Object.entries(stats).map(([stat, val]) => (
              <div
                key={stat}
                className="bg-dnd-dark rounded p-1.5 text-center border border-dnd-border"
              >
                <div className="text-xs text-gray-500 uppercase">{stat.slice(0, 3)}</div>
                <div className="text-lg font-bold text-white">{val}</div>
              </div>
            ))}
          </div>
        </Section>
      )}

      {character.feats.length > 0 && (
        <Section title="Feats">
          {character.feats.map((f) => (
            <div key={f} className="py-0.5 text-gray-300">{f}</div>
          ))}
        </Section>
      )}

      {character.subclasses.length > 0 && (
        <Section title="Subclasses">
          {character.subclasses.map((s) => (
            <div key={s} className="py-0.5 text-gray-300">{s}</div>
          ))}
        </Section>
      )}

      {character.skill_proficiencies.length > 0 && (
        <Section title="Skills">
          <div className="flex flex-wrap gap-1">
            {character.skill_proficiencies.map((s) => (
              <span key={s} className="text-xs bg-dnd-dark border border-dnd-border rounded px-1.5 py-0.5">
                {s}
              </span>
            ))}
          </div>
        </Section>
      )}

      {character.languages.length > 0 && (
        <Section title="Languages">
          <div className="flex flex-wrap gap-1">
            {character.languages.map((l) => (
              <span key={l} className="text-xs bg-dnd-dark border border-dnd-border rounded px-1.5 py-0.5">
                {l}
              </span>
            ))}
          </div>
        </Section>
      )}

      {character.weapons.length > 0 && (
        <Section title="Weapons">
          {character.weapons.map((w) => (
            <div key={w} className="py-0.5 text-gray-300">{w}</div>
          ))}
        </Section>
      )}

      {spells && Object.values(spells).some((list) => list.length > 0) && (
        <Section title="Spells">
          {Object.entries(spells)
            .filter(([, list]) => list.length > 0)
            .map(([level, list]) => (
              <div key={level} className="mb-2">
                <div className="text-xs text-gray-500 mb-1">{level.replace(/_/g, " ")}</div>
                <div className="flex flex-wrap gap-1">
                  {list.map((s: string) => (
                    <span key={s} className="text-xs bg-dnd-dark border border-dnd-border rounded px-1.5 py-0.5">
                      {s}
                    </span>
                  ))}
                </div>
              </div>
            ))}
        </Section>
      )}

      <Section title="Identity">
        <Stat label="Name" value={cd?.name} />
        <Stat label="Age" value={cd?.age} />
        <Stat label="Sex" value={cd?.sex} />
        <Stat label="Alignment" value={cd?.alignment} />
        <Stat label="Background" value={cd?.background} />
        <Stat label="Race" value={character.race} />
        <Stat label="Level" value={character.level} />
        <Stat label="HP" value={character.health} />
        <Stat label="AC" value={character.ac} />
        <Stat label="Initiative" value={character.initiative} />
      </Section>
    </div>
  );
}
