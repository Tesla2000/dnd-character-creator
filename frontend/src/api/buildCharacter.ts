import type { BuildResult, PipelineBlock } from "../types";

export async function buildCharacter(blocks: PipelineBlock[]): Promise<BuildResult> {
  const building_blocks = blocks.map((b) => ({
    type: b.blockType,
    ...b.config,
  }));

  const res = await fetch("/create_character", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      building_blocks,
      increment_chain: {},
    }),
  });

  const data = await res.json();
  if (!res.ok && res.status !== 422) {
    return { character: null, error: data.detail ?? "Unknown error" };
  }
  return { character: data.character ?? null, error: data.error ?? null };
}
