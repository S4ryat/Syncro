from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)

class Post(BaseModel):
    __tablename__ = "posts"
    title = Column(String)
    body = Column(Text)

class User(BaseModel):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    musics = relationship("UserMusic", back_populates="user")
    recommendations = relationship("Recommendation", back_populates="user")
class Music(BaseModel):
    __tablename__ = "musics"
    title = Column(String, index=True, nullable=False)
    artist = Column(String, nullable=False)
    users = relationship("UserMusic", back_populates="music")
    recommendations = relationship("Recommendation", back_populates="music")

class UserMusic(BaseModel):
    __tablename__ = "user_music"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    music_id = Column(Integer, ForeignKey("musics.id"), primary_key=True)
    user = relationship("User", back_populates="musics")
    music = relationship("Music", back_populates="users")

class Recommendation(BaseModel):
    __tablename__ = "recommendations"
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    music_id = Column(Integer, ForeignKey("musics.id"), nullable=False)
    comment = Column(String, index=True, nullable=True)
    user = relationship("User", back_populates="recommendations")
    music = relationship("Music", back_populates="recommendations")
