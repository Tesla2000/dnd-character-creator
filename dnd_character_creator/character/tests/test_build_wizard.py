from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.builder import Builder


class TestBuildWizard:
    def test_build_wizard(self):
        character = Builder()._init_character()
        assert isinstance(character, Blueprint)
