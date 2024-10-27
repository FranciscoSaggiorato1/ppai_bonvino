from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Table
from sqlalchemy.orm import relationship
from database_config import Base

# Tabla intermedia para la relación muchos a muchos entre Vino y Varietal
vino_varietal = Table(
    'vino_varietal',
    Base.metadata,
    Column('id_vino', Integer, ForeignKey('vino.id_vino'), primary_key=True),
    Column('id_varietal', Integer, ForeignKey('varietal.id_varietal'), primary_key=True)
)

# Tabla intermedia para la relación muchos a muchos entre Vino y Maridaje
vino_maridaje = Table(
    'vino_maridaje',
    Base.metadata,
    Column('id_vino', Integer, ForeignKey('vino.id_vino'), primary_key=True),
    Column('id_maridaje', Integer, ForeignKey('maridaje.id_maridaje'), primary_key=True)
)

class Vino(Base):
    __tablename__ = "vino"

    # Columnas
    id_vino = Column(Integer, primary_key=True, autoincrement=True)
    añada = Column(Integer, nullable=False)
    nombre = Column(String, nullable=False, unique=True)
    fechaActualizacion = Column(Date, nullable=False)
    imagenEtiqueta = Column(String)
    notaCata = Column(String)
    precioArs = Column(Float, nullable=False)
    
    # Clave foránea hacia la tabla bodega
    id_bodega = Column(Integer, ForeignKey("bodega.id_bodega"), nullable=False)

    # Relaciones
    bodega = relationship("Bodega", back_populates="vinos")
    varietales = relationship("Varietal", secondary=vino_varietal, back_populates="vinos")
    maridajes = relationship("Maridaje", secondary=vino_maridaje, back_populates="vinos")

    def __init__(self, añada, fechaActualizacion, nombre, imagenEtiqueta, notaCata, precioArs, bodega):
        self.añada = añada
        self.nombre = nombre
        self.fechaActualizacion = fechaActualizacion
        self.imagenEtiqueta = imagenEtiqueta
        self.notaCata = notaCata
        self.precioArs = precioArs
        self.bodega = bodega

    def __repr__(self):
        return f"<Vino(nombre='{self.nombre}', añada='{self.añada}', precio='{self.precioArs}')>"
