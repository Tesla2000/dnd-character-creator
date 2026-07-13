from typing import Annotated
from typing import Literal
from typing import Union

from dnd.character.blueprint.building_blocks.level_up.health_increase.average import (
    HealthIncreaseAverage,
)
from dnd.character.blueprint.building_blocks.level_up.health_increase.random import (
    HealthIncreaseRandom,
)
from dnd.character.blueprint.building_blocks.level_up.health_increase.random_min_two import (
    HealthIncreaseRandomMinTwo,
)
from dnd.character.blueprint.building_blocks.level_up.health_increase.random_reroll_ones import (
    HealthIncreaseRandomRerollOnes,
)
from dnd.choices.equipment_creation.weapons import HitDieSize
from pydantic import Field

# 16 static aliases — subscript by die size using Literal type args
D6HealthIncreaseAverage = HealthIncreaseAverage[Literal[HitDieSize.SIX]]
D8HealthIncreaseAverage = HealthIncreaseAverage[Literal[HitDieSize.EIGHT]]
D10HealthIncreaseAverage = HealthIncreaseAverage[Literal[HitDieSize.TEN]]
D12HealthIncreaseAverage = HealthIncreaseAverage[Literal[HitDieSize.TWELVE]]

D6HealthIncreaseRandom = HealthIncreaseRandom[Literal[HitDieSize.SIX]]
D8HealthIncreaseRandom = HealthIncreaseRandom[Literal[HitDieSize.EIGHT]]
D10HealthIncreaseRandom = HealthIncreaseRandom[Literal[HitDieSize.TEN]]
D12HealthIncreaseRandom = HealthIncreaseRandom[Literal[HitDieSize.TWELVE]]

D6HealthIncreaseRandomMinTwo = HealthIncreaseRandomMinTwo[Literal[HitDieSize.SIX]]
D8HealthIncreaseRandomMinTwo = HealthIncreaseRandomMinTwo[Literal[HitDieSize.EIGHT]]
D10HealthIncreaseRandomMinTwo = HealthIncreaseRandomMinTwo[Literal[HitDieSize.TEN]]
D12HealthIncreaseRandomMinTwo = HealthIncreaseRandomMinTwo[Literal[HitDieSize.TWELVE]]

D6HealthIncreaseRandomRerollOnes = HealthIncreaseRandomRerollOnes[
    Literal[HitDieSize.SIX]
]
D8HealthIncreaseRandomRerollOnes = HealthIncreaseRandomRerollOnes[
    Literal[HitDieSize.EIGHT]
]
D10HealthIncreaseRandomRerollOnes = HealthIncreaseRandomRerollOnes[
    Literal[HitDieSize.TEN]
]
D12HealthIncreaseRandomRerollOnes = HealthIncreaseRandomRerollOnes[
    Literal[HitDieSize.TWELVE]
]

# Die-size-specific discriminated unions (for use in level block fields)
AnyD6HealthIncrease = Annotated[
    Union[
        D6HealthIncreaseAverage,
        D6HealthIncreaseRandom,
        D6HealthIncreaseRandomMinTwo,
        D6HealthIncreaseRandomRerollOnes,
    ],
    Field(discriminator="type"),
]
AnyD8HealthIncrease = Annotated[
    Union[
        D8HealthIncreaseAverage,
        D8HealthIncreaseRandom,
        D8HealthIncreaseRandomMinTwo,
        D8HealthIncreaseRandomRerollOnes,
    ],
    Field(discriminator="type"),
]
AnyD10HealthIncrease = Annotated[
    Union[
        D10HealthIncreaseAverage,
        D10HealthIncreaseRandom,
        D10HealthIncreaseRandomMinTwo,
        D10HealthIncreaseRandomRerollOnes,
    ],
    Field(discriminator="type"),
]
AnyD12HealthIncrease = Annotated[
    Union[
        D12HealthIncreaseAverage,
        D12HealthIncreaseRandom,
        D12HealthIncreaseRandomMinTwo,
        D12HealthIncreaseRandomRerollOnes,
    ],
    Field(discriminator="type"),
]

__all__ = [
    "HealthIncreaseAverage",
    "HealthIncreaseRandom",
    "HealthIncreaseRandomMinTwo",
    "HealthIncreaseRandomRerollOnes",
    "D6HealthIncreaseAverage",
    "D8HealthIncreaseAverage",
    "D10HealthIncreaseAverage",
    "D12HealthIncreaseAverage",
    "D6HealthIncreaseRandom",
    "D8HealthIncreaseRandom",
    "D10HealthIncreaseRandom",
    "D12HealthIncreaseRandom",
    "D6HealthIncreaseRandomMinTwo",
    "D8HealthIncreaseRandomMinTwo",
    "D10HealthIncreaseRandomMinTwo",
    "D12HealthIncreaseRandomMinTwo",
    "D6HealthIncreaseRandomRerollOnes",
    "D8HealthIncreaseRandomRerollOnes",
    "D10HealthIncreaseRandomRerollOnes",
    "D12HealthIncreaseRandomRerollOnes",
    "AnyD6HealthIncrease",
    "AnyD8HealthIncrease",
    "AnyD10HealthIncrease",
    "AnyD12HealthIncrease",
]
