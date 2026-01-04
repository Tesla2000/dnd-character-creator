import os
from contextlib import suppress
from typing import Any
from typing import Optional

from dnd_character_creator.character.blueprint.building_blocks import (
    AnyBuildingBlock,
)
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BLOCK_TYPE_FIELD_NAME,
)
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    SerializableBlock,
)
from dnd_character_creator.character.blueprint.simplified_blocks.simplified_blocks import (
    Classes,
)
from dnd_character_creator.character.blueprint.simplified_blocks.simplified_blocks import (
    SimplifiedBlocks,
)
from dnd_character_creator.character.builder import Builder
from dnd_character_creator.character.checkpoint import IncrementChain
from dnd_character_creator.character.checkpoint import IncrementStorage
from dnd_character_creator.character.checkpoint import MemoryStorage
from dnd_character_creator.character.presentable_character import (
    PresentableCharacter,
)
from dnd_character_creator.choices.class_creation.character_class import Class
from dnd_character_creator.server.example_generators.example_building_blocks import (
    example_building_blocks,
)
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.staticfiles import StaticFiles
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from pydantic import Field
from pydantic import TypeAdapter
from pydantic import ValidationError
from starlette.responses import RedirectResponse
from starlette.responses import Response
from subclass_getter import get_unique_subclasses


class _CreateCharacterResponse(BaseModel):
    character: Optional[PresentableCharacter] = None
    increment_chain: IncrementChain
    error: Optional[str] = None


EXAMPLES = (
    SimplifiedBlocks(
        classes=Classes(class_levels={Class.WIZARD: 1})
    ).model_dump(include={"classes", BLOCK_TYPE_FIELD_NAME}, mode="json"),
    SimplifiedBlocks(
        classes=Classes(class_levels={Class.WIZARD: 1})
    ).model_dump(exclude={"blocks"}, mode="json"),
    example_building_blocks().model_dump(mode="json"),
)


class _CreateCharacterRequestSchema(BaseModel):
    building_blocks: dict[str, Any] = Field(examples=list(EXAMPLES))
    increment_chain: dict[str, Any] = Field(examples=[IncrementChain()])


_building_block_creator = TypeAdapter(AnyBuildingBlock)


# LLM configuration factory (lazy initialization to avoid API key issues at import time)
def _get_llm_config(config_id: str) -> ChatOpenAI:
    """Get LLM configuration by ID with lazy initialization.

    Args:
        config_id: Configuration ID (e.g., 'gpt-4o', 'gpt-4o-mini').

    Returns:
        ChatOpenAI instance for the specified configuration.
    """
    configs = {
        "gpt-4o": lambda: ChatOpenAI(model="gpt-4o", temperature=0.7),
        "gpt-4o-mini": lambda: ChatOpenAI(
            model="gpt-4o-mini", temperature=0.3
        ),
        "gpt-3.5-turbo": lambda: ChatOpenAI(
            model="gpt-3.5-turbo", temperature=0.5
        ),
    }
    factory = configs.get(config_id, configs["gpt-4o-mini"])
    return factory()


def _preprocess_building_blocks(data: Any) -> Any:
    """Replace LLM config strings with ChatOpenAI instances.

    Args:
        data: Dictionary, list, or other data structure to preprocess.

    Returns:
        Preprocessed data with LLM config strings replaced by ChatOpenAI objects.
    """
    if isinstance(data, dict):
        result = {}
        for key, value in data.items():
            if key == "llm" and isinstance(value, str):
                # Replace LLM config string with actual ChatOpenAI object
                result[key] = _get_llm_config(value)
            elif isinstance(value, (dict, list)):
                result[key] = _preprocess_building_blocks(value)
            else:
                result[key] = value
        return result
    elif isinstance(data, list):
        return [_preprocess_building_blocks(item) for item in data]
    return data


def _generate_building_blocks_metadata() -> list[dict[str, Any]]:
    """Generate metadata for all building blocks.

    Returns:
        List of building block metadata dictionaries, sorted alphabetically by name.
    """
    blocks_metadata = []
    for block_class in get_unique_subclasses(SerializableBlock):
        fields = {}
        for field_name, field_info in block_class.model_fields.items():
            if field_name == BLOCK_TYPE_FIELD_NAME:
                continue  # Skip discriminator field

            if hasattr(field_info.annotation, "__name__"):
                field_type = field_info.annotation.__name__
            elif hasattr(field_info.annotation, "_name"):
                field_type = field_info.annotation._name
            else:
                field_type = str(field_info.annotation)

            default_value = None
            if field_info.default is not None:
                with suppress(Exception):
                    if isinstance(
                        field_info.default, (str, int, float, bool, list, dict)
                    ):
                        default_value = field_info.default

            fields[field_name] = {
                "type": field_type,
                "description": field_info.description or "",
                "default": default_value,
            }

        assert (
            block_class.__doc__
        ), f"{block_class.__name__} is missing a docstring"

        blocks_metadata.append(
            {
                "block_type": block_class.get_block_type(),
                "name": block_class.__name__,
                "description": block_class.__doc__.strip(),
                "fields": fields,
            }
        )

    blocks_metadata.sort(key=lambda x: x["name"])

    return blocks_metadata


def create_app(storage: IncrementStorage):
    app_ = FastAPI()

    # Generate building blocks metadata once at startup
    blocks_metadata = _generate_building_blocks_metadata()

    @app_.post(
        "/create_character",
        response_model=_CreateCharacterResponse,
        response_model_exclude_unset=True,
    )
    def create_character(
        request: _CreateCharacterRequestSchema, response: Response
    ) -> _CreateCharacterResponse:
        # Preprocess building blocks to replace LLM config strings with ChatOpenAI objects
        preprocessed_blocks = _preprocess_building_blocks(
            request.building_blocks
        )

        errors = []
        try:
            if (
                preprocessed_blocks.get(BLOCK_TYPE_FIELD_NAME)
                == SimplifiedBlocks.get_block_type()
            ):
                building_blocks = SimplifiedBlocks.model_validate(
                    preprocessed_blocks
                )
            else:
                building_blocks = _building_block_creator.validate_python(
                    preprocessed_blocks
                )
        except ValidationError as e:
            errors.append(e)
        try:
            increment_chain = IncrementChain.model_validate(
                request.increment_chain
            )
        except ValidationError as e:
            errors.append(e)
        if errors:
            raise HTTPException(
                status_code=422, detail="\n\n".join(map(str, errors))
            )
        builder = Builder(
            building_blocks=(building_blocks,),
            increment_storage=storage,
        )
        result = builder.build(increment_chain)
        output_increment_chain = storage.load_chain(result.chain_id)
        response.status_code = 422 if result.error else 200
        return _CreateCharacterResponse(
            character=result.character,
            increment_chain=output_increment_chain,
            error=str(result.error) if result.error else None,
        )

    @app_.get("/building_blocks")
    def get_building_blocks():
        """Return metadata about all available building blocks (cached at startup)."""
        return {"building_blocks": blocks_metadata}

    @app_.get("/simplified_templates")
    def get_simplified_templates():
        """Return example SimplifiedBlocks configurations."""

        # Template 1: Level 1 Wizard (minimal config)
        wizard_l1 = SimplifiedBlocks(
            classes=Classes(class_levels={Class.WIZARD: 1})
        )

        # Template 2: Level 3 Wizard
        wizard_l3 = SimplifiedBlocks(
            classes=Classes(class_levels={Class.WIZARD: 3})
        )

        # Template 3: Level 5 Sorcerer
        sorcerer_l5 = SimplifiedBlocks(
            classes=Classes(class_levels={Class.SORCERER: 5})
        )

        return {
            "templates": [
                {
                    "name": "Level 1 Wizard",
                    "description": "Minimal configuration with only class specified",
                    "config": wizard_l1.model_dump(
                        exclude={"blocks"}, exclude_unset=True, mode="json"
                    ),
                    "config_with_defaults": wizard_l1.model_dump(
                        exclude={"blocks"}, mode="json"
                    ),
                },
                {
                    "name": "Level 3 Wizard",
                    "description": "Mid-level wizard with standard defaults",
                    "config": wizard_l3.model_dump(
                        exclude={"blocks"}, exclude_unset=True, mode="json"
                    ),
                    "config_with_defaults": wizard_l3.model_dump(
                        exclude={"blocks"}, mode="json"
                    ),
                },
                {
                    "name": "Level 5 Sorcerer",
                    "description": "Mid-level sorcerer caster",
                    "config": sorcerer_l5.model_dump(
                        exclude={"blocks"}, exclude_unset=True, mode="json"
                    ),
                    "config_with_defaults": sorcerer_l5.model_dump(
                        exclude={"blocks"}, mode="json"
                    ),
                },
            ]
        }

    @app_.post("/format_simplified")
    def format_simplified(request: dict[str, Any], show_defaults: bool = True):
        """Validate and reformat SimplifiedBlocks config with or without defaults.

        This endpoint preserves user changes while toggling default value display.
        """

        try:
            simplified = SimplifiedBlocks.model_validate(request)
            if show_defaults:
                return simplified.model_dump(exclude={"blocks"}, mode="json")
            else:
                return simplified.model_dump(
                    exclude={"blocks"}, exclude_unset=True, mode="json"
                )
        except ValidationError as e:
            raise HTTPException(status_code=422, detail=str(e))

    @app_.get("/health")
    def health():
        return {"status": "ok"}

    @app_.get("/")
    def redirect_doc():
        return RedirectResponse("/docs")

    # Serve static files
    static_dir = os.path.join(os.path.dirname(__file__), "static")
    if os.path.exists(static_dir):
        app_.mount("/static", StaticFiles(directory=static_dir), name="static")

    # Redirect to building blocks page
    @app_.get("/blocks")
    def blocks_page():
        return RedirectResponse("/static/building_blocks.html")

    # Redirect to builder page
    @app_.get("/builder")
    def builder_page():
        return RedirectResponse("/static/builder.html")

    return app_


app = create_app(MemoryStorage())
