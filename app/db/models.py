from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String, index=True, nullable=False)
    artist = Column(String, nullable=False)

class Recommendation(Base):
    __tablename__ = 'recommendations'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    song_id = Column(Integer, ForeignKey('songs.id'), nullable=False)
    comment = Column(String, index=True, nullable=True)

class UserMusic(Base):
    __tablename__ = 'user_music'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    song_id = Column(Integer, ForeignKey('songs.id'), primary_key=True)
