from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import get_db
from utils.log import Loggers


@asynccontextmanager
async def lifespan(app: FastAPI):
    Loggers.init_config()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/db")
async def db_test(db: Session = Depends(get_db)):
    pass
