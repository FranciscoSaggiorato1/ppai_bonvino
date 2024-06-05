from Modelo.varietal import Varietal
from datetime import datetime
from Modelo.bodega import Bodega

class Vino:
    """
    Clase para representar un Vino.
    """
    def __init__(self, añada, fechaActualizacion, nombre, imagenEtiqueta, notaCata, precioArs, varietal, maridaje, bodega):
        self.añada = añada
        self.nombre = nombre
        self.fechaActualizacion = fechaActualizacion
        self.bodega = bodega
        self.maridaje = maridaje
        self.notaCata = notaCata
        self.precioArs = precioArs
        self.varietal = varietal
        self.imagenEtiqueta = imagenEtiqueta

    # Método para crear y devolver una nueva instancia de Vino
    @classmethod
    def new(cls, nombre, añada, fechaActualizacion, precioArs, notaCata, bodega, imagenEtiqueta, maridaje, descripcion, porcentajeComposicion, tiposUvas):
        varietales = []
        for descripcion, porcentaje, tipo in zip(descripcion, porcentajeComposicion, tiposUvas):
            nuevo = cls.crearVarietal(descripcion, porcentaje, tipo)
            varietales.append(nuevo)
        return cls(añada, fechaActualizacion, nombre, imagenEtiqueta, notaCata, precioArs, varietales, maridaje, bodega)


    # Método para verificar si el objeto es efectivamente un vino
    def sosEsteVino(self, nombreVino):
        if self.nombre == nombreVino:
            return True
        return False
    

    def agregarVinoEnBodega(self):
        self.bodega.agregarVino(self)


    # Métodos getter y setter para los atributos de la clase
    def getNombre(self):
        return self.nombre
    

    def setNombre(self, nombre):
        self.nombre = nombre
    
    
    def getAñada(self):
        return self.añada
    
    
    def setAñada(self, añada):
        self.añada = añada
    
    
    def getFechaActualizacion(self):
        return self.fechaActualizacion
    
    
    def setFechaActualizacion(self, fechaActualizacion):
        self.fechaActualizacion = fechaActualizacion
    
    
    def getBodega(self):
        return self.bodega
    
    
    def setBodega(self, bodega):
        self.bodega = bodega
    
    
    def getMaridaje(self):
        for m in self.maridaje:
            return m
    
    
    def setMaridaje(self, maridaje):
        self.maridaje = maridaje
    
    
    def getNotaCata(self):
        return self.notaCata
    
    
    def setNotaCata(self, notaCata):
        self.notaCata = notaCata
    
    
    def getPrecioArs(self):
        return self.precioARS
    
    
    def setPrecioArs(self, precioARS):
        self.precioARS = precioARS
    
    
    def getImagenEtiqueta(self):
        return self.imagenEtiqueta
    
    
    def setImagenEtiqueta(self, imagenEtiqueta):
        self.imagenEtiqueta = imagenEtiqueta
    
    
    def getVarietal(self):
        for v in self.varietal:
            return v
        

    def setVarietal(self, varietal):
        self.varietal = varietal


    # Método para crear una nueva instancia de Varietal
    @staticmethod
    def crearVarietal(descripcion, porcentajeComposicion, tipoUva):
        varietalNuevo = Varietal.new(
            descripcion=descripcion, 
            porcentajeComposicion=porcentajeComposicion, 
            tipoUva=tipoUva)
        return varietalNuevo


    # Método para verificar si el vino necesita actualización
    def sosVinoParaActualizar(self, fechaActual):
        if datetime.strptime(self.fechaActualizacion, "%Y-%m-%d") < datetime.strptime(fechaActual, "%Y-%m-%d"):
            return True
        else:
            return False