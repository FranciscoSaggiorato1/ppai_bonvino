from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database_config import Base

class Enofilo(Base):
    __tablename__ = "enofilo"

    # Columnas
    id_enofilo = Column(Integer, primary_key=True, autoincrement=True)
    apellido = Column(String, nullable=False)
    imagenPerfil = Column(String)
    nombre = Column(String, nullable=False)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)

    # Relación con usuario
    usuario = relationship("Usuario", back_populates="enofilo")
    seguidos = relationship("Bodega", secondary="siguiendo")

    def __init__(self, apellido, imagenPerfil, nombre, usuario):
        self.apellido = apellido
        self.imagenPerfil = imagenPerfil
        self.nombre = nombre
        self.usuario = usuario

    def __repr__(self):
        return f"<Enofilo(nombre='{self.nombre}', apellido='{self.apellido}')>"
