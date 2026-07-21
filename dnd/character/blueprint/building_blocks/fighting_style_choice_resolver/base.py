from abc import ABC
from abc import abstractmethod

from pydantic import ConfigDict

from dnd.character.blueprint.building_blocks.building_block import BuildingBlock
from dnd.character.blueprint.building_blocks.building_block import _WideBlueprint
from dnd.character.blueprint.states.state import _BPT
from dnd.choices.abilities.fighting_style import FightingStyle


class FightingStyleChoiceResolver(BuildingBlock, ABC):
    """Abstract base class for resolving n_fighting_style_choices.

    When a class grants a fighting-style choice (n_fighting_style_choices > 0),
    this component determines which style to select from
    fighting_styles_to_choose_from.
    """

    model_config = ConfigDict(frozen=True)

    @abstractmethod
    def _select_style(self, state: _WideBlueprint) -> FightingStyle: ...

    def apply(self, blueprint: _BPT) -> _BPT:
        if blueprint.n_fighting_style_choices == 0:
            return blueprint

        selected = self._select_style(blueprint)
        return blueprint.model_copy(
            update={
                "fighting_style": selected,
                "n_fighting_style_choices": 0,
                "fighting_styles_to_choose_from": frozenset(),
            }
        )
