from typing import Any, List

from fastapi import Depends, FastAPI, HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

from app.db.database import SessionLocal, engine
from app import actions, models, schemas
from app.models import User, Post, Music, UserMusic



models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session.
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def index():
    return {"message": "Hello world!"}

# Routes pour Post
@app.get("/posts", response_model=List[schemas.Post], tags=["posts"])
def list_posts(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    posts = actions.post.get_all(db=db, skip=skip, limit=limit)
    return posts

@app.post("/posts", response_model=schemas.Post, status_code=HTTP_201_CREATED, tags=["posts"])
def create_post(*, db: Session = Depends(get_db), post_in: schemas.PostCreate) -> Any:
    post = actions.post.create(db=db, obj_in=post_in)
    return post

@app.put("/posts/{id}", response_model=schemas.Post, responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}}, tags=["posts"])
def update_post(*, db: Session = Depends(get_db), id: UUID4, post_in: schemas.PostUpdate) -> Any:
    post = actions.post.get(db=db, id=id)
    if not post:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Post not found")
    post = actions.post.update(db=db, db_obj=post, obj_in=post_in)
    return post

@app.get("/posts/{id}", response_model=schemas.Post, responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}}, tags=["posts"])
def get_post(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    post = actions.post.get(db=db, id=id)
    if not post:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Post not found")
    return post

@app.delete("/posts/{id}", response_model=schemas.Post, responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}}, tags=["posts"])
def delete_post(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    post = actions.post.get(db=db, id=id)
    if not post:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Post not found")
    post = actions.post.remove(db=db, id=id)
    return post

# Routes pour User
@app.get("/users", response_model=List[schemas.User], tags=["users"])
def list_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    users = actions.user.get_all(db=db, skip=skip, limit=limit)
    return users

@app.post("/users", response_model=schemas.User, status_code=HTTP_201_CREATED, tags=["users"])
def create_user(*, db: Session = Depends(get_db), user_in: schemas.UserCreate) -> Any:
    user = actions.user.create(db=db, obj_in=user_in)
    return user

@app.put("/users/{id}", response_model=schemas.User, responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}}, tags=["users"])
def update_user(*, db: Session = Depends(get_db), id: UUID4, user_in: schemas.UserUpdate) -> Any:
    user = actions.user.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")
    user = actions.user.update(db=db, db_obj=user, obj_in=user_in)
    return user

@app.get("/users/{id}", response_model=schemas.User, responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}}, tags=["users"])
def get_user(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    user = actions.user.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")
    return user

@app.delete("/users/{id}", response_model=schemas.User, responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}}, tags=["users"])
def delete_user(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    user = actions.user.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")
    user = actions.user.remove(db=db, id=id)
    return user

# Routes pour Music
@app.get("/music", response_model=List[schemas.Music], tags=["music"])
def list_music(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    music = actions.music.get_all(db=db, skip=skip, limit=limit)
    return music

@app.post("/music", response_model=schemas.Music, status_code=HTTP_201_CREATED, tags=["music"])
def create_music(*, db: Session = Depends(get_db), music_in: schemas.MusicCreate) -> Any:
    music = actions.music.create(db=db, obj_in=music_in)
    return music

@app.put("/music/{id}", response_model=schemas.Music, responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}}, tags=["music"])
def update_music(*, db: Session = Depends(get_db), id: UUID4, music_in: schemas.MusicUpdate) -> Any:
    music = actions.music.get(db=db, id=id)
    if not music:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Music not found")
    music = actions.music.update(db=db, db_obj=music, obj_in=music_in)
    return music

@app.get("/music/{id}", response_model=schemas.Music, responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}}, tags=["music"])
def get_music(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    music = actions.music.get(db=db, id=id)
    if not music:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Music not found")
    return music

@app.delete("/music/{id}", response_model=schemas.Music, responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}}, tags=["music"])
def delete_music(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    music = actions.music.get(db=db, id=id)
    if not music:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Music not found")
    music = actions.music.remove(db=db, id=id)
    return music

# Routes pour Recommendation
@app.get("/recommendations", response_model=List[schemas.Recommendation], tags=["recommendations"])
def list_recommendations(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    recommendations = actions.get_all(db=db, skip=skip, limit=limit)
    return recommendations

@app.post("/recommendations", response_model=schemas.Recommendation, status_code=HTTP_201_CREATED, tags=["recommendations"])
def create_recommendation(*, db: Session = Depends(get_db), recommendation_in: schemas.RecommendationCreate) -> Any:
    recommendation = actions.recommendation.create(db=db, obj_in=recommendation_in)
    return recommendation

@app.put("/recommendations/{id}", response_model=schemas.Recommendation, responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}}, tags=["recommendations"])
def update_recommendation(*, db: Session = Depends(get_db), id: UUID4, recommendation_in: schemas.RecommendationUpdate) -> Any:
    recommendation = actions.recommendation.get(db=db, id=id)
    if not recommendation:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Recommendation not found")
    recommendation = actions.recommendation.update(db=db, db_obj=recommendation, obj_in=recommendation_in)
    return recommendation

@app.get("/recommendations/{id}", response_model=schemas.Recommendation, responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}}, tags=["recommendations"])
def get_recommendation(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    recommendation = actions.recommendation.get(db=db, id=id)
    if not recommendation:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Recommendation not found")
    return recommendation

@app.delete("/recommendations/{id}", response_model=schemas.Recommendation, responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}}, tags=["recommendations"])
def delete_recommendation(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    recommendation = actions.recommendation.get(db=db, id=id)
    if not recommendation:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Recommendation not found")
    recommendation = actions.recommendation.remove(db=db, id=id)
    return recommendation
