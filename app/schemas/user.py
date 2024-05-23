from typing import Optional
from pydantic import UUID4, EmailStr, BaseModel

class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = None

class UserCreate(UserBase):
    email: EmailStr
    username: str
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserInDBBase(UserBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True

class User(UserInDBBase):
    pass

class UserInDB(UserInDBBase):
    hashed_password: str
