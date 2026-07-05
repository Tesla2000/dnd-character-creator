from dnd.character.blueprint.building_blocks import (
    AnyBuildingBlock,
)
from dnd.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd.character.blueprint.building_blocks.building_block import (
    CombinedBlock,
)
from dnd.character.blueprint.state import BlueprintProtocol
from dnd.character.delta.delta import Delta
from dnd.character.builder import Builder
from dnd.character.checkpoint import IncrementChain
from dnd.character.checkpoint import IncrementStorage
from dnd.character.checkpoint import MemoryStorage
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
from starlette.responses import Response


class _CreateCharacterResponse(BaseModel):
    character: PresentableCharacter | None = None
    increment_chain: IncrementChain
    error: str | None = None


EXAMPLES = (example_building_blocks().model_dump(mode="json"),)


class _CreateCharacterRequestSchema(BaseModel):
    building_blocks: dict[str, object] = Field(examples=list(EXAMPLES))
    increment_chain: dict[str, object] = Field(examples=[IncrementChain()])


_building_block_creator: TypeAdapter[
    BuildingBlock[BlueprintProtocol, Delta, BlueprintProtocol] | CombinedBlock
] = TypeAdapter(AnyBuildingBlock)


def create_app(storage: IncrementStorage) -> FastAPI:
    app_ = FastAPI()

    @app_.post(
        "/create_character",
        response_model=_CreateCharacterResponse,
        response_model_exclude_unset=True,
    )
    def create_character(
        request: _CreateCharacterRequestSchema, response: Response
    ) -> _CreateCharacterResponse:
        blocks = request.building_blocks

        errors = []
        building_blocks: (
            BuildingBlock[BlueprintProtocol, Delta, BlueprintProtocol] | CombinedBlock
        )
        try:
            building_blocks = _building_block_creator.validate_python(blocks)
        except ValidationError as e:
            errors.append(e)
        try:
            increment_chain = IncrementChain.model_validate(request.increment_chain)
        except ValidationError as e:
            errors.append(e)
        if errors:
            raise HTTPException(status_code=422, detail="\n\n".join(map(str, errors)))
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

    return app_


app = create_app(MemoryStorage())
