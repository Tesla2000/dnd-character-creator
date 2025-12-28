from typing import Any
from typing import Optional

from dnd_character_creator.character.blueprint.building_blocks import (
    AnyBuildingBlock,
)
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BLOCK_TYPE_FIELD_NAME,
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
from pydantic import BaseModel
from pydantic import Field
from pydantic import TypeAdapter
from pydantic import ValidationError
from starlette.responses import RedirectResponse
from starlette.responses import Response


class _CreateCharacterResponse(BaseModel):
    character: Optional[PresentableCharacter] = None
    increment_chain: IncrementChain
    error: Optional[str] = None


class _CreateCharacterRequestSchema(BaseModel):
    building_blocks: dict[str, Any] = Field(
        examples=[
            SimplifiedBlocks(
                classes=Classes(class_levels={Class.WIZARD: 1})
            ).model_dump(exclude={"blocks"}),
            SimplifiedBlocks(
                classes=Classes(class_levels={Class.WIZARD: 1})
            ).model_dump(include={"classes"}),
            example_building_blocks().model_dump(),
        ]
    )
    increment_chain: dict[str, Any] = Field(examples=[IncrementChain()])


_building_block_creator = TypeAdapter(AnyBuildingBlock)


def create_app(storage: IncrementStorage):
    app_ = FastAPI()

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

    @app_.get("/health")
    def health():
        return {"status": "ok"}

    @app_.get("/")
    def redirect_doc():
        return RedirectResponse("/docs")

    return app_


app = create_app(MemoryStorage())
