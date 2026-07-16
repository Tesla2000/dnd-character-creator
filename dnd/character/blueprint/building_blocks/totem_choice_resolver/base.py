from abc import ABC
from abc import abstractmethod

from pydantic import ConfigDict

from dnd.character.blueprint.building_blocks.building_block import BuildingBlock
from dnd.choices.abilities.totem_animal import TotemAnimal


class TotemChoiceResolverBase(BuildingBlock, ABC):
    model_config = ConfigDict(frozen=True)

    @abstractmethod
    def resolve(self) -> TotemAnimal: ...
