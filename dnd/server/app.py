import logging
import traceback
from typing import TYPE_CHECKING

from dnd.character.blueprint.building_blocks import (
    AnyBuildingBlock,
)
from dnd.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd.character.blueprint.building_blocks.character_converter import (
    CharacterConverter,
)
from dnd.character.blueprint.state import EmptyBlueprint
from dnd.character.presentable_character import (
    PresentableCharacter,
)
from dnd.server.example_generators.example_building_blocks import (
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

_logger = logging.getLogger(__name__)


class _CreateCharacterResponse(BaseModel):
    character: PresentableCharacter | None = None
    error: str | None = None


_building_blocks_creator: TypeAdapter[tuple[AnyBuildingBlock, ...]] = TypeAdapter(
    tuple[AnyBuildingBlock, ...]
)

EXAMPLES = (
    _building_blocks_creator.dump_python(example_building_blocks(), mode="json"),
)


class _CreateCharacterRequestSchema(BaseModel):
    building_blocks: list[dict[str, object]] = Field(examples=list(EXAMPLES))


def create_app() -> FastAPI:
    app_ = FastAPI()

    @app_.get("/", include_in_schema=False)
    def root() -> RedirectResponse:
        return RedirectResponse(url="/docs")

    @app_.post(
        "/create_character",
        response_model=_CreateCharacterResponse,
    )
    def create_character(
        request: _CreateCharacterRequestSchema, response: Response
    ) -> _CreateCharacterResponse:
        if TYPE_CHECKING:
            return _CreateCharacterResponse()
        try:
            building_blocks = _building_blocks_creator.validate_python(
                request.building_blocks
            )
        except ValidationError as e:
            raise HTTPException(status_code=422, detail=str(e)) from e
        try:
            blueprint = EmptyBlueprint()
            for block in building_blocks:
                blueprint = block.apply(blueprint)
            character = CharacterConverter().apply(blueprint)
            response.status_code = 200
            return _CreateCharacterResponse(character=character, error=None)
        except Exception as e:
            _logger.error(traceback.format_exc())
            response.status_code = 422
            return _CreateCharacterResponse(character=None, error=str(e))

    return app_


app = create_app()
