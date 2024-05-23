from typing import Optional
from pydantic import BaseModel, BaseConfig, EmailStr
from datetime import date


# User -----

class UserCreate(BaseModel):
    Name: str
    Email: EmailStr


class UserRead(BaseModel):
    id: int
    Name: str
    Email: EmailStr

    class Config:
        orm_mode = True


# Birthday -------

class BirthdayCreate(BaseModel):
    Name: str
    Date: date


class BirthdayRead(BaseModel):
    id: Optional[int]
    user_id: Optional[int]
    Name: str = "Friend"
    Date: date = date.today()

    class Config:
        orm_mode = True
