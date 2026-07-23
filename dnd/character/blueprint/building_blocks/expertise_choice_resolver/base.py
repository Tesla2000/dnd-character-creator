from abc import ABC
from abc import abstractmethod

from dnd.character.blueprint.building_blocks.building_block import BuildingBlock
from dnd.character.blueprint.building_blocks.building_block import _WideBlueprint
from dnd.character.blueprint.states.state import _BPT
from dnd.skill_proficiency import Skill
from pydantic import ConfigDict


class ExpertiseChoiceResolver(BuildingBlock, ABC):
    """Abstract base class for resolving n_expertise_choices.

    When a class grants expertise (doubled proficiency bonus) on a number of
    already-proficient skills (n_expertise_choices > 0), this component
    determines which skills to select from expertise_choices_from.
    """

    model_config = ConfigDict(frozen=True)

    @abstractmethod
    def _select_expertise(self, state: _WideBlueprint) -> frozenset[Skill]: ...

    def apply(self, blueprint: _BPT) -> _BPT:
        if blueprint.n_expertise_choices == 0:
            selected: frozenset[Skill] = frozenset()
        else:
            selected = self._select_expertise(blueprint)

        return blueprint.model_copy(
            update={
                "skill_expertise": blueprint.skill_expertise + tuple(selected),
                "n_expertise_choices": 0,
                "expertise_choices_from": frozenset(),
            }
        )
