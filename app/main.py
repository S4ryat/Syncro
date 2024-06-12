from typing import Any, List
from fastapi import FastAPI, HTTPException, Depends
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session
from app.actions import CRUDOperations
from app.db.database import get_db
from app.schemas import User, UserCreate, Song, SongCreate, Recommendation, RecommendationCreate, UserMusic, UserMusicCreate
from app.db.models import User as SQLAlchemyUser, Song as SQLAlchemySong, Recommendation as SQLAlchemyRecommendation, UserMusic as SQLAlchemyUserMusic

app = FastAPI(
    title="Music Recommendation API",
    description="API for Music Recommendation",
    version="1.0.0",
)

user_crud = CRUDOperations(SQLAlchemyUser)
song_crud = CRUDOperations(SQLAlchemySong)
recommendation_crud = CRUDOperations(SQLAlchemyRecommendation)
user_music_crud = CRUDOperations(SQLAlchemyUserMusic)

@app.get("/")
def index():
    return {"message": "Hello world!"}

# User Endpoints
@app.get("/users", response_model=List[User], tags=["users"])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> Any:
    users = user_crud.get_all(db=db, skip=skip, limit=limit)
    return users

@app.post("/users", response_model=User, status_code=HTTP_201_CREATED, tags=["users"])
def create_user(body: UserCreate, db: Session = Depends(get_db)) -> Any:
    user = user_crud.create(db=db, obj_in=body)
    return user

@app.put("/users/{id}", response_model=User, tags=["users"])
def update_user(id: int, user_in: UserCreate, db: Session = Depends(get_db)) -> Any:
    user = user_crud.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")
    user = user_crud.update(db=db, db_obj=user, obj_in=user_in)
    return user

@app.get("/users/{id}", response_model=User, tags=["users"])
def get_user(id: int, db: Session = Depends(get_db)) -> Any:
    user = user_crud.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")
    return user

@app.delete("/users/{id}", response_model=User, tags=["users"])
def delete_user(id: int, db: Session = Depends(get_db)) -> Any:
    user = user_crud.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")
    user = user_crud.remove(db=db, id=id)
    return user

# Song Endpoints
@app.get("/songs", response_model=List[Song], tags=["songs"])
def list_songs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> Any:
    songs = song_crud.get_all(db=db, skip=skip, limit=limit)
    return songs

@app.post("/songs", response_model=Song, status_code=HTTP_201_CREATED, tags=["songs"])
def create_song(body: SongCreate, db: Session = Depends(get_db)) -> Any:
    song = song_crud.create(db=db, obj_in=body)
    return song

@app.put("/songs/{id}", response_model=Song, tags=["songs"])
def update_song(id: int, song_in: SongCreate, db: Session = Depends(get_db)) -> Any:
    song = song_crud.get(db=db, id=id)
    if not song:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Song not found")
    song = song_crud.update(db=db, db_obj=song, obj_in=song_in)
    return song

@app.get("/songs/{id}", response_model=Song, tags=["songs"])
def get_song(id: int, db: Session = Depends(get_db)) -> Any:
    song = song_crud.get(db=db, id=id)
    if not song:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Song not found")
    return song

@app.delete("/songs/{id}", response_model=Song, tags=["songs"])
def delete_song(id: int, db: Session = Depends(get_db)) -> Any:
    song = song_crud.get(db=db, id=id)
    if not song:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Song not found")
    song = song_crud.remove(db=db, id=id)
    return song

# Recommendation Endpoints
@app.get("/recommendations", response_model=List[Recommendation], tags=["recommendations"])
def list_recommendations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> Any:
    recommendations = recommendation_crud.get_all(db=db, skip=skip, limit=limit)
    return recommendations

@app.post("/recommendations", response_model=Recommendation, status_code=HTTP_201_CREATED, tags=["recommendations"])
def create_recommendation(body: RecommendationCreate, db: Session = Depends(get_db)) -> Any:
    recommendation = recommendation_crud.create(db=db, obj_in=body)
    return recommendation

@app.put("/recommendations/{id}", response_model=Recommendation, tags=["recommendations"])
def update_recommendation(id: int, recommendation_in: RecommendationCreate, db: Session = Depends(get_db)) -> Any:
    recommendation = recommendation_crud.get(db=db, id=id)
    if not recommendation:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Recommendation not found")
    recommendation = recommendation_crud.update(db=db, db_obj=recommendation, obj_in=recommendation_in)
    return recommendation

@app.get("/recommendations/{id}", response_model=Recommendation, tags=["recommendations"])
def get_recommendation(id: int, db: Session = Depends(get_db)) -> Any:
    recommendation = recommendation_crud.get(db=db, id=id)
    if not recommendation:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Recommendation not found")
    return recommendation

@app.delete("/recommendations/{id}", response_model=Recommendation, tags=["recommendations"])
def delete_recommendation(id: int, db: Session = Depends(get_db)) -> Any:
    recommendation = recommendation_crud.get(db=db, id=id)
    if not recommendation:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Recommendation not found")
    recommendation = recommendation_crud.remove(db=db, id=id)
    return recommendation

# UserMusic Endpoints
@app.get("/user_music", response_model=List[UserMusic], tags=["user_music"])
def list_user_music(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> Any:
    user_music = user_music_crud.get_all(db=db, skip=skip, limit=limit)
    return user_music

@app.post("/user_music", response_model=UserMusic, status_code=HTTP_201_CREATED, tags=["user_music"])
def create_user_music(body: UserMusicCreate, db: Session = Depends(get_db)) -> Any:
    user_music = user_music_crud.create(db=db, obj_in=body)
    return user_music

@app.put("/user_music/{user_id}/{song_id}", response_model=UserMusic, tags=["user_music"])
def update_user_music(user_id: int, song_id: int, user_music_in: UserMusicCreate, db: Session = Depends(get_db)) -> Any:
    user_music = user_music_crud.get(db=db, id=(user_id, song_id))
    if not user_music:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="UserMusic not found")
    user_music = user_music_crud.update(db=db, db_obj=user_music, obj_in=user_music_in)
    return user_music

@app.get("/user_music/{user_id}/{song_id}", response_model=UserMusic, tags=["user_music"])
def get_user_music(user_id: int, song_id: int, db: Session = Depends(get_db)) -> Any:
    user_music = user_music_crud.get(db=db, id=(user_id, song_id))
    if not user_music:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="UserMusic not found")
    return user_music

@app.delete("/user_music/{user_id}/{song_id}", response_model=UserMusic, tags=["user_music"])
def delete_user_music(user_id: int, song_id: int, db: Session = Depends(get_db)) -> Any:
    user_music = user_music_crud.get(db=db, id=(user_id, song_id))
    if not user_music:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="UserMusic not found")
    user_music = user_music_crud.remove(db=db, id=(user_id, song_id))
    return user_music
