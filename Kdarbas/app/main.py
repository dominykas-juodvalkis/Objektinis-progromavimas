from fastapi import FastAPI
from database import engine
from routers.router import router
from models import Base

app = FastAPI()
app.include_router(router)

Base.metadata.create_all(bind=engine)
