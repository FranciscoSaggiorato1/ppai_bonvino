class Usuario:
    """
    Clase para representar un Usuario.
    """
    def __init__(self, contraseña, nombre, premium):
        self.nombre = nombre
        self.contraseña = contraseña
        self.premium = premium 


    # Métodos getter y setter para los atributos de la clase
    def getNombre(self):
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