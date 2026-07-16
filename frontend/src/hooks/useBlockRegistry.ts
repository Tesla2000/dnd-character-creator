import { useState, useEffect, useMemo } from "preact/hooks";
import type { BlockInfo } from "../types";
import generatedBlocks from "../data/blocks-generated.json";

let cached: BlockInfo[] | null = null;

const HIDDEN_BLOCK_TYPES = new Set(["null_block"]);

function buildRegistry(): BlockInfo[] {
  return (generatedBlocks as BlockInfo[]).filter((b) => !HIDDEN_BLOCK_TYPES.has(b.type));
}

export function useBlockRegistry() {
  const [registry, setRegistry] = useState<BlockInfo[]>(() => {
    if (!cached) cached = buildRegistry();
    return cached;
  });
  const [loading] = useState(false);

  useEffect(() => {
    if (!cached) {
      cached = buildRegistry();
      setRegistry(cached);
    }
  }, []);

  const byType = useMemo(
    () => new Map<string, BlockInfo>(registry.map((b) => [b.type, b])),
    [registry],
  );

  return { registry, loading, byType };
}
