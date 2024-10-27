import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))

from database_config import session
from Entidades.siguiendo import Siguiendo as SiguiendoPersistente
from Modelo.siguiendo import Siguiendo

class SiguiendoConversor:

    @staticmethod
    def get_all():
        resultados = session.query(SiguiendoPersistente).all()
        return [SiguiendoConversor.mapear_siguiendo(s) for s in resultados]

    @staticmethod
    def get_by_enofilo_bodega(enofilo_id, bodega_id):
        resultado = session.query(SiguiendoPersistente).filter(
            SiguiendoPersistente.enofilo_id == enofilo_id,
            SiguiendoPersistente.bodega_id == bodega_id
        ).first()
        return SiguiendoConversor.mapear_siguiendo(resultado) if resultado else None

    @staticmethod
    def mapear_siguiendo(siguiendo_persistente):
        return Siguiendo(
            fechaInicio=siguiendo_persistente.fechaInicio,
            fechaFin=siguiendo_persistente.fechaFin,
            enofilo=siguiendo_persistente.enofilo,
            bodega=siguiendo_persistente.bodega
        )

    @staticmethod
    def guardar_siguiendo(siguiendo: Siguiendo):
        siguiendo_persistente = SiguiendoPersistente(
            fechaInicio=siguiendo.fechaInicio,
            fechaFin=siguiendo.fechaFin,
            enofilo=siguiendo.enofilo,
            bodega=siguiendo.bodega
        )
        session.add(siguiendo_persistente)
        session.commit()
