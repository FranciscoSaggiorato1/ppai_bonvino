class Siguiendo:
    """
    Clase para representar una relación de seguimiento entre un enófilo y una bodega.
    """

    def __init__(self, fechaInicio, fechaFin, enofilo_seguido, bodega, enofilo_seguidor):
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.enofilo_seguido = enofilo_seguido
        self.bodega = bodega
        self.enofilo_seguidor = enofilo_seguidor
        

    def sosDeBodega(self, bodega):
        if self.bodega is not None and bodega is not None:
            if self.bodega.nombre == bodega.nombre:
                return True
        else:
            return False
        
    def __str__(self):
        return f"Siguiendo desde {self.fechaInicio} hasta {self.fechaFin} a el enofilo seguido {self.enofilo_seguido} o a la bodega {self.bodega} por el enofilo seguidor {self.enofilo_seguidor}"