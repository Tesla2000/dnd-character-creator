import type { ArgSpec, BlockInfo, BlueprintState, PipelineBlock } from "../types";

function argCompatible(current: ArgSpec, expected: ArgSpec): boolean {
  if (expected.kind === "free") return true;
  // A union current must satisfy expected with ALL members (subtype check: A|B <: C iff A<:C and B<:C)
  if (current.kind === "union") return current.members.every((m) => argCompatible(m, expected));
  // A union expected is satisfied by current if ANY member matches
  if (expected.kind === "union") return expected.members.some((m) => argCompatible(current, m));
  if (expected.kind === "type" && current.kind === "literal") return true;
  if (current.kind !== expected.kind) return false;
  if (current.kind === "none") return true;
  if (current.kind === "type" && expected.kind === "type") return current.name === expected.name;
  if (current.kind === "literal" && expected.kind === "literal") {
    const expectedSet = new Set(expected.values.map(String));
    return current.values.every((v) => expectedSet.has(String(v)));
  }
  if (current.kind === "generic" && expected.kind === "generic") {
    if (current.origin !== expected.origin) return false;
    return expected.args.every((e, i) => {
      const c = current.args[i];
      return c === undefined || argCompatible(c, e);
    });
  }
  return false;
}

function isSuborigin(
  current: string,
  expected: string,
  hierarchy: Record<string, string[]>
): boolean {
  return current === expected || (hierarchy[current] ?? []).includes(expected);
}

function isBlockCompatibleAt(
  sig: BlockInfo["blueprint_sig"],
  state: BlueprintState,
  hierarchy: Record<string, string[]>
): boolean {
  if (!sig || !sig.input) return true;
  const { input } = sig;
  if (!isSuborigin(state.origin, input.origin, hierarchy)) return false;
  const pairCount = Math.min(state.args.length, input.args.length);
  for (let j = 0; j < pairCount; j++) {
    if (!argCompatible(state.args[j], input.args[j])) return false;
  }
  return true;
}

function mergeArg(output: ArgSpec, prev: ArgSpec): ArgSpec {
  if (output.kind === "free") return prev;
  if (
    output.kind === "generic" &&
    prev.kind === "generic" &&
    output.origin === prev.origin
  ) {
    return {
      kind: "generic",
      origin: output.origin,
      args: output.args.map((a, i) => mergeArg(a, prev.args[i] ?? a)),
    };
  }
  return output;
}

export function computeBlueprintSnapshots(
  blocks: PipelineBlock[],
  byType: Map<string, BlockInfo>,
  emptyArgs: ArgSpec[],
  originHierarchy: Record<string, string[]>
): BlueprintState[] {
  const snapshots: BlueprintState[] = [{ origin: "Blueprint", args: emptyArgs }];

  for (const block of blocks) {
    const prev = snapshots[snapshots.length - 1];
    const info = byType.get(block.blockType);
    const sig = info?.blueprint_sig;

    if (!sig || !sig.output || !isBlockCompatibleAt(sig, prev, originHierarchy)) {
      snapshots.push(prev);
      continue;
    }

    const output = sig.output;
    const newArgs = output.args.map((a, j) =>
      mergeArg(a, j < prev.args.length ? prev.args[j] : a)
    );
    snapshots.push({ origin: output.origin, args: newArgs });
  }

  return snapshots;
}

export function compatibleBlocksAt(
  state: BlueprintState,
  registry: BlockInfo[],
  originHierarchy: Record<string, string[]>
): BlockInfo[] {
  return registry.filter((info) => isBlockCompatibleAt(info.blueprint_sig, state, originHierarchy));
}

const BLUEPRINT_ARG_NAMES = [
  "race", "stats", "health",
  "stat choices remaining", "skill choices remaining",
  "wizard level", "sorcerer level", "fighter level", "barbarian level",
  "rogue level", "cleric level", "druid level", "paladin level",
  "ranger level", "monk level", "bard level", "warlock level",
  "artificer level", "character data",
];

export function pipelineMissingFields(
  finalState: BlueprintState,
  presentableArgs: ArgSpec[]
): string[] {
  const missing: string[] = [];
  const limit = Math.min(finalState.args.length, presentableArgs.length);
  for (let i = 0; i < limit; i++) {
    if (!argCompatible(finalState.args[i], presentableArgs[i])) {
      missing.push(BLUEPRINT_ARG_NAMES[i] ?? `arg[${i}]`);
    }
  }
  return missing;
}
