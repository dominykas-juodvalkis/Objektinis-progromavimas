from pydantic import BaseModel, EmailStr
from datetime import date


# User -----

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True



#Birthday -------

class BirthdayCreate(BaseModel):
    user_id: int
    name: str
    date: date

class BirthdayRead(BaseModel):
    id: int
    user_id: int
    name: str
    date: date

    class Config:
        from_attributes = True
    