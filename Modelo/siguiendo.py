class Siguiendo:
    """
    Clase para representar una relación de seguimiento entre un enófilo y una bodega.
    """

    def __init__(self, fechaInicio, fechaFin, enofilo, bodega):
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.enofilo = enofilo
        self.bodega = bodega
        

    def sosDeBodega(self, bodega):
        if self.bodega == bodega:
            return True
        else:
            return False