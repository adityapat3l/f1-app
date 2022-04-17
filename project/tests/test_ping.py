# from app import main
# from tests.confest import test_app
from tests import test_app


def test_ping(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"environment": "dev", "ping": "pong!", "testing": True}