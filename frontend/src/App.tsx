import { useState, useMemo } from "preact/hooks";
import { useBlockRegistry } from "./hooks/useBlockRegistry";
import { usePipelineState } from "./hooks/usePipelineState";
import { Pipeline } from "./components/Pipeline";
import { BlockForm } from "./components/BlockForm";
import { CharacterPreview } from "./components/CharacterPreview";
import { buildCharacter } from "./api/buildCharacter";
import { downloadCharacter } from "./api/downloadCharacter";
import { computeBlueprintSnapshots, pipelineMissingFields } from "./utils/blueprintState";
import { blockHasUnfilledRequired } from "./utils/blockValidation";
import type { ArgSpec, CharacterResult } from "./types";
import pipelineMeta from "./data/pipeline-meta.json";

export function App() {
  const { registry, byType } = useBlockRegistry();
  const { blocks, addBlock, removeBlock, updateConfig } = usePipelineState();
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [buildResult, setBuildResult] = useState<CharacterResult | null>(null);
  const [buildError, setBuildError] = useState<string | null>(null);
  const [building, setBuilding] = useState(false);
  const [, setShowResult] = useState(false);

  const blueprintSnapshots = useMemo(
    () =>
      computeBlueprintSnapshots(
        blocks,
        byType,
        pipelineMeta.emptyBlueprintArgs as ArgSpec[],
        pipelineMeta.originHierarchy as Record<string, string[]>
      ),
    [blocks, byType]
  );

  const selectedBlock = blocks.find((b) => b.id === selectedId) ?? null;
  const selectedInfo = selectedBlock ? byType.get(selectedBlock.blockType) : null;

  const hasIncomplete = useMemo(
    () =>
      blocks.some((b) => {
        const info = byType.get(b.blockType);
        return info ? blockHasUnfilledRequired(b, info) : false;
      }),
    [blocks, byType],
  );

  const missingFields = useMemo(() => {
    const finalState = blueprintSnapshots[blueprintSnapshots.length - 1];
    if (!finalState) return [];
    return pipelineMissingFields(
      finalState,
      pipelineMeta.presentableBlueprintArgs as ArgSpec[]
    );
  }, [blueprintSnapshots]);

  async function handleBuild() {
    setBuilding(true);
    setBuildError(null);
    setBuildResult(null);
    try {
      const result = await buildCharacter(blocks);
      if (result.error) {
        setBuildError(result.error);
      } else {
        setBuildResult(result.character);
        setShowResult(true);
      }
    } catch (e) {
      setBuildError(String(e));
    } finally {
      setBuilding(false);
    }
  }

  return (
    <div className="flex flex-col h-screen bg-dnd-dark text-white">
      {/* Header */}
      <header className="flex items-center justify-between px-6 py-3 bg-dnd-panel border-b border-dnd-border flex-shrink-0">
        <div className="flex items-center gap-3">
          <span className="text-2xl">⚔️</span>
          <h1 className="text-xl font-bold text-dnd-gold" style={{ fontFamily: "Inter, sans-serif" }}>
            DnD Character Builder
          </h1>
        </div>
        <div className="flex items-center gap-3">
          <div className="flex flex-col items-end gap-1">
            <button
              onClick={handleBuild}
              disabled={building || blocks.length === 0 || hasIncomplete || missingFields.length > 0}
              className="bg-dnd-red hover:bg-red-700 disabled:opacity-40 disabled:cursor-not-allowed text-white font-semibold px-4 py-1.5 rounded transition-colors text-sm"
            >
              {building ? "Building..." : "Build Character"}
            </button>
            {missingFields.length > 0 && (
              <p className="text-xs text-yellow-500">
                Missing: {missingFields.join(", ")}
              </p>
            )}
          </div>
        </div>
      </header>

      {/* Main layout */}
      <div className="flex flex-1 overflow-hidden">
        {/* Left: Pipeline */}
        <div className="w-72 border-r border-dnd-border flex flex-col flex-shrink-0">
          <div className="px-4 py-2 border-b border-dnd-border">
            <h2 className="text-xs font-semibold text-gray-400 uppercase tracking-wider">
              Pipeline
            </h2>
            <p className="text-xs text-gray-600 mt-0.5">{blocks.length} blocks</p>
          </div>
          <div className="flex-1 overflow-y-auto px-3 py-2">
            <Pipeline
              blocks={blocks}
              byType={byType}
              registry={registry}
              blueprintSnapshots={blueprintSnapshots}
              selectedId={selectedId}
              onSelect={setSelectedId}
              onAppend={(blockType) => {
                const info = byType.get(blockType);
                addBlock(blockType, info?.default_config ?? {});
              }}
              onRemoveLast={() => {
                const last = blocks[blocks.length - 1];
                if (!last) return;
                removeBlock(last.id);
                if (selectedId === last.id) setSelectedId(null);
              }}
            />
          </div>
        </div>

        {/* Center: Config form */}
        <div className="flex-1 flex flex-col overflow-hidden">
          <div className="px-4 py-2 border-b border-dnd-border">
            <h2 className="text-xs font-semibold text-gray-400 uppercase tracking-wider">
              Configuration
            </h2>
          </div>
          <div className="flex-1 overflow-y-auto p-4">
            {selectedBlock && selectedInfo ? (
              <BlockForm
                block={selectedBlock}
                info={selectedInfo}
                onChange={(config) => updateConfig(selectedBlock.id, config)}
              />
            ) : (
              <div className="flex flex-col items-center justify-center h-full text-gray-600">
                <span className="text-4xl mb-3">🎲</span>
                <p className="text-sm">Select a block to configure it</p>
              </div>
            )}
          </div>
        </div>

        {/* Right: Character Preview */}
        <div className="w-72 border-l border-dnd-border flex flex-col flex-shrink-0">
          <div className="px-4 py-2 border-b border-dnd-border flex items-center justify-between">
            <h2 className="text-xs font-semibold text-gray-400 uppercase tracking-wider">
              Character
            </h2>
            {buildResult && (
              <div className="flex items-center gap-2">
                <button
                  className="text-xs text-dnd-gold hover:text-yellow-300"
                  onClick={async () => {
                    const json = await downloadCharacter(buildResult);
                    if (!json) return;
                    const blob = new Blob([json], { type: "application/json" });
                    const url = URL.createObjectURL(blob);
                    const a = document.createElement("a");
                    a.href = url;
                    a.download = `${buildResult.character_data?.name ?? "character"}.json`;
                    a.click();
                    URL.revokeObjectURL(url);
                  }}
                >
                  download
                </button>
                <button
                  className="text-xs text-gray-500 hover:text-white"
                  onClick={() => {
                    setBuildResult(null);
                    setShowResult(false);
                  }}
                >
                  clear
                </button>
              </div>
            )}
          </div>
          <div className="flex-1 overflow-y-auto p-4">
            {buildError && (
              <div className="mb-4 p-3 bg-red-900/30 border border-red-700 rounded text-xs text-red-300 whitespace-pre-wrap">
                {buildError}
              </div>
            )}
            {buildResult ? (
              <CharacterPreview character={buildResult} />
            ) : (
              <div className="flex flex-col items-center justify-center h-full text-gray-600">
                <span className="text-4xl mb-3">📜</span>
                <p className="text-sm text-center">
                  {building ? "Building character..." : "Build your character to see results"}
                </p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
