import warnings
from collections.abc import Generator
from unittest.mock import patch

import pytest
from pydantic import TypeAdapter
from starlette.testclient import TestClient

import dnd.server.app as app_module
from dnd.character.blueprint.building_blocks import AnyBuildingBlock
from dnd.character.blueprint.building_blocks.initial_data_filler import (
    RandomInitialDataFiller,
)
from dnd.character.blueprint.building_blocks.level_up.health_increase import (
    D6HealthIncreaseAverage,
)
from dnd.character.blueprint.building_blocks.level_up.sorcerer.draconic_bloodline.level_1 import (
    SorcererLevel1DraconicBloodline,
)
from dnd.character.blueprint.building_blocks.level_up.spell_assignment import (
    SorcererRandomSpellAssigner,
)
from dnd.character.blueprint.building_blocks.null_block import NullBlock
from dnd.character.blueprint.building_blocks.race_assigner import HumanRaceAssigner
from dnd.character.blueprint.building_blocks.stats_builder.standard_array import (
    StandardArray,
)
from dnd.character.race.subraces import SubraceName
from dnd.choices.stats_creation.statistic import Statistic
from dnd.server.app import create_app

_PRIORITY = (
    Statistic.CHARISMA,
    Statistic.CONSTITUTION,
    Statistic.DEXTERITY,
    Statistic.INTELLIGENCE,
    Statistic.WISDOM,
    Statistic.STRENGTH,
)
_ta: TypeAdapter[list[AnyBuildingBlock]] = TypeAdapter(list[AnyBuildingBlock])
_VALID_JSON = _ta.dump_python(
    [
        StandardArray(stats_priority=_PRIORITY),
        HumanRaceAssigner(subrace=SubraceName.HUMAN_STANDARD_HUMAN_PLAYERSHANDBOOK),
        SorcererLevel1DraconicBloodline(
            health_increase=D6HealthIncreaseAverage(),
            spell_assigner=SorcererRandomSpellAssigner(seed=42),
        ),
        RandomInitialDataFiller(seed=42),
    ],
    mode="json",
)


@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    with (
        patch.object(app_module, "example_building_blocks", return_value=()),
        warnings.catch_warnings(),
    ):
        warnings.simplefilter("ignore", DeprecationWarning)
        yield TestClient(create_app())


@pytest.mark.unit
class TestServerApp:
    def test_root_redirects_to_docs(self, client: TestClient) -> None:
        response = client.get("/", follow_redirects=False)
        assert response.status_code == 307
        assert response.headers["location"] == "/docs"

    def test_create_character_valid_pipeline_returns_200(
        self, client: TestClient
    ) -> None:
        with patch.object(app_module, "_validate_pipeline", return_value=None):
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
        # NullBlock alone produces an empty blueprint — PresentableCharacter validation fails
        body = _ta.dump_python([NullBlock()], mode="json")
        response = client.post("/create_character", json=body)
        assert response.status_code == 422
        assert "race" in response.json()["detail"]

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
