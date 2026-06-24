from fastapi.testclient import TestClient

import app as app_module


def test_read_root():
    with TestClient(app_module.app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == "Hello, Docker!"


def test_create_and_list_hero():
    with TestClient(app_module.app) as client:
        create_response = client.post(
            "/heroes/",
            json={
                "name": "my hero",
                "secret_name": "austing",
                "age": 12,
            },
        )
        assert create_response.status_code == 200
        created = create_response.json()
        assert created["id"] is not None
        assert created["name"] == "my hero"

        list_response = client.get("/heroes/")
        assert list_response.status_code == 200
        heroes = list_response.json()
        assert len(heroes) >= 1
        assert any(hero["name"] == "my hero" for hero in heroes)
