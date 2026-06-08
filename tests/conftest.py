from importlib import reload
import pytest
from fastapi.testclient import TestClient
import src.app as app_module


@pytest.fixture()
def client():
    # Arrange: reload module to reset in-memory activities
    reload(app_module)
    with TestClient(app_module.app) as client:
        yield client
