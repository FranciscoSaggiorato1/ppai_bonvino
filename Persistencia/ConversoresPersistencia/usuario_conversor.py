import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))

from database_config import session
from Entidades.usuario import Usuario as UsuarioPersistente
from Modelo.usuario import Usuario

class UsuarioConversor:

    @staticmethod
    def get_all():
        resultados = session.query(UsuarioPersistente).all()
        return [UsuarioConversor.mapear_usuario(u) for u in resultados]

    @staticmethod
    def get_by_nombre(nombre):
        resultado = session.query(UsuarioPersistente).filter(
            UsuarioPersistente.nombre == nombre
        ).first()
        return UsuarioConversor.mapear_usuario(resultado) if resultado else None

    @staticmethod
    def mapear_usuario(usuario_persistente):
        return Usuario(
            nombre=usuario_persistente.nombre,
            contraseña=usuario_persistente.contraseña,
            premium=usuario_persistente.premium
        )

    @staticmethod
    def guardar_usuario(usuario: Usuario):
        usuario_persistente = UsuarioPersistente(
            nombre=usuario.nombre,
            contraseña=usuario.contraseña,
            premium=usuario.premium
        )
        session.add(usuario_persistente)
        session.commit()

    @staticmethod
    def eliminar_usuario(nombre):
        usuario_persistente = session.query(UsuarioPersistente).filter(
            UsuarioPersistente.nombre == nombre
        ).first()
        
        if usuario_persistente:
            session.delete(usuario_persistente)
            session.commit()
        else:
            raise ValueError("El usuario especificado no existe en la base de datos.")
