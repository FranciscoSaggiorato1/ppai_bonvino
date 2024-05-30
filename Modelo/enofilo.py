from siguiendo import Siguiendo  # Importa la clase Siguiendo del módulo siguiendo
from usuario import Usuario  # Importa la clase Usuario del módulo usuario
import csv  # Importa el módulo csv para trabajar con archivos CSV
import os  # Importa el módulo os para manejar rutas de archivos

class Enofilo:
    # Propiedades de la clase ENOFILO
    id = ""  # Atributo para almacenar el ID del enófilo
    apellido = ""  # Atributo para almacenar el apellido del enófilo
    imagenPerfil = None  # Atributo para almacenar la imagen de perfil del enófilo
    nombre = ""  # Atributo para almacenar el nombre del enófilo
    seguidos = []  # Lista para almacenar los usuarios seguidos por el enófilo
    usuario = None  # Atributo para almacenar el usuario relacionado con el enófilo

    # Método de inicialización de la clase ENOFILO
    def __init__(self,id, apellido, imagenPerfil, nombre, seguido, usuario):
        self.id = id  # Asigna el ID proporcionado al atributo id
        self.apellido = apellido  # Asigna el apellido proporcionado al atributo apellido
        self.imagenPerfil = imagenPerfil  # Asigna la imagen de perfil proporcionada al atributo imagenPerfil
        self.nombre = nombre  # Asigna el nombre proporcionado al atributo nombre
        self.seguido = seguido  # Asigna los usuarios seguidos proporcionados al atributo seguidos
        self.usuario = usuario  # Asigna el usuario proporcionado al atributo usuario

    # Método para crear y devolver una nueva instancia de Enofilo
    def new(self,id, apellido, imagenPerfil, nombre, seguido, usuario):
        return Enofilo(id,apellido, imagenPerfil, nombre, seguido, usuario)

    # Método especial para representar la instancia de Enofilo como una cadena
    def __repr__(self):
        return (
            f"Enofilo(id={self.id}, "
            f"apellido={self.apellido},  "
            f"imagenPerfil={self.imagenPerfil},"
            f"nombre={self.nombre},"
            f"seguido={self.seguido},"
            f"usuario={self.usuario}"
        )

    # Métodos getter y setter para los atributos de la clase
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

    # Método para verificar si el enófilo sigue alguna bodega
    def seguisBodega(self):
        for i in self.seguido:
            if i.sosDeBodega():
                return True
        return False

    # Método para obtener el nombre del usuario relacionado con el enófilo
    def obtenerNombreUsuario(self):
        return self.usuario.getNombre()

    # Método estático para cargar datos desde un archivo CSV
    @staticmethod
    def cargarData(filepath):
        enofilos = []  # Lista para almacenar las instancias de Enofilo
        with open(filepath, newline='', encoding='utf-8') as csvfile:  # Abre el archivo CSV
            reader = csv.DictReader(csvfile)  # Crea un lector de CSV
            for row in reader:  # Itera sobre las filas del archivo CSV
                try:
                    # Crea una instancia de Enofilo con los datos de la fila actual
                    enofilo = Enofilo(
                        id=row['id'],
                        apellido=row['apellido'],
                        imagenPerfil=row['imagenPerfil'],
                        nombre=row['nombre'],
                        seguidos=[],
                        usuario=row['usuario']
                    )
                    # Carga los datos de los usuarios seguidos desde el archivo CSV
                    script_dir = os.path.dirname(__file__)
                    path_siguiendos = os.path.join(script_dir, '..', 'Modelo', './data/siguiendo.csv')
                    TodosLosSiguiendos = Siguiendo.cargarData(path_siguiendos)
                    
                    # Agrega los usuarios seguidos a la lista de seguidos del enófilo
                    for siguiendo_id in row['seguido'].split(';'):
                        for siguiendo in TodosLosSiguiendos:
                            if siguiendo.get_Id() == siguiendo_id:
                                enofilo.seguidos.append(siguiendo)
                    enofilos.append(enofilo)  # Agrega el enófilo a la lista de enófilos
                except ValueError as e:
                    print(f"Error al procesar la fila: {row}. Error: {e}")
        return enofilos  # Devuelve la lista de enófilos cargados desde el archivo CSV

    # Método para convertir la instancia de Enofilo a un diccionario
    def to_dict(self):
        return {
            "id": self.id,
            "apellido": self.apellido,
            "imagenPerfil": self.imagenPerfil,
            "nombre": self.nombre,
            "seguido": self.seguido,
            "usuario": self.usuario
        }

# Ejemplo de uso
if __name__ == "__main__":
    enofilos=Enofilo.cargarData("ruta_al_archivo.csv")  # Carga los datos de enófilos desde un archivo CSV
    for enofilo in enofilos:  # Itera sobre los enófilos cargados
        print(enofilo)  # Imprime cada enófilo
