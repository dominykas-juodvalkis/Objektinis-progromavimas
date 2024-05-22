from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import Database
from ..repository.user_repository import UserRepository
from ..repository.bday_repository import BdayRepository
from ..schemas import UserCreate, UserRead, BirthdayCreate, BirthdayRead
from ..users import RegularUser
from ..files import FileOperator as oper, filename

router = APIRouter()


def get_db():
    db = Database().get_db()
    try:
        yield next(db)
    finally:
        next(db).close()


user_repository = UserRepository()
bday_repository = BdayRepository()


# User -----

@router.post("/users/regular/", response_model=UserRead)
def create_regular_user(user: UserCreate, db: Session = Depends(get_db)):
    factory = RegularUser()
    regular_user = factory.create_user(user)
    db_user = user_repository.create_user(db=db, user=regular_user)
    return db_user


@router.put("/users/{user_id}/", response_model=UserRead)
def update_user(user_id: int, user_update: UserCreate, db: Session = Depends(get_db)):
    db_user = user_repository.update_user(db=db, user_id=user_id, user_update=user_update)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.delete("/users/{user_id}/", response_model=UserRead)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_repository.delete_user(db=db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# Birthday -------

@router.post("/birthdays/", response_model=BirthdayRead)
def create_birthday(birthday: BirthdayCreate, db: Session = Depends(get_db)):
    db_birthday = bday_repository.create_birthday(db=db, birthday=birthday)
    return db_birthday


@router.get("/users/{user_id}/birthdays/", response_model=List[BirthdayRead])
def read_birthdays(user_id: int, db: Session = Depends(get_db)):
    birthdays = bday_repository.get_birthdays(db, user_id=user_id)
    if not birthdays:
        raise HTTPException(status_code=404, detail="Birthdays not found")
    return birthdays


@router.put("/birthdays/{birthday_id}/", response_model=BirthdayRead)
def update_birthday(birthday_id: int, birthday_update: BirthdayCreate, db: Session = Depends(get_db)):
    db_birthday = bday_repository.update_birthday(db=db, birthday_id=birthday_id, birthday_update=birthday_update)
    if not db_birthday:
        raise HTTPException(status_code=404, detail="Birthday not found")
    return db_birthday


@router.delete("/birthdays/{birthday_id}/", response_model=BirthdayRead)
def delete_birthday(birthday_id: int, db: Session = Depends(get_db)):
    db_birthday = bday_repository.delete_birthday(db=db, birthday_id=birthday_id)
    if not db_birthday:
        raise HTTPException(status_code=404, detail="Birthday not found")
    return db_birthday


# Files -------


# @router.post("/save-birthdays/")
# async def save_birthdays():
#     oper.save_birthdays_to_file(x, filename)
#     return {"message": "Birthdays saved to file"}

@router.get("/load-birthdays/")
async def load_birthdays(filename):
    birthdays = oper.load_birthdays_from_file(filename)
    return birthdays


@router.post("/add-birthday/")
async def add_birthday(birthday: dict):
    birthdays = oper.load_birthdays_from_file(filename)
    birthdays.append(birthday)
    oper.save_birthdays_to_file(birthdays, filename)
    return {"message": "Birthday added successfully"}


@router.get("/get-birthdays/")
async def get_birthdays():
    return oper.load_birthdays_from_file(filename)
