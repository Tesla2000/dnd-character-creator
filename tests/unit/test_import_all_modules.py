import importlib
import pkgutil

import pytest
import dnd


@pytest.mark.unit
def test_every_module_in_dnd_imports() -> None:
    names = [info.name for info in pkgutil.walk_packages(dnd.__path__, prefix="dnd.")]
    assert names
    for name in names:
        importlib.import_module(name)
