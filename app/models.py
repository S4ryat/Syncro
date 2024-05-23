from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)


class Post(BaseModel):
    __tablename__ = "posts"

    title = Column(String)
    body = Column(Text)
