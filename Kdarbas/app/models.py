from database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from datetime import date

# User -----

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)



#Birthday -------

class Birthday(Base):
    __tablename__ = 'birthdays'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String, index=True)
    b_date = Column(Date, index=True)
