from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from database_config import Base

class Siguiendo(Base):
    __tablename__ = "siguiendo"

    # Columnas
    id_siguiendo = Column(Integer, primary_key=True, autoincrement=True)
    fechaInicio = Column(Date, nullable=False)
    fechaFin = Column(Date, nullable=True)
    id_enofilo = Column(Integer, ForeignKey("enofilo.id_enofilo"), nullable=False)
    id_bodega = Column(Integer, ForeignKey("bodega.id_bodega"), nullable=False)

    # Relaciones
    enofilo = relationship("Enofilo", back_populates="seguidos")
    bodega = relationship("Bodega")

    def __init__(self, fechaInicio, fechaFin, enofilo, bodega):
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.enofilo = enofilo
        self.bodega = bodega

    def __repr__(self):
        return f"<Siguiendo(enofilo_id='{self.id_enofilo}', bodega_id='{self.id_bodega}', fechaInicio='{self.fechaInicio}')>"
