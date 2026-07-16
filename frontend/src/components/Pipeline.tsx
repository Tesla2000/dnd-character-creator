import { useState } from "preact/hooks";
import type { BlockInfo, BlueprintState, PipelineBlock } from "../types";
import { BlockPicker } from "./BlockPicker";
import { compatibleBlocksAt } from "../utils/blueprintState";
import { blockHasUnfilledRequired } from "../utils/blockValidation";
import pipelineMeta from "../data/pipeline-meta.json";

interface Props {
  blocks: PipelineBlock[];
  byType: Map<string, BlockInfo>;
  registry: BlockInfo[];
  blueprintSnapshots: BlueprintState[];
  selectedId: string | null;
  onSelect: (id: string) => void;
  onAppend: (blockType: string) => void;
  onRemoveLast: () => void;
  onReorder: (newBlocks: PipelineBlock[]) => void;
  onSave: () => void;
  onLoad: (e: Event) => void;
}

const _hierarchy = pipelineMeta.originHierarchy as Record<string, string[]>;

export function Pipeline({
  blocks,
  byType,
  registry,
  blueprintSnapshots,
  selectedId,
  onSelect,
  onAppend,
  onRemoveLast,
  onReorder,
  onSave,
  onLoad,
}: Props) {
  const [pickerOpen, setPickerOpen] = useState(false);
  const [dragIdx, setDragIdx] = useState<number | null>(null);
  const [dragOverIdx, setDragOverIdx] = useState<number | null>(null);

  const endState = blueprintSnapshots[blocks.length] ?? blueprintSnapshots[0];
  const nextOptions = compatibleBlocksAt(endState, registry, _hierarchy);

  function handleDrop(toIdx: number) {
    if (dragIdx === null || dragIdx === toIdx) return;
    const next = [...blocks];
    const [item] = next.splice(dragIdx, 1);
    next.splice(toIdx, 0, item);
    onReorder(next);
  }

  function clearDrag() {
    setDragIdx(null);
    setDragOverIdx(null);
  }

  return (
    <div className="flex flex-col h-full">
      <div className="flex flex-col gap-1 flex-1 overflow-y-auto">
        {blocks.length === 0 && (
          <p className="text-center text-gray-600 text-sm py-8">
            Add your first block below to start building
          </p>
        )}
        {blocks.map((block, index) => {
          const info = byType.get(block.blockType);
          const isLast = index === blocks.length - 1;
          const isSelected = block.id === selectedId;
          const incomplete = info ? blockHasUnfilledRequired(block, info) : false;
          const isDragging = dragIdx === index;
          const isTarget = dragOverIdx === index && dragIdx !== index;

          return (
            <div
              key={block.id}
              draggable
              onDragStart={() => setDragIdx(index)}
              onDragOver={(e) => { e.preventDefault(); setDragOverIdx(index); }}
              onDrop={() => { handleDrop(index); clearDrag(); }}
              onDragEnd={clearDrag}
              className={`flex items-center gap-2 px-3 py-2.5 rounded border transition-all ${
                isDragging
                  ? "opacity-30 border-dnd-border bg-dnd-panel"
                  : isSelected
                    ? "border-dnd-gold bg-dnd-card"
                    : incomplete
                      ? "border-red-700 bg-dnd-panel hover:border-red-500"
                      : "border-dnd-border bg-dnd-panel hover:border-gray-500"
              } ${isTarget ? "border-t-2 border-t-dnd-gold" : ""}`}
              onClick={() => onSelect(block.id)}
              style={{ cursor: isDragging ? "grabbing" : "grab" }}
            >
              <span className="text-gray-600 flex-shrink-0 select-none" style={{ fontSize: "10px", lineHeight: 1, letterSpacing: "-1px" }}>
                ⠿
              </span>
              <span className="text-xs text-gray-500 w-5 flex-shrink-0">{index + 1}.</span>
              <span className={`flex-1 text-sm ${isSelected ? "text-dnd-gold" : "text-white"}`}>
                {info?.label ?? block.blockType}
              </span>
              {incomplete && !isSelected && (
                <span className="text-xs text-red-400" title="Required fields missing">!</span>
              )}
              {info?.is_ai && (
                <span className="text-xs text-purple-400 bg-purple-900/40 px-1 rounded">AI</span>
              )}
              {isLast && (
                <button
                  className="text-gray-500 hover:text-red-400 text-lg leading-none ml-1"
                  onClick={(e) => {
                    e.stopPropagation();
                    onRemoveLast();
                  }}
                >
                  ×
                </button>
              )}
            </div>
          );
        })}
      </div>

      <div className="flex flex-col gap-1.5 pt-2 border-t border-dnd-border mt-1">
        <div className="flex items-center gap-2">
          <div className="flex-1 h-px bg-dnd-border" />
          <button
            className="text-xs text-gray-500 hover:text-dnd-gold border border-dnd-border hover:border-dnd-gold rounded px-2 py-0.5 transition-colors disabled:opacity-30 disabled:cursor-not-allowed"
            disabled={nextOptions.length === 0}
            onClick={() => setPickerOpen(true)}
          >
            + Add next block
          </button>
          <div className="flex-1 h-px bg-dnd-border" />
        </div>
        <div className="flex gap-2 pb-1">
          <button
            onClick={onSave}
            disabled={blocks.length === 0}
            className="flex-1 flex items-center justify-center gap-1.5 text-xs border border-dnd-border rounded px-2 py-1.5 text-gray-400 hover:text-dnd-gold hover:border-dnd-gold transition-colors disabled:opacity-30 disabled:cursor-not-allowed"
          >
            <span>⬇</span>
            Save pipeline
          </button>
          <label className="flex-1 flex items-center justify-center gap-1.5 text-xs border border-dnd-border rounded px-2 py-1.5 text-gray-400 hover:text-dnd-gold hover:border-dnd-gold transition-colors cursor-pointer">
            <span>⬆</span>
            Load pipeline
            <input type="file" accept=".json" className="hidden" onChange={onLoad} />
          </label>
        </div>
      </div>

      {pickerOpen && (
        <BlockPicker
          available={nextOptions}
          onSelect={(type) => {
            onAppend(type);
            setPickerOpen(false);
          }}
          onClose={() => setPickerOpen(false)}
        />
      )}
    </div>
  );
}
