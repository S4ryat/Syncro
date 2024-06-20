from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    pseudoname = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    preferences = relationship('UserMusic', back_populates='user')


class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String, index=True, nullable=False)
    artist = Column(String, nullable=False)
    recommendations = relationship('UserMusic', back_populates='song')


class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    profils = relationship('Profil', back_populates='genre')


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
    user = relationship('User', back_populates='preferences')
    song = relationship('Song', back_populates='recommendations')


class Profil(Base):
    __tablename__ = 'profils'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    genre_id = Column(Integer, ForeignKey('genres.id'), primary_key=True)
    user = relationship('User', back_populates='profils')
    song = relationship('genre', back_populates='profils')
