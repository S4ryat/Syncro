from typing import Any, Dict, List, Optional, Union, Type
from sqlalchemy.orm import Session
from app.db.models import Base

class CRUDOperations:

    def __init__(self, model: Type[Base]):
        self.model = model

    def get(self, db: Session, id: int) -> Optional[Base]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[Base]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in: Base) -> Base:
        db_obj = self.model(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        db_obj: Base,
        obj_in: Union[Base, Dict[str, Any]],
    ) -> Base:
        update_data = (
            obj_in if isinstance(obj_in, dict) else obj_in.dict(exclude_unset=True)
        )
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, id: int) -> Base:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj
