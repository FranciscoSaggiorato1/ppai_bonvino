from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from database_config import Base

class Usuario(Base):
    __tablename__ = "usuario"

    # Columnas
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False, unique=True)
    contraseña = Column(String, nullable=False)
    premium = Column(Boolean, default=False)

    enofilos = relationship("Enofilo", back_populates="usuario")

    def __init__(self, nombre, contraseña, premium):
        self.nombre = nombre
        self.contraseña = contraseña
        self.premium = premium

    def __repr__(self):
        return f"<Usuario(nombre='{self.nombre}', premium='{self.premium}')>"
