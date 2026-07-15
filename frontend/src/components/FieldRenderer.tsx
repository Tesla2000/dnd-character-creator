import { useRef } from "preact/hooks";
import type { FieldSchema, SubBlockTypeInfo } from "../types";

interface Props {
  name: string;
  schema: FieldSchema;
  value: unknown;
  onChange: (value: unknown) => void;
}

function OrderedEnumList({
  label,
  options,
  value,
  onChange,
  description,
}: {
  label: string;
  options: string[];
  value: unknown;
  onChange: (v: string[]) => void;
  description?: string;
}) {
  const current: string[] =
    Array.isArray(value) && value.length === options.length
      ? (value as string[])
      : [...options];

  const dragIndex = useRef<number | null>(null);

  function onDragStart(i: number) {
    dragIndex.current = i;
  }

  function onDrop(i: number) {
    const from = dragIndex.current;
    if (from === null || from === i) return;
    const next = [...current];
    const [item] = next.splice(from, 1);
    next.splice(i, 0, item);
    onChange(next);
    dragIndex.current = null;
  }

  function move(i: number, dir: -1 | 1) {
    const j = i + dir;
    if (j < 0 || j >= current.length) return;
    const next = [...current];
    [next[i], next[j]] = [next[j], next[i]];
    onChange(next);
  }

  return (
    <div className="mb-3">
      <label className="block text-xs text-gray-400 mb-1">{label}</label>
      <div className="flex flex-col gap-1">
        {current.map((stat, i) => (
          <div
            key={stat}
            draggable
            onDragStart={() => onDragStart(i)}
            onDragOver={(e) => e.preventDefault()}
            onDrop={() => onDrop(i)}
            className="flex items-center gap-2 bg-dnd-dark border border-dnd-border rounded px-2 py-1 cursor-grab active:cursor-grabbing select-none"
          >
            <span className="text-xs text-gray-600 w-4 text-right">{i + 1}</span>
            <span className="flex-1 text-sm text-white capitalize">{stat}</span>
            <button
              type="button"
              className="text-gray-600 hover:text-white text-xs px-1 disabled:opacity-20"
              disabled={i === 0}
              onClick={() => move(i, -1)}
            >
              ▲
            </button>
            <button
              type="button"
              className="text-gray-600 hover:text-white text-xs px-1 disabled:opacity-20"
              disabled={i === current.length - 1}
              onClick={() => move(i, 1)}
            >
              ▼
            </button>
          </div>
        ))}
      </div>
      {description && <p className="text-xs text-gray-500 mt-1">{description}</p>}
    </div>
  );
}

function SubBlockRenderer({
  label,
  subBlockTypes,
  value,
  onChange,
  description,
}: {
  label: string;
  subBlockTypes: SubBlockTypeInfo[];
  value: unknown;
  onChange: (v: unknown) => void;
  description?: string;
}) {
  const inputClass =
    "w-full bg-dnd-dark border border-dnd-border rounded px-2 py-1 text-sm text-white focus:outline-none focus:border-dnd-gold";
  const current = (value ?? {}) as Record<string, unknown>;
  const currentType = typeof current.type === "string" ? current.type : subBlockTypes[0]?.type_value;
  const selectedType = subBlockTypes.find((t) => t.type_value === currentType) ?? subBlockTypes[0];

  function handleTypeChange(newTypeValue: string) {
    const typeInfo = subBlockTypes.find((t) => t.type_value === newTypeValue);
    if (!typeInfo) return;
    const newConfig: Record<string, unknown> = { type: newTypeValue };
    for (const [fname, fschema] of Object.entries(typeInfo.fields)) {
      if (fschema.enum?.length) newConfig[fname] = fschema.enum[0];
      else if (fschema.type === "array" && fschema.items?.enum) newConfig[fname] = [...fschema.items.enum];
      else if (fschema.default !== undefined) newConfig[fname] = fschema.default;
    }
    onChange(newConfig);
  }

  function handleSubField(fname: string, v: unknown) {
    onChange({ ...current, type: currentType, [fname]: v });
  }

  const subFields = selectedType ? Object.entries(selectedType.fields) : [];

  return (
    <div className="mb-3">
      <label className="block text-xs text-gray-400 mb-1">{label}</label>
      <select
        className={inputClass + " mb-2"}
        value={currentType ?? ""}
        onChange={(e) => handleTypeChange((e.target as HTMLSelectElement).value)}
      >
        {subBlockTypes.map((t) => (
          <option key={t.type_value} value={t.type_value}>
            {t.label}
          </option>
        ))}
      </select>
      {subFields.length > 0 && (
        <div className="pl-3 border-l border-dnd-border">
          {subFields.map(([fname, fschema]) => (
            <FieldRenderer
              key={fname}
              name={fname}
              schema={fschema}
              value={current[fname]}
              onChange={(v) => handleSubField(fname, v)}
            />
          ))}
        </div>
      )}
      {description && <p className="text-xs text-gray-500 mt-1">{description}</p>}
    </div>
  );
}

export function FieldRenderer({ name, schema, value, onChange }: Props) {
  const label = name.replace(/_/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());
  const inputClass =
    "w-full bg-dnd-dark border border-dnd-border rounded px-2 py-1 text-sm text-white focus:outline-none focus:border-dnd-gold";

  if (schema.type === "nested_model" && schema.properties) {
    const nested = (value ?? {}) as Record<string, unknown>;
    return (
      <div className="mb-3">
        <p className="text-xs text-gray-400 uppercase tracking-wider mb-2">{label}</p>
        <div className="pl-3 border-l border-dnd-border">
          {Object.entries(schema.properties).map(([sub, subSchema]) => (
            <FieldRenderer
              key={sub}
              name={sub}
              schema={subSchema}
              value={nested[sub]}
              onChange={(v) => onChange({ ...nested, [sub]: v })}
            />
          ))}
        </div>
        {schema.description && (
          <p className="text-xs text-gray-500 mt-1">{schema.description}</p>
        )}
      </div>
    );
  }

  if (schema.type === "sub_block" && schema.sub_block_types?.length) {
    return (
      <SubBlockRenderer
        label={label}
        subBlockTypes={schema.sub_block_types}
        value={value}
        onChange={onChange}
        description={schema.description}
      />
    );
  }

  if (schema.type === "array" && schema.items?.enum) {
    return (
      <OrderedEnumList
        label={label}
        options={schema.items.enum}
        value={value}
        onChange={onChange}
        description={schema.description}
      />
    );
  }

  if (schema.note?.includes("complex nested type")) {
    return (
      <div className="mb-3">
        <label className="block text-xs text-gray-400 mb-1">{label}</label>
        <textarea
          className={`${inputClass} font-mono text-xs`}
          rows={4}
          value={typeof value === "object" ? JSON.stringify(value, null, 2) : String(value ?? "")}
          onInput={(e) => {
            try {
              onChange(JSON.parse((e.target as HTMLTextAreaElement).value));
            } catch {
              onChange((e.target as HTMLTextAreaElement).value);
            }
          }}
          placeholder={`JSON for ${label}`}
        />
        {schema.description && (
          <p className="text-xs text-gray-500 mt-1">{schema.description}</p>
        )}
      </div>
    );
  }

  if (schema.enum) {
    return (
      <div className="mb-3">
        <label className="block text-xs text-gray-400 mb-1">{label}</label>
        <select
          className={inputClass}
          value={String(value ?? schema.default ?? "")}
          onChange={(e) => onChange((e.target as HTMLSelectElement).value)}
        >
          {!schema.required && <option value="">— choose —</option>}
          {schema.enum.map((opt) => (
            <option key={opt} value={opt}>
              {opt.replace(/_/g, " ")}
            </option>
          ))}
        </select>
        {schema.description && (
          <p className="text-xs text-gray-500 mt-1">{schema.description}</p>
        )}
      </div>
    );
  }

  if (schema.type === "boolean") {
    return (
      <div className="mb-3 flex items-center gap-2">
        <input
          type="checkbox"
          id={name}
          className="w-4 h-4 accent-dnd-gold"
          checked={Boolean(value ?? schema.default ?? false)}
          onChange={(e) => onChange((e.target as HTMLInputElement).checked)}
        />
        <label htmlFor={name} className="text-xs text-gray-400">
          {label}
        </label>
      </div>
    );
  }

  if (schema.type === "integer" || schema.type === "number") {
    return (
      <div className="mb-3">
        <label className="block text-xs text-gray-400 mb-1">{label}</label>
        <input
          type="number"
          className={inputClass}
          value={value as number ?? (schema.default as number) ?? ""}
          onInput={(e) =>
            onChange(parseInt((e.target as HTMLInputElement).value, 10))
          }
          placeholder={label}
        />
        {schema.description && (
          <p className="text-xs text-gray-500 mt-1">{schema.description}</p>
        )}
      </div>
    );
  }

  // Default: text input
  return (
    <div className="mb-3">
      <label className="block text-xs text-gray-400 mb-1">{label}</label>
      <input
        type="text"
        className={inputClass}
        value={String(value ?? schema.default ?? "")}
        onInput={(e) => onChange((e.target as HTMLInputElement).value)}
        placeholder={label}
      />
      {schema.description && (
        <p className="text-xs text-gray-500 mt-1">{schema.description}</p>
      )}
    </div>
  );
}
