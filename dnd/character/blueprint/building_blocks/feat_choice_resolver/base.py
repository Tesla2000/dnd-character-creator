from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from dnd.character.blueprint.building_blocks.building_block import BuildingBlock
from dnd.character.blueprint.state import _BPT
from dnd.character.feature.feats import FeatName
from pydantic import ConfigDict


class FeatChoiceResolver(BuildingBlock, ABC):
    """Resolves FeatName.ANY_OF_YOUR_CHOICE placeholders.

    This resolver replaces ANY_OF_YOUR_CHOICE placeholders in the
    blueprint's feats set with concrete FeatName choices.

    Handles special logic for ABILITY_SCORE_IMPROVEMENT:
    - Excluded from choices if character is level 1
    - Converted to n_stat_choices for StatChoiceResolver
    - Filtered out from final feats tuple
    """

    model_config = ConfigDict(frozen=True)

    @abstractmethod
    def _select_from_available(
        self, available: list[FeatName], state: _BPT
    ) -> FeatName | None: ...

    def apply(self, blueprint: _BPT) -> _BPT:
        existing_classes = blueprint.classes
        ability_score_improvement_allowed = existing_classes.total_level() != 1

        resolved = set()
        for feat in blueprint.feats:
            result = self._resolve_feat(
                feat, blueprint, ability_score_improvement_allowed
            )
            resolved.add(result if result is not None else feat)

        n_asi = sum(1 for f in resolved if f == FeatName.ABILITY_SCORE_IMPROVEMENT)
        final_feats = tuple(
            f for f in resolved if f != FeatName.ABILITY_SCORE_IMPROVEMENT
        )

        return blueprint.model_copy(
            update={
                "feats": final_feats,
                "n_stat_choices": blueprint.n_stat_choices + 2 * n_asi,
            }
        )

    def _resolve_feat(
        self, feat: FeatName, state: _BPT, ability_score_improvement_allowed: bool
    ) -> FeatName | None:
        if feat not in FeatName.not_choosables():
            return feat
        excluded = list(FeatName.not_choosables())
        if not ability_score_improvement_allowed:
            excluded.append(FeatName.ABILITY_SCORE_IMPROVEMENT)
        available = [f for f in FeatName if f not in excluded]
        return self._select_from_available(available, state)
