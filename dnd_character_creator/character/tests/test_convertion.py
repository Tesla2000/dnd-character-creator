import pytest
from pydantic import ValidationError

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.builder import Builder
from dnd_character_creator.character.character import Character
from dnd_character_creator.choices.alignment import Alignment
from dnd_character_creator.choices.background_creatrion.background import \
    Background
from dnd_character_creator.choices.race_creation.main_race import Race
from dnd_character_creator.choices.sex import Sex


class TestConvertion:
    def test_invalid(self):
        with pytest.raises(ValidationError):
            Builder._convert_to_character(Blueprint())
    
    def test_valid(self):
        blueprint = Blueprint(
            sex=Sex.MALE,
            backstory="Ain't much but an honest work",
            level=1,
            age=20,
            race=Race.HUMAN,
            name="Joe Doe",
            background=Background.SMUGGLER,
            alignment=Alignment.CHAOTIC_NEUTRAL,
            height=175,
            weight=69,
            eye_color="blue",
            skin_color="black",
            hairstyle="none",
            appearance="existing",
            character_traits="Ain't much but an honest work",
            ideals="Ain't much but an honest work",
            bonds="Ain't much but an honest work",
            weaknesses="Ain't much but an honest work",
        )
        assert isinstance(Builder._convert_to_character(blueprint), Character)