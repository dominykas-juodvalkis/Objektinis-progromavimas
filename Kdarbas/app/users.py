from abc import ABC, abstractmethod
import models as mod
import schemas as schemas

class User(ABC):
    @abstractmethod
    def create_user(name: str, email: str):
        pass

class RegularUser(User):
    def create_user(name: str, email: str):
        return mod.User(Name=name, Email=email)
