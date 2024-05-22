from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from ..models import User, Birthday
from ..schemas import UserCreate, BirthdayCreate

class UserMethod(ABC):
    @abstractmethod
    def get_user(self, db: Session, user_id: int) -> User:
        pass

    @abstractmethod
    def create_user(self, db: Session, user: UserCreate) -> User:
        pass

    @abstractmethod
    def update_user(self, db: Session, user_id: int, user_update: UserUpdate) -> User:
        pass

    @abstractmethod
    def delete_user(self, db: Session, user_id: int) -> User:
        pass


class BirthdayMethod(ABC):
    @abstractmethod
    def get_birthdays(self, db: Session, user_id: int) -> list[Birthday]:
        pass

    @abstractmethod
    def create_birthday(self, db: Session, birthday: BirthdayCreate) -> Birthday:
        pass

    @abstractmethod
    def update_birthday(self, db: Session, birthday_id: int, birthday_update: BirthdayUpdate) -> Birthday:
        pass

    @abstractmethod
    def delete_birthday(self, db: Session, birthday_id: int) -> Birthday:
        pass