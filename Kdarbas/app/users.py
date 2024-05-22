from abc import ABC, abstractmethod
from models import User
from schemas import UserCreate

class User(ABC):
    @abstractmethod
    def create_user(self, user: UserCreate) -> User:
        pass

class RegularUser(User):
    def create_user(self, user: UserCreate) -> User:
        return User(name=user.name, email=user.email)
