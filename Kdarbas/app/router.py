from datetime import date
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models as mod
import database as data
import user_repository as UserRep
import bday_repository as BdayRep
import schemas as scheme
import files as oper

router = APIRouter(
    prefix='/api/bday'
)

def get_db():
    db = data.Database.get_db()
    try:
        yield db
    finally:
        db.close()


# User -----

@router.post("/users/", response_model=scheme.UserRead, tags=["Users"])
def create_user(user_create: scheme.UserCreate, db: Session = Depends(get_db)):
    user = UserRep.UserRepository.create_user(db, user_create)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user.id, "Name": user.Name, "Email": user.Email}


@router.get("/users/", response_model=List[scheme.UserRead], tags=["Users"])
def read_users(db: Session = Depends(get_db)):
    users = UserRep.UserRepository.get_users(db=db)
    if not users:
        raise HTTPException(status_code=404, detail="User Error")
    user_dicts = [{"id": user.id, "Name": user.Name, "Email": user.Email} for user in users]
    return user_dicts


@router.put("/users/{user_id}/", response_model=scheme.UserRead, tags=["Users"])
def update_user(user_id: int, user_update: scheme.UserCreate, db: Session = Depends(get_db)):
    user = UserRep.UserRepository.update_user(db, user_id, user_update)
    return {"id": user.id, "Name": user.Name, "Email": user.Email}


@router.delete("/users/{user_id}/", response_model=scheme.UserRead, tags=["Users"])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    UserRep.UserRepository.delete_user(db, user_id)
    return {"id": user_id, "Name": 'deleted', "Email": 'deleted'}


# Birthday -------

@router.post("/birthdays/", response_model=scheme.BirthdayRead, tags=["Birthdays"])
def create_birthday(user_id: int, birthday_create: scheme.BirthdayCreate, db: Session = Depends(get_db)):
    user = db.query(mod.User).filter(mod.User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )
    
    birthday = BdayRep.BdayRepository.create_birthday(db, birthday_create, user_id)
    if not birthday:
        raise HTTPException(status_code=404, detail="Birthday Error")
    
    return {"id": birthday.id, "user_id": birthday.user_id, "Name": birthday.Name, "Date": birthday.B_date}

    


@router.get("/users/{user_id}/birthdays/", response_model=List[scheme.BirthdayRead], tags=["Birthdays"])
def read_birthdays(user_id: int, db: Session = Depends(get_db)):
    birthdays = BdayRep.BdayRepository.get_birthdays(db, user_id)
    if not birthdays:
        raise HTTPException(status_code=404, detail="Birthdays not found")
    bday_dicts = [{"id": birthday.id, "user_id": birthday.user_id, "Name": birthday.Name, "Date": birthday.B_date} for birthday in birthdays]
    return bday_dicts


@router.put("/birthdays/{birthday_id}/", response_model=scheme.BirthdayRead, tags=["Birthdays"])
def update_birthday(birthday_id: int, birthday_update: scheme.BirthdayCreate, db: Session = Depends(get_db)):
    birthday = BdayRep.BdayRepository.update_birthday(db, birthday_id, birthday_update)
    return {"id": birthday.id, "user_id": birthday.user_id, "Name": birthday.Name, "Date": birthday.B_date}


@router.delete("/birthdays/{birthday_id}/", response_model=scheme.BirthdayRead, tags=["Birthdays"])
def delete_birthday(birthday_id: int, db: Session = Depends(get_db)):
    BdayRep.BdayRepository.delete_birthday(db, birthday_id)
    return {"id": birthday_id, "user_id": 0, "Name": 'deleted', "Date": date(1, 1, 1)}


# Files -------


@router.get("/save-birthdays/", response_model=List[scheme.BirthdayRead], tags=["Files"])
async def save_birthdays(db: Session = Depends(get_db)):
    birthdays = BdayRep.BdayRepository.get_all_birthdays(db)

    birthday_list = [scheme.BirthdayRead.from_orm(birthday) for birthday in birthdays]
    oper.FileOperator.save_birthdays_to_file(birthday_list, oper.filename)
    return birthday_list
