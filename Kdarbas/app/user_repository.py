from abc import ABC, abstractmethod
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import models as mod
import schemas as scheme
import users as User


class UserMethod(ABC):
    @abstractmethod
    def create_user(db: Session, user_create: scheme.UserCreate):
        pass

    @abstractmethod
    def get_users(db: Session):
        pass

    @abstractmethod
    def update_user(db: Session, user_id: int, user_update: scheme.UserCreate):
        pass

    @abstractmethod
    def delete_user(db: Session, user_id: int):
        pass


class UserRepository(UserMethod):
    def create_user(db: Session, user_create: scheme.UserCreate):
        user = User.RegularUser.create_user(name=user_create.Name, email=user_create.Email)
        db.add(user)
        db.commit()
        db.refresh(user)

        return user
    
    def get_users(db: Session):
        return db.query(mod.User).all()

    def update_user(db: Session, user_id: int, user_update: scheme.UserCreate):
        user = db.query(mod.User).filter(mod.User.id == user_id).first()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found"
        )

        user.Name = user_update.Name
        user.Email = user_update.Email
        db.commit()

        return user

    def delete_user(db: Session, user_id: int):
        user = db.query(mod.User).filter(mod.User.id == user_id)

        if not user.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Human with id {user_id} not found"
            )

        user.delete(synchronize_session=False)
        db.commit()

        return {"details": "Success"}

