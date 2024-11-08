import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))


from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database_config import Base

class Varietal(Base):
    __tablename__ = "varietal"
    __table_args__ = {'extend_existing': True}

    # Columnas
    id_varietal= Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String, nullable=False)
    porcentajeComposicion = Column(String, nullable=False)
    tipo_uva_id = Column(Integer, ForeignKey("tipo_uva.id_tipo_uva"), nullable=False)

    # Relaciones
    tipoUva = relationship("TipoUva")
    vinos = relationship("Vino", secondary="vinoXvarietal", back_populates="varietal")

    def __init__(self, descripcion, porcentajeComposicion, tipoUva):
        self.descripcion = descripcion
        self.porcentajeComposicion = porcentajeComposicion
        self.tipoUva = tipoUva

    def __repr__(self):
        return f"<Varietal(descripcion='{self.descripcion}', porcentajeComposicion='{self.porcentajeComposicion}')>"
