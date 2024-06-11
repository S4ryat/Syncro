from fastapi.testclient import TestClient
from app.main import app
from app.db.database import SessionLocal, Base
import pytest

client = TestClient(app)

@pytest.fixture(scope="module")
def test_db():
    # Set up tests database
    Base.metadata.create_all(bind=SessionLocal.bind)
    yield
    # Tear down tests database
    Base.metadata.drop_all(bind=SessionLocal.bind)

def test_create_music(test_db):
    response = client.post("/music", json={"title": "Test Music", "artist": "Test Artist"})
    assert response.status_code == 201
    assert response.json()["title"] == "Test Music"

def test_read_music(test_db):
    response = client.get("/music")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_update_music(test_db):
    music_id = client.get("/music").json()[0]["id"]
    response = client.put(f"/music/{music_id}", json={"title": "Updated Music", "artist": "Updated Artist"})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Music"

def test_delete_music(test_db):
    music_id = client.get("/music").json()[0]["id"]
    response = client.delete(f"/music/{music_id}")
    assert response.status_code == 200
    assert client.get(f"/music/{music_id}").status_code == 404
