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
        self.vinosParaActualizar = []

    def nuevaImportacionActualizacionVinos(self):
        self.bodegasParaActualizar = self.buscarBodegasConActualizaciones()
        for bodega in self.bodegasParaActualizar:
            self.tomarBodegaSeleccionada(bodega)
            self.obtenerActualizacionVinosBodega()

    def getFechaActual(self):
        self.fechaActual = datetime.now()
        return self.fechaActual

    def buscarBodegasConActualizaciones(self):
        script_dir = os.path.dirname(__file__)
        csv_path = os.path.join(script_dir, '..', 'Modelo', './data/bodega.csv')
        todas_las_bodegas = Bodega.cargarData(csv_path)
        fechaActual = self.getFechaActual()
        for bodega in todas_las_bodegas:
            if bodega.tieneActualizacionDisponible(self.getFechaActual()):
                self.bodegasParaActualizar.append(bodega.tieneActualizacionDisponible(fechaActual))
        for bodega in self.bodegasParaActualizar:
            bodega.get_nombre()
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
        # Simulación de obtención de actualizaciones de vinos para la bodega seleccionada.
        self.vinosActualizados = [
            {
                'nombre': 'Trumpeter', 
                'añada': 2018, 
                'fecha Actualizacion': "2024-01-15", 
                'Imagen Etiqueta': 'https://i.colnect.net/f/3919/903/Trumpeter---Sauvignon-Blanc.jpg',
                'Nota de Cata': 'Notas de ciruela y roble',
                'Precio ARS': 1500,
                'Maridajes': ['m1', 'm2', 'm3'],
                'Varietales': 'v1;v2;v3',
                'bodega': self.bodegaSeleccionada
            },
            {
                'nombre': 'Dada', 
                'añada': 2019, 
                'fecha Actualizacion': "2024-02-10", 
                'Imagen Etiqueta': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQelj-P5HqS_pTzC8YnXnpWkmpjBhBrSnErPORRgquoP03L_IrIxzSX1-mtCRVDWn1yyTc&usqp=CAU',
                'Nota de Cata': 'Notas de cassis y pimienta negra',
                'Precio ARS': 2000,
                'Maridajes': ['m4', 'm5'],
                'Varietales': 'v3;v6',
                'bodega': self.bodegaSeleccionada
            },
            {
                'nombre': 'Vino3', 
                'añada': 2020, 
                'fecha Actualizacion': "2024-02-10", 
                'Imagen Etiqueta': 'https://example.com/vino3.jpg',
                'Nota de Cata': 'Aromas de frutas rojas y especias',
                'Precio ARS': 1800,
                'Maridajes': ['m2', 'm3'],
                'Varietales': 'v2;v4',
                'bodega': self.bodegaSeleccionada
            },
            {
                'nombre': 'Vino4', 
                'añada': 2021, 
                'fecha Actualizacion': "2024-03-12", 
                'Imagen Etiqueta': 'https://example.com/vino4.jpg',
                'Nota de Cata': 'Sabor intenso con notas de chocolate y vainilla',
                'Precio ARS': 2200,
                'Maridajes': ['m1', 'm5'],
                'Varietales': 'v1;v5',
                'bodega': self.bodegaSeleccionada
            },
            {
                'nombre': 'Vino5', 
                'añada': 2017, 
                'fecha Actualizacion': "2023-11-08", 
                'Imagen Etiqueta': 'https://example.com/vino5.jpg',
                'Nota de Cata': 'Textura suave y aterciopelada con toques de mora',
                'Precio ARS': 2500,
                'Maridajes': ['m3', 'm4'],
                'Varietales': 'v3;v6',
                'bodega': self.bodegaSeleccionada
            }
        ]

    def determinarVinosParaActualizar(self):
        for vino in self.vinosActualizados: 
            if Bodega.tienesEsteVino(self,vino.nombre):
                self.vinosParaActualizar.append(vino)


    def actualizarOCrearVinos(self):
        self.obtenerActualizacionVinosBodega()
        obtenerResumenVinos_dict = None

        for vino in self.vinosActualizados:
            if vino in self.vinosParaActualizar:
                print(f"Actualizando {vino}")
                self.actualizarCaracteristicasVino(vino['fechaActualizacion'],self.fechaActual,vino['precio'],vino['cata'],vino['img'])
                self.vinosCreados.append(vino)
                print(f"Vino {vino} actualizado")
            else:
                print(f"Creando nuevo {vino}")
                self.crearVino(vino)
                self.vinosCreados.append(vino)
            # Obtener un resumen de los vinos actualizados y creados en formato de diccionario
            obtenerResumenVinos_dict = [vino.to_dict() for vino in (self.vinosActualizados + self.vinosCreados)]
        
        return obtenerResumenVinos_dict
        # self.mostrarResumenVinos(obtenerResumenVinos_dict)

    def actualizarCaracteristicasVino(self,fechaActualizacion,fechaActual,precio,notaCata,img):  
        Bodega.actualizarDatosVino(self,fechaActualizacion,fechaActual,precio,notaCata,img)

    def crearVino(self, vino):
        maridaje = self.buscarMaridaje(vino)
        tipoUva = self.buscarTipoUva(vino)
        self.vinosCreados.append(vino)
        print(f"Creando nuevo {vino.nombre}")

    def buscarMaridaje(self, vino):
        maridajes = []
        for maridaje in vino['Maridajes']:
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
    # print(f"\nTotal de bodegas con actualizaciones disponibles: {bodegas_actualizadas}")

    bodegasActual = gestor.actualizarOCrearVinos()
    print(f"\nResumen de vinos actualizados y creados: {bodegasActual}")