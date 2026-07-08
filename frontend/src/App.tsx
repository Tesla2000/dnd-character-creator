import { useState, useMemo, useCallback } from "preact/hooks";
import { useBlockRegistry } from "./hooks/useBlockRegistry";
import { usePipelineState, computeSatisfiedSnapshots } from "./hooks/usePipelineState";
import { Pipeline } from "./components/Pipeline";
import { BlockForm } from "./components/BlockForm";
import { CharacterPreview } from "./components/CharacterPreview";
import { buildCharacter } from "./api/buildCharacter";
import type { CharacterResult, PipelineBlock } from "./types";

export function App() {
  const { registry, byType } = useBlockRegistry();
  const { blocks, removeBlock, updateConfig, reorderBlocks } = usePipelineState();
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [buildResult, setBuildResult] = useState<CharacterResult | null>(null);
  const [buildError, setBuildError] = useState<string | null>(null);
  const [building, setBuilding] = useState(false);
  const [, setShowResult] = useState(false);

  const snapshots = useMemo(
    () => computeSatisfiedSnapshots(blocks, byType),
    [blocks, byType]
  );

  const selectedBlock = blocks.find((b) => b.id === selectedId) ?? null;
  const selectedInfo = selectedBlock ? byType.get(selectedBlock.blockType) : null;

  const handleAddAtIndex = useCallback(
    (blockType: string, atIndex: number): void => {
      // We simulate insert by adding at end then moving
      const newId = `block-insert-${Date.now()}`;
      const newBlock: PipelineBlock = { id: newId, blockType, config: {} };
      const next = [...blocks];
      next.splice(atIndex, 0, newBlock);
      reorderBlocks(next);
      setSelectedId(newId);
    },
    [blocks, reorderBlocks]
  );

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

  const invalidCount = blocks.filter((b, i) => {
    const meta = byType.get(b.blockType);
    if (!meta) return false;
    const prev = snapshots[i] ?? new Set();
    return (
      !meta.requires.every((p) => prev.has(p)) || meta.conflicts.some((p) => prev.has(p))
    );
  }).length;

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
          {invalidCount > 0 && (
            <span className="text-xs text-red-400 bg-red-900/30 border border-red-700 rounded px-2 py-1">
              {invalidCount} block{invalidCount > 1 ? "s" : ""} with unmet requirements
            </span>
          )}
          <button
            onClick={handleBuild}
            disabled={building || blocks.length === 0}
            className="bg-dnd-red hover:bg-red-700 disabled:opacity-40 disabled:cursor-not-allowed text-white font-semibold px-4 py-1.5 rounded transition-colors text-sm"
          >
            {building ? "Building..." : "Build Character"}
          </button>
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
              snapshots={snapshots}
              selectedId={selectedId}
              onSelect={setSelectedId}
              onAdd={handleAddAtIndex}
              onRemove={(id) => {
                removeBlock(id);
                if (selectedId === id) setSelectedId(null);
              }}
              onReorder={reorderBlocks}
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
              <button
                className="text-xs text-gray-500 hover:text-white"
                onClick={() => {
                  setBuildResult(null);
                  setShowResult(false);
                }}
              >
                clear
              </button>
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
