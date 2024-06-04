import csv
from datetime import datetime, date
from dateutil.relativedelta import relativedelta  
from Modelo.vino import Vino
import os


class Bodega:
    """
    Clase para representar una Bodega.
    """
    def __init__(self, coordenadasUbicacion, descripcion, historia, nombre, periodoActualizacion, fechaUltimaActualizacion):
        self.coordenadasUbicacion = coordenadasUbicacion
        self.descripcion = descripcion
        self.historia = historia
        self.nombre = nombre
        self.periodoActualizacion = periodoActualizacion
        self.fechaUltimaActualizacion = fechaUltimaActualizacion
        self.vinos = [] 


    # Esta funcion agrega los vinos a la bodega
    def agregarVino(self, vino):
        self.vinos.append(vino)


    # Métodos de la clase BODEGA
    def getCoordenadasUbicacion(self):
        return self.coordenadasUbicacion


    def setCoordenadasUbicacion(self, coordenadasUbicacion):
        self.coordenadasUbicacion = coordenadasUbicacion


    def getDescripcion(self):
        return self.descripcion


    def setDescripcion(self, descripcion):
        self.descripcion = descripcion


    def getHistoria(self):
        return self.historia


    def setHistoria(self, historia):
        self.historia = historia


    def getNombre(self):
        return self.nombre


    def setNombre(self, nombre):
        self.nombre = nombre


    def setPeriodoActualizacion(self, periodoActualizacion):
        self.periodoActualizacion = int(periodoActualizacion)


    def getVinos(self):
        return self.vinos


    def setVinos(self, vinos):
        self.vinos = vinos


    def tieneActualizacionDisponible(self, fechaActual):
        # Calculamos si tiene actualizacion disponible
        fechaUltimaActualizacion = self.getFechaUltimaActualizacion()
        periodoActualizacion = self.getPeriodoActualizacion()
        fechaActualizacion = fechaUltimaActualizacion + relativedelta(months=periodoActualizacion)

        if fechaActualizacion < fechaActual:
            return True
        else:
           return False


    def getFechaUltimaActualizacion(self):
        if self.fechaUltimaActualizacion:
            # Si fechaUltimaActualizacion ya es un objeto datetime.date, simplemente devolverlo
            if isinstance(self.fechaUltimaActualizacion, date):
                return self.fechaUltimaActualizacion
            # Si no, convertirlo desde cadena de texto
            return datetime.strptime(self.fechaUltimaActualizacion, '%d/%m/%y')
        return None

    
    def getPeriodoActualizacion(self):
        return self.periodoActualizacion


    def setFechaUltimaActualizacion(self, fechaUltimaActualizacion):
        self.fechaUltimaActualizacion = fechaUltimaActualizacion


    def tienesEsteVino(self, nombreVino):
        for vino in self.vinos:
           if vino.sosEsteVino(nombreVino):
                return True
           
        return False


    def actualizarDatosVino(self, nombre, fechaActual, precio, notaCata, img):
        for vino in self.vinos:
            if vino.sosEsteVino(nombre):
                vino.setPrecioARS(precio)
                vino.setNotaCataBodega(notaCata)
                vino.setImagenEtiqueta(img)
                vino.setFechaActualizacion(fechaActual)
        return False
    
    # Esta función se encarga de transformar un objeto en diccionario
    def toDict(self):
        return {
            'coordenadasUbicacion': self.coordenadasUbicacion,
            'descripcion': self.descripcion,
            'historia': self.historia,
            'nombre': self.nombre,
            'periodoActualizacion': self.periodoActualizacion,
            'fechaUltimaActualizacion': self.fechaUltimaActualizacion,
            'vinos': self.vinos
        }