class Varietal():
    descripcion = ""
    porcentajeComposicion = 0
    tipoUva= None

def get_Descripcion(self):
    return self.descripcion
def set_Descripcion(self,descripcion):
    self.descripcion = descripcion
def get_Porcentaje_Composicion(self):
    return self.porcentajeComposicion
def set_Porcentaje_Composicion(self,porcentajeComposicion):
    self.porcentajeComposicion = porcentajeComposicion
def get_Tipo_Uva(self):
    return self.tipoUva
def set_Tipo_Uva(self,tipoUva):
    self.tipoUva = tipoUva

def __init__(self, descripcion, porcentajeComposicion):
        self.descripcion = descripcion
        self.porcentajeComposicion = porcentajeComposicion
def new(self, descripcion, porcentajeComposicion):
    return Varietal(descripcion, porcentajeComposicion)        