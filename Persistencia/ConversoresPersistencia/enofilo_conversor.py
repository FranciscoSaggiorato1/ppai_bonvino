import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))

from database_config import session
from Entidades.enofilo import Enofilo as EnofiloPersistente
from Modelo.enofilo import Enofilo
from Entidades.usuario import Usuario as UsuarioPersistente

class EnofiloConversor:

    @staticmethod
    def get_all():
        resultados = session.query(EnofiloPersistente).all()
        return [EnofiloConversor.mapear_enofilo(e) for e in resultados]

    @staticmethod
    def get_by_nombre(nombre):
        resultado = session.query(EnofiloPersistente).filter(
            EnofiloPersistente.nombre == nombre
        ).first()
        return EnofiloConversor.mapear_enofilo(resultado) if resultado else None

    @staticmethod
    def mapear_enofilo(enofilo_persistente):
        return Enofilo(
            apellido=enofilo_persistente.apellido,
            imagenPerfil=enofilo_persistente.imagenPerfil,
            nombre=enofilo_persistente.nombre,
            seguidos=[bodega.nombre for bodega in enofilo_persistente.seguidos],
            usuario=enofilo_persistente.usuario
        )

    @staticmethod
    def guardar_enofilo(enofilo: Enofilo):
        # Obtener el usuario persistente usando su nombre
        usuario_persistente = session.query(UsuarioPersistente).filter(
            UsuarioPersistente.nombre == enofilo.usuario.nombre
        ).first()
        
        if not usuario_persistente:
            raise ValueError("El usuario especificado no existe en la base de datos.")

        enofilo_persistente = EnofiloPersistente(
            apellido=enofilo.apellido,
            imagenPerfil=enofilo.imagenPerfil,
            nombre=enofilo.nombre,
            usuario=usuario_persistente  # Asignar el usuario persistente
        )
        
        session.add(enofilo_persistente)
        session.commit()
        
    @staticmethod
    def eliminar_enofilo(nombre):
        enofilo_persistente = session.query(EnofiloPersistente).filter(
            EnofiloPersistente.nombre == nombre
        ).first()
        
        if enofilo_persistente:
            session.delete(enofilo_persistente)
            session.commit()
        else:
            raise ValueError("El enofilo especificado no existe en la base de datos.")
