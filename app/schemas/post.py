from typing import Optional
from pydantic import UUID4, BaseModel

class PostBase(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None

class PostCreate(PostBase):
    title: str
    body: str

class PostUpdate(PostBase):
    pass

class PostInDBBase(PostBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True

class Post(PostInDBBase):
    pass

class PostInDB(PostInDBBase):
    pass
