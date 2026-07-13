from typing import Annotated

from fastapi import FastAPI, Body
from fastapi import HTTPException
from starlette.responses import RedirectResponse

from dnd.character.blueprint.building_blocks import (
    AnyBuildingBlock,
)
from dnd.character.blueprint.building_blocks.character_converter import (
    CharacterConverter,
)
from dnd.server._validate_pipeline import (
    _validate_pipeline,
)
from dnd.character.blueprint.states.state import EmptyBlueprint
from dnd.character.presentable_character import (
    PresentableCharacter,
)
from dnd.server.example_generators.example_building_blocks import (
    example_building_blocks,
)
from typing import cast


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
            _validate_pipeline(
                EmptyBlueprint(), building_blocks + (CharacterConverter(),)
            )
        except TypeError as e:
            raise HTTPException(status_code=422, detail=str(e))
        blueprint = EmptyBlueprint()
        for block in building_blocks:
            blueprint = block.apply(blueprint)  # type: ignore
        return cast(PresentableCharacter, blueprint)

    return app_


app = create_app()
