import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))

from database_config import session
from Entidades.bodega import Bodega as BodegaPersistente
from Modelo.bodega import Bodega

class BodegaConversor:

    @staticmethod
    def get_all():
        resultados = session.query(BodegaPersistente).all()
        return [BodegaConversor.mapear_bodega(b) for b in resultados]
    
    @staticmethod
    def get_by_nombre(nombre):
        resultado = session.query(BodegaPersistente).filter(
            BodegaPersistente.nombre == nombre
        ).first()
        return BodegaConversor.mapear_bodega(resultado) if resultado else None

    @staticmethod
    def mapear_bodega(bodega_persistente):
        return Bodega(
            coordenadasUbicacion=bodega_persistente.coordenadasUbicacion,
            descripcion=bodega_persistente.descripcion,
            historia=bodega_persistente.historia,
            nombre=bodega_persistente.nombre,
            periodoActualizacion=bodega_persistente.periodoActualizacion,
            fechaUltimaActualizacion=bodega_persistente.fechaUltimaActualizacion
        )

    @staticmethod
    def guardar_bodega(bodega: Bodega):
        bodega_persistente = BodegaPersistente(
            coordenadasUbicacion=bodega.coordenadasUbicacion,
            descripcion=bodega.descripcion,
            historia=bodega.historia,
            nombre=bodega.nombre,
            periodoActualizacion=bodega.periodoActualizacion,
            fechaUltimaActualizacion=bodega.fechaUltimaActualizacion
        )
        session.add(bodega_persistente)
        session.commit()

    @staticmethod
    def actualizar_bodega(bodega: Bodega):
        bodega_persistente = session.query(BodegaPersistente).filter(
            BodegaPersistente.nombre == bodega.nombre
        ).first()

        if bodega_persistente:
            bodega_persistente.coordenadasUbicacion = bodega.coordenadasUbicacion
            bodega_persistente.descripcion = bodega.descripcion
            bodega_persistente.historia = bodega.historia
            bodega_persistente.periodoActualizacion = bodega.periodoActualizacion
            bodega_persistente.fechaUltimaActualizacion = bodega.fechaUltimaActualizacion

            session.commit()
        else:
            raise ValueError("La bodega especificada no existe en la base de datos.")
    
    @staticmethod
    def eliminar_bodega(nombre):
        bodega_persistente = session.query(BodegaPersistente).filter(
            BodegaPersistente.nombre == nombre
        ).first()
        
        if bodega_persistente:
            session.delete(bodega_persistente)
            session.commit()
        else:
            raise ValueError("La bodega especificada no existe en la base de datos.")
