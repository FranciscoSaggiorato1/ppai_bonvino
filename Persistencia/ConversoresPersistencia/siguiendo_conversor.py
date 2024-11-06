import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))

from database_config import session
from Persistencia.Entidades.siguiendoDB import Siguiendo as SiguiendoPersistente
from Modelo.siguiendo import Siguiendo
from Persistencia.Entidades.bodegaDB import Bodega as BodegaPersistente
from Persistencia.Entidades.enofiloDB import Enofilo as EnofiloPersistente

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
        id_enofilo = None
        id_bodega = None

        # Obtener el enófilo persistente si existe
        if siguiendo.enofilo is not None:
            enofilo_persistente = session.query(EnofiloPersistente).filter(
                EnofiloPersistente.nombre == siguiendo.enofilo.nombre
            ).first()
            
            if not enofilo_persistente:
                raise ValueError("El enófilo especificado no existe en la base de datos.")
            id_enofilo = enofilo_persistente.id_enofilo  # Guardar el ID del enófilo
        
        # Obtener la bodega persistente si existe
        if siguiendo.bodega is not None:
            bodega_persistente = session.query(BodegaPersistente).filter(
                BodegaPersistente.nombre == siguiendo.bodega.nombre
            ).first()

            if not bodega_persistente:
                raise ValueError("La bodega especificada no existe en la base de datos.")
            id_bodega = bodega_persistente.id_bodega  # Guardar el ID de la bodega

        siguiendo_persistente = SiguiendoPersistente(
            fechaInicio=siguiendo.fechaInicio,
            fechaFin=siguiendo.fechaFin,
            id_enofilo=id_enofilo,  # Asignar el ID del enófilo (puede ser None)
            id_bodega= id_bodega  # Asignar el ID de la bodega (puede ser None)
        )
        
        session.add(siguiendo_persistente)
        session.commit()
        session.close()
