import { useState, useCallback } from "preact/hooks";
import type { BlockInfo, PipelineBlock } from "../types";
import { INITIAL_PROTOCOLS } from "../data/blockMeta";

let idCounter = 0;
function newId() {
  return `block-${++idCounter}`;
}

export function computeSatisfiedSnapshots(
  blocks: PipelineBlock[],
  byType: Map<string, BlockInfo>
): Set<string>[] {
  const snapshots: Set<string>[] = [new Set(INITIAL_PROTOCOLS)];
  for (const block of blocks) {
    const prev = snapshots[snapshots.length - 1];
    const meta = byType.get(block.blockType);
    const next = new Set(prev);
    if (meta) {
      const valid =
        meta.requires.every((p) => prev.has(p)) && meta.conflicts.every((p) => !prev.has(p));
      if (valid) {
        meta.provides.forEach((p) => next.add(p));
      }
    }
    snapshots.push(next);
  }
  return snapshots;
}

export function availableAt(
  index: number,
  snapshots: Set<string>[],
  registry: BlockInfo[]
): BlockInfo[] {
  const satisfied = snapshots[index] ?? new Set(INITIAL_PROTOCOLS);
  return registry.filter(
    (meta) =>
      meta.requires.every((p) => satisfied.has(p)) &&
      meta.conflicts.every((p) => !satisfied.has(p))
  );
}

export function usePipelineState() {
  const [blocks, setBlocks] = useState<PipelineBlock[]>([]);

  const addBlock = useCallback((blockType: string, config: Record<string, unknown> = {}) => {
    setBlocks((prev) => [...prev, { id: newId(), blockType, config }]);
  }, []);

  const removeBlock = useCallback((id: string) => {
    setBlocks((prev) => prev.filter((b) => b.id !== id));
  }, []);

  const updateConfig = useCallback((id: string, config: Record<string, unknown>) => {
    setBlocks((prev) => prev.map((b) => (b.id === id ? { ...b, config } : b)));
  }, []);

  const moveBlock = useCallback((fromIndex: number, toIndex: number) => {
    setBlocks((prev) => {
      const next = [...prev];
      const [item] = next.splice(fromIndex, 1);
      next.splice(toIndex, 0, item);
      return next;
    });
  }, []);

  const reorderBlocks = useCallback((newOrder: PipelineBlock[]) => {
    setBlocks(newOrder);
  }, []);

  return { blocks, addBlock, removeBlock, updateConfig, moveBlock, reorderBlocks };
}
