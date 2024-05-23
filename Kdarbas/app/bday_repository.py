from abc import ABC, abstractmethod
from typing import List
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import models as mod
import schemas as scheme

class BirthdayMethod(ABC):
    @abstractmethod
    def create_birthday(db: Session, birthday_create: scheme.BirthdayCreate, user_id: int):
        pass

    @abstractmethod
    def get_birthdays(db: Session, user_id: int):
        pass

    @abstractmethod
    def update_birthday(db: Session, birthday_id: int, birthday_update: scheme.BirthdayCreate):
        pass

    @abstractmethod
    def delete_birthday(db: Session, birthday_id: int):
        pass


class BdayRepository(BirthdayMethod):
    def create_birthday(db: Session, birthday_create: scheme.BirthdayCreate, user_id: int):
        birthday = mod.Birthday(user_id = user_id, Name=birthday_create.Name, B_date=birthday_create.Date)

        db.add(birthday)
        db.commit()
        db.refresh(birthday)

        return birthday
    

    def get_birthdays(db: Session, user_id: int):
        return db.query(mod.Birthday).filter(mod.Birthday.user_id == user_id).all()


    def update_birthday(db: Session, birthday_id: int, birthday_update: scheme.BirthdayCreate):
        birthday = db.query(mod.Birthday).filter(mod.Birthday.id == birthday_id).first()

        if not birthday:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Birthday with id {birthday_id} not found"
            )


        birthday.Name = birthday_update.Name
        birthday.B_date = birthday_update.Date
        db.commit()

        return birthday


    def delete_birthday(db: Session, birthday_id: int):
        birthday = db.query(mod.Birthday).filter(mod.Birthday.id == birthday_id)

        if not birthday.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Birthday with id {birthday_id} not found"
            )
    
        birthday.delete(synchronize_session=False)
        db.commit()

        return {"details": "Success"}
    

    def get_all_birthdays(db: Session):
        birthdays = db.query(mod.Birthday).all()

        if not birthdays:
            raise HTTPException(status_code=404, detail="Birthdays not found")
        
        return birthdays