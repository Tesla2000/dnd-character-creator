import type { CharacterResult } from "../types";

export async function downloadCharacter(character: CharacterResult): Promise<string | null> {
  const res = await fetch("/convert_character_json", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(character),
  });

  if (!res.ok) return null;
  return res.text();
}
