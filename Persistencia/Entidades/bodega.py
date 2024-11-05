import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))


from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship
from database_config import Base

class Bodega(Base):
    __tablename__ = "bodega"

    # Columnas
    id_bodega = Column(Integer, primary_key=True, autoincrement=True)
    coordenadasUbicacion = Column(String)
    descripcion = Column(String)
    historia = Column(String)
    nombre = Column(String, unique=True, nullable=False)
    periodoActualizacion = Column(Integer)  # En meses
    fechaUltimaActualizacion = Column(Date)

    # Relación inversa con Vino
    vinos = relationship("Vino", back_populates="bodega")

    def __init__(self, coordenadasUbicacion, descripcion, historia, nombre, periodoActualizacion, fechaUltimaActualizacion):
        self.coordenadasUbicacion = coordenadasUbicacion
        self.descripcion = descripcion
        self.historia = historia
        self.nombre = nombre
        self.periodoActualizacion = periodoActualizacion
        self.fechaUltimaActualizacion = fechaUltimaActualizacion

    def __repr__(self):
        return f"<Bodega(nombre='{self.nombre}', descripcion='{self.descripcion}', historia='{self.historia}')>"
