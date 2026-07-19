from typing import ClassVar
from typing import Generic

from pydantic import BaseModel
from pydantic import ConfigDict

from dnd.character.blueprint.sentinels import _BAK_co


class BarbarianInfo(BaseModel, Generic[_BAK_co]):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)
