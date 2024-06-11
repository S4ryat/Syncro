from fastapi.testclient import TestClient
from app.main import app
from app.db.database import engine
from app.db.models import Base

client = TestClient(app)

def setup_module(module):
    Base.metadata.create_all(bind=engine)

def teardown_module(module):
    Base.metadata.drop_all(bind=engine)

def test_signup_user():
    response = client.post("/users/signup", json={"email": "user@example.com", "password": "string"})
    assert response.status_code == 201
    assert "id" in response.json()

def test_login_user():
    client.post("/users/signup", json={"email": "user@example.com", "password": "string"})
    response = client.post("/users/login", data={"username": "user@example.com", "password": "string"})
    assert response.status_code == 200
    assert "access_token" in response.json()
