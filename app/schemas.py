from pydantic import BaseModel
from typing import Optional, List

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    profils: List["Profil"] = []

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

class GenreBase(BaseModel):
    name: str

class GenreCreate(GenreBase):
    pass

class Genre(GenreBase):
    id: int
    profils: List["Profil"] = []

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

class ProfilBase(BaseModel):
    user_id: int
    genre_id: int
    infos: Optional[str] = None

class ProfilCreate(ProfilBase):
    pass

class Profil(ProfilBase):
    id: int

    class Config:
        from_attributes = True
