import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))

from database_config import session
from Entidades.vino import Vino as VinoPersistente, vino_varietal, vino_maridaje
from Modelo.vino import Vino
from ConversoresPersistencia.bodega_conversor import BodegaConversor
from ConversoresPersistencia.varietal_conversor import VarietalConversor
from ConversoresPersistencia.maridaje_conversor import MaridajeConversor

class VinoConversor:

    @staticmethod
    def get_all():
        resultados = session.query(VinoPersistente).all()
        return [VinoConversor.mapear_vino(v) for v in resultados]

    @staticmethod
    def get_by_nombre(nombre):
        resultado = session.query(VinoPersistente).filter(
            VinoPersistente.nombre == nombre
        ).first()
        return VinoConversor.mapear_vino(resultado) if resultado else None

    @staticmethod
    def mapear_vino(vino_persistente):
        bodega = BodegaConversor.mapear_bodega(vino_persistente.bodega)
        varietales = [VarietalConversor.mapear_varietal(v) for v in vino_persistente.varietales]
        maridajes = [MaridajeConversor.mapear_maridaje(m) for m in vino_persistente.maridajes]

        return Vino(
            nombre=vino_persistente.nombre,
            añada=vino_persistente.añada,
            fechaActualizacion=vino_persistente.fechaActualizacion,
            imagenEtiqueta=vino_persistente.imagenEtiqueta,
            notaCata=vino_persistente.notaCata,
            precioArs=vino_persistente.precioArs,
            bodega=bodega,
            varietal=varietales,
            maridaje=maridajes
        )

    @staticmethod
    def guardar_vino(vino: Vino):
        bodega_persistente = BodegaConversor.get_by_nombre(vino.bodega.nombre)

        vino_persistente = VinoPersistente(
            nombre=vino.nombre,
            añada=vino.añada,
            fechaActualizacion=vino.fechaActualizacion,
            imagenEtiqueta=vino.imagenEtiqueta,
            notaCata=vino.notaCata,
            precioArs=vino.precioArs,
            bodega=bodega_persistente
        )

        # Agregar varietales y maridajes
        vino_persistente.varietales = [
            VarietalConversor.get_by_descripcion(varietal.descripcion) for varietal in vino.varietal
        ]
        vino_persistente.maridajes = [
            MaridajeConversor.get_by_nombre(maridaje.nombre) for maridaje in vino.maridaje
        ]

        session.add(vino_persistente)
        session.commit()

    @staticmethod
    def eliminar_vino(nombre):
        vino_persistente = session.query(VinoPersistente).filter(
            VinoPersistente.nombre == nombre
        ).first()

        if vino_persistente:
            session.delete(vino_persistente)
            session.commit()
        else:
            raise ValueError("El vino especificado no existe en la base de datos.")
