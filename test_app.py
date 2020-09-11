""" Testing code to test flask app """
import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    """ create test flask_app client """
    return app.test_client()

def test_index(app, client):
    """ Test Root Url """
    res = client.get('/')
    assert res.status_code == 200, "Test Failed" #First Test
