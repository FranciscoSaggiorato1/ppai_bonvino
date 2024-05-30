from siguiendo import Siguiendo
from usuario import Usuario
import csv
import os
class Enofilo:
    #Propiedades de la clase ENOFILO
    id = ""
    apellido = ""
    imagenPerfil = None
    nombre = ""
    seguidos = []
    usuario = None

    def __init__(self,id, apellido, imagenPerfil, nombre, seguido, usuario):
        self.id = id
        self.apellido = apellido
        self.imagenPerfil = imagenPerfil
        self.nombre = nombre
        self.seguido = seguido
        self.usuario = usuario
    def new(self,id, apellido, imagenPerfil, nombre, seguido, usuario):
        return Enofilo(id,apellido, imagenPerfil, nombre, seguido, usuario)
    def __repr__(self):
            return (
                f"Enofilo(id={self.id}, "
                f"apellido={self.apellido},  "
                f"imagenPerfil={self.imagenPerfil},"
                f"nombre={self.nombre},"
                f"seguido={self.seguido},"
                f"usuario={self.usuario}")

    #Metodos de la clase ENOFILO
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
        for i in self.seguido:
            if i.sosDeBodega():
                return True
        return False

    def obtenerNombreUsuario(self):
        return self.usuario.getNombre()
    def cargarData(filepath):
        enofilos = []
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
                        usuario=row['usuario']
                    )
                    script_dir = os.path.dirname(__file__)
                    path_siguiendos = os.path.join(script_dir, '..', 'Modelo', './data/siguiendo.csv')
                    TodosLosSiguiendos = Siguiendo.cargarData(path_siguiendos)
                    
                    for siguiendo_id in row['seguido'].split(';'):
                        for siguiendo in TodosLosSiguiendos:
                            if siguiendo.get_Id() == siguiendo_id:
                                enofilo.seguidos.append(siguiendo)
                    enofilos.append(enofilo)
                except ValueError as e:
                    print(f"Error al procesar la fila: {row}. Error: {e}")
        return enofilos
    
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
    enofilos=Enofilo.cargarData("ruta_al_archivo.csv")
    for enofilo in enofilos:
        print(enofilo)