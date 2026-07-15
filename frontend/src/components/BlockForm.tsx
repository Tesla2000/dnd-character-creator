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
