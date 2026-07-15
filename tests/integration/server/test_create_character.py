import pytest
from pydantic import TypeAdapter

from dnd.character.blueprint.building_blocks import AnyBuildingBlock
from dnd.character.blueprint.building_blocks.initial_data_filler.random_filler import (
    RandomInitialDataFiller,
)
from dnd.character.blueprint.building_blocks.race_assigner.random_race_assigner import (
    RandomRaceAssigner,
)
from dnd.character.blueprint.building_blocks.stats_builder.standard_array import (
    StandardArray,
)
from dnd.choices.stats_creation.statistic import Statistic
from tests.integration.server.test_client import TestClient

_PRIORITY = (
    Statistic.STRENGTH,
    Statistic.DEXTERITY,
    Statistic.CONSTITUTION,
    Statistic.INTELLIGENCE,
    Statistic.WISDOM,
    Statistic.CHARISMA,
)
_ta: TypeAdapter[list[AnyBuildingBlock]] = TypeAdapter(list[AnyBuildingBlock])


def _blocks_json() -> list[object]:
    blocks: list[AnyBuildingBlock] = [
        StandardArray(stats_priority=_PRIORITY),
        RandomRaceAssigner(),
        RandomInitialDataFiller(seed=42),
    ]
    return _ta.dump_python(blocks, mode="json")


@pytest.mark.smoke
class TestCreateCharacter(TestClient):
    def test_create_character_success(self, client) -> None:
        response = client.post("/create_character", json=_blocks_json())
        assert response.status_code == 200
        data = response.json()
        assert "race" in data
        assert "stats" in data

    def test_create_character_empty_pipeline_returns_422(self, client) -> None:
        response = client.post("/create_character", json=[])
        assert response.status_code == 422

    def test_invalid_building_blocks_returns_422(self, client) -> None:
        response = client.post(
            "/create_character",
            json=[{"type": "invalid_block_type"}],
        )
        assert response.status_code == 422
