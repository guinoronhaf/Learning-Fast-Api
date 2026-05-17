from fastapi import FastAPI

from core.database import Base, engine, get_db
from routers.remedio_router import router as remedio_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(remedio_router)

@app.get("/")
def hello():
    return {
            "message": "Hello!"
    }
