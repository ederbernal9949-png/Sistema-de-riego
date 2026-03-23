from pydantic import BaseModel

class Sensores(BaseModel):
    humedad1: int
    humedad2: int
    humedad3: int
    humedad4: int

class Config(BaseModel):
    humedad_minima: int