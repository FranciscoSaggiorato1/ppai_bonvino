import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))

from database_config import session
from Entidades.vino import Vino as VinoPersistente, vino_varietal, vino_maridaje
from Modelo.vino import Vino
from ConversoresPersistencia.bodega_conversor import BodegaConversor
from ConversoresPersistencia.varietal_conversor import VarietalConversor
from ConversoresPersistencia.maridaje_conversor import MaridajeConversor
from Entidades.bodega import Bodega as BodegaPersistente
from Entidades.maridaje import Maridaje as MaridajePersistente
from Entidades.varietal import Varietal as VarietalPersistente

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
        # Obtener la bodega persistente usando su nombre
        bodega_persistente = session.query(BodegaPersistente).filter(
            BodegaPersistente.nombre == vino.bodega.nombre
        ).first()
        
        if not bodega_persistente:
            raise ValueError("La bodega especificada no existe en la base de datos.")

        vino_persistente = VinoPersistente(
            añada=vino.añada,
            fechaActualizacion=vino.fechaActualizacion,
            nombre=vino.nombre,
            imagenEtiqueta=vino.imagenEtiqueta,
            notaCata=vino.notaCata,
            precioArs=vino.precioArs,
            bodega=bodega_persistente
        )

        # Agregar maridajes
        for maridaje in vino.maridaje:
            maridaje_persistente = session.query(MaridajePersistente).filter(
                MaridajePersistente.descripcion == maridaje.descripcion
            ).first()
            
            if not maridaje_persistente:
                raise ValueError(f"El maridaje '{maridaje.descripcion}' no existe en la base de datos.")
            
            vino_persistente.maridaje.append(maridaje_persistente)
        
        # Agregar varietales
        for varietal in vino.varietal:
            varietal_persistente = session.query(VarietalPersistente).filter(
                VarietalPersistente.descripcion == varietal.descripcion
            ).first()
            
            if not varietal_persistente:
                raise ValueError(f"El varietal '{varietal.descripcion}' no existe en la base de datos.")
            
            vino_persistente.varietal.append(varietal_persistente)

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
