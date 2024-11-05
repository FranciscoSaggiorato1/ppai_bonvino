import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))


from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Table
from sqlalchemy.orm import relationship
from database_config import Base

# Tabla intermedia para la relación muchos a muchos entre Vino y Varietal
vino_varietal = Table(
    'vinoXvarietal',
    Base.metadata,
    Column('id_vino', Integer, ForeignKey('vino.id_vino'), primary_key=True),
    Column('id_varietal', Integer, ForeignKey('varietal.id_varietal'), primary_key=True),
    extend_existing=True
)

# Tabla intermedia para la relación muchos a muchos entre Vino y Maridaje
vino_maridaje = Table(
    'vinoXmaridaje',
    Base.metadata,
    Column('id_vino', Integer, ForeignKey('vino.id_vino'), primary_key=True),
    Column('id_maridaje', Integer, ForeignKey('maridaje.id_maridaje'), primary_key=True),
    extend_existing=True
)

class Vino(Base):
    __tablename__ = "vino"
    __table_args__ = {'extend_existing': True}

    # Columnas
    id_vino = Column(Integer, primary_key=True, autoincrement=True)
    añada = Column(Integer, nullable=False)
    fechaActualizacion = Column(Date, nullable=False)
    nombre = Column(String, nullable=False, unique=True)
    imagenEtiqueta = Column(String)
    notaCata = Column(String)
    precioArs = Column(Float, nullable=False)
    
    # Clave foránea hacia la tabla bodega
    id_bodega = Column(Integer, ForeignKey("bodega.id_bodega"), nullable=False)

    # Relaciones
    maridaje = relationship("Maridaje", secondary=vino_maridaje, back_populates="vinos")
    varietal = relationship("Varietal", secondary=vino_varietal, back_populates="vinos")
    bodega = relationship("Bodega", back_populates="vinos")
    

    def __init__(self, añada, fechaActualizacion, nombre, imagenEtiqueta, notaCata, precioArs, bodega):
        self.añada = añada
        self.fechaActualizacion = fechaActualizacion
        self.nombre = nombre
        self.imagenEtiqueta = imagenEtiqueta
        self.notaCata = notaCata
        self.precioArs = precioArs
        self.bodega = bodega

    def __repr__(self):
        return f"<Vino(nombre='{self.nombre}', añada='{self.añada}', precio='{self.precioArs}')>"
