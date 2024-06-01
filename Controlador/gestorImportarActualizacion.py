# Controlador/gestorImportarActualizacion.py

import os
import sys
from datetime import datetime, date 

# Añadir el directorio principal del proyecto al sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from Modelo.bodega import Bodega
from Modelo.maridaje import Maridaje
from Modelo.tipoUva import TipoUva
from Modelo.base import bodegas, varietales, tiposUva, vino
    
class GestorImportadorBodega:
    def __init__(self): 
        self.fechaActual = None
        self.bodegasParaActualizar = [] 
        self.bodegaSeleccionada = None
        self.vinosActualizados = []
        self.vinosCreados = []
        self.maridaje = None
        self.tipoDeUva = None
        self.bodegas= None
        self.varietales= None
        self.seguidoresDeBodega = []
        self.vinosParaActualizar = []

    def nuevaImportacionActualizacionVinos(self):
        self.cargarBase()
        self.getFechaActual()
        self.bodegasParaActualizar = self.buscarBodegasConActualizaciones()
        return self.bodegasParaActualizar

    def cargarBase(self):
        self.bodegas = bodegas
        self.varietales= varietales
        self.tipoDeUva= tiposUva


    def getFechaActual(self):
        self.fechaActual = datetime.now().date()
        return self.fechaActual

    def buscarBodegasConActualizaciones(self):
        script_dir = os.path.dirname(__file__)
        csv_path = os.path.join(script_dir, '..', 'Modelo', './data/bodega.csv')
        self.bodegasParaActualizar = []
        for bodega in bodegas:
            if bodega.tieneActualizacionDisponible(self.fechaActual):
                self.bodegasParaActualizar.append(bodega)
        for bodega in self.bodegasParaActualizar:
            bodega.get_nombre()
        bodegas_con_actualizaciones_dicts = [bodega.to_dict() for bodega in self.bodegasParaActualizar]
        
        return bodegas_con_actualizaciones_dicts


    def tomarBodegaSeleccionada(self, bodega):
        self.bodegaSeleccionada = Bodega.from_dict(bodega)
        # print(f"Bodega seleccionada desde gestor: {self.bodegaSeleccionada}")
        self.obtenerActualizacionVinosBodega()
        self.determinarVinosParaActualizar()
        self.actualizarOCrearVinos()
        # self.buscarSeguidoresDeBodega()
        

    def obtenerActualizacionVinosBodega(self):
        # Simulación de obtención de actualizaciones de vinos para la bodega seleccionada por parte de una API.
        self.vinosActualizados = [
            {
                'nombre': 'Trumpeter', 
                'añada': 2018,
                'fecha Actualizacion': "2024-01-15", 
                'Imagen Etiqueta': 'https://i.colnect.net/f/3919/903/Trumpeter---Sauvignon-Blanc.jpg',
                'Nota de Cata': 'Notas de ciruela y roble',
                'Precio ARS': 1500,
                'Maridajes': ["Malbec y Gouda", "Chardonnay y Salmón", "Cabernet Sauvignon y Cordero"],
                'Varietales': ["Vino tinto de color rojo rubí con aromas a cereza, vainilla y cuero."],
                'bodega': self.bodegaSeleccionada,
                'nombre Bodega': self.bodegaSeleccionada.nombre,
                'tipoUva': ["Pinot Grigio"]
            },
            {
                'nombre': 'Dada', 
                'añada': 2019, 
                'fecha Actualizacion': "2024-02-10", 
                'Imagen Etiqueta': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQelj-P5HqS_pTzC8YnXnpWkmpjBhBrSnErPORRgquoP03L_IrIxzSX1-mtCRVDWn1yyTc&usqp=CAU',
                'Nota de Cata': 'Notas de cassis y pimienta negra',
                'Precio ARS': 2000,
                'Maridajes': ["Pinot Noir y Ensalada","Brut Rosé y Sushi"],
                'Varietales': ["Vino tinto de color rojo claro con aromas a fresa, cereza roja y setas.", "Vino blanco de color amarillo pajizo con aromas a heno, melocotón y cítricos."],
                'bodega': self.bodegaSeleccionada,
                'nombre Bodega': self.bodegaSeleccionada.nombre,
                'tipoUva': ["Syrah", "Sauvignon Blanc"]
            },
            {
                'nombre': 'Vino3', 
                'añada': 2020, 
                'fecha Actualizacion': "2024-02-10", 
                'Imagen Etiqueta': 'https://example.com/vino3.jpg',
                'Nota de Cata': 'Aromas de frutas rojas y especias',
                'Precio ARS': 1800,
                'Maridajes': ["Chardonnay y Salmón", "Cabernet Sauvignon y Cordero"],
                'Varietales': ["Vino tinto de color púrpura oscuro con aromas a grosella negra, cedro y tabaco.", "Vino tinto de color rojo rubí con aromas a cereza, vainilla y cuero."],
                'bodega': self.bodegaSeleccionada,
                'nombre Bodega': self.bodegaSeleccionada.nombre,
                'tipoUva': ["Malbec", "Pinot Grigio"]
            },
            {
                'nombre': 'Vino4', 
                'añada': 2021, 
                'fecha Actualizacion': "2024-03-12", 
                'Imagen Etiqueta': 'https://example.com/vino4.jpg',
                'Nota de Cata': 'Sabor intenso con notas de chocolate y vainilla',
                'Precio ARS': 2200,
                'Maridajes': ["Malbec y Gouda", "Brut Rosé y Sushi"],
                'Varietales': ["Vino tinto de color rojo intenso con aromas a frutos rojos, especias y cuero.", "Vino blanco de color amarillo pajizo con aromas a heno, melocotón y cítricos."],
                'bodega': self.bodegaSeleccionada,
                'nombre Bodega': self.bodegaSeleccionada.nombre,
                'tipoUva': ["Cabernet Sauvignon", "Sauvignon Blanc"]
            },
            {
                'nombre': 'Vino5', 
                'añada': 2017, 
                'fecha Actualizacion': "2023-11-08", 
                'Imagen Etiqueta': 'https://example.com/vino5.jpg',
                'Nota de Cata': 'Textura suave y aterciopelada con toques de mora',
                'Precio ARS': 2500,
                'Maridajes': ["Verdejo y Tapas", "Sauvignon Blanc y Ceviche"],
                'Varietales': ["Vino tinto de color violeta intenso con aromas a frutos negros, pimienta negra y violetas.", "Vino blanco de color verde pálido con aromas a grosella espinosa, hierba fresca y pomelo."],
                'bodega': self.bodegaSeleccionada,
                'nombre Bodega': self.bodegaSeleccionada.nombre,
                'tipoUva': ["Gewürztraminer", "Chardonnay"]
            }
        ]


    def determinarVinosParaActualizar(self):
        """Esta función determina todos los vinos que nos devolvió la simulación de la API, que pertenecen a la bodega seleccionada"""
        self.vinosParaActualizar = []
        for vino in self.vinosActualizados:
            if self.bodegaSeleccionada.tienesEsteVino(vino['nombre']):
                self.vinosParaActualizar.append(vino)


    def actualizarOCrearVinos(self):
        vinos_actualizados = []
        vinos_creados = []

        for vino in self.vinosActualizados:
            if vino in self.vinosParaActualizar:
                self.bodegaSeleccionada.actualizarDatosVino(vino['nombre'], vino['fecha Actualizacion'], self.fechaActual, vino['Precio ARS'], vino['Nota de Cata'], vino['Imagen Etiqueta'])
                vinos_actualizados.append.append(vino)
            else:
                self.crearVino(vino)
                vinos_creados.append(vino)
        
        # print(f"FORMATO: {obtenerResumenVinos_dict}")
        return vinos_actualizados, vinos_creados
    

    def crearVino(self, vino):
        self.buscarMaridaje(vino)
        self.buscarTipoUva(vino)
        self.vinosCreados.append(vino)
        # print(f"Creando nuevo {vino['nombre']}")


    def buscarMaridaje(self, vino):
        maridajes = []
        for maridaje_nombre in vino['Maridajes']:
            maridaje = Maridaje.sosMaridaje(maridaje_nombre)
            if maridaje:
                maridajes.append(maridaje)
        return maridajes

        
    def buscarTipoUva(self, vino):
        tiposUva = []
        for tipoUva_nombre in vino['tipoUva']:
            tipoUva = TipoUva.sosTipoUva(tipoUva_nombre)
            if tipoUva:
                tiposUva.append(tipoUva)
        return tiposUva
    

    """def buscarSeguidoresDeBodega(self):
        from Modelo.enofilo import Enofilo
        script_dir = os.path.dirname(__file__)
        csv_path = os.path.join(script_dir, '..', 'Modelo', './data/enofilo.csv')
        todos_los_Enofilos = Enofilo.cargarData(csv_path)
        
        for enofilo in todos_los_Enofilos:
            if enofilo.seguisBodega(self.bodegaSeleccionada):
                self.seguidoresDeBodega.append(enofilo)
        print("seguidores encontrados")

        for i in self.seguidoresDeBodega:
            print(i.obtenerNombre())"""
        
    def finCU(self):
        sys.exit()