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
        errors = []
        try:
            if (
                request.building_blocks.get(BLOCK_TYPE_FIELD_NAME)
                == SimplifiedBlocks.get_block_type()
            ):
                building_blocks = SimplifiedBlocks.model_validate(
                    request.building_blocks
                )
            else:
                building_blocks = _building_block_creator.validate_python(
                    request.building_blocks
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

    return app_


app = create_app(MemoryStorage())
