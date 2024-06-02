from Modelo.varietal import Varietal  # Importa la clase Varietal desde el módulo Modelo.varietal
from datetime import datetime  # Importa la clase datetime para trabajar con fechas
import csv  # Importa el módulo csv para trabajar con archivos CSV
import os
from Modelo.maridaje import Maridaje  # Importa el módulo Modelo.maridaje para trabajar con maridajes

class Vino:

    # Método de inicialización de la clase Vino
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
    def new(self, nombre, añada, fechaActualizacion, precioArs, notaCata, bodega, imagenEtiqueta, maridaje, descripcion, porcentajeComposicion, tiposUvas):
        varietales = []
        for tipo in tiposUvas:
            nuevo = self.crearVarietal(descripcion, porcentajeComposicion, tipo)
            varietales.append(nuevo)
        return Vino(añada, fechaActualizacion, nombre, imagenEtiqueta, notaCata, precioArs, varietales, maridaje, bodega)

    # Método especial para representar la instancia de Vino como una cadena
    def __repr__(self):
        return (f"Vino(nombre={self.nombre}, "
                f"fechaActualizacion={self.fechaActualizacion},  "
                f"precioARS={self.precioARS},"
                f"varietal={self.varietal},"
                f"notaCata={self.notaCata},"
                f"bodega={self.bodega},"
                f"imagenEtiqueta={self.imagenEtiqueta},"
                f"maridaje={self.maridaje}"
                f"añada={self.añada}")

    # Método para verificar si el objeto es efectivamente un vino
    def sosEsteVino(self, nombreVino):
        if self.nombre == nombreVino:
            return True
        return False
        #return isinstance(vino, Vino)

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
        return self.notaCata
    def setNotaCataBodega(self, notaCata):
        self.notaCata = notaCata
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
    def crearVarietal(self, descripcion, porcentajeComposicion, tipoUva):
        varietalNuevo = Varietal.new(descripcion, porcentajeComposicion, tipoUva)
        return varietalNuevo

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
                    vino = Vino(
                        id=row['id'],
                        nombre=row['Nombre'],
                        añada=row['añada'],
                        fechaActualizacion=row['fecha Actualizacion'],
                        precioARS=row['Precio ARS'],
                        notaCata=row['Nota de Cata'],
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
        # Método para convertir la instancia de Vino a un diccionario
        return {
            "id": self.id,
            "nombre": self.nombre,
            "añada": self.añada,
            "fechaActualizacion": self.fechaActualizacion,
            "precioARS": self.precioARS,
            "varietal": self.varietal,
            "notaCata": self.notaCata,
            "bodega": self.bodega,
            "imagenEtiqueta": self.imagenEtiqueta,
            "maridaje": self.maridaje
        }