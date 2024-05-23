import database as data
from sqlalchemy import Column, Integer, String, ForeignKey, Date


# User -----

class User(data.Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, index=True)
    Email = Column(String, unique=True, index=True)


#Birthday -------

class Birthday(data.Base):
    __tablename__ = 'birthdays'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    Name = Column(String, index=True)
    B_date = Column(Date, index=True)