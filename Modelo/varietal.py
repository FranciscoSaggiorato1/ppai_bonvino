class Varietal:
    """
    Clase para representar un Varietal.
    """
    def __init__(self, descripcion, porcentajeComposicion, tipoUva):
        self.descripcion = descripcion
        self.porcentajeComposicion = porcentajeComposicion
        self.tipoUva = tipoUva

    @classmethod
    def new(cls, descripcion, porcentajeComposicion, tipoUva):
        return cls(descripcion, porcentajeComposicion, tipoUva) 
    
    
    def getDescripcion(self):
        return self.descripcion
    
    
    def setDescripcion(self,descripcion):
        self.descripcion = descripcion
    
    
    def getProcentajeComposicion(self):
        return self.porcentajeComposicion
    
    
    def setPorcentajeComposicion(self,porcentajeComposicion):
        self.porcentajeComposicion = porcentajeComposicion
    
    
    def getTipoUva(self):
        return self.tipoUva
    
    
    def setTipoUva(self,tipoUva):
        self.tipoUva = tipoUva