from typing import Any, Dict, List, Optional, Union
from sqlalchemy.orm import Session
from pydantic import UUID4

from . import models, schemas

# CRUD Operations for Post
class CRUDPost:
    def get(self, db: Session, id: UUID4) -> Optional[models.Post]:
        return db.query(models.Post).filter(models.Post.id == id).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[models.Post]:
        return db.query(models.Post).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in: schemas.PostCreate) -> models.Post:
        db_obj = models.Post(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: models.Post, obj_in: Union[schemas.PostUpdate, Dict[str, Any]]) -> models.Post:
        update_data = obj_in if isinstance(obj_in, dict) else obj_in.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, id: UUID4) -> models.Post:
        obj = db.query(models.Post).get(id)
        db.delete(obj)
        db.commit()
        return obj

# CRUD Operations for User
class CRUDUser:
    def get(self, db: Session, id: UUID4) -> Optional[models.User]:
        return db.query(models.User).filter(models.User.id == id).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[models.User]:
        return db.query(models.User).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in: schemas.UserCreate) -> models.User:
        db_obj = models.User(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: models.User, obj_in: Union[schemas.UserUpdate, Dict[str, Any]]) -> models.User:
        update_data = obj_in if isinstance(obj_in, dict) else obj_in.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, id: UUID4) -> models.User:
        obj = db.query(models.User).get(id)
        db.delete(obj)
        db.commit()
        return obj

# CRUD Operations for Music
class CRUDMusic:
    def get(self, db: Session, id: UUID4) -> Optional[models.Music]:
        return db.query(models.Music).filter(models.Music.id == id).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[models.Music]:
        return db.query(models.Music).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in: schemas.MusicCreate) -> models.Music:
        db_obj = models.Music(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: models.Music, obj_in: Union[schemas.MusicUpdate, Dict[str, Any]]) -> models.Music:
        update_data = obj_in if isinstance(obj_in, dict) else obj_in.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, id: UUID4) -> models.Music:
        obj = db.query(models.Music).get(id)
        db.delete(obj)
        db.commit()
        return obj

# CRUD Operations for Recommendation
class CRUDRecommendation:
    def get(self, db: Session, id: UUID4) -> Optional[models.Recommendation]:
        return db.query(models.Recommendation).filter(models.Recommendation.id == id).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[models.Recommendation]:
        return db.query(models.Recommendation).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in: schemas.RecommendationCreate) -> models.Recommendation:
        db_obj = models.Recommendation(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: models.Recommendation, obj_in: Union[schemas.RecommendationUpdate, Dict[str, Any]]) -> models.Recommendation:
        update_data = obj_in if isinstance(obj_in, dict) else obj_in.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, id: UUID4) -> models.Recommendation:
        obj = db.query(models.Recommendation).get(id)
        db.delete(obj)
        db.commit()
        return obj

music = CRUDMusic()
user = CRUDUser()
post = CRUDPost()
recommendation = CRUDRecommendation()
