# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a D&D 5e character creator that uses LLMs (via LangChain and OpenAI) to generate characters and outputs them as formatted PDF character sheets using LaTeX. The project supports both single character generation and batch generation.

## Common Development Commands

### Setup
```bash
make setup  # Initialize project: install dependencies, git init, and pre-commit hooks
uv sync  # Install dependencies only
```

### Running
```bash
python main.py  # Run character generation
```

### Testing
```bash
pytest tests/  # Run all tests
pytest tests/test_fighter.py  # Run specific test file
```

### Code Quality
```bash
pre-commit run --all-files  # Run all pre-commit hooks manually
```

Pre-commit hooks automatically run on commit and include:
- black (formatter with --line-length 79)
- reorder-python-imports (with __future__ annotations)
- autoflake (removes unused imports)
- flake8 (linter, ignoring E203, W503, E501)

### Docker
```bash
docker build -t dnd_creator .
docker run -it dnd_creator /bin/sh
python main.py
```

## Architecture Overview

### Character Generation Pipeline

The character generation follows a multi-stage pipeline:

1. **Base Character Generation** (`main.py` → `character_base.py`)
   - Uses LLM with structured output to create base character attributes
   - Supports single or batch generation (n_instances)
   - Takes user description and pre-defined fields from Config

2. **Details Filling** (`character_details_filler.py`)
   - Enriches base character with additional details
   - Uses separate LLM (typically cheaper model like gpt-4o-mini)
   - Wraps character in CharacterWrapper for further processing

3. **PDF Generation** (`pdf_creator/`)
   - Updates LaTeX prototype with character data
   - Runs LuaLaTeX to compile PDF
   - Removes blank pages and moves output to characters_output/

### Builder Pattern (New Architecture - builder-refactor branch)

The project is transitioning to a builder pattern for character creation:

- **Builder** (`character/builder.py`): Orchestrates character construction
- **Blueprint** (`character/blueprint/blueprint.py`): Dynamic model based on Character with all optional fields
- **BuildingBlock** (`character/blueprint/building_blocks/`): Abstract interface for modifying blueprints
  - `ClassAssigner`: Assigns character classes
  - Additional blocks can be created by extending BuildingBlock ABC

The builder pattern allows composable character construction:
```python
builder = Builder(building_blocks=[ClassAssigner(class_=Class.FIGHTER)])
builder.add(some_building_block)
character = builder.build()  # Returns Character instance
```

### Data Model Hierarchy

**Character** (`character/character.py`):
- Core character model with all required fields
- Includes: sex, backstory, level, age, classes (multiclass support), race, stats, equipment, spells
- Uses Pydantic BaseModel for validation

**Config** (`config.py`):
- Central configuration using pydantic-settings
- Paths to scraped data (races, classes, spells, feats, backgrounds)
- LLM model settings (character_llm, details_llm with separate temperatures)
- Character constraints and preferences
- Validates sub-race and sub-class selections

**Spells** (`character/spells.py`):
- Spell management for the character

### Data Sources

The project uses web-scraped D&D content stored in `wiki_scraper/scraped_data/`:

- **abilities/**: Race abilities organized by race name
- **sub_races/**: Sub-race data organized by race and source book (e.g., MordenkainenPresentsMonstersoftheMultiverse)
- **main_class/**: Class features and progression
- **main_class_abilities/**: Class-specific abilities
- **sub_class_abilities/**: Subclass features
- **spells/**: Spell descriptions and mechanics
- **feats/**: Available feats
- **background/**: Character backgrounds

Each race/class can have multiple versions from different source books (DNDResource enum).

### Key Choices System

The `choices/` directory contains enums and models for character options:

- **race_creation/**: Race, sub-races, and racial abilities
- **class_creation/**: Character classes and subclasses
- **stats_creation/**: Ability scores (Statistic enum: STR, DEX, CON, INT, WIS, CHA) and creation methods
- **spell_slots/**: Spell level classes (Cantrip, FirstLevel, etc.)
- **equipment_creation/**: Armor and weapons
- **feat_creation/**: Character feats
- **background_creatrion/**: Backgrounds (note: typo in directory name)
- **fighting_styles/**: Combat styles (e.g., Defense, Dueling)
- **battle_maneuvers/**: Fighter maneuvers
- **invocations/**: Warlock eldritch invocations

### LaTeX PDF Generation

The PDF creator uses a custom D&D template:

- **prototype.tex**: Base LaTeX template for character sheets
- **dndbook.cls, dnd.sty, dndtemplate.sty**: Custom D&D styling
- **update_prototype.py**: Fills template with character data
- **run_lunatex.py**: Compiles LaTeX using LuaLaTeX
- **remove_blank_page.py**: Post-processes PDF to remove artifacts

Requires LuaLaTeX installed on system.

## Important Implementation Details

### LLM Integration

Two separate LLMs are used:
- **character_llm**: Main model for base character generation (default: gpt-4o, temp: 0.7)
- **details_llm**: Cheaper model for details (default: gpt-4o-mini, temp: 0)

Both use LangChain's `with_structured_output()` to ensure Pydantic model compliance.

### Multiclass Support

Characters support multiclassing via `classes: dict[Class, PositiveInt]` where:
- Keys are Class enums
- Values are levels in that class
- Total level is sum of all class levels (capped at 20)

### Configuration Loading

Config supports multiple sources (priority order):
1. Command-line arguments
2. Configuration file (TOML)
3. Environment variables (.env file loaded via python-dotenv)
4. Default values in Config class

Use `parse_arguments()` and `create_config_with_args()` helpers for proper initialization.

### Validators

Config includes important validators:
- `_validate_subrace`: Ensures sub_race matches selected main_race
- `_validate_subclass`: Ensures main_class is set if sub_class is specified

### Blueprint System

The Blueprint is dynamically created from Character model with all fields made optional. This allows incremental building:

```python
Blueprint = create_model("Blueprint", __base__=Character, **{
    field_name: _make_field_optional(field_info)
    for field_name, field_info in Character.model_fields.items()
})
```

BuildingBlocks modify the blueprint in-place via `apply(blueprint: Blueprint) -> None`.

## Project Dependencies

Key dependencies:
- **langchain & langchain-openai**: LLM integration
- **pydantic & pydantic-settings**: Data validation and config management
- **beautifulsoup4**: Web scraping D&D content
- **pypdf2**: PDF manipulation
- **uv**: Fast Python package installer and dependency manager
- **pre-commit**: Code quality automation
- **pytest**: Testing framework

## Notes

- Python 3.11+ required
- OpenAI API key needed (loaded from environment)
- LuaLaTeX must be installed for PDF generation
- The project is currently on `builder-refactor` branch implementing the builder pattern
- Directory name typo exists: `background_creatrion` should be `background_creation` (not fixed to maintain compatibility)