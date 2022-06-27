"""Pytest fixtures for the api."""
import pytest
from api.app import flask_app


@pytest.fixture()
def test_app():
    """App fixture for testing purposes."""
    flask_app.config.update({'TESTING': True})
    yield flask_app


@pytest.fixture()
def test_client(test_app):
    """Client that will make requests to our endpoints in tests."""
    with test_app.test_client() as client:
        yield client


class MockResponse:
    """Mocks object that will be returned by requests library."""

    def __init__(self, content, status_code=200):
        self.content = content
        self.status_code = status_code

    def json(self):
        return self.content


@pytest.fixture()
def mock_response():
    """Wrapper to make mocked response available as fixture"""
    return MockResponse
