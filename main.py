from fastapi import FastAPI
from riego import router
from database import engine, Base
from models_db import RegistroHumedad

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Sistema de Riego Automatizado",
    version="1.0"
)

app.include_router(router, prefix="/riego")