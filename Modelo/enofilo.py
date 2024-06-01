import csv
import os

from Modelo.siguiendo import Siguiendo
from Modelo.usuario import Usuario
from Modelo.bodega import Bodega

class Enofilo:
    """
    Clase para representar un enófilo.
    """
    def __init__(self, apellido, imagenPerfil, nombre, seguidos, usuario):
        """
        Inicializa un objeto Enofilo.

        :param id: ID del enófilo.
        :param apellido: Apellido del enófilo.
        :param imagenPerfil: Imagen de perfil del enófilo.
        :param nombre: Nombre del enófilo.
        :param seguidos: Lista de usuarios seguidos por el enófilo.
        :param usuario: Usuario relacionado con el enófilo.
        """
        self.apellido = apellido
        self.imagenPerfil = imagenPerfil
        self.nombre = nombre
        self.seguidos = seguidos
        self.usuario = usuario

    def new(self, id, apellido, imagenPerfil, nombre, seguido, usuario):
        """
        Método para crear y devolver una nueva instancia de Enofilo.

        :param id: ID del enófilo.
        :param apellido: Apellido del enófilo.
        :param imagenPerfil: Imagen de perfil del enófilo.
        :param nombre: Nombre del enófilo.
        :param seguidos: Lista de usuarios seguidos por el enófilo.
        :param usuario: Usuario relacionado con el enófilo.
        :return: Nueva instancia de Enofilo.
        """
        return Enofilo(id, apellido, imagenPerfil, nombre, seguido, usuario)

    def __repr__(self):
        """
        Método especial para representar la instancia de Enofilo como una cadena.

        :return: Cadena representando la instancia de Enofilo.
        """
        return (
            f"Enofilo(id={self.id}, "
            f"apellido={self.apellido},  "
            f"imagenPerfil={self.imagenPerfil},"
            f"nombre={self.nombre},"
            f"seguido={self.seguido},"
            f"usuario={self.usuario}"
        )

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_apellido(self):
        return self.apellido

    def set_apellido(self, apellido):
        self.apellido = apellido

    def get_imagenPerfil(self):
        return self.imagenPerfil

    def set_imagenPerfil(self, imagenPerfil):
        self.imagenPerfil = imagenPerfil

    def get_nombre(self):
        return self.nombre        

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_seguido(self):
        return self.seguido

    def set_seguido(self, seguido):
        self.seguido = seguido

    def get_usuario(self):
        return self.usuario  

    def set_usuario(self, usuario):
        self.usuario = usuario

    def seguisBodega(self):
        """
        Método para verificar si el enófilo sigue alguna bodega.

        :return: True si el enófilo sigue alguna bodega, False en caso contrario.
        """
        for i in self.seguido:
            if i.sosDeBodega():
                return True
        return False

    def obtenerNombreUsuario(self):
        """
        Método para obtener el nombre del usuario relacionado con el enófilo.

        :return: Nombre del usuario relacionado con el enófilo.
        """
        return self.usuario.getNombre()

    @staticmethod
    def cargarData(filepath, siguiendos_data=None):
        """
        Método estático para cargar datos desde un archivo CSV.

        :param filepath: Ruta del archivo CSV.
        :param siguiendos_data: Datos de usuarios seguidos, opcional.
        :return: Lista de instancias de Enofilo.
        """
        enofilos = []
        if siguiendos_data is None:
            script_dir = os.path.dirname(__file__)
            path_siguiendos = os.path.join(script_dir, '..', 'Modelo', './data/siguiendo.csv')
            siguiendos_data = Siguiendo.cargarData(path_siguiendos)

        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    enofilo = Enofilo(
                        id=row['id'],
                        apellido=row['apellido'],
                        imagenPerfil=row['imagenPerfil'],
                        nombre=row['nombre'],
                        seguidos=[],
                        usuario=None
                    )
                    for siguiendo_id in row['seguido'].split(';'):
                        for siguiendo in siguiendos_data:
                            if siguiendo.id == siguiendo_id:
                                enofilo.seguidos.append(siguiendo)

                    script_dir = os.path.dirname(__file__)
                    path_usuario = os.path.join(script_dir, '..', 'Modelo', './data/usuario.csv')
                    TodosLosUsuario = Usuario.cargarData(path_usuario)
                    usuario_id = row['tipoUva']
                    for usuario in TodosLosUsuario:
                        if usuario.id == usuario_id:
                            enofilo.usuario = usuario
                    enofilos.append(enofilo)
                except ValueError as e:
                    print(f"Error al procesar la fila: {row}. Error: {e}")
        return enofilos

    def to_dict(self):
        """
        Método para convertir la instancia de Enofilo a un diccionario.

        :return: Diccionario representando la instancia de Enofilo.
        """
        return {
            "id": self.id,
            "apellido": self.apellido,
            "imagenPerfil": self.imagenPerfil,
            "nombre": self.nombre,
            "seguido": self.seguido,
            "usuario": self.usuario
        }
