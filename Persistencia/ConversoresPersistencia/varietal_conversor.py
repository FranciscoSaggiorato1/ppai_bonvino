import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))

from database_config import session
from Entidades.varietal import Varietal as VarietalPersistente
from Modelo.varietal import Varietal
from ConversoresPersistencia.tipoUva_conversor import TipoUvaConversor

class VarietalConversor:

    @staticmethod
    def get_all():
        resultados = session.query(VarietalPersistente).all()
        return [VarietalConversor.mapear_varietal(v) for v in resultados]

    @staticmethod
    def get_by_descripcion(descripcion):
        resultado = session.query(VarietalPersistente).filter(
            VarietalPersistente.descripcion == descripcion
        ).first()
        return VarietalConversor.mapear_varietal(resultado) if resultado else None

    @staticmethod
    def mapear_varietal(varietal_persistente):
        tipo_uva = TipoUvaConversor.mapear_tipo_uva(varietal_persistente.tipoUva)
        return Varietal(
            descripcion=varietal_persistente.descripcion,
            porcentajeComposicion=varietal_persistente.porcentajeComposicion,
            tipoUva=tipo_uva
        )

    @staticmethod
    def guardar_varietal(varietal: Varietal):
        tipo_uva_persistente = TipoUvaConversor.get_by_nombre(varietal.tipoUva.nombre)
        
        varietal_persistente = VarietalPersistente(
            descripcion=varietal.descripcion,
            porcentajeComposicion=varietal.porcentajeComposicion,
            tipoUva=tipo_uva_persistente
        )
        
        session.add(varietal_persistente)
        session.commit()

    @staticmethod
    def eliminar_varietal(descripcion):
        varietal_persistente = session.query(VarietalPersistente).filter(
            VarietalPersistente.descripcion == descripcion
        ).first()
        
        if varietal_persistente:
            session.delete(varietal_persistente)
            session.commit()
        else:
            raise ValueError("El varietal especificado no existe en la base de datos.")
