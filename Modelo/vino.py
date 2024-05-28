from Modelo.varietal import Varietal
from datetime import datetime
class Vino():
    id=""
    añada = 0
    fechaActualizacion=""
    nombre = ""
    imagenEtiqueta = ""
    notaCataBodega= 0
    precioARS = 0
    maridaje = []
    varietal = []
    bodega = None

    def __init__(self,id, nombre, añada, fechaActualizacion,precioARS,varietal,notaCataBodega, bodega, maridaje):
        self.id = id
        self.nombre = nombre
        self.añada = añada
        self.fechaActualizacion = fechaActualizacion
        self.bodega = bodega
        self.maridaje = maridaje
        self.notaCataBodega = notaCataBodega
        self.precioARS = precioARS
        self.varietal = varietal
        
    def new(self,id, nombre, añada, fechaActualizacion, tipoUva, bodega, maridaje):
        return Vino(id,nombre, añada, fechaActualizacion, tipoUva, bodega, maridaje)

    #Metodos
    def sos_Este_Vino(self,nombre):
        if self.nombre == nombre:
            return True
        else:
            return False

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
        return self.maridaje
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
        return self.varietal
    def setVarietal(self,varietal):
        self.varietal = varietal


    def crear_Varietal(self,descripcion, porcentajeComposicion):
        varietal_nuevo = Varietal.new(descripcion, porcentajeComposicion)
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
          