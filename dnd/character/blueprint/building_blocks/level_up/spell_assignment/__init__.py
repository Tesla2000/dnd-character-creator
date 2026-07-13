from typing import Annotated
from typing import Union

from dnd.character.blueprint.building_blocks.level_up.spell_assignment.llm import (
    SorcererLLMSpellAssigner,
    WizardLLMSpellAssigner,
)
from dnd.character.blueprint.building_blocks.level_up.spell_assignment.random import (
    SorcererRandomSpellAssigner,
    WizardRandomSpellAssigner,
)
from pydantic import Field

AnyWizardSpellAssigner = Annotated[
    Union[WizardRandomSpellAssigner, WizardLLMSpellAssigner],
    Field(discriminator="type"),
]

AnySorcererSpellAssigner = Annotated[
    Union[SorcererRandomSpellAssigner, SorcererLLMSpellAssigner],
    Field(discriminator="type"),
]

AnySpellAssigner = Annotated[
    Union[
        WizardRandomSpellAssigner,
        SorcererRandomSpellAssigner,
        WizardLLMSpellAssigner,
        SorcererLLMSpellAssigner,
    ],
    Field(discriminator="type"),
]

__all__ = [
    "WizardRandomSpellAssigner",
    "SorcererRandomSpellAssigner",
    "WizardLLMSpellAssigner",
    "SorcererLLMSpellAssigner",
    "AnyWizardSpellAssigner",
    "AnySorcererSpellAssigner",
    "AnySpellAssigner",
]
