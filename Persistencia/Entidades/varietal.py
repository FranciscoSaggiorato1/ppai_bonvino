from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database_config import Base

class Varietal(Base):
    __tablename__ = "varietal"

    # Columnas
    id_varietal= Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String, nullable=False)
    porcentajeComposicion = Column(Float, nullable=False)
    tipo_uva_id = Column(Integer, ForeignKey("tipo_uva.id_tipo_uva"), nullable=False)

    # Relaciones
    tipoUva = relationship("TipoUva")
    vinos = relationship("Vino", secondary="vino_varietal", back_populates="varietales")

    def __init__(self, descripcion, porcentajeComposicion, tipoUva):
        self.descripcion = descripcion
        self.porcentajeComposicion = porcentajeComposicion
        self.tipoUva = tipoUva

    def __repr__(self):
        return f"<Varietal(descripcion='{self.descripcion}', porcentajeComposicion='{self.porcentajeComposicion}')>"
