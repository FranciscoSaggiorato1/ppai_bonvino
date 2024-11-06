import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))


from sqlalchemy import Column, String, Integer
from database_config import Base

class TipoUva(Base):
    __tablename__ = "tipo_uva"
    __table_args__ = {'extend_existing': True}

    # Columnas
    id_tipo_uva = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String, nullable=False)
    nombre = Column(String, unique=True, nullable=False)

    def __init__(self, descripcion, nombre):
        self.descripcion = descripcion
        self.nombre = nombre

    def __repr__(self):
        return f"<TipoUva(nombre='{self.nombre}', descripcion='{self.descripcion}')>"
