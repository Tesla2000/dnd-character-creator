import warnings

import pytest
from pydantic import TypeAdapter
from starlette.testclient import TestClient

from dnd.character.blueprint.building_blocks import AnyBuildingBlock
from dnd.character.blueprint.building_blocks.initial_data_filler import (
    RandomInitialDataFiller,
)
from dnd.character.blueprint.building_blocks.null_block import NullBlock
from dnd.server.app import create_app
from dnd.server.example_generators.example_building_blocks import (
    example_building_blocks,
)

_ta: TypeAdapter[list[AnyBuildingBlock]] = TypeAdapter(list[AnyBuildingBlock])
_VALID_JSON = _ta.dump_python(list(example_building_blocks()), mode="json")


@pytest.fixture
def client() -> TestClient:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        return TestClient(create_app())


@pytest.mark.unit
class TestServerApp:
    def test_root_redirects_to_docs(self, client: TestClient) -> None:
        response = client.get("/", follow_redirects=False)
        assert response.status_code == 307
        assert response.headers["location"] == "/docs"

    def test_create_character_valid_pipeline_returns_200(
        self, client: TestClient
    ) -> None:
        response = client.post("/create_character", json=_VALID_JSON)
        assert response.status_code == 200
        data = response.json()
        assert "race" in data
        assert "stats" in data

    def test_create_character_invalid_block_type_returns_422(
        self, client: TestClient
    ) -> None:
        response = client.post(
            "/create_character",
            json=[{"type": "NonExistentBlock"}],
        )
        assert response.status_code == 422

    def test_create_character_invalid_body_structure_returns_422(
        self, client: TestClient
    ) -> None:
        response = client.post(
            "/create_character",
            json={"building_blocks": []},
        )
        assert response.status_code == 422

    def test_create_character_invalid_pipeline_sequence_returns_422(
        self, client: TestClient
    ) -> None:
        # NullBlock before CharacterConverter (appended by endpoint) — origin mismatch
        body = _ta.dump_python([NullBlock()], mode="json")
        response = client.post("/create_character", json=body)
        assert response.status_code == 422
        assert "ConvertibleBlueprint" in response.json()["detail"]

    def test_create_character_type_arg_mismatch_returns_422(
        self, client: TestClient
    ) -> None:
        # Two RandomInitialDataFillers — second expects character_data=None but first produced CharacterData
        body = _ta.dump_python(
            [RandomInitialDataFiller(), RandomInitialDataFiller()], mode="json"
        )
        response = client.post("/create_character", json=body)
        assert response.status_code == 422
        assert "type arg" in response.json()["detail"]
