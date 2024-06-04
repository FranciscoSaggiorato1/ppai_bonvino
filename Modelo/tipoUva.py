class TipoUva:
    """
    Clase para representar un objeto Tipo Uva.
    """
    def __init__(self, descripcion, nombre):
        self.descripcion = descripcion
        self.nombre = nombre
    
    
    def sosTipoUva(self, nombreTipoUva):
        if self.nombre == nombreTipoUva:
            return True
        return False
     

    def getDescripcion(self):
        return self.descripcion 
    

    def setDescripcion(self,descripcion):  
        self.descripcion = descripcion


    def getNombre(self):
        return self.nombre

    
    def setNombre(self,nombre):
        self.nombre = nombre