from __future__ import annotations

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_healthcheck() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_products_returns_data() -> None:
    response = client.get("/products/")
    assert response.status_code == 200
    products = response.json()
    assert isinstance(products, list)
    assert products, "Expected at least one product in the catalogue"
    product = products[0]
    assert {"id", "name", "description", "price", "category", "image_url"} <= set(product)


def test_get_product_by_id() -> None:
    response = client.get("/products/1")
    assert response.status_code == 200
    product = response.json()
    assert product["id"] == 1


def test_get_product_not_found() -> None:
    response = client.get("/products/999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Product with id 999999 not found."
