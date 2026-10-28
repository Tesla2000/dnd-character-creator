import pytest
from pydantic import ValidationError

from dnd.character.race.subrace_stats.race_statistics import RaceStatistics
from dnd.character.race.subrace_stats.subrace_stats import Subrace
from dnd.choices.language import Language
from dnd.skill_proficiency import Skill


_MINIMAL_SUBRACE_KWARGS: dict[str, object] = dict(
    speed=30,
    dark_vision_range=0,
    languages=(Language.COMMON,),
    obligatory_skills=(),
    tool_proficiencies=(),
    additional_feat=False,
    statistics=RaceStatistics(
        strength=0,
        dexterity=0,
        constitution=0,
        intelligence=0,
        wisdom=0,
        charisma=0,
        any_of_your_choice=0,
    ),
    other_active_abilities=(),
)


@pytest.mark.unit
class TestSubraceValidators:
    def test_n_skills_exceeds_options_raises(self) -> None:
        with pytest.raises(ValidationError, match="More skill choices"):
            Subrace(
                **_MINIMAL_SUBRACE_KWARGS,
                skills_to_choose_from=(),
                n_skills=1,
            )

    def test_valid_skill_choices_construct(self) -> None:
        subrace = Subrace(
            **_MINIMAL_SUBRACE_KWARGS,
            skills_to_choose_from=(Skill.ACROBATICS,),
            n_skills=1,
        )
        assert subrace.n_skills == 1

    def test_skills_to_choose_from_without_n_skills_raises(self) -> None:
        with pytest.raises(ValidationError, match="Skills to choose from present"):
            Subrace(
                **_MINIMAL_SUBRACE_KWARGS,
                skills_to_choose_from=(Skill.ACROBATICS,),
                n_skills=0,
            )
