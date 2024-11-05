import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))

from database_config import session
from Persistencia.Entidades.maridajeDB import Maridaje as MaridajePersistente
from Modelo.maridaje import Maridaje

class MaridajeConversor:

    @staticmethod
    def get_all():
        resultados = session.query(MaridajePersistente).all()
        return [MaridajeConversor.mapear_maridaje(m) for m in resultados]

    @staticmethod
    def get_by_nombre(nombre):
        resultado = session.query(MaridajePersistente).filter(
            MaridajePersistente.nombre == nombre
        ).first()
        return MaridajeConversor.mapear_maridaje(resultado) if resultado else None

    @staticmethod
    def mapear_maridaje(maridaje_persistente):
        return Maridaje(
            descripcion=maridaje_persistente.descripcion,
            nombre=maridaje_persistente.nombre
        )

    @staticmethod
    def guardar_maridaje(maridaje: Maridaje):
        maridaje_persistente = MaridajePersistente(
            descripcion=maridaje.descripcion,
            nombre=maridaje.nombre
        )
        session.add(maridaje_persistente)
        session.commit()
        session.close()

    @staticmethod
    def eliminar_maridaje(nombre):
        maridaje_persistente = session.query(MaridajePersistente).filter(
            MaridajePersistente.nombre == nombre
        ).first()
        
        if maridaje_persistente:
            session.delete(maridaje_persistente)
            session.commit()
            session.close()
        else:
            raise ValueError("El maridaje especificado no existe en la base de datos.")
