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

    def cargar_bodegas_desde_csv(filepath):
        bodegas = []
        with open(filepath, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Verificar si la cadena no está vacía antes de intentar convertirla a un entero
                actualizacion_disponible = row['actualizacionDisponible']
                if actualizacion_disponible:
                    actualizacion_disponible = bool(int(actualizacion_disponible))
                else:
                    actualizacion_disponible = False
                bodega = Bodega(
                    nombre=row['nombre'],
                    coordenadasUbicacion=row['coordenadasUbicacion'],
                    descripcion=row['descripcion'],
                    historia=row['historia'],
                    periodoActualizacion=row['periodoActualizacion'],
                    actualizacionDisponible=actualizacion_disponible
                )
                bodegas.append(bodega)
        return bodegas

    def tieneActualizacionDisponible(bodegas):
        # Filtrar las bodegas que tienen actualizacionDisponible igual a True
        return [bodega for bodega in bodegas if bodega.actualizacionDisponible]
