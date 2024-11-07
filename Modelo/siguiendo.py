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
        print(type(self.bodega))
        if bodega is not None and self.bodega == bodega:
            return True
        else:
            return False