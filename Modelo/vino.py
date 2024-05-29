from Modelo.varietal import Varietal
from datetime import datetime
import csv
import os
from Modelo.maridaje import Maridaje

class Vino:
    id = ""
    nombre = ""
    añada = ""
    fechaActualizacion = ""
    precioARS = 0
    varietal = []
    notaCataBodega = ""
    bodega = ""
    imagenEtiqueta = ""
    maridaje = []


    def __init__(self,id, nombre, añada, fechaActualizacion,precioARS,varietal,notaCataBodega, bodega,imagenEtiqueta, maridaje):
        self.id = id
        self.nombre = nombre
        self.añada = añada
        self.fechaActualizacion = fechaActualizacion
        self.bodega = bodega
        self.maridaje = maridaje
        self.notaCataBodega = notaCataBodega
        self.precioARS = precioARS
        self.varietal = varietal
        self.imagenEtiqueta = imagenEtiqueta
        
    def new(self,id,nombre, añada, fechaActualizacion,precioARS,varietales,  notaCataBodega,bodega , imagenEtiqueta,maridaje,id_varietal,descripcion, porcentajeComposicion,tiposUvas ):
        varietales = []
        for tipo in tiposUvas:
            nuevo= self.crear_Varietal(id_varietal,descripcion, porcentajeComposicion,tipo)
            varietales.append(nuevo)
        return Vino(id,nombre, añada, fechaActualizacion,precioARS,varietales,  notaCataBodega,bodega , imagenEtiqueta,maridaje)    
    
    def __repr__(self):
        return (f"Vino(nombre={self.nombre}, "
                f"fechaActualizacion={self.fechaActualizacion},  "
                f"precioARS={self.precioARS},"
                f"varietal={self.varietal},"
                f"notaCataBodega={self.notaCataBodega},"
                f"bodega={self.bodega},"
                f"imagenEtiqueta={self.imagenEtiqueta},"
                f"maridaje={self.maridaje}"
                f"añada={self.añada}" )
    
    #Metodos
    def sos_Este_Vino(self,nombre):
        if self.nombre == nombre:
            return True
        else:
            return False
    def esTuId(self,vino):
        if self.id == vino.id:
            return self
        else:
            return None

    def get_Id(self):
        return self.id
    def set_Id(self,id):
        self.id = id
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre = nombre
    def getAñada(self):
        return self.añada
    def setAñada(self,añada):
        self.añada = añada
    def getFechaActualizacion(self):
        return self.fechaActualizacion
    def setFechaActualizacion(self,fechaActualizacion):
        self.fechaActualizacion = fechaActualizacion
    def getBodega(self):
        return self.bodega
    def setBodega(self,bodega):
        self.bodega = bodega
    def getMaridaje(self):
        for m in self.maridaje:
            return m
    def setMaridaje(self,maridaje): 
        self.maridaje = maridaje
    def getNotaCataBodega(self):
        return self.notaCataBodega
    def setNotaCataBodega(self,notaCataBodega):
        self.notaCataBodega = notaCataBodega
    def getPrecioARS(self):
        return self.precioARS
    def setPrecioARS(self,precioARS):
        self.precioARS = precioARS
    def getImagenEtiqueta(self):
        return self.imagenEtiqueta
    def setImagenEtiqueta(self,imagenEtiqueta):
        self.imagenEtiqueta = imagenEtiqueta
    def getVarietal(self):
        for v in self.varietal:
            return v
    def setVarietal(self,varietal):
        self.varietal = varietal


    def crear_Varietal(self,id,descripcion, porcentajeComposicion,tipoUva):
        varietal_nuevo = Varietal.new(id,descripcion, porcentajeComposicion,tipoUva)
        self.varietal.append(varietal_nuevo)
        return varietal_nuevo


    def es_De_Bodega(self,bodega):
        if self.bodega == bodega:
            return True
        else:
            return False 

    def es_De_Region_Vitivinicola(self,region):
        if self.region == region:
            return True
        else:
            return False

    def get_Fecha_Actualizacion(self):
        return self.fechaActualizacion  


    def sosVinoParaActualizar(self, fechaActual):
        if datetime.strptime(self.fechaActualizacion, "%Y-%m-%d") < datetime.strptime(fechaActual, "%Y-%m-%d"):
            return True
        else:
            return False
          

    def cargarData(filepath):
        vinos = []
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    vino = Vino(
                        id=row['id'],
                        nombre=row['Nombre'],
                        añada=row['añada'],
                        fechaActualizacion=row['fecha Actualizacion'],
                        precioARS=row['Precio ARS'],
                        varietal=row['Varietales'],
                        notaCataBodega=row['Nota de Cata'],
                        bodega=row['Bodega'],
                        imagenEtiqueta=row['Imagen Etiqueta'],
                        maridaje = [],
                        varietal = []
                    )
                    script_dir = os.path.dirname(__file__)
                    path_maridaje = os.path.join(script_dir, '..', 'Modelo', './data/maridaje.csv')
                    TodosLosMaridajes = Maridaje.cargarData(path_maridaje)

                    for maridaje_id in row['Maridajes'].split(';'):
                        for maridaje in TodosLosMaridajes:
                            if maridaje.get_Id() == maridaje_id:
                                vino.maridaje.append(maridaje)

                    script_dir = os.path.dirname(__file__)
                    path_varietal = os.path.join(script_dir, '..', 'Modelo', './data/varietal.csv')
                    TodosLosVarietales = Varietal.cargarData(path_varietal)

                    for varietal_id in row['Varietales'].split(';'):
                        for varietal in TodosLosVarietales:
                            if varietal.get_Id() == varietal_id:
                                vino.varietal.append(varietal)                    

                    vinos.append(vino)

                except ValueError as e:
                    print(f"Error al procesar la fila: {row}. Error: {e}")
        return vinos
    
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "añada": self.añada,
            "fechaActualizacion": self.fechaActualizacion,
            "precioARS": self.precioARS,
            "varietal": self.varietal,
            "notaCataBodega": self.notaCataBodega,
            "bodega": self.bodega,
            "imagenEtiqueta": self.imagenEtiqueta,
            "maridaje": self.maridaje
        }

 # Ejemplo de uso
if __name__ == "__main__":
      vinos = Vino.cargarData("./Modelo/data/vino.csv")
      for vino in vinos:
          print(vino)