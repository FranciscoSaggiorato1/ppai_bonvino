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
from Modelo.vino import Vino
from Modelo.base import bodegas, varietales, tiposUva, vinos, enofilos, siguiendos, usuarios, maridajes

    
class GestorImportadorBodega:
    def __init__(self): 
        self.fechaActual = None
        self.bodegasParaActualizar = [] 
        self.bodegaSeleccionada = None
        self.vinosActualizados = []
        self.vinosCreados = []
        self.varietales= None
        self.seguidoresDeBodega = []
        self.vinosParaActualizar = []
        self.vinos = []
        self.bodegas= []
        self.varietales = []
        self.maridajes = []
        self.tiposUva = []
        self.enofilos = []
        self.siguiendo = []
        self.usarios = []        

    def nuevaImportacionActualizacionVinos(self):
        self.cargarBase()
        self.getFechaActual()
        self.bodegasParaActualizar = self.buscarBodegasConActualizaciones()
        return self.bodegasParaActualizar

    def cargarBase(self):
        self.bodegas = bodegas
        self.enofilos = enofilos
        self.maridaje = maridajes
        self.siguiendo = siguiendos
        self.tiposUva= tiposUva
        self.usuarios = usuarios
        self.varietales= varietales
        self.vinos = vinos


    def getFechaActual(self):
        self.fechaActual = datetime.now().date()
        return self.fechaActual

    def buscarBodegasConActualizaciones(self):
        self.bodegasParaActualizar = []
        for bodega in bodegas:
            if bodega.tieneActualizacionDisponible(self.fechaActual):
                self.bodegasParaActualizar.append(bodega)
        for bodega in self.bodegasParaActualizar:
            # Validar con diagrama de secuencias, no está este método en el diagrama
            bodega.getNombre()
        bodegasDict = [bodega.toDict() for bodega in self.bodegasParaActualizar]
        
        return bodegasDict

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
                'fechaActualizacion': "2024-01-15", 
                'imagenEtiqueta': 'https://i.colnect.net/f/3919/903/Trumpeter---Sauvignon-Blanc.jpg',
                'notaCata': 'Notas de ciruela y roble',
                'precioArs': 1500,
                'maridajes': ["Malbec y Gouda", "Chardonnay y Salmón", "Cabernet Sauvignon y Cordero"],
                'varietales': ["Vino tinto de color rojo rubí con aromas a cereza, vainilla y cuero."],
                'bodega': self.bodegaSeleccionada,
                'nombreBodega': self.bodegaSeleccionada.nombre,
                'tipoUva': ["Pinot Grigio"]
            },
            {
                'nombre': 'Dada', 
                'añada': 2019, 
                'fechaActualizacion': "2024-02-10", 
                'imagenEtiqueta': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQelj-P5HqS_pTzC8YnXnpWkmpjBhBrSnErPORRgquoP03L_IrIxzSX1-mtCRVDWn1yyTc&usqp=CAU',
                'notaCata': 'Notas de cassis y pimienta negra',
                'precioArs': 2000,
                'maridajes': ["Pinot Noir y Ensalada","Brut Rosé y Sushi"],
                'varietales': ["Vino tinto de color rojo claro con aromas a fresa, cereza roja y setas.", "Vino blanco de color amarillo pajizo con aromas a heno, melocotón y cítricos."],
                'bodega': self.bodegaSeleccionada,
                'nombreBodega': self.bodegaSeleccionada.nombre,
                'tipoUva': ["Syrah", "Sauvignon Blanc"]
            },
            {
                'nombre': 'Vino3', 
                'añada': 2020, 
                'fechaActualizacion': "2024-02-10", 
                'imagenEtiqueta': 'https://example.com/vino3.jpg',
                'notaCata': 'Aromas de frutas rojas y especias',
                'precioArs': 1800,
                'maridajes': ["Chardonnay y Salmón", "Cabernet Sauvignon y Cordero"],
                'varietales': ["Vino tinto de color púrpura oscuro con aromas a grosella negra, cedro y tabaco.", "Vino tinto de color rojo rubí con aromas a cereza, vainilla y cuero."],
                'bodega': self.bodegaSeleccionada,
                'nombreBodega': self.bodegaSeleccionada.nombre,
                'tipoUva': ["Malbec", "Pinot Grigio"]
            },
            {
                'nombre': 'Vino4', 
                'añada': 2021, 
                'fechaActualizacion': "2024-03-12", 
                'imagenEtiqueta': 'https://example.com/vino4.jpg',
                'notaCata': 'Sabor intenso con notas de chocolate y vainilla',
                'precioArs': 2200,
                'maridajes': ["Malbec y Gouda", "Brut Rosé y Sushi"],
                'varietales': ["Vino tinto de color rojo intenso con aromas a frutos rojos, especias y cuero.", "Vino blanco de color amarillo pajizo con aromas a heno, melocotón y cítricos."],
                'bodega': self.bodegaSeleccionada,
                'nombreBodega': self.bodegaSeleccionada.nombre,
                'tipoUva': ["Cabernet Sauvignon", "Sauvignon Blanc"]
            },
            {
                'nombre': 'Vino5', 
                'añada': 2017, 
                'fechaActualizacion': "2023-11-08", 
                'imagenEtiqueta': 'https://example.com/vino5.jpg',
                'notaCata': 'Textura suave y aterciopelada con toques de mora',
                'precioArs': 2500,
                'maridajes': ["Verdejo y Tapas", "Sauvignon Blanc y Ceviche"],
                'varietales': ["Vino tinto de color violeta intenso con aromas a frutos negros, pimienta negra y violetas.", "Vino blanco de color verde pálido con aromas a grosella espinosa, hierba fresca y pomelo."],
                'bodega': self.bodegaSeleccionada,
                'nombreBodega': self.bodegaSeleccionada.nombre,
                'tipoUva': ["Gewürztraminer", "Chardonnay"]
            }
        ]

        """for vino in vinosActualizados:   
            self.vinosActualizados.append(Vino(vino['añada'], vino['fechaActualizacion'], vino['nombre'], vino['imagenEtiqueta'], vino['notaCata'], vino['precioArs'], vino['varietales'], vino['maridajes'], vino['bodega']))"""


    def determinarVinosParaActualizar(self):
        """Esta función determina todos los vinos que nos devolvió la simulación de la API, que pertenecen a la bodega seleccionada"""
        self.vinosParaActualizar = []
        print('Vinos actualizados: ', self.vinosActualizados)
        print('\nSELECCIONADA BODEGA:', self.bodegaSeleccionada)
        for vino in self.vinosActualizados:
            #HAY QUE FIJARNOS DE CREAR UNA FUNCION QUE PERMITA AÑADIRLE VINOS A LA BODEGA, PORQUE ACA NO TE LOS APPENDEA YA QUE LA BODEGA NO TIENE VINOS
            if self.bodegaSeleccionada.tienesEsteVino(vino):
                self.vinosParaActualizar.append(vino)

        print('Vinos actualizados: ', self.vinosActualizados)


    def actualizarOCrearVinos(self):
        vinosActualizados = []
        vinosCreados = []

        for vino in self.vinosActualizados:
            if vino in self.vinosParaActualizar:
                self.bodegaSeleccionada.actualizarDatosVino(vino['nombre'], vino['fechaActualizacion'], self.fechaActual, vino['precioArs'], vino['notaCata'], vino['imagenEtiqueta'])
                vinosActualizados.append(vino)
            else:
                self.crearVino(vino)
                vinosCreados.append(vino)
        
        # print(f"FORMATO: {obtenerResumenVinos_dict}")
        return vinosActualizados, vinosCreados
    

    def crearVino(self, vino):
        maridajes = self.buscarMaridaje(vino)
        tiposUva = self.buscarTipoUva(vino)
        self.vinosCreados.append(vino)
        # FALTARÍA AGREGAR EL VINO AL ARCHIVO BASE.PY Y HABRÍA QUE LLAMAR AL METODO NEW() DEL VINO
        # print(f"Creando nuevo {vino['nombre']}")


    def buscarMaridaje(self, vino):
        arrayMaridajes = []

        for maridaje in self.maridajes:
            for strMaridajeVino in vino['maridajes']:
                if maridaje.sosMaridaje(strMaridajeVino):
                    arrayMaridajes.append(maridaje)

        return arrayMaridajes
            #if maridaje.sosMaridaje(vino.maridaje):
        """for maridaje in vino.maridaje:
            if Maridaje.sosMaridaje(maridaje):
                maridajes.append(maridaje)
        return maridajes"""

        
    def buscarTipoUva(self, vino):
        arrayTiposUva = []
        #VINO NO TIENE ATRIBUTO TIPOUVA, TENEMOS QUE CAMBIAR LOS VINOS TRAIDOS POR LA API
        for tipoUva in self.tiposUva:
            for strTipoUvaNombre in vino['tipoUva']:
                if tipoUva.sosTipoUva(strTipoUvaNombre):
                    arrayTiposUva.append(tipoUva)

        return arrayTiposUva
            
        """vino.tipoUva:
            if TipoUva.sosTipoUva(tipoUva):
                tiposUva.append(tipoUva)
        return tiposUva"""
    

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