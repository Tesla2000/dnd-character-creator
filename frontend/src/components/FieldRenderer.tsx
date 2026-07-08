import type { FieldSchema } from "../types";

interface Props {
  name: string;
  schema: FieldSchema;
  value: unknown;
  onChange: (value: unknown) => void;
}

export function FieldRenderer({ name, schema, value, onChange }: Props) {
  const label = name.replace(/_/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());
  const inputClass =
    "w-full bg-dnd-dark border border-dnd-border rounded px-2 py-1 text-sm text-white focus:outline-none focus:border-dnd-gold";

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
          value={String(value ?? schema.default ?? schema.enum[0] ?? "")}
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
