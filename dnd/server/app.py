from typing import Annotated

from fastapi import FastAPI, Body
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from starlette.responses import RedirectResponse

from dnd.character.blueprint.building_blocks import (
    AnyBuildingBlock,
)
from dnd.server._validate_pipeline import (
    _validate_pipeline,
)
from dnd.character.blueprint.states.state import EmptyBlueprint
from dnd.character.ordered_presentable_character_serializer import (
    OrderedPresentableCharacterSerializer,
)
from dnd.character.presentable_character import (
    PresentableCharacter,
)
from dnd.server.example_generators.example_building_blocks import (
    example_building_blocks,
)
from pydantic import ValidationError

_DEFAULT_SERIALIZER: OrderedPresentableCharacterSerializer = (
    OrderedPresentableCharacterSerializer()
)


def create_app() -> FastAPI:
    app_ = FastAPI()

    @app_.get("/", include_in_schema=False)
    def root() -> RedirectResponse:
        return RedirectResponse(url="/docs")

    @app_.post(
        "/create_character",
        response_model=PresentableCharacter,
    )
    def create_character(
        building_blocks: Annotated[
            tuple[AnyBuildingBlock, ...],
            Body(
                examples=[example_building_blocks()],
            ),
        ],
    ) -> PresentableCharacter:
        try:
            _validate_pipeline(EmptyBlueprint(), building_blocks)
        except TypeError as e:
            raise HTTPException(status_code=422, detail=str(e))
        blueprint = EmptyBlueprint()
        for block in building_blocks:
            blueprint = block.apply(blueprint)  # type: ignore
        try:
            return PresentableCharacter.model_validate(blueprint.model_dump())
        except ValidationError as e:
            raise HTTPException(status_code=422, detail=str(e))

    @app_.post("/convert_character_json")
    def convert_character_json(character: PresentableCharacter) -> JSONResponse:
        return JSONResponse(content=_DEFAULT_SERIALIZER.serialize(character))

    return app_
