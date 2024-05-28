# Controlador/gestorImportarActualizacion.py

import os
import sys
from datetime import datetime

# Añadir el directorio principal del proyecto al sys.path
# Esto se agregó porque tengo un quilombo en los path de mi computadora
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from Modelo.bodega import Bodega
from Modelo.vino import Vino
from Modelo.maridaje import Maridaje
from Modelo.tipoUva import TipoUva
    
class GestorImportadorBodega:
    def __init__(self): 
        self.fechaActual = datetime.now() 
        self.bodegasParaActualizar = [] 
        self.bodegaSeleccionada = None
        self.vinosActualizados = []
        self.vinosCreados = []
        self.maridaje = None
        self.tipoDeUva = None
        self.seguidoresDeBodega = []

    def nuevaImportacionActualizacionVinos(self):
        """
        Realiza una nueva importación de actualización de vinos.
        Busca las bodegas con actualizaciones y obtiene las actualizaciones de vinos para cada bodega.
        """
        self.bodegasParaActualizar = self.buscarBodegasConActualizaciones()
        for bodega in self.bodegasParaActualizar:
            self.tomarBodegaSeleccionada(bodega)
            self.obtenerActualizacionVinosBodega()

    def buscarBodegasConActualizaciones(self):
        # Construir la ruta al archivo CSV
        script_dir = os.path.dirname(__file__)
        csv_path = os.path.join(script_dir, '..', 'data', 'ppaiDataExcel.csv')
        
        # Cargar todas las bodegas desde el CSV
        todas_las_bodegas = Bodega.cargar_bodegas_desde_csv(csv_path)
        
        # Obtener las bodegas con actualizaciones disponibles
        bodegas_con_actualizaciones = Bodega.tieneActualizacionDisponible(todas_las_bodegas)
        
        return bodegas_con_actualizaciones

    def buscarBodegaActDisponible(self):
        """
        Simulación de búsqueda de una bodega con actualizaciones disponibles.
        Retorna el nombre de la bodega seleccionada.
        """
        return "Bodega1"

    def tomarBodegaSeleccionada(self, bodega):
        """
        Selecciona una bodega para realizar la importación de actualización de vinos.
        """
        self.bodegaSeleccionada = bodega

    def obtenerActualizacionVinosBodega(self):
        """
        Simulación de obtención de actualizaciones de vinos para la bodega seleccionada.
        Actualiza la lista de vinos actualizados con los nuevos vinos obtenidos.
        """
        self.vinosActualizados = [
            Vino("Vino1", 2020, datetime.now(), "Cabernet Sauvignon", self.bodegaSeleccionada),
            Vino("Vino2", 2019, datetime.now(), "Merlot", self.bodegaSeleccionada)
        ]

    def determinarVinosParaActualizar(self):
        """
        Determina los vinos que necesitan ser actualizados.
        Retorna una lista de vinos que tienen una fecha de actualización anterior a la fecha actual.
        """
        return [vino for vino in self.vinosActualizados if vino.fechaActualizacion < self.fechaActual]

    def getFechaActual(self):
        """
        Obtiene la fecha actual.
        Actualiza el atributo fechaActual con la fecha actual y la retorna.
        """
        self.fechaActual = datetime.now()
        return self.fechaActual

    def actualizarOCrearVinos(self):
        """
        Actualiza o crea los vinos necesarios.
        Itera sobre la lista de vinos para actualizar y verifica si cada vino ya ha sido creado o no.
        Si el vino ya ha sido creado, se actualizan sus características.
        Si el vino no ha sido creado, se crea un nuevo vino.
        """
        vinos_para_actualizar = self.determinarVinosParaActualizar()
        for vino in vinos_para_actualizar:
            if vino in self.vinosCreados:
                self.actualizarCaracteristicasVino(vino)
            else:
                self.crearVino(vino)

    def actualizarCaracteristicasVino(self, vino):
        """
        Actualiza las características de un vino existente.
        Actualiza la fecha de actualización del vino con la fecha actual.
        Imprime un mensaje indicando que se están actualizando las características del vino.
        """
        vino.fechaActualizacion = datetime.now()
        print(f"Actualizando características del {vino.nombre}")

    def crearVino(self, vino):
        """
        Crea un nuevo vino.
        Agrega el vino a la lista de vinos creados.
        Imprime un mensaje indicando que se está creando un nuevo vino.
        """
        self.vinosCreados.append(vino)
        print(f"Creando nuevo {vino.nombre}")

    def buscarMaridaje(self):
        """
        Simulación de búsqueda de maridaje.
        Retorna un objeto Maridaje con un nombre y una descripción.
        """
        self.maridaje = Maridaje("Maridaje1", "Descripción del maridaje")
        return self.maridaje

    def buscarTipoUva(self):
        """
        Simulación de búsqueda de tipo de uva.
        Retorna un objeto TipoUva con un nombre y una descripción.
        """
        self.tipoDeUva = TipoUva("TipoUva1", "Descripción del tipo de uva")
        return self.tipoDeUva

    def buscarSeguidoresDeBodega(self):
        """
        Simulación de búsqueda de seguidores de la bodega seleccionada.
        Retorna una lista de seguidores de la bodega seleccionada.
        """
        self.seguidoresDeBodega = self.bodegaSeleccionada.seguidores
        return self.seguidoresDeBodega

    def calcularFechaActualizacion(self):
        """
        Calcula la fecha de próxima actualización.
        Retorna la fecha actual.
        """
        return self.fechaActual

    def finCU(self):
        """
        Finaliza el caso de uso.
        Imprime un mensaje indicando que se está finalizando el caso de uso.
        """
        print("Finalizando caso de uso")

    def generarNotificacion(self):
        """
        Genera una notificación.
        Imprime un mensaje indicando que se está generando una notificación.
        """
        print("Generando notificación")

# Función de prueba
if __name__ == "__main__":
    gestor = GestorImportadorBodega()
    bodegas_actualizadas = gestor.buscarBodegasConActualizaciones()
    print(f"Total de bodegas con actualizaciones disponibles: {bodegas_actualizadas}")
