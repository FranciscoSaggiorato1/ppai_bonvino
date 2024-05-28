from siguiendo import Siguiendo
from usuario import Usuario

class Enofilo:
    #Propiedades de la clase ENOFILO
    id = ""
    apellido = ""
    imagenPerfil = None
    nombre = ""
    seguido = []
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
    self.usuario = Usuario(usuario)#RARO

def seguisBodega(self):
    for i in self.seguido:
        if i.sosDeBodega():
            return True
    return False

def obtenerNombreUsuario(self):
    return self.usuario.getNombre()
