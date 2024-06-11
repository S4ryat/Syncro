from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_SERVER}:{5432}/{settings.POSTGRES_DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    try:
        db = SessionLocal()
        return db
    finally:
        db.close()
