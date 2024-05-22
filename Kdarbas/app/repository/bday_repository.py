from sqlalchemy.orm import Session
from ..models import Birthday
from ..schemas import BirthdayCreate
from repo_structure import BirthdayMethod
from typing import List

class BdayRepository(BirthdayMethod):
    def get_birthdays(self, db: Session, user_id: int) -> List[Birthday]:
        return db.query(Birthday).filter(Birthday.user_id == user_id).all()

    def create_birthday(self, db: Session, birthday: BirthdayCreate) -> Birthday:
        db_birthday = Birthday(user_id=birthday.user_id, name=birthday.name, date=birthday.date)
        db.add(db_birthday)
        db.commit()
        db.refresh(db_birthday)
        return db_birthday
    
    def update_birthday(self, db: Session, birthday_id: int, birthday_update: BirthdayCreate) -> Birthday:
        db_birthday = db.query(Birthday).filter(Birthday.id == birthday_id).first()
        if db_birthday:
            for key, value in birthday_update.dict(exclude_unset=True).items():
                setattr(db_birthday, key, value)
            db.commit()
            db.refresh(db_birthday)
        return db_birthday

    def delete_birthday(self, db: Session, birthday_id: int) -> Birthday:
        birthday = db.query(Birthday).filter(Birthday.id == birthday_id).first()
        if birthday:
            db.delete(birthday)
            db.commit()
        return birthday