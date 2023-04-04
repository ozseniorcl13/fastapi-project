import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# this is to include backend dir in sys.path so that we can import from main.py

from fastapi.testclient import TestClient
from fastapi import FastAPI
import pytest
from typing import Generator
from typing import Any

from main import api


@pytest.fixture(scope="function")
def app() -> Generator[FastAPI, Any, None]:
    yield api


@pytest.fixture(scope="function")
def client(
    app: FastAPI
) -> Generator[TestClient, Any, None]:
    with TestClient(app) as client:
        yield client
