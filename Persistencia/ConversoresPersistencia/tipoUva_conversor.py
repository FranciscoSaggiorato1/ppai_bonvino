import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))

from database_config import session
from Entidades.tipoUva import TipoUva as TipoUvaPersistente
from Modelo.tipoUva import TipoUva

class TipoUvaConversor:

    @staticmethod
    def get_all():
        resultados = session.query(TipoUvaPersistente).all()
        return [TipoUvaConversor.mapear_tipo_uva(t) for t in resultados]

    @staticmethod
    def get_by_nombre(nombre):
        resultado = session.query(TipoUvaPersistente).filter(
            TipoUvaPersistente.nombre == nombre
        ).first()
        return TipoUvaConversor.mapear_tipo_uva(resultado) if resultado else None

    @staticmethod
    def mapear_tipo_uva(tipo_uva_persistente):
        return TipoUva(
            descripcion=tipo_uva_persistente.descripcion,
            nombre=tipo_uva_persistente.nombre
        )

    @staticmethod
    def guardar_tipo_uva(tipo_uva: TipoUva):
        tipo_uva_persistente = TipoUvaPersistente(
            descripcion=tipo_uva.descripcion,
            nombre=tipo_uva.nombre
        )
        session.add(tipo_uva_persistente)
        session.commit()

    @staticmethod
    def eliminar_tipo_uva(nombre):
        tipo_uva_persistente = session.query(TipoUvaPersistente).filter(
            TipoUvaPersistente.nombre == nombre
        ).first()
        
        if tipo_uva_persistente:
            session.delete(tipo_uva_persistente)
            session.commit()
        else:
            raise ValueError("El tipo de uva especificado no existe en la base de datos.")
