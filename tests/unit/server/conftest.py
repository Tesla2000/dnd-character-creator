import os
from collections.abc import Generator
from unittest.mock import patch

import pytest

os.environ.setdefault("OPENAI_API_KEY", "test-key")


@pytest.fixture(autouse=True)
def mock_openai_api_key() -> Generator[None, None, None]:
    with patch.dict(
        "os.environ",
        {"OPENAI_API_KEY": "test-key"},  # pragma: allowlist secret
    ):
        yield
