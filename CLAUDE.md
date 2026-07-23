# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Filip's assistant for SWE tasks. Fast, pedantic, iterative. No big features unsupervised.

# Commands

Run backend (requires OPENAI_API_KEY):
```
OPENAI_API_KEY=... uv run uvicorn dnd.server.app:app --port 8000 --reload
```

Run tests:
```
uv run pytest -m unit                                                    # fast, no I/O
uv run pytest -m integration                                             # multi-component, no AI
uv run pytest tests/path/test_foo.py::TestClass::test_name              # single test
```
Smoke/e2e markers require a live OPENAI_API_KEY.

Run frontend dev server (proxies API calls to localhost:8000):
```
cd frontend && npm run dev
```

Regenerate frontend block metadata from Python types (run from `frontend/`):
```
python3 scripts/generate_blocks.py
```

# Architecture

## Blueprint pipeline

Character creation is modeled as a typed pipeline. `Blueprint` (`dnd/character/blueprint/states/state.py`) is a Pydantic generic with 19 type parameters tracking what has been set (race, stats, health, class levels, character data, etc.). Each `BuildingBlock` subclass declares `apply(self, blueprint: SomeBlueprint) -> OtherBlueprint`, narrowing one or more type parameters on output.

The server (`dnd/server/app.py`) receives an ordered list of building blocks as JSON, validates the chain at the type level via `dnd/server/_validate_pipeline.py`, then executes `block.apply(blueprint)` in sequence to produce a `PresentableCharacter`.

Building blocks live under `dnd/character/blueprint/building_blocks/`. Most choices (spells, feats, skills, race, stats) have three variants: `ai.py` (LLM-driven), `random.py`, and a deterministic strategy. Level-up logic is split per class and subclass under `building_blocks/level_up/<class>/`.

## Frontend

A Preact + TypeScript SPA (`frontend/src/`) lets users compose a pipeline by drag-and-dropping building blocks, configure each block's fields, then call `POST /create_character`. Block metadata (field names, types, allowed values, required/optional) is generated from Python types by `frontend/scripts/generate_blocks.py` into `frontend/src/data/pipeline-meta.json`. The dev server proxies `/create_character` and `/convert_character_json` to `localhost:8000`.

# Hard rules (always apply)

- Never use functions. Only methods on classes.
- Never ignore mypy errors -- report them immediately.
- Never use local imports unless explicitly allowed.
- Never use `Any` in type hints -- narrow to a specific type, `object`, or `Union`.
- Prefer Enum over `Literal` with more than one element; only use a multi-element `Literal` when Enum is not viable (e.g. matching an external API's exact string constants, or a Pydantic discriminator field).
- Avoid a generic method whose type parameter isn't reflected in its return type, unless there's a valid reason (e.g. constraining two or more parameters to agree with each other); otherwise use the bound type directly instead of a TypeVar.
- Never use # type: ignore[import-not-found] -- add package or create stubs.
- Never use # pragma: no cover unless user explicitly allows it.
- Never commit or git add unless asked.
- Run mypy (and pre-commit) after non-trivial changes to `dnd/` as standard validation -- no need to wait to be asked.
- Use uv add to add dependencies. Never edit pyproject.toml or .pre-commit-config.yaml manually.
- Always type hint arguments and return type.
- Use only ASCII punctuation. No em dashes, curly quotes, ellipsis characters.
- When mentioning files always use full path from root with line number: full_path:69
- Present all changes to a file in one approval -- never split imports from code.
- Use timeouts or run in background with a check for long-running commands.
- Don't implement in plan mode -- wait for approval, then execute.
- Save pre-commit output and read it instead of re-running: `pre-commit run --all-files 2>&1 | tee pre-commit-output.txt`
- Save test output and read it instead of re-running with different config to see other lines.

# Skills (load on demand)

Use /python-style for: comprehensions, defaultdict, staticmethod/classmethod, imports, typing, module exports.
Use /pydantic for: frozen models, Annotated validators, cross-field defaults, InstanceOf fields.
Use /services for: service creation pattern, types.py, __init__.py exports, PydanticLogger.
Use /exception-handling for: return-value error pattern, specific exception types, no raise.
Use /testing for: patch.object format, autospec, coverage, saving test output.
Use /cli for: BaseSettings CLI pattern, cli_cmd entry point.

# Knowledge base

Full rule documentation with examples lives at:
~/PassionProjects/ai-knowledge/topics/

Index: ~/PassionProjects/ai-knowledge/index.md

# How to update rules

1. Edit the relevant skill file in ~/.claude/skills/<name>/SKILL.md
2. Mirror the change in ~/PassionProjects/ai-knowledge/topics/<domain>/<file>.md
3. Run: python3 ~/PassionProjects/ai-knowledge/scripts/rebuild_index.py
4. If the rule must always load (not just on demand), add it to the Hard rules section above.
