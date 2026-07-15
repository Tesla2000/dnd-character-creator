import type { BuildResult, PipelineBlock } from "../types";

export async function buildCharacter(blocks: PipelineBlock[]): Promise<BuildResult> {
  const building_blocks = blocks.map((b) => ({
    type: b.blockType,
    ...b.config,
  }));

  const res = await fetch("/create_character", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(building_blocks),
  });

  const text = await res.text();
  if (!res.ok) {
    if (!text) return { character: null, error: `HTTP ${res.status}` };
    try {
      const parsed = JSON.parse(text) as {
        detail?: string | Array<{ msg: string; loc?: unknown[] }>;
      };
      const detail = parsed.detail;
      if (typeof detail === "string") {
        return { character: null, error: detail };
      }
      if (Array.isArray(detail)) {
        const msgs = detail.map((e) =>
          e.loc ? `${e.loc.slice(2).join(".")}: ${e.msg}` : e.msg,
        );
        return { character: null, error: msgs.join("\n") };
      }
      return { character: null, error: text };
    } catch {
      return { character: null, error: text };
    }
  }
  if (!text) {
    return { character: null, error: "Empty response from server" };
  }
  return { character: JSON.parse(text) as BuildResult["character"], error: null };
}
