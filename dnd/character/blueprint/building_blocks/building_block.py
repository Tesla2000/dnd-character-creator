from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import Any

from dnd.character.blueprint.state import Blueprint
from pydantic import BaseModel
from pydantic import ConfigDict

_WideBlueprint = Blueprint[
    Any, Any, Any, Any, Any, Any, Any, Any, Any, Any, Any, Any, Any, Any, Any, Any, Any, Any, Any  # ignore
]


class BuildingBlock(BaseModel):
    """Abstract base for a pipeline step that transforms blueprint state."""

    model_config = ConfigDict(frozen=True)
