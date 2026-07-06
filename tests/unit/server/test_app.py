import pytest
from dnd.character.blueprint.building_blocks import SexAssigner
from dnd.character.checkpoint import IncrementChain, MemoryStorage
from dnd.choices.sex import Sex
from dnd.server.app import EXAMPLES, create_app
from starlette.testclient import TestClient


@pytest.fixture
def storage():
    return MemoryStorage()


@pytest.fixture
def client(storage):
    return TestClient(create_app(storage))


@pytest.mark.unit
class TestServerApp:
    def test_create_character_simple(self, client: TestClient) -> None:
        response = client.post(
            "/create_character",
            json={
                "building_blocks": EXAMPLES[0],
                "increment_chain": {},
            },
        )
        assert response.status_code == 200
        data = response.json()
        assert data["error"] is None

    def test_create_character_invalid_blocks(self, client: TestClient) -> None:
        response = client.post(
            "/create_character",
            json={
                "building_blocks": {"block_type": "NonExistentBlock"},
                "increment_chain": {},
            },
        )
        assert response.status_code == 422

    def test_create_character_invalid_block_type(self, client: TestClient) -> None:
        response = client.post(
            "/create_character",
            json={
                "building_blocks": [{"type": "NonExistentBlock"}],
                "increment_chain": {},
            },
        )
        assert response.status_code == 422

    def test_create_character_incomplete_build(self, client: TestClient) -> None:
        block = SexAssigner(sex=Sex.MALE)
        response = client.post(
            "/create_character",
            json={
                "building_blocks": block.model_dump(mode="json"),
                "increment_chain": IncrementChain().model_dump(mode="json"),
            },
        )
        assert response.status_code == 422

    def test_create_character_build_failure_returns_error(
        self, client: TestClient
    ) -> None:
        block = SexAssigner(sex=Sex.MALE)
        response = client.post(
            "/create_character",
            json={
                "building_blocks": [block.model_dump(mode="json")],
                "increment_chain": IncrementChain().model_dump(mode="json"),
            },
        )
        assert response.status_code == 422
        data = response.json()
        assert data["error"] is not None

    def test_create_character_stores_chain(
        self, client: TestClient, storage: MemoryStorage
    ) -> None:
        response = client.post(
            "/create_character",
            json={
                "building_blocks": EXAMPLES[0],
                "increment_chain": IncrementChain().model_dump(mode="json"),
            },
        )
        assert response.status_code == 200
        assert len(storage.list_chains()) > 0

    def test_examples_are_valid(self, client: TestClient) -> None:
        for example in EXAMPLES:
            response = client.post(
                "/create_character",
                json={
                    "building_blocks": example,
                    "increment_chain": IncrementChain().model_dump(mode="json"),
                },
            )
            assert response.status_code == 200

    def test_create_character_with_increment_chain(self, client: TestClient) -> None:
        first = client.post(
            "/create_character",
            json={
                "building_blocks": EXAMPLES[0],
                "increment_chain": IncrementChain().model_dump(mode="json"),
            },
        )
        assert first.status_code == 200
        chain = first.json()["increment_chain"]
        second = client.post(
            "/create_character",
            json={
                "building_blocks": EXAMPLES[0],
                "increment_chain": chain,
            },
        )
        assert second.status_code == 200

    def test_create_character_invalid_increment_chain(self, client: TestClient) -> None:
        response = client.post(
            "/create_character",
            json={
                "building_blocks": EXAMPLES[0],
                "increment_chain": {"increments": [{"delta_type": "NonExistentDelta"}]},
            },
        )
        assert response.status_code == 422
