from fastapi.testclient import TestClient
from app.main import app
from app.db.database import SessionLocal, engine
from app.db.models import Base, User, UserMusic

client = TestClient(app)

def setup_module(module):
    Base.metadata.create_all(bind=engine)

def teardown_module(module):
    Base.metadata.drop_all(bind=engine)

def test_recommend_profiles():
    db = SessionLocal()

    # Créer des utilisateurs et des musiques pour le tests
    user1 = User(email="user1@example.com", hashed_password="fakehashedpassword")
    user2 = User(email="user2@example.com", hashed_password="fakehashedpassword")
    music1 = Music(title="Song1")
    music2 = Music(title="Song2")

    db.add(user1)
    db.add(user2)
    db.add(music1)
    db.add(music2)
    db.commit()

   # user_music1 = UserMusic(user_id=user1.id, music_id=music1.id)
     # user_music2 = UserMusic(user_id=user2.id, music_id=music1.id)

   # db.add(user_music1)
    # db.add(user_music2)
    # db.commit()

    response = client.get(f"/recommendations/{user1.id}")
    assert response.status_code == 200
    assert len(response.json()) > 0

    db.close()
