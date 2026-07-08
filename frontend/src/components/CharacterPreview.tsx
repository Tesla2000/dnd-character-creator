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
  const classes = character.classes as Record<string, number> | undefined;
  const stats = character.stats as Record<string, number> | undefined;
  const spells = character.spells as Record<string, string[]> | undefined;

  return (
    <div className="overflow-y-auto">
      <Section title="Identity">
        <Stat label="Name" value={character.name} />
        <Stat label="Age" value={character.age} />
        <Stat label="Sex" value={character.sex} />
        <Stat label="Alignment" value={character.alignment} />
        <Stat label="Background" value={character.background} />
        <Stat label="Race" value={character.race} />
        <Stat label="Level" value={character.level} />
        <Stat label="HP" value={character.health_base} />
      </Section>

      {classes && Object.keys(classes).length > 0 && (
        <Section title="Classes">
          {Object.entries(classes).map(([cls, lvl]) => (
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

      {(character.feats as string[] | undefined)?.length ? (
        <Section title="Feats">
          {(character.feats as string[]).map((f) => (
            <div key={f} className="py-0.5 text-gray-300">
              {f}
            </div>
          ))}
        </Section>
      ) : null}

      {(character.subclasses as string[] | undefined)?.length ? (
        <Section title="Subclasses">
          {(character.subclasses as string[]).map((s) => (
            <div key={s} className="py-0.5 text-gray-300">
              {s}
            </div>
          ))}
        </Section>
      ) : null}

      {(character.skill_proficiencies as string[] | undefined)?.length ? (
        <Section title="Skills">
          <div className="flex flex-wrap gap-1">
            {(character.skill_proficiencies as string[]).map((s) => (
              <span
                key={s}
                className="text-xs bg-dnd-dark border border-dnd-border rounded px-1.5 py-0.5"
              >
                {s}
              </span>
            ))}
          </div>
        </Section>
      ) : null}

      {(character.languages as string[] | undefined)?.length ? (
        <Section title="Languages">
          <div className="flex flex-wrap gap-1">
            {(character.languages as string[]).map((l) => (
              <span
                key={l}
                className="text-xs bg-dnd-dark border border-dnd-border rounded px-1.5 py-0.5"
              >
                {l}
              </span>
            ))}
          </div>
        </Section>
      ) : null}

      {(character.weapons as string[] | undefined)?.length ? (
        <Section title="Weapons">
          {(character.weapons as string[]).map((w) => (
            <div key={w} className="py-0.5 text-gray-300">
              {w}
            </div>
          ))}
        </Section>
      ) : null}

      {spells && Object.keys(spells).some((k) => spells[k]?.length) && (
        <Section title="Spells">
          {Object.entries(spells)
            .filter(([, list]) => list?.length)
            .map(([level, list]) => (
              <div key={level} className="mb-2">
                <div className="text-xs text-gray-500 mb-1">{level.replace(/_/g, " ")}</div>
                <div className="flex flex-wrap gap-1">
                  {list.map((s) => (
                    <span
                      key={s}
                      className="text-xs bg-dnd-dark border border-dnd-border rounded px-1.5 py-0.5"
                    >
                      {s}
                    </span>
                  ))}
                </div>
              </div>
            ))}
        </Section>
      )}
    </div>
  );
}
