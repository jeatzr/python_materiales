from fastapi import FastAPI

from database.database import Base, engine
from routes import users

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "API de usuarios con FastAPI y SQLite"}