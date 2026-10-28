import pytest
from dnd.character.character import Character
from dnd.character.classes import Class
from dnd.character.classes import ClassModifier
from dnd.character.stats import Stats
from dnd.character.subrace import StandardHumanPlayersHandbookRace


@pytest.mark.unit
def test_character_level_up_delegates_to_class_modifier() -> None:
    character = Character(
        class_modifier=ClassModifier(),
        race_modifier=StandardHumanPlayersHandbookRace(),
        stats=Stats(
            strength=10,
            dexterity=10,
            constitution=10,
            intelligence=10,
            wisdom=10,
            charisma=10,
        ),
    )
    character.level_up(Class.FIGHTER)
    character.level_up(Class.WIZARD)
    assert character.level == 2
    assert character.class_modifier.class_level(Class.WIZARD) == 1
