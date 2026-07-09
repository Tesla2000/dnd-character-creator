import pytest
from dnd.server.app import create_app
from starlette.testclient import TestClient as StarletteTestClient


class TestClient:
    @pytest.fixture
    def client(self):
        return StarletteTestClient(create_app())
