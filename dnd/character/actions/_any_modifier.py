from typing import Annotated, Union

from pydantic import Field

from dnd.character.actions.advantage_modifier import (
    RecklessAdvantageModifier,
    RecklessGrantsAdvantageModifier,
)
from dnd.character.actions.attack_bonus_modifier import RageAttackBonusModifier
from dnd.character.actions.conditional_immunity_modifier import (
    MindlessRageConditionalImmunityModifier,
)
from dnd.character.actions.damage_resistance_modifier import (
    RageDamageResistanceModifier,
)
from dnd.character.actions.duration_modifier import RageRoundCounterModifier
from dnd.character.actions.magical_damage_modifier import (
    PrimalStrikeMagicalDamageModifier,
)

AnyModifier = Annotated[
    Union[
        RageAttackBonusModifier,
        RecklessAdvantageModifier,
        RecklessGrantsAdvantageModifier,
        RageDamageResistanceModifier,
        MindlessRageConditionalImmunityModifier,
        RageRoundCounterModifier,
        PrimalStrikeMagicalDamageModifier,
    ],
    Field(discriminator="type"),
]

__all__ = ["AnyModifier"]
