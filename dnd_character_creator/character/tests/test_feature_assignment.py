from __future__ import annotations

import pytest
from dnd_character_creator.character.blueprint.building_blocks import (
    FeatureAssigner,
)
from dnd_character_creator.character.feature.feature import Feature
from dnd_character_creator.character.feature.specialized_features import (
    AbilityFeature,
)
from dnd_character_creator.character.feature.specialized_features import (
    ACBonusFeature,
)
from dnd_character_creator.character.feature.specialized_features import (
    SavingThrowBonusFeature,
)
from dnd_character_creator.character.feature.specialized_features import (
    SkillProficiencyFeature,
)
from dnd_character_creator.character.feature.specialized_features import (
    StatBoostFeature,
)
from dnd_character_creator.character.stats import Stats
from dnd_character_creator.choices.stats_creation.statistic import Statistic
from dnd_character_creator.skill_proficiency import Skill


class TestFeatureAssignment:
    """Test that features can be assigned to blueprints correctly."""

    @pytest.fixture
    def base_blueprint(self):
        """Create a minimal blueprint for testing."""
        from dnd_character_creator.character.blueprint.blueprint import (
            Blueprint,
        )

        return Blueprint(
            stats=Stats(
                strength=10,
                dexterity=10,
                constitution=10,
                intelligence=10,
                wisdom=10,
                charisma=10,
            ),
            stats_cup=Stats(
                strength=20,
                dexterity=20,
                constitution=20,
                intelligence=20,
                wisdom=20,
                charisma=20,
            ),
            saving_throw_bonuses=Stats(
                strength=0,
                dexterity=0,
                constitution=0,
                intelligence=0,
                wisdom=0,
                charisma=0,
            ),
            ac_bonus=0,
            skill_proficiencies=frozenset(),
            other_active_abilities=(),
        )

    def _apply_building_block(self, block, blueprint):
        """Helper to apply a building block to a blueprint."""
        gen = block.get_change(blueprint)
        diff = next(gen)
        return blueprint.add_diff(diff)

    def test_basic_feature_assignment(self, base_blueprint):
        """Test that a basic feature can be assigned."""
        feature = Feature(
            name="Trance",
            description="Elves don't need to sleep. Instead, they meditate deeply for 4 hours a day.",
        )
        assigner = FeatureAssigner(feature=feature)

        result = self._apply_building_block(assigner, base_blueprint)

        assert len(result.other_active_abilities) == 1
        assert (
            result.other_active_abilities[0]
            == "Trance: Elves don't need to sleep. Instead, they meditate deeply for 4 hours a day."
        )

    def test_ability_feature_assignment(self, base_blueprint):
        """Test that an ability feature can be assigned."""
        feature = AbilityFeature(
            name="Relentless Endurance",
            description="When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead.",
        )
        assigner = FeatureAssigner(feature=feature)

        result = self._apply_building_block(assigner, base_blueprint)

        assert len(result.other_active_abilities) == 1
        assert result.other_active_abilities[0].startswith(
            "Relentless Endurance:"
        )

    def test_stat_boost_feature_assignment(self, base_blueprint):
        """Test that a stat boost feature can be assigned."""
        feature = StatBoostFeature(
            name="Ability Score Improvement",
            description="Increase Strength by 2",
            stat=Statistic.STRENGTH,
            boost_amount=2,
        )
        assigner = FeatureAssigner(feature=feature)

        result = self._apply_building_block(assigner, base_blueprint)

        # Check stats were boosted
        assert result.stats.strength == 12
        # Check feature was recorded
        assert len(result.other_active_abilities) == 1
        assert result.other_active_abilities[0].startswith(
            "Ability Score Improvement:"
        )

    def test_stat_boost_respects_cap(self, base_blueprint):
        """Test that stat boost respects the stats_cup."""
        # Set strength to near cap
        base_blueprint = type(base_blueprint)(
            **{
                **base_blueprint.model_dump(),
                "stats": Stats(
                    strength=19,
                    dexterity=10,
                    constitution=10,
                    intelligence=10,
                    wisdom=10,
                    charisma=10,
                ),
            }
        )

        feature = StatBoostFeature(
            name="Ability Score Improvement",
            description="Increase Strength by 2",
            stat=Statistic.STRENGTH,
            boost_amount=2,
        )
        assigner = FeatureAssigner(feature=feature)

        result = self._apply_building_block(assigner, base_blueprint)

        # Should cap at 20
        assert result.stats.strength == 20

    def test_skill_proficiency_feature(self, base_blueprint):
        """Test that skill proficiency features work."""
        feature = SkillProficiencyFeature(
            name="Skill Expert",
            description="Gain proficiency in Perception and Stealth",
            skills=frozenset([Skill.PERCEPTION, Skill.STEALTH]),
        )
        assigner = FeatureAssigner(feature=feature)

        result = self._apply_building_block(assigner, base_blueprint)

        assert Skill.PERCEPTION in result.skill_proficiencies
        assert Skill.STEALTH in result.skill_proficiencies
        assert len(result.other_active_abilities) == 1

    def test_ac_bonus_feature(self, base_blueprint):
        """Test that AC bonus features work."""
        feature = ACBonusFeature(
            name="Defense Fighting Style",
            description="While wearing armor, you gain +1 AC",
            ac_bonus=1,
        )
        assigner = FeatureAssigner(feature=feature)

        result = self._apply_building_block(assigner, base_blueprint)

        assert result.ac_bonus == 1
        assert len(result.other_active_abilities) == 1

    def test_saving_throw_bonus_feature_specific(self, base_blueprint):
        """Test saving throw bonus for a specific stat."""
        feature = SavingThrowBonusFeature(
            name="Resilient (Constitution)",
            description="Gain +1 bonus to Constitution saving throws",
            stat=Statistic.CONSTITUTION,
            bonus=1,
        )
        assigner = FeatureAssigner(feature=feature)

        result = self._apply_building_block(assigner, base_blueprint)

        assert result.saving_throw_bonuses.constitution == 1
        # Other saves should be unchanged
        assert result.saving_throw_bonuses.strength == 0
        assert len(result.other_active_abilities) == 1

    def test_saving_throw_bonus_feature_universal(self, base_blueprint):
        """Test universal saving throw bonus."""
        feature = SavingThrowBonusFeature(
            name="Bless",
            description="Gain +1 bonus to all saving throws",
            stat=None,
            bonus=1,
        )
        assigner = FeatureAssigner(feature=feature)

        result = self._apply_building_block(assigner, base_blueprint)

        # All saves should be increased
        assert result.saving_throw_bonuses.strength == 1
        assert result.saving_throw_bonuses.dexterity == 1
        assert result.saving_throw_bonuses.constitution == 1
        assert result.saving_throw_bonuses.intelligence == 1
        assert result.saving_throw_bonuses.wisdom == 1
        assert result.saving_throw_bonuses.charisma == 1

    def test_multiple_features(self, base_blueprint):
        """Test that multiple features can be stacked."""
        feature1 = StatBoostFeature(
            name="ASI (Strength)",
            description="Increase Strength by 2",
            stat=Statistic.STRENGTH,
            boost_amount=2,
        )
        feature2 = ACBonusFeature(
            name="Defense", description="+1 AC", ac_bonus=1
        )
        feature3 = AbilityFeature(name="Trance", description="4 hour rest")

        assigner1 = FeatureAssigner(feature=feature1)
        assigner2 = FeatureAssigner(feature=feature2)
        assigner3 = FeatureAssigner(feature=feature3)

        result = self._apply_building_block(assigner1, base_blueprint)
        result = self._apply_building_block(assigner2, result)
        result = self._apply_building_block(assigner3, result)

        assert result.stats.strength == 12
        assert result.ac_bonus == 1
        assert len(result.other_active_abilities) == 3
