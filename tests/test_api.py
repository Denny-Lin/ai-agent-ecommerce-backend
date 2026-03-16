from fastapi.testclient import TestClient
from backend.server import app

client = TestClient(app)


def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200


def test_get_order():
    response = client.get("/order/1001")
    assert response.status_code == 200