from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import threading

SQLALCHEMY_DATABASE_URL = 'sqlite:///.database.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

class Database:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(Database, cls).__new__(cls)
                    cls._instance.engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
                    cls._instance.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=cls._instance.engine)
        return cls._instance
    
    def get_db():
        return SessionLocal()