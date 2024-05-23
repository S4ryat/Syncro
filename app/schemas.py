from pydantic import BaseModel, UUID4
from typing import Optional

# Post schemas
class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass

class Post(PostBase):
    id: UUID4

    class Config:
        orm_mode: True


# User schemas
class UserBase(BaseModel):
    email: str
    name: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: UUID4

    class Config:
        orm_mode: True


# Music schemas
class MusicBase(BaseModel):
    title: str
    artist: str

class MusicCreate(MusicBase):
    pass

class MusicUpdate(MusicBase):
    pass

class Music(MusicBase):
    id: UUID4

    class Config:
        orm_mode: True


# Recommendation schemas
class RecommendationBase(BaseModel):
    post_id: UUID4
    user_id: UUID4

class RecommendationCreate(RecommendationBase):
    pass

class RecommendationUpdate(RecommendationBase):
    pass

class Recommendation(RecommendationBase):
    id: UUID4

    class Config:
        orm_mode: True


# HTTP Error schema
class HTTPError(BaseModel):
    detail: str
