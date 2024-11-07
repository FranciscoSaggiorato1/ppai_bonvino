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
        id_enofilo_seguido = None
        id_bodega = None
        id_enofilo_seguidor = None

        # Obtener el enófilo seguido persistente, si existe
        if siguiendo.enofilo_seguido is not None:
            enofilo_persistente = session.query(EnofiloPersistente).filter(
                EnofiloPersistente.nombre == siguiendo.enofilo_seguido.getNombre()
            ).first()
            if not enofilo_persistente:
                raise ValueError("El enófilo especificado para seguir no existe en la base de datos.")
            id_enofilo_seguido = enofilo_persistente.id_enofilo

        # Obtener la bodega persistente, si existe
        if siguiendo.bodega is not None:
            bodega_persistente = session.query(BodegaPersistente).filter(
                BodegaPersistente.nombre == siguiendo.bodega.nombre
            ).first()
            if not bodega_persistente:
                raise ValueError("La bodega especificada no existe en la base de datos.")
            id_bodega = bodega_persistente.id_bodega

        # Obtener el enófilo seguidor persistente
        enofilo_seguidor_persistente = session.query(EnofiloPersistente).filter(
            EnofiloPersistente.nombre == siguiendo.enofilo_seguidor.getNombre()
        ).first()
        if not enofilo_seguidor_persistente:
            raise ValueError("El enófilo seguidor especificado no existe en la base de datos.")
        id_enofilo_seguidor = enofilo_seguidor_persistente.id_enofilo

        # Crear el objeto de SiguiendoPersistente y asignar los IDs
        siguiendo_persistente = SiguiendoPersistente(
            fechaInicio=siguiendo.fechaInicio,
            fechaFin=siguiendo.fechaFin,
            id_enofilo_seguido=id_enofilo_seguido,
            id_bodega=id_bodega,
            id_enofilo_seguidor=id_enofilo_seguidor
        )

        # Guardar en la base de datos
        session.add(siguiendo_persistente)
        session.commit()
        session.close()

