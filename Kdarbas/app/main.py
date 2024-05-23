from fastapi import FastAPI
import router as Myrouter
import database as data

app = FastAPI()
app.include_router(Myrouter.router)

@app.get("/")
def read_root():
    return {"message": "Root URL"}

data.Base.metadata.create_all(data.engine)

for route in app.routes:
    print(f"{route.path} -> {route.name}")
