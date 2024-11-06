import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))


from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from database_config import Base

class Usuario(Base):
    __tablename__ = "usuario"
    __table_args__ = {'extend_existing': True}

    # Columnas
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    contraseña = Column(String, nullable=False)
    nombre = Column(String, nullable=False, unique=True)
    premium = Column(Boolean, default=False)

    enofilo = relationship("Enofilo", back_populates="usuario")

    def __init__(self, contraseña, nombre, premium):
        self.contraseña = contraseña
        self.nombre = nombre
        self.premium = premium

    def __repr__(self):
        return f"<Usuario(nombre='{self.nombre}', premium='{self.premium}')>"
