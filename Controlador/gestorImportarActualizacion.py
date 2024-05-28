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
from Modelo.varietal import Varietal
    
class GestorImportadorBodega:
    def __init__(self): 
        self.fechaActual = None
        self.bodegasParaActualizar = [] 
        self.bodegaSeleccionada = None
        self.vinosActualizados = []
        self.vinosCreados = []
        self.maridaje = None
        self.tipoDeUva = None
        self.seguidoresDeBodega = []
        self.vinos_para_actualizar = []

    def nuevaImportacionActualizacionVinos(self):
        self.bodegasParaActualizar = self.buscarBodegasConActualizaciones()
        for bodega in self.bodegasParaActualizar:
            self.tomarBodegaSeleccionada(bodega)
            self.obtenerActualizacionVinosBodega

    def getFechaActual(self):
        self.fechaActual = datetime.now()
        return self.fechaActual

    def buscarBodegasConActualizaciones(self):
        script_dir = os.path.dirname(__file__)
        csv_path = os.path.join(script_dir, '..', 'Modelo', './data/bodega.csv')
        todas_las_bodegas = Bodega.cargarData(csv_path)
        for bodega in todas_las_bodegas:
            self.bodegasParaActualizar.append(bodega.tieneActualizacionDisponible(self.fechaActual))
        for bodega in self.bodegasParaActualizar:
            bodega.getNombre()
        bodegas_con_actualizaciones_dicts = [bodega.to_dict() for bodega in self.bodegasParaActualizar]
        
        return bodegas_con_actualizaciones_dicts


    def buscarBodegaActDisponible(self):
        
        #Simulación de búsqueda de una bodega con actualizaciones disponibles.
        #Retorna el nombre de la bodega seleccionada.
        return "Bodega1"

    def tomarBodegaSeleccionada(self, bodega):
        self.bodegaSeleccionada = bodega
        print(f"Bodega seleccionada desde gestor: {self.bodegaSeleccionada}")
        return bodega

    def obtenerActualizacionVinosBodega(self):
        #Simulación de obtención de actualizaciones de vinos para la bodega seleccionada.
        #Actualiza la lista de vinos actualizados con los nuevos vinos obtenidos.(self, nombre, añada, fechaActualizacion, tipoUva, bodega, maridaje
        self.vinosActualizados = [{'nombre':'Vino1', 'añada':2020, 'fecha de actualizacion': 2021,'Varietal':'Cabernet Sauvignon','bodega' :self.bodegaSeleccionada},
            {"Vino2", 2019, datetime.now(), "Merlot", self.bodegaSeleccionada}]

    def determinarVinosParaActualizar(self):
        for vino in self.vinosActualizados: 
            if Bodega.tienesEsteVino(self,vino.nombre):
                self.vinos_para_actualizar.append(vino)


    def actualizarOCrearVinos(self):
        for vino in self.vinosActualizados:
            if vino in self.vinos_para_actualizar:
                #se actualizan los vinos que ya estan en el sistema
                #Pactar funcion actualizar caracteristicas vinos con los chicos tema true false
                self.actualizarCaracteristicasVino(self,vino.fechaActualizacion,self.fechaActual,vino.precio,vino.cata,vino.img)
            else:
                #se crean los vinos que no estan en el sistema
                self.crearVino(vino)

    def actualizarCaracteristicasVino(self,fechaActualizacion,fechaActual,precio,notaCata,img):  
        Bodega.actualizarDatosVino(self,fechaActualizacion,fechaActual,precio,notaCata,img)

    def crearVino(self, vino):
        maridaje = self.buscarMaridaje(vino)
        tipoUva = self.buscarTipoUva(vino)
        self.vinosCreados.append(vino)
        print(f"Creando nuevo {vino.nombre}")

    def buscarMaridaje(self, vino):
        maridajes = []
        for maridaje in vino['maridaje']:
            maridajes.append(Maridaje.sosMaridaje(maridaje)) 

        return maridajes
        
    def buscarTipoUva(self, vino):
        tiposUva = []
        for tipoUva in vino['tiposUva']:
            tiposUva.append(Maridaje.sosMaridaje(tipoUva)) 

        return tiposUva

# Función de prueba
if __name__ == "__main__":
    gestor = GestorImportadorBodega()
    bodegas_actualizadas = gestor.buscarBodegasConActualizaciones()
    print(f"Total de bodegas con actualizaciones disponibles: {bodegas_actualizadas}")