"""
Tests fastapi app
"""
import asyncio
import pytest

from starlette.testclient import TestClient

from src.settings.config import configurations
from src.utils.db_manager import db_upgrade, db_downgrade
from src.main import app

@pytest.fixture
def test_app():
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="session", autouse=True)
def do_something(request):
    asyncio.run(db_upgrade())

def pytest_sessionfinish(session, exitstatus):
    asyncio.run(db_downgrade())
