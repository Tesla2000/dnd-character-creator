import pytest

from dnd.character.blueprint.building_blocks.abstract_feat_block import (
    AbstractFeatBlock,
)
from dnd.character.blueprint.building_blocks.feat_block.ability_score_improvement import (
    AbilityScoreImprovementFeatBlock,
)
from dnd.character.blueprint.building_blocks.feat_block.any_feat_selection import (
    AnyFeatSelectionBlock,
    _feat_block_for,
)
from dnd.character.blueprint.building_blocks.feat_choice_resolver.max_first import (
    MaxFirstResolver,
)
from dnd.character.blueprint.building_blocks.feat_choice_resolver.random import (
    RandomFeatChoiceResolver,
)
from dnd.character.blueprint.states.state import Blueprint
from dnd.character.class_levels import ClassLevels
from dnd.character.feature.feats import FeatName
from dnd.character.stats import Stats

_MATCHED_FEATS = tuple(
    feat
    for feat in FeatName
    if feat
    not in (
        FeatName.ABILITY_SCORE_IMPROVEMENT,
        FeatName.ANY_OF_YOUR_CHOICE,
        FeatName.ANY_EXCEPT_ABILITY_SCORE_IMPROVEMENT,
    )
)

_BELOW_CAP_STATS = Stats(
    strength=10,
    dexterity=10,
    constitution=10,
    intelligence=10,
    wisdom=10,
    charisma=10,
)


@pytest.mark.unit
class TestFeatBlockFor:
    @pytest.mark.parametrize("feat", _MATCHED_FEATS)
    def test_returns_a_feat_block_for_every_named_feat(self, feat: FeatName) -> None:
        block = _feat_block_for(feat)
        assert isinstance(block, AbstractFeatBlock)

    def test_ability_score_improvement_returns_dedicated_block(self) -> None:
        block = _feat_block_for(FeatName.ABILITY_SCORE_IMPROVEMENT)
        assert isinstance(block, AbilityScoreImprovementFeatBlock)

    def test_unmatched_feat_raises_value_error(self) -> None:
        with pytest.raises(ValueError, match="No feat block for"):
            _feat_block_for(FeatName.ANY_OF_YOUR_CHOICE)


@pytest.mark.unit
class TestAnyFeatSelectionBlockApply:
    def test_selects_ability_score_improvement_when_stat_below_cap(self) -> None:
        state = Blueprint(stats=_BELOW_CAP_STATS, classes=ClassLevels(wizard=2))
        block = AnyFeatSelectionBlock(feat_resolver=MaxFirstResolver())
        result = block.apply(state)

        assert FeatName.ABILITY_SCORE_IMPROVEMENT not in result.feats
        assert sum(result.stats.model_dump().values()) == sum(
            _BELOW_CAP_STATS.model_dump().values()
        ) + 2

    def test_selects_a_concrete_feat_when_no_stat_choice_made(self) -> None:
        state = Blueprint(classes=ClassLevels(wizard=1))
        block = AnyFeatSelectionBlock(
            feat_resolver=MaxFirstResolver(then=RandomFeatChoiceResolver(seed=1))
        )
        result = block.apply(state)

        assert len(result.feats) == 1
        chosen = result.feats[0]
        assert chosen not in FeatName.not_choosables()
        assert chosen != FeatName.ABILITY_SCORE_IMPROVEMENT
