import { useState, useEffect } from "preact/hooks";
import type { BlockInfo } from "../types";
import generatedBlocks from "../data/blocks-generated.json";
import { BLOCK_META } from "../data/blockMeta";

let cached: BlockInfo[] | null = null;

function buildRegistry(): BlockInfo[] {
  return (generatedBlocks as Omit<BlockInfo, "requires" | "provides" | "conflicts">[]).map(
    (b) => {
      const meta = BLOCK_META[b.type] ?? { requires: [], provides: [], conflicts: [] };
      return { ...b, ...meta };
    }
  );
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

  const byType = new Map<string, BlockInfo>(registry.map((b) => [b.type, b]));

  return { registry, loading, byType };
}
