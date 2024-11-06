class Maridaje:
    """
    Clase para representar un Maridaje.
    """
    def __init__(self, descripcion, nombre): 
        self.descripcion = descripcion  
        self.nombre = nombre 
    
    
    def sosMaridaje(self, nombreMaridaje):
        if self.nombre == nombreMaridaje:
            return True
        return False
        

    # Métodos getter y setter para los atributos de la clase
    def getDescripcion(self):
        return self.descripcion
    

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion
    

    def getNombre(self):
        return self.nombre
    

    def setNombre(self, nombre):
        self.nombre = nombre