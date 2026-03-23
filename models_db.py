from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class RegistroHumedad(Base):
    __tablename__ = "historial"

    id = Column(Integer, primary_key=True, index=True)
    humedad1 = Column(Integer)
    humedad2 = Column(Integer)
    humedad3 = Column(Integer)
    humedad4 = Column(Integer)
    decision = Column(String)
    fecha = Column(DateTime, default=datetime.utcnow)