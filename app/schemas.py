from pydantic import BaseModel
from typing import Optional, List

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    hashed_password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

class SongBase(BaseModel):
    title: str
    artist: str

class SongCreate(SongBase):
    pass

class Song(SongBase):
    id: int

    class Config:
        from_attributes = True

class RecommendationBase(BaseModel):
    user_id: int
    song_id: int
    comment: Optional[str] = None

class RecommendationCreate(RecommendationBase):
    pass

class Recommendation(RecommendationBase):
    id: int

    class Config:
        from_attributes = True

class UserMusicBase(BaseModel):
    user_id: int
    song_id: int

class UserMusicCreate(UserMusicBase):
    pass

class UserMusic(UserMusicBase):
    class Config:
        from_attributes = True
