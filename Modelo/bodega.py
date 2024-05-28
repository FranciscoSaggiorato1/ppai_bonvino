import datetime
import csv
import os
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta  

class Bodega():
    id = ""
    coordenadasUbicacion = ""
    descripcion = ""
    historia = ""
    nombre = ""
    periodoActualizacion = 0
    fechaUltimaActualizacion = None
    vinos = []

    def __init__(self,id,coordenadasUbicacion,descripcion,historia,nombre,periodoActualizacion,fechaUltimaActualizacion,vinos):
        self.id = id
        self.coordenadasUbicacion = coordenadasUbicacion
        self.descripcion = descripcion
        self.historia = historia
        self.nombre = nombre
        self.periodoActualizacion = periodoActualizacion
        self.fechaUltimaActualizacion = fechaUltimaActualizacion
        self.vinos = vinos

        #CHATGPT DICE:
    def __repr__(self):
        return (f"Bodega(nombre={self.nombre}, "
                f"fechaUltimaActualizacion={self.fechaUltimaActualizacion},  "
                f"periodoActualizacion={self.periodoActualizacion},"
                 f"coordenadasUbicacion={self.coordenadasUbicacion},"
                 f"descripcion={self.descripcion},"
                  f"historia={self.historia},"
                  f"vino={self.vinos})")

    def new(self,id,coordenadasUbicacion,descripcion,historia,nombre,periodoActualizacion,fechaUltimaActualizacion,vinos):
        return Bodega(id,coordenadasUbicacion,descripcion,historia,nombre,periodoActualizacion,fechaUltimaActualizacion,vinos)

    #Metodos de la clase BODEGA
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_coordenadasUbicacion(self):
        return self.coordenadasUbicacion
    def set_coordenadasUbicacion(self, coordenadasUbicacion):
        self.coordenadasUbicacion = coordenadasUbicacion
    def get_descripcion(self):
        return self.descripcion
    def set_descripcion(self, descripcion):
        self.descripcion = descripcion
    def get_historia(self):
        return self.historia
    def set_historia(self, historia):
        self.historia = historia
    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nombre):
        self.nombre = nombre
    def get_periodoActualizacion(self):
        return self.periodoActualizacion
    def set_periodoActualizacion(self, periodoActualizacion):
        self.periodoActualizacion = periodoActualizacion
    def get_fechaUltimaActualizacion(self):
        return datetime.strptime(self.fechaUltimaActualizacion, '%d/%m/%Y')
    def set_fechaUltimaActualizacion(self, fechaUltimaActualizacion):
        self.fechaUltimaActualizacion = fechaUltimaActualizacion

    def get_Vinos(self):
        for vino in self.vinos:
            return vino
    def set_Vinos(self, idVino, nombreVino, precioARS, precioUSD, notaCataBodega, imagenEtiqueta, fechaActualizacion):
        for vino in self.vinos:
            if vino.get_Id() == idVino:
                vino.setNombreVino(nombreVino)
                vino.setPrecioARS(precioARS)
                vino.setPrecioUSD(precioUSD)
                vino.setNotaCataBodega(notaCataBodega)
                vino.setImagenEtiqueta(imagenEtiqueta)
                vino.setFechaActualizacion(fechaActualizacion)
                return True



    def tieneActualizacionDisponible(self, fechaActual):
        # Obtener la fecha de la última actualización
        fechaUltimaActualizacion = self.get_fechaUltimaActualizacion()

        # Obtener el período de actualización
        periodoActualizacion = self.get_periodoActualizacion()

        # Calcular la fecha de la próxima actualización
        fechaActualizacion = fechaUltimaActualizacion + relativedelta(months=periodoActualizacion)

        # Verificar si la fecha actual es mayor que la fecha de actualización calculada
        if fechaActual > fechaActualizacion:
            return self
        else:
            return False

        """fechaActualizacion = self.fechaUltimaActualizacion + relativedelta(months=self.get_periodoActualizacion())
        if fechaActual > fechaActualizacion:
            return self
        else:
            return False"""
        

    def tienesEsteVino(self,nombreVino):
        for vino in self.vinos:
            if vino.sos_Este_Vino(nombreVino):
                return True
        return False

    def actualizarDatosVino(self,fechaActualizacion,fechaActual,precio,notaCata,img):
        for vino in self.vinos:
            if vino.sosVinoParaActualizar(fechaActual):
                vino.setPrecioARS(precio)
                vino.setNotaCataBodega(notaCata)
                vino.setImagenEtiqueta(img)
                vino.setFechaActualizacion(fechaActualizacion)
                return True
        return False


    def cargarData(filepath):
            bodegas = []
            with open(filepath, newline='',encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    
                    bodega = Bodega(
                        id=row['id'],
                        nombre=row['nombre'],
                        coordenadasUbicacion=row['coordenadasUbicacion'],
                        descripcion=row['descripcion'],
                        historia=row['historia'],
                        periodoActualizacion=row['periodoActualizacion'],
                        fechaUltimaActualizacion=row['Fecha Ultima Actualizacion'],
                        vinos=row['Vinos'].split(',')
                            # Pass the vinos list as the 'vinos' argument
                        
                    )
                    bodegas.append(bodega)
            return bodegas





   