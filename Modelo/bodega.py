import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta  
from Modelo.vino import Vino
import os
import os

class Bodega:
    id = ""
    coordenadasUbicacion = ""
    descripcion = ""
    historia = ""
    nombre = ""
    periodoActualizacion = 0
    fechaUltimaActualizacion = ""
    vinos = []


    def __init__(self, id, coordenadasUbicacion, descripcion, historia, nombre, periodoActualizacion, fechaUltimaActualizacion, vinos):
        self.id = id
        self.coordenadasUbicacion = coordenadasUbicacion
        self.descripcion = descripcion
        self.historia = historia
        self.nombre = nombre
        self.periodoActualizacion = int(periodoActualizacion) if periodoActualizacion else 0
        self.fechaUltimaActualizacion = fechaUltimaActualizacion
        self.vinos = vinos

    def __repr__(self):
        return (f"Bodega(nombre={self.nombre}, "
                f"fechaUltimaActualizacion={self.fechaUltimaActualizacion},  "
                f"periodoActualizacion={self.periodoActualizacion},"
                f"coordenadasUbicacion={self.coordenadasUbicacion},"
                f"descripcion={self.descripcion},"
                f"historia={self.historia},"
                f"vino={self.vinos})")

    # MÃ©todos de la clase BODEGA
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

    def set_periodoActualizacion(self, periodoActualizacion):
        self.periodoActualizacion = int(periodoActualizacion)

    def get_Vinos(self):
        return self.vinos

    def set_Vinos(self, vinos):
        self.vinos = vinos

    def tieneActualizacionDisponible(self, fechaActual):
        fechaUltimaActualizacion = self.get_fechaUltimaActualizacion()

        periodoActualizacion = self.get_periodoActualizacion()
        fechaActualizacion = fechaUltimaActualizacion + relativedelta(months=periodoActualizacion)

        if fechaActualizacion < fechaActual:
            return self
        
    def get_fechaUltimaActualizacion(self):
        if self.fechaUltimaActualizacion:
            return datetime.strptime(self.fechaUltimaActualizacion, '%d/%m/%Y')
        return None
    
    def get_periodoActualizacion(self):
        return self.periodoActualizacion

    def set_fechaUltimaActualizacion(self, fechaUltimaActualizacion):
        self.fechaUltimaActualizacion = fechaUltimaActualizacion

    def tienesEsteVino(self, nombreVino):
        for vino in self.vinos:
           if vino.sos_Este_Vino(nombreVino):
                return True


    def actualizarDatosVino(self, fechaActualizacion, fechaActual, precio, notaCata, img):
        for vino in self.vinos:
            if vino.sosVinoParaActualizar(fechaActual):
                vino.setPrecioARS(precio)
                vino.setNotaCataBodega(notaCata)
                vino.setImagenEtiqueta(img)
                vino.setFechaActualizacion(fechaActualizacion)
                return True
        return False

    @staticmethod
    def cargarData(filepath):
        bodegas = []
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    bodega = Bodega(
                        id=row['id'],
                        nombre=row['nombre'],
                        coordenadasUbicacion=row['coordenadasUbicacion'],
                        descripcion=row['descripcion'],
                        historia=row['historia'],
                        periodoActualizacion=int(row['periodoActualizacion']),
                        fechaUltimaActualizacion=row['Fecha Ultima Actualizacion'],
                        vinos=[]
                    )
                    
                    # Si se quiere cargar la lista de vinos de la bodega, se puede hacer algo como:
                    #
                    script_dir = os.path.dirname(__file__)
                    path_vinos = os.path.join(script_dir, '..', 'Modelo', './data/vino.csv')
                    TodosLosVinos = Vino.cargarData(path_vinos)
                    
                    for vino_id in row['Vinos'].split(';'):
                        for vino in TodosLosVinos:
                            if vino.get_Id() == vino_id:
                                bodega.vinos.append(vino)
                    
                    bodegas.append(bodega)
                except ValueError as e:
                    print(f"Error al procesar la fila: {row}. Error: {e}")
        return bodegas
    
    def to_dict(self):
        return {
            'id': self.id,
            'coordenadasUbicacion': self.coordenadasUbicacion,
            'descripcion': self.descripcion,
            'historia': self.historia,
            'nombre': self.nombre,
            'periodoActualizacion': self.periodoActualizacion,
            'fechaUltimaActualizacion': self.fechaUltimaActualizacion,
            'vinos': self.vinos
        }
    def from_dict(data):
        id = data['id']
        coordenadasUbicacion = data['coordenadasUbicacion']
        descripcion = data['descripcion']
        historia = data['historia']
        nombre = data['nombre']
        periodoActualizacion = data['periodoActualizacion']
        fechaUltimaActualizacion = data['fechaUltimaActualizacion']
        vinos = data['vinos']
        
        return Bodega(id, coordenadasUbicacion, descripcion, historia, nombre, periodoActualizacion, fechaUltimaActualizacion, vinos)

# Ejemplo de uso
if __name__ == "__main__":
    bodegas = Bodega.cargarData("ruta_al_archivo.csv")
    for bodega in bodegas:
        print(bodega)