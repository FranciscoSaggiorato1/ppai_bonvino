from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from database_config import Base

class Siguiendo(Base):
    __tablename__ = "siguiendo"
    __table_args__ = {'extend_existing': True}

    # Columnas
    id_siguiendo = Column(Integer, primary_key=True, autoincrement=True)
    fechaInicio = Column(Date, nullable=False)
    fechaFin = Column(Date, nullable=True)
    id_enofilo_seguido = Column(Integer, ForeignKey("enofilo.id_enofilo"), nullable=True)
    id_bodega = Column(Integer, ForeignKey("bodega.id_bodega"), nullable=True)
    id_enofilo_seguidor = Column(Integer, ForeignKey("enofilo.id_enofilo"), nullable=False)

    # Relaciones
    enofilo_seguido = relationship("Enofilo", foreign_keys=[id_enofilo_seguido], back_populates="seguidores")
    enofilo_seguidor = relationship("Enofilo", foreign_keys=[id_enofilo_seguidor], back_populates="seguidos")
    bodega = relationship("Bodega", back_populates="seguidos")

    def __init__(self, fechaInicio, fechaFin, id_enofilo_seguido, id_bodega, id_enofilo_seguidor):
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.id_enofilo_seguido = id_enofilo_seguido
        self.id_bodega = id_bodega
        self.id_enofilo_seguidor = id_enofilo_seguidor

    def __repr__(self):
        return f"<Siguiendo(enofilo_seguidor_id='{self.id_enofilo_seguidor}', enofilo_seguido_id='{self.id_enofilo_seguido}', fechaInicio='{self.fechaInicio}')>"
