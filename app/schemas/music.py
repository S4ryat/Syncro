from typing import Optional
from pydantic import UUID4, BaseModel

class MusicBase(BaseModel):
    title: Optional[str] = None
    artist: Optional[str] = None
    genre: Optional[str] = None

class MusicCreate(MusicBase):
    title: str
    artist: str

class MusicUpdate(MusicBase):
    pass

class MusicInDBBase(MusicBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True

class Music(MusicInDBBase):
    pass

class MusicInDB(MusicInDBBase):
    pass
