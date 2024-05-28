# Modelo/bodega.py

import csv

class Bodega:
    def __init__(self, nombre, coordenadasUbicacion, descripcion, historia, periodoActualizacion, actualizacionDisponible):
        self.nombre = nombre
        self.coordenadasUbicacion = coordenadasUbicacion
        self.descripcion = descripcion
        self.historia = historia
        self.periodoActualizacion = int(periodoActualizacion)
        self.actualizacionDisponible = bool(int(actualizacionDisponible)) if actualizacionDisponible else False  # Convertir a booleano si no está vacío, de lo contrario, establecer como False

    @classmethod
    def cargar_bodegas_desde_csv(cls, csv_path):
        bodegas = []
        with open(csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                actualizacion_disponible = row['actualizacionDisponible']
                if actualizacion_disponible:
                    actualizacion_disponible = bool(int(actualizacion_disponible))
                else:
                    actualizacion_disponible = False
                bodega = cls(
                    nombre=row['nombre'],
                    coordenadasUbicacion=row['coordenadasUbicacion'],
                    descripcion=row['descripcion'],
                    historia=row['historia'],
                    periodoActualizacion=row['periodoActualizacion'],
                    actualizacionDisponible=actualizacion_disponible
                )
                bodegas.append(bodega)
        return bodegas

    @classmethod
    def tieneActualizacionDisponible(cls, bodegas):
        return [bodega for bodega in bodegas if bodega.actualizacionDisponible]

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'coordenadasUbicacion': self.coordenadasUbicacion,
            'descripcion': self.descripcion,
            'historia': self.historia,
            'periodoActualizacion': self.periodoActualizacion,
            'actualizacionDisponible': self.actualizacionDisponible,
        }
