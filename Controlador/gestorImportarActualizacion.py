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
        self.vinosApi = []
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
        """
        Asocia cada vino a su respectiva bodega.

        Este método recorre la lista de vinos (`self.vinos`) y, para cada vino, llama al método
        `agregar_vino` de la bodega correspondiente, asociando así el vino a su bodega.

        """
        # Itera sobre cada vino en la lista de vinos
        for vino in self.vinos:
            # Asocia el vino a su bodega correspondiente
            vino.bodega.agregar_vino(vino)


    def getFechaActual(self):
        """
        Obtiene la fecha actual y la guarda en el atributo `fechaActual`.

        Este método utiliza la clase `datetime` para obtener la fecha actual y la guarda en el
        atributo `self.fechaActual`. Luego, retorna esta fecha.

        Returns:
            date: La fecha actual.
        """
        # Obtiene la fecha actual
        self.fechaActual = datetime.now().date()
        # Retorna la fecha actual
        return self.fechaActual


    def buscarBodegasConActualizaciones(self):
        """
        Busca las bodegas que tienen actualizaciones disponibles en la fecha actual.

        Este método recorre la lista de bodegas (`self.bodegas`) y verifica si cada bodega
        tiene actualizaciones disponibles para la fecha actual (`self.fechaActual`). Si una
        bodega tiene actualizaciones, se añade a la lista `self.bodegasParaActualizar`.
        Finalmente, retorna una lista de diccionarios con las bodegas que tienen actualizaciones.

        Returns:
            list: Una lista de diccionarios con las bodegas que tienen actualizaciones disponibles.
        """
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
        """
        Selecciona una bodega y actualiza sus vinos.

        Este método toma un diccionario con la información de una bodega, la busca en la lista
        de bodegas conocidas (`self.bodegas`), y si la encuentra, la establece como la bodega
        seleccionada (`self.bodegaSeleccionada`). Luego, realiza varias operaciones de actualización
        de vinos para esta bodega.

        Args:
            bodega (dict): Un diccionario que contiene los datos de la bodega a seleccionar. Debe tener
                        la clave 'nombre'.
        """
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
                'nombre': 'Vino3', 
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
                'nombre': 'Vino4', 
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
                'nombre': 'Vino5', 
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
        """Esta función determina todos los vinos que nos devolvió la simulación de la API, que pertenecen a la bodega seleccionada"""
        self.vinosParaActualizar = []
        for vino in self.vinosApi:
            if self.bodegaSeleccionada.tienesEsteVino(vino['nombre']):
                self.vinosParaActualizar.append(vino)


    def actualizarOCrearVinos(self):
        """
            Actualiza los datos de los vinos existentes o crea nuevos vinos según los datos proporcionados.

            Este método recorre la lista de vinos proporcionada por la API (`self.vinosApi`) y, para cada vino,
            verifica si debe ser actualizado (si está en `self.vinosParaActualizar`) o si debe ser creado
            como un nuevo vino. Los vinos actualizados y creados se almacenan en listas separadas, las cuales
            se retornan al final del método.

            Returns:
                tuple: Dos listas, la primera contiene los vinos actualizados y la segunda los vinos creados.
        """

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
        """
            Crea un nuevo objeto Vino y lo añade a la lista de vinos.

            Este método toma un diccionario con los datos de un vino, busca los maridajes y tipos de uva
            asociados, y luego crea un nuevo objeto `Vino` con esos datos. El nuevo vino se añade a las listas
            `self.vinosCreados` y `self.vinos`.

            Args:
                vino (dict): Un diccionario que contiene los datos del vino. Debe tener las siguientes claves:
                    - 'nombre': str, nombre del vino
                    - 'añada': str, año de producción del vino
                    - 'precioArs': float, precio en ARS del vino
                    - 'notaCata': str, nota de cata del vino
                    - 'imagenEtiqueta': str, URL o ruta de la imagen de la etiqueta del vino
                    - 'varietales': str, descripción de los varietales del vino
                    - 'porcentaje': float, porcentaje de composición del vino
        """
        
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
        """
        Busca y retorna los maridajes adecuados para un vino.

        Este método recorre la lista de maridajes (`self.maridajes`) y verifica si cada maridaje es adecuado
        para el vino proporcionado (`vino`). Si un maridaje es adecuado, se añade a la lista de maridajes del vino.

        Args:
            vino (dict): Un diccionario que contiene los datos del vino. Debe tener una clave 'maridajes' con
                        una lista de maridajes en formato de cadena de texto.

        Returns:
            list: Una lista de objetos maridaje que son adecuados para el vino proporcionado.
        """
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
        """
        Busca y retorna los tipos de uva adecuados para un vino.

        Este método recorre la lista de tipos de uva (`self.tiposUva`) y verifica si cada tipo de uva es adecuado
        para el vino proporcionado (`vino`). Si un tipo de uva es adecuado, se añade a la lista de tipos de uva del vino.

        Args:
            vino (dict): Un diccionario que contiene los datos del vino. Debe tener una clave 'tipoUva' con
                        una lista de tipos de uva en formato de cadena de texto.

        Returns:
            list: Una lista de objetos tipo de uva que son adecuados para el vino proporcionado.
        """
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
        """
        Busca y almacena los seguidores de la bodega seleccionada.

        Este método recorre la lista de enófilos (`self.enofilos`) y verifica si cada enófilo sigue la bodega
        seleccionada (`self.bodegaSeleccionada`). Si un enófilo sigue la bodega, se añade a la lista de
        seguidores de la bodega (`self.seguidoresDeBodega`). Luego, almacena los nombres de usuario de
        estos seguidores en `self.nombresUsuarios`.

        """
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


    def finCU(self):
        """
        Termina la ejecución del programa.

        Este método finaliza la ejecución del programa llamando a `sys.exit()`.
        """
        sys.exit()