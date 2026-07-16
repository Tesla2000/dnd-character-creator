from typing import Literal

from pydantic import BaseModel
from pydantic import Field
from structured_output_creator import OpenAIService
from structured_output_creator import RaisingService

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.totem_choice_resolver.base import (
    TotemChoiceResolverBase,
)
from dnd.choices.abilities.totem_animal import TotemAnimal


class AITotemChoiceResolver(TotemChoiceResolverBase):
    type: Literal[BuildingBlockType.AI_TOTEM_CHOICE_RESOLVER] = (
        BuildingBlockType.AI_TOTEM_CHOICE_RESOLVER
    )
    llm: RaisingService[BaseModel] = Field(
        exclude=True,
        default_factory=lambda: RaisingService(service=OpenAIService()),
    )

    def resolve(self) -> TotemAnimal:
        class TotemSelection(BaseModel):
            totem: TotemAnimal

        prompt = (
            "You are choosing a totem animal for a D&D 5e Barbarian "
            "following the Path of the Totem Warrior. "
            "Choose the most thematically fitting totem animal. "
            f"Options: {', '.join(a.value for a in TotemAnimal)}."
        )
        return self.llm.create_structured_output(prompt, TotemSelection).totem
