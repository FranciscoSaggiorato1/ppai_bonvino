from sqlalchemy import Column, String, Integer
from database_config import Base

class Maridaje(Base):
    __tablename__ = "maridaje"

    # Columnas
    id_maridaje = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String, nullable=False)
    nombre = Column(String, unique=True, nullable=False)

    def __init__(self, descripcion, nombre):
        self.descripcion = descripcion
        self.nombre = nombre

    def __repr__(self):
        return f"<Maridaje(nombre='{self.nombre}', descripcion='{self.descripcion}')>"
