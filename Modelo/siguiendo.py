class Siguiendo():
    #Propiedades de la clase SIGUIENDO
    fechaInicio = ""
    fechaFin = ""
    bodega = None
    enofilo= None
#Metodos de la clase SIGUIENDO
def __init__(self, fechaInicio, fechaFin, bodega, enofilo):
    self.fechaInicio = fechaInicio
    self.fechaFin = fechaFin
    self.bodega = bodega
    self.enofilo = enofilo
def new(self, fechaInicio, fechaFin, bodega, enofilo):
    return Siguiendo(fechaInicio, fechaFin, bodega, enofilo)


def get_fechaInicio(self):
    return self.fechaInicio

def set_fechaInicio(self,fechaInicio):
    self.fechaInicio = fechaInicio

def get_fechaFin(self):
    return self.fechaFin

def set_fechaFin(self,fechaFin):
    self.fechaFin = fechaFin

def get_bodega(self):
    return self.bodega
def set_bodega(self,bodega):
    self.bodega = bodega
def get_enofilo(self):
    return self.enofilo
def set_enofilo(self,enofilo):
    self.enofilo = enofilo

def sosDeBodega(self):
    if self.bodega != None:
        return True
    else:
        return False