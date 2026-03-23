from fastapi import APIRouter
from models import Sensores, Config
from database import SessionLocal
from models_db import RegistroHumedad

router = APIRouter()


config = {
    "humedad_minima": 500  
}

@router.get("/")
def inicio():
    return {"mensaje": "Sistema de riego activo"}


@router.post("/configurar")
def configurar(c: Config):
    config["humedad_minima"] = c.humedad_minima
    return {"mensaje": "Configuración actualizada"}


@router.post("/evaluar")
def evaluar(data: Sensores):

    db = SessionLocal()

    resultado = {
        "zona1": "regar" if data.humedad1 < config["humedad_minima"] else "no_regar",
        "zona2": "regar" if data.humedad2 < config["humedad_minima"] else "no_regar",
        "zona3": "regar" if data.humedad3 < config["humedad_minima"] else "no_regar",
        "zona4": "regar" if data.humedad4 < config["humedad_minima"] else "no_regar"
    }

    registro = RegistroHumedad(
        humedad1=data.humedad1,
        humedad2=data.humedad2,
        humedad3=data.humedad3,
        humedad4=data.humedad4,
        decision=str(resultado)
    )

    db.add(registro)
    db.commit()
    db.close()

    return resultado