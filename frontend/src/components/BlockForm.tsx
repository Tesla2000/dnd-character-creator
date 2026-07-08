import type { BlockInfo, PipelineBlock } from "../types";
import { FieldRenderer } from "./FieldRenderer";

interface Props {
  block: PipelineBlock;
  info: BlockInfo;
  onChange: (config: Record<string, unknown>) => void;
}

export function BlockForm({ block, info, onChange }: Props) {
  const fields = Object.entries(info.fields);

  function handleField(name: string, value: unknown) {
    onChange({ ...block.config, [name]: value });
  }

  return (
    <div>
      <h2 className="text-lg font-semibold text-dnd-gold mb-1">{info.label}</h2>
      {info.description && (
        <p className="text-xs text-gray-400 mb-4">{info.description}</p>
      )}

      {info.requires.length > 0 && (
        <div className="mb-4 text-xs">
          <span className="text-gray-500">Requires: </span>
          {info.requires.map((r) => (
            <span
              key={r}
              className="inline-block bg-blue-900 text-blue-300 rounded px-1.5 py-0.5 mr-1"
            >
              {r}
            </span>
          ))}
        </div>
      )}

      {info.provides.length > 0 && (
        <div className="mb-4 text-xs">
          <span className="text-gray-500">Provides: </span>
          {info.provides.map((p) => (
            <span
              key={p}
              className="inline-block bg-green-900 text-green-300 rounded px-1.5 py-0.5 mr-1"
            >
              {p}
            </span>
          ))}
        </div>
      )}

      {info.is_ai && (
        <div className="mb-4 p-2 bg-purple-900/30 border border-purple-700 rounded text-xs text-purple-300">
          AI-powered block — LLM configuration required at runtime
        </div>
      )}

      {fields.length === 0 ? (
        <p className="text-xs text-gray-500 italic">No configuration needed.</p>
      ) : (
        fields.map(([name, schema]) => (
          <FieldRenderer
            key={name}
            name={name}
            schema={schema}
            value={block.config[name]}
            onChange={(v) => handleField(name, v)}
          />
        ))
      )}
    </div>
  );
}
