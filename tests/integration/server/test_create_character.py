import pytest
from pydantic import TypeAdapter

from dnd.character.blueprint.building_blocks import AnyBuildingBlock
from dnd.character.blueprint.building_blocks.all_choices_resolver.base import (
    AllChoicesResolver,
)
from dnd.character.blueprint.building_blocks.equipment_chooser.random import (
    RandomEquipmentChooser,
)
from dnd.character.blueprint.building_blocks.feat_choice_resolver.random import (
    RandomFeatChoiceResolver,
)
from dnd.character.blueprint.building_blocks.initial_builder import InitialBuilder
from dnd.character.blueprint.building_blocks.initial_data_filler.random_filler import (
    RandomInitialDataFiller,
)
from dnd.character.blueprint.building_blocks.language_choice_resolver.random import (
    RandomLanguageChoiceResolver,
)
from dnd.character.blueprint.building_blocks.race_assigner.random_race_assigner import (
    RandomRaceAssigner,
)
from dnd.character.blueprint.building_blocks.skill_choice_resolver.random import (
    RandomSkillChoiceResolver,
)
from dnd.character.blueprint.building_blocks.stat_choice_resolver.priority import (
    PriorityStatChoiceResolver,
)
from dnd.character.blueprint.building_blocks.stats_builder.standard_array import (
    StandardArray,
)
from dnd.character.blueprint.building_blocks.tool_proficiency_choice_resolver.random import (
    RandomToolProficiencyChoiceResolver,
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
_ACR = AllChoicesResolver(
    language_choice_resolver=RandomLanguageChoiceResolver(),
    skill_choice_resolver=RandomSkillChoiceResolver(),
    feat_choice_resolver=RandomFeatChoiceResolver(),
    tool_proficiency_choice_resolver=RandomToolProficiencyChoiceResolver(),
    stat_choice_resolver=PriorityStatChoiceResolver(priority=_PRIORITY),
    equipment_chooser=RandomEquipmentChooser(),
)
_BUILDING_BLOCKS: list[AnyBuildingBlock] = [
    InitialBuilder(
        stats_builder=StandardArray(stats_priority=_PRIORITY),
        race_assigner=RandomRaceAssigner(),
        all_choices_resolver=_ACR,
    ),
    RandomInitialDataFiller(seed=42),
    _ACR,
]
_ta: TypeAdapter[list[AnyBuildingBlock]] = TypeAdapter(list[AnyBuildingBlock])
_BLOCKS_JSON = _ta.dump_python(_BUILDING_BLOCKS, mode="json")


@pytest.mark.integration
class TestCreateCharacter(TestClient):
    def test_create_character_success(self, client) -> None:
        response = client.post("/create_character", json=_BLOCKS_JSON)
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
