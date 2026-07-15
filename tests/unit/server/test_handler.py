import importlib
import sys
from types import ModuleType
from unittest.mock import patch

import pytest

import dnd.server.app as app_module


@pytest.mark.unit
class TestHandler:
    def test_handler_is_callable(self) -> None:
        sys.modules.pop("dnd.server.handler", None)
        with patch.object(app_module, "example_building_blocks", return_value=()):
            handler_module: ModuleType = importlib.import_module("dnd.server.handler")

            assert callable(handler_module.handler)
