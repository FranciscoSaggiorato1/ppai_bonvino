class Usuario:
    #Propiedades de la clase Usuario
    id=""
    contraseña = ""
    nombre = ""
    premium = None

def __init__(self,id, nombre, contraseña, premium):
    self.id = id
    self.nombre = nombre
    self.contraseña = contraseña
    self.premium = premium
def new(self,id, nombre, contraseña, premium):
    return Usuario(id,nombre, contraseña, premium)
#Metodos de la clase Usuario
def get_Id(self):
    return self.id
def set_Id(self, id):
    self.id = id
def getNombre(self, nombre):
    return self.nombre
def setNombre(self, nombre):
    self.nombre = nombre
def getContraseña(self, contraseña):
    return self.contraseña
def setContraseña(self, contraseña):
    self.contraseña = contraseña
def getPremium(self):
    return self.premium
def setPremium(self, premium):
    self.premium = premium
