import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))


from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from database_config import Base

class Maridaje(Base):
    __tablename__ = "maridaje"
    __table_args__ = {'extend_existing': True}

    # Columnas
    id_maridaje = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String, nullable=False)
    nombre = Column(String, unique=True, nullable=False)

    vinos = relationship("Vino", secondary="vinoXmaridaje", back_populates="maridaje")
    def __init__(self, descripcion, nombre):
        self.descripcion = descripcion
        self.nombre = nombre

    def __repr__(self):
        return f"<Maridaje(nombre='{self.nombre}', descripcion='{self.descripcion}')>"
