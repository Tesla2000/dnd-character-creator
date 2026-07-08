import { useState } from "preact/hooks";
import {
  DndContext,
  closestCenter,
  KeyboardSensor,
  PointerSensor,
  useSensor,
  useSensors,
  type DragEndEvent,
} from "@dnd-kit/core";
import {
  SortableContext,
  sortableKeyboardCoordinates,
  verticalListSortingStrategy,
  useSortable,
} from "@dnd-kit/sortable";
import { CSS } from "@dnd-kit/utilities";
import type { BlockInfo, PipelineBlock } from "../types";
import { BlockPicker } from "./BlockPicker";

interface SortableBlockProps {
  block: PipelineBlock;
  index: number;
  info: BlockInfo | undefined;
  isSelected: boolean;
  isValid: boolean;
  onSelect: () => void;
  onRemove: () => void;
}

function SortableBlock({
  block,
  index,
  info,
  isSelected,
  isValid,
  onSelect,
  onRemove,
}: SortableBlockProps) {
  const { attributes, listeners, setNodeRef, transform, transition, isDragging } = useSortable({
    id: block.id,
  });

  const style = {
    transform: CSS.Transform.toString(transform),
    transition,
    opacity: isDragging ? 0.5 : 1,
  };

  return (
    <div ref={setNodeRef} style={style}>
      <div
        className={`flex items-center gap-2 px-3 py-2.5 rounded border cursor-pointer transition-all ${
          isSelected
            ? "border-dnd-gold bg-dnd-card"
            : "border-dnd-border bg-dnd-panel hover:border-gray-500"
        } ${!isValid ? "border-red-700" : ""}`}
        onClick={onSelect}
      >
        <span
          className="text-gray-500 cursor-grab active:cursor-grabbing text-sm select-none"
          {...(attributes as unknown as Record<string, unknown>)}
          {...(listeners as unknown as Record<string, unknown> | undefined)}
        >
          ⠿
        </span>
        <span className="text-xs text-gray-500 w-5 flex-shrink-0">{index + 1}.</span>
        <span className={`flex-1 text-sm ${isSelected ? "text-dnd-gold" : "text-white"}`}>
          {info?.label ?? block.blockType}
        </span>
        {!isValid && <span title="Requirements not met">⚠️</span>}
        {info?.is_ai && (
          <span className="text-xs text-purple-400 bg-purple-900/40 px-1 rounded">AI</span>
        )}
        <button
          className="text-gray-500 hover:text-red-400 text-lg leading-none ml-1"
          onClick={(e) => {
            e.stopPropagation();
            onRemove();
          }}
        >
          ×
        </button>
      </div>
    </div>
  );
}

interface InsertButtonProps {
  registry: BlockInfo[];
  onAdd: (blockType: string) => void;
}

function InsertButton({ registry, onAdd }: InsertButtonProps) {
  const [open, setOpen] = useState(false);

  return (
    <div className="flex items-center gap-2 py-1">
      <div className="flex-1 h-px bg-dnd-border" />
      <button
        className="text-xs text-gray-500 hover:text-dnd-gold border border-dnd-border hover:border-dnd-gold rounded px-2 py-0.5 transition-colors"
        onClick={() => setOpen(true)}
      >
        + Add block
      </button>
      <div className="flex-1 h-px bg-dnd-border" />
      {open && (
        <BlockPicker
          available={registry}
          onSelect={(type) => {
            onAdd(type);
            setOpen(false);
          }}
          onClose={() => setOpen(false)}
        />
      )}
    </div>
  );
}

interface Props {
  blocks: PipelineBlock[];
  byType: Map<string, BlockInfo>;
  registry: BlockInfo[];
  snapshots: Set<string>[];
  selectedId: string | null;
  onSelect: (id: string) => void;
  onAdd: (blockType: string, atIndex: number) => void;
  onRemove: (id: string) => void;
  onReorder: (newOrder: PipelineBlock[]) => void;
}


export function Pipeline({
  blocks,
  byType,
  registry,
  snapshots,
  selectedId,
  onSelect,
  onAdd,
  onRemove,
  onReorder,
}: Props) {
  const sensors = useSensors(
    useSensor(PointerSensor),
    useSensor(KeyboardSensor, { coordinateGetter: sortableKeyboardCoordinates })
  );

  function handleDragEnd(event: DragEndEvent) {
    const { active, over } = event;
    if (over && active.id !== over.id) {
      const oldIndex = blocks.findIndex((b) => b.id === active.id);
      const newIndex = blocks.findIndex((b) => b.id === over.id);
      const next = [...blocks];
      const [item] = next.splice(oldIndex, 1);
      next.splice(newIndex, 0, item);
      onReorder(next);
    }
  }

  function isBlockValid(index: number, block: PipelineBlock): boolean {
    const meta = byType.get(block.blockType);
    if (!meta) return true;
    const prev = snapshots[index] ?? new Set();
    return (
      meta.requires.every((p) => prev.has(p)) && meta.conflicts.every((p) => !prev.has(p))
    );
  }

  return (
    <div className="flex flex-col h-full">
      <InsertButton
        registry={registry}
        onAdd={(type) => onAdd(type, 0)}
      />

      <DndContext sensors={sensors} collisionDetection={closestCenter} onDragEnd={handleDragEnd}>
        <SortableContext items={blocks.map((b) => b.id)} strategy={verticalListSortingStrategy}>
          <div className="flex flex-col gap-1">
            {blocks.map((block, index) => (
              <div key={block.id}>
                <SortableBlock
                  block={block}
                  index={index}
                  info={byType.get(block.blockType)}
                  isSelected={block.id === selectedId}
                  isValid={isBlockValid(index, block)}
                  onSelect={() => onSelect(block.id)}
                  onRemove={() => onRemove(block.id)}
                />
                <InsertButton
                  registry={registry}
                  onAdd={(type) => onAdd(type, index + 1)}
                />
              </div>
            ))}
          </div>
        </SortableContext>
      </DndContext>

      {blocks.length === 0 && (
        <p className="text-center text-gray-600 text-sm py-8">
          Add your first block above to start building
        </p>
      )}
    </div>
  );
}
