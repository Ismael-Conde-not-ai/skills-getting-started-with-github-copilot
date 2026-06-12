import pytest
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture
def client():
    """Fixture that provides a TestClient for synchronous testing"""
    with TestClient(app) as c:
        yield c
