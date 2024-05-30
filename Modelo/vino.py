from Modelo.varietal import Varietal  # Importa la clase Varietal desde el módulo Modelo.varietal
from datetime import datetime  # Importa la clase datetime para trabajar con fechas
import csv  # Importa el módulo csv para trabajar con archivos CSV

class Vino:
    # Atributos de la clase Vino
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

    # Método de inicialización de la clase Vino
    def __init__(self, id, nombre, añada, fechaActualizacion, precioARS, varietal, notaCataBodega, bodega, imagenEtiqueta, maridaje):
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

    # Método para crear y devolver una nueva instancia de Vino
    def new(self, id, nombre, añada, fechaActualizacion, precioARS, varietal, notaCataBodega, bodega, imagenEtiqueta, maridaje, id_varietal, descripcion, porcentajeComposicion, tiposUvas):
        varietales = []
        for tipo in tiposUvas:
            nuevo = self.crear_Varietal(id_varietal, descripcion, porcentajeComposicion, tipo)
            varietales.append(nuevo)
        return Vino(id, nombre, añada, fechaActualizacion, precioARS, varietales, notaCataBodega, bodega, imagenEtiqueta, maridaje)

    # Método especial para representar la instancia de Vino como una cadena
    def __repr__(self):
        return (f"Vino(nombre={self.nombre}, "
                f"fechaActualizacion={self.fechaActualizacion},  "
                f"precioARS={self.precioARS},"
                f"varietal={self.varietal},"
                f"notaCataBodega={self.notaCataBodega},"
                f"bodega={self.bodega},"
                f"imagenEtiqueta={self.imagenEtiqueta},"
                f"maridaje={self.maridaje}"
                f"añada={self.añada}")

    # Método para verificar si el nombre del vino coincide
    def sos_Este_Vino(self, nombre):
        if self.nombre == nombre:
            return True
        else:
            return False

    # Método para verificar si el ID del vino coincide
    def esTuId(self, vino):
        if self.id == vino.id:
            return self
        else:
            return None

    # Métodos getter y setter para los atributos de la clase
    def get_Id(self):
        return self.id
    def set_Id(self, id):
        self.id = id
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
    def getNotaCataBodega(self):
        return self.notaCataBodega
    def setNotaCataBodega(self, notaCataBodega):
        self.notaCataBodega = notaCataBodega
    def getPrecioARS(self):
        return self.precioARS
    def setPrecioARS(self, precioARS):
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
    def crear_Varietal(self, id, descripcion, porcentajeComposicion, tipoUva):
        varietal_nuevo = Varietal.new(id, descripcion, porcentajeComposicion, tipoUva)
        self.varietal.append(varietal_nuevo)
        return varietal_nuevo

    # Método para verificar si el vino es de una bodega específica
    def es_De_Bodega(self, bodega):
        if self.bodega == bodega:
            return True
        else:
            return False

    # Método para verificar si el vino es de una región vitivinícola específica
    def es_De_Region_Vitivinicola(self, region):
        if self.region == region:
            return True
        else:
            return False

    # Método para obtener la fecha de actualización del vino
    def get_Fecha_Actualizacion(self):
        return self.fechaActualizacion

    # Método para verificar si el vino necesita actualización
    def sosVinoParaActualizar(self, fechaActual):
        if datetime.strptime(self.fechaActualizacion, "%Y-%m-%d") < datetime.strptime(fechaActual, "%Y-%m-%d"):
            return True
        else:
            return False

    # Método estático para cargar datos desde un archivo CSV
    @staticmethod
    def cargarData(filepath):
        vinos = []
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    # Crea una instancia de Vino con los datos de la fila actual
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
                        maridaje=row['Maridajes']
                    )
                    vinos.append(vino)  # Agrega el vino a la lista de vinos
                except ValueError as e:
                    print(f"Error al procesar la fila: {row}. Error: {e}")
        return vinos
    
    def to_dict(self):
        # Método para convertir la instancia de Vino a un diccionario
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