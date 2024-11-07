class Enofilo:
    """
    Clase para representar un enófilo.
    """
    def __init__(self, apellido, imagenPerfil, nombre, usuario):
        self.apellido = apellido
        self.imagenPerfil = imagenPerfil
        self.nombre = nombre
        self.seguidos = []
        self.usuario = usuario

    def agregarSiguiendo(self, seguido):
        self.seguidos.append(seguido)

    def getApellido(self):
        return self.apellido

    def setApellido(self, apellido):
        self.apellido = apellido

    def getImagenPerfil(self):
        return self.imagenPerfil

    def setImagenPerfil(self, imagenPerfil):
        self.imagenPerfil = imagenPerfil

    def getNombre(self):
        return self.nombre        

    def setNombre(self, nombre):
        self.nombre = nombre

    def getSeguido(self):
        return self.seguidos

    def setSeguido(self, seguido):
        self.seguidos = seguido

    def getUsuario(self):
        return self.usuario  

    def setUsuario(self, usuario):
        self.usuario = usuario

    def seguisBodega(self, bodega):
        for seguido in self.seguidos:
            if seguido.sosDeBodega(bodega):
                return True
        return False

    def obtenerNombreUsuario(self):
        return self.usuario.getNombre()
    
    def __str__(self):
        return f"Enófilo: {self.nombre} {self.apellido} | seguidos: {self.seguidos}"