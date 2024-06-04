# Controlador/gestorImportarActualizacion.py

import os
import sys
from datetime import datetime 

# Añadir el directorio principal del proyecto al sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from Modelo.vino import Vino
from Modelo.base import bodegas, varietales, tiposUva, vinos, enofilos, siguiendos, usuarios, maridajes

    
class GestorImportadorBodega:
    def __init__(self): 
        self.fechaActual = None
        self.bodegasParaActualizar = [] 
        self.bodegaSeleccionada = None
        self.vinosApi = []
        self.vinosCreados = []
        self.seguidoresDeBodega = []
        self.vinosParaActualizar = []
        self.vinos = []
        self.bodegas= []
        self.varietales = []
        self.maridajes = []
        self.tiposUva = []
        self.enofilos = []
        self.siguiendo = []     
        self.nombresUsuarios = []  


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
        self.cargarVinosEnBodegas()


    def cargarVinosEnBodegas(self):
        # Itera sobre cada vino en la lista de vinos
        for vino in self.vinos:
            # Asocia el vino a su bodega correspondiente
            vino.bodega.agregarVino(vino)


    def getFechaActual(self):
        # Obtiene la fecha actual
        self.fechaActual = datetime.now().date()
        # Retorna la fecha actual
        return self.fechaActual


    def buscarBodegasConActualizaciones(self):
        # Inicializa la lista de bodegas para actualizar
        self.bodegasParaActualizar = []

        # Itera sobre cada bodega en la lista de bodegas
        for bodega in self.bodegas:
            # Verifica si la bodega tiene actualizaciones disponibles para la fecha actual
            if bodega.tieneActualizacionDisponible(self.fechaActual):
                # Añade la bodega a la lista de bodegas para actualizar
                self.bodegasParaActualizar.append(bodega)

        # Convierte las bodegas a diccionarios
        bodegasDict = [bodega.toDict() for bodega in self.bodegasParaActualizar]
        
        # Retorna la lista de diccionarios de bodegas con actualizaciones
        return bodegasDict


    def tomarBodegaSeleccionada(self, bodega):
        # Busca la bodega en la lista de bodegas conocidas
        for bodegaConocida in self.bodegas:
            if bodegaConocida.getNombre() == bodega['nombre']:
                # Establece la bodega como la bodega seleccionada
                self.bodegaSeleccionada = bodegaConocida
        
        # Realiza las operaciones de actualización de vinos para la bodega seleccionada
        self.obtenerActualizacionVinosBodega()
        self.determinarVinosParaActualizar()
        self.actualizarOCrearVinos()
        self.buscarSeguidoresDeBodega()
        

    def obtenerActualizacionVinosBodega(self):
        """ Simulación de obtención de actualizaciones de vinos para la bodega seleccionada por parte de una API. """
        self.vinosApi = [
            {
                'nombre': 'Trumpeter', 
                'añada': 2018,
                'fechaActualizacion': "2024-01-15", 
                'imagenEtiqueta': 'https://i.colnect.net/f/3919/903/Trumpeter---Sauvignon-Blanc.jpg',
                'notaCata': 'Notas de ciruela y roble',
                'precioArs': 1500,
                'maridajes': ["Malbec y Gouda", "Chardonnay y Salmón", "Cabernet Sauvignon y Cordero"],
                'varietales': ["Vino tinto de color rojo rubí con aromas a cereza, vainilla y cuero."],
                'porcentaje': ["90%"],
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
                'porcentaje': ["50%", "50%"],
                'bodega': self.bodegaSeleccionada,
                'nombreBodega': self.bodegaSeleccionada.nombre,
                'tipoUva': ["Syrah", "Sauvignon Blanc"]
            },
            {
                'nombre': 'Vino Toro', 
                'añada': 2020, 
                'fechaActualizacion': "2024-02-10", 
                'imagenEtiqueta': 'https://example.com/vino3.jpg',
                'notaCata': 'Aromas de frutas rojas y especias',
                'precioArs': 1800,
                'maridajes': ["Chardonnay y Salmón", "Cabernet Sauvignon y Cordero"],
                'varietales': ["Vino tinto de color púrpura oscuro con aromas a cedro, tomillo y tabaco.", "Vino tinto de color rojo rubí con aromas a frutilla, maracuya y lienzo."],
                'porcentaje': ["70%", "30%"],
                'bodega': self.bodegaSeleccionada,
                'nombreBodega': self.bodegaSeleccionada.nombre,
                'tipoUva': ["Malbec", "Pinot Grigio"]
            },
            {
                'nombre': 'Tronador', 
                'añada': 2021, 
                'fechaActualizacion': "2024-03-12", 
                'imagenEtiqueta': 'https://example.com/vino4.jpg',
                'notaCata': 'Sabor intenso con notas de chocolate y vainilla',
                'precioArs': 2200,
                'maridajes': ["Malbec y Gouda", "Brut Rosé y Sushi"],
                'varietales': ["Vino tinto de color rojo intenso con aromas a frutos rojos, nuez y menta.", "Vino blanco de color naranja pajizo con aromas a hiervas secas, melón y limón."],
                'porcentaje': ["60%", "40%"],
                'bodega': self.bodegaSeleccionada,
                'nombreBodega': self.bodegaSeleccionada.nombre,
                'tipoUva': ["Cabernet Sauvignon", "Sauvignon Blanc"]
            },
            {
                'nombre': 'Amelia', 
                'añada': 2017, 
                'fechaActualizacion': "2023-11-08", 
                'imagenEtiqueta': 'https://example.com/vino5.jpg',
                'notaCata': 'Textura suave y aterciopelada con toques de mora',
                'precioArs': 2500,
                'maridajes': ["Verdejo y Tapas", "Sauvignon Blanc y Ceviche"],
                'varietales': ["Vino tinto de color violeta intenso con aromas amaderados y citricos.", "Vino blanco de color verde pálido con aromas a eucalipto, menta fresca y cereza."],
                'porcentaje': ["80%", "70%"],
                'bodega': self.bodegaSeleccionada,
                'nombreBodega': self.bodegaSeleccionada.nombre,
                'tipoUva': ["Gewürztraminer", "Chardonnay"]
            }
        ]


    def determinarVinosParaActualizar(self):

        # Lista para almacenar los vinos para actualizar
        self.vinosParaActualizar = []

        # Iteramos todos los vinos obtenidos desde la API
        for vino in self.vinosApi:
            if self.bodegaSeleccionada.tienesEsteVino(vino['nombre']):
                self.vinosParaActualizar.append(vino)


    def actualizarOCrearVinos(self):

        # Listas para almacenar los vinos actualizados y creados
        vinosActualizados = []
        vinosCreados = []

        # Itera sobre cada vino en la lista de vinos proporcionada por la API
        for vino in self.vinosApi:
            if vino in self.vinosParaActualizar:
                # Si el vino está en la lista de vinos para actualizar, se actualizan sus datos
                self.bodegaSeleccionada.actualizarDatosVino(
                    vino['nombre'], 
                    self.fechaActual, 
                    vino['precioArs'], 
                    vino['notaCata'], 
                    vino['imagenEtiqueta']
                )
                # Añade el vino a la lista de vinos actualizados
                vinosActualizados.append(vino)
            else:
                # Si el vino no está en la lista de vinos para actualizar, se crea como un nuevo vino
                self.crearVino(vino)
                # Añade el vino a la lista de vinos creados
                vinosCreados.append(vino)
        
        # Retorna las listas de vinos actualizados y creados
        return vinosActualizados, vinosCreados
    

    def crearVino(self, vino):
        # Busca los maridajes asociados al vino
        maridajes = self.buscarMaridaje(vino)
        # Busca los tipos de uva asociados al vino
        tiposUva = self.buscarTipoUva(vino)
        
        # Añade el diccionario del vino a la lista de vinos creados
        self.vinosCreados.append(vino)
        
        # Crea un nuevo objeto Vino con los datos proporcionados y las búsquedas realizadas
        nuevo_vino = Vino.new(
            nombre=vino['nombre'],
            añada=vino['añada'],
            fechaActualizacion=self.fechaActual,
            precioArs=vino['precioArs'],
            notaCata=vino['notaCata'],
            bodega=self.bodegaSeleccionada,
            imagenEtiqueta=vino['imagenEtiqueta'],
            maridaje=maridajes,
            descripcion=vino['varietales'],
            porcentajeComposicion=vino['porcentaje'],
            tiposUvas=tiposUva
        )
        
        # Añade el nuevo objeto Vino a la lista de vinos
        self.vinos.append(nuevo_vino)


    def buscarMaridaje(self, vino):
        arrayMaridajes = []

        # Itera sobre cada maridaje en la lista de maridajes
        for maridaje in self.maridajes:
            # Itera sobre cada maridaje en la lista de maridajes del vino
            for strMaridajeVino in vino['maridajes']:
                # Verifica si el maridaje es adecuado para el vino
                if maridaje.sosMaridaje(strMaridajeVino):
                    arrayMaridajes.append(maridaje)

        # Retorna la lista de maridajes adecuados para el vino
        return arrayMaridajes


    def buscarTipoUva(self, vino):
        arrayTiposUva = []

        # Itera sobre cada tipo de uva en la lista de tipos de uva
        for tipoUva in self.tiposUva:
            # Itera sobre cada tipo de uva en la lista de tipos de uva del vino
            for strTipoUvaNombre in vino['tipoUva']:
                # Verifica si el tipo de uva es adecuado para el vino
                if tipoUva.sosTipoUva(strTipoUvaNombre):
                    arrayTiposUva.append(tipoUva)

        # Retorna la lista de tipos de uva adecuados para el vino
        return arrayTiposUva


    def buscarSeguidoresDeBodega(self):
        # Inicializa la lista de nombres de usuarios
        self.nombresUsuarios = []

        # Itera sobre cada enófilo en la lista de enófilos
        for enofilo in self.enofilos:
            # Verifica si el enófilo sigue la bodega seleccionada
            if enofilo.seguisBodega(self.bodegaSeleccionada):
                self.seguidoresDeBodega.append(enofilo)

        # Itera sobre cada seguidor de la bodega
        for seguidor in self.seguidoresDeBodega:
            # Obtiene y almacena el nombre de usuario del seguidor
            nomUsuarios = seguidor.obtenerNombreUsuario()
            self.nombresUsuarios.append(nomUsuarios)


    def generarNotificacionNovedades():
        # Genera la notificación con los datos obtenidos
        pass

    def finCU(self):
        """ Termina la ejecución del programa. """
        sys.exit()