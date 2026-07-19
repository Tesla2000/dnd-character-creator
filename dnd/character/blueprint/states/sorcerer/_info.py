from typing import ClassVar
from typing import Generic

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from dnd.character.blueprint.sentinels import _SOK_co
from dnd.choices.abilities.metamagic import MetamagicOption


class SorcererInfo(BaseModel, Generic[_SOK_co]):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)

    metamagic_options: tuple[MetamagicOption, ...] = Field(default=())
    n_metamagic_choices: int = 0
