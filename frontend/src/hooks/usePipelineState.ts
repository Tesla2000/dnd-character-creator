import { useState, useCallback } from "preact/hooks";
import type { PipelineBlock } from "../types";

let idCounter = 0;
function newId() {
  return `block-${++idCounter}`;
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

  const loadBlocks = useCallback((entries: { type: string; [k: string]: unknown }[]) => {
    setBlocks(entries.map(({ type, ...config }) => ({
      id: newId(),
      blockType: type,
      config,
    })));
  }, []);

  return { blocks, addBlock, removeBlock, updateConfig, moveBlock, reorderBlocks, loadBlocks };
}
