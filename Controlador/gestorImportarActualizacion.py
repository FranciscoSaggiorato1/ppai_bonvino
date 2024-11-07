# Controlador/gestorImportarActualizacion.py

import os
import sys
from datetime import datetime, date

# Añadir el directorio principal del proyecto al sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from Modelo.vino import Vino
#from Modelo.base import bodegas, varietales, tiposUva, vinos, enofilos, siguiendos, usuarios, maridajes
from Modelo.ISujetoNotificacionPush import ISujetoNotificacionPush
from Interfaz.InterfazNotificacionPush import InterfazNotificacionPush
from Persistencia.Entidades.usuarioDB import Usuario as UsuarioDB
from Persistencia.Entidades.bodegaDB import Bodega as BodegaDB
from Persistencia.Entidades.enofiloDB import Enofilo as EnofiloDB
from Persistencia.Entidades.siguiendoDB import Siguiendo as SiguiendoDB
from Persistencia.Entidades.tipoUvaDB import TipoUva as TipoUvaDB
from Persistencia.Entidades.varietalDB import Varietal as VarietalDB
from Persistencia.Entidades.maridajeDB import Maridaje as MaridajeDB
from Persistencia.Entidades.vinoDB import Vino as VinoDB

from Persistencia.ConversoresPersistencia.tipoUva_conversor import TipoUvaConversor
from Persistencia.ConversoresPersistencia.varietal_conversor import VarietalConversor
from Persistencia.ConversoresPersistencia.maridaje_conversor import MaridajeConversor
from Persistencia.ConversoresPersistencia.bodega_conversor import BodegaConversor
from Persistencia.ConversoresPersistencia.vino_conversor import VinoConversor
from Persistencia.ConversoresPersistencia.usuario_conversor import UsuarioConversor
from Persistencia.ConversoresPersistencia.siguiendo_conversor import SiguiendoConversor
from Persistencia.ConversoresPersistencia.enofilo_conversor import EnofiloConversor


from sqlalchemy.orm import sessionmaker
from Persistencia.database_config import engine

# Crea una sesión de base de datos
Session = sessionmaker(bind=engine)
session = Session()


class GestorImportadorBodega(ISujetoNotificacionPush):
    def __init__(self): 
        self.fechaActual = None
        self.bodegasParaActualizar = [] 
        self.bodegaSeleccionada = None
        self.vinosApi = []
        self.vinosCreados = []
        self.vinosActualizados = []
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
        self.observadores = []


    def nuevaImportacionActualizacionVinos(self):
        self.cargarBase()
        self.getFechaActual()
        self.bodegasParaActualizar = self.buscarBodegasConActualizaciones()
        return self.bodegasParaActualizar


    def cargarBase(self):
        # Cargar datos desde la base de datos
        self.bodegas = [BodegaConversor.mapear_bodega(b) for b in session.query(BodegaDB).all()]
        self.enofilos = [EnofiloConversor.mapear_enofilo(e) for e in session.query(EnofiloDB).all()]
        self.maridajes = [MaridajeConversor.mapear_maridaje(m) for m in session.query(MaridajeDB).all()]
        self.siguiendo = [SiguiendoConversor.mapear_siguiendo(s) for s in session.query(SiguiendoDB).all()]
        self.tiposUva = [TipoUvaConversor.mapear_tipo_uva(t) for t in session.query(TipoUvaDB).all()]
        self.usuarios = [UsuarioConversor.mapear_usuario(u) for u in session.query(UsuarioDB).all()]
        self.vinos = [VinoConversor.mapear_vino(v) for v in session.query(VinoDB).all()]
        self.cargarVinosEnBodegas()
        self.cargarSiguiendoEnEnofilo()

    def cargarVinosEnBodegas(self):
        # Itera sobre cada vino en la lista de vinos
        for vino in self.vinos:
            # Encuentra la bodega correspondiente para este vino
            bodega = next((b for b in self.bodegas if b.getNombre() == vino.bodega.getNombre()), None)
            if bodega:
                # Agrega el vino a la bodega
                bodega.agregarVino(vino)
                print(f"Agregado el vino '{vino.nombre}' a la bodega '{bodega.getNombre()}'")
            else:
                print(f"No se encontró la bodega para el vino '{vino.nombre}'")

    def cargarSiguiendoEnEnofilo(self):
        # Itera sobre cada siguiendo en la lista de siguiendo
        for sig in self.siguiendo:
            # Encuentra el enofilo para este siguiendo
            enofilo = next((e for e in self.enofilos if e.nombre == sig.enofilo_seguidor.nombre), None)

            if enofilo:
                # Agrega el vino a la bodega
                enofilo.agregarSiguiendo(sig)
                print(f"Agregado el siguiendo al enofilo '{enofilo.getNombre()}'")
            else:
                print(f"No se encontró el enofilo para el siguiendo")
        



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
        
        # Establece la bodega como la bodega seleccionada y actualiza su fecha ultima actualizacion
        self.bodegaSeleccionada = self.buscarNombreBodega(bodega)
        self.establecerFechaUltimaActualizacion()
        
        # Realiza las operaciones de actualización de vinos para la bodega seleccionada
        self.obtenerActualizacionVinosBodega()
        self.determinarVinosParaActualizar()
        self.actualizarOCrearVinos()
        return self.vinosActualizados, self.vinosCreados

    
    def buscarNombreBodega(self, bodega):
        # Busca la bodega en la lista de bodegas conocidas
        for bodegaConocida in self.bodegas:
            if bodegaConocida.getNombre() == bodega['nombre']:
                return bodegaConocida
        

    def establecerFechaUltimaActualizacion(self):
        self.bodegaSeleccionada.setFechaUltimaActualizacion(self.fechaActual)
        # Se actualiza la bodega seleccionada
        BodegaConversor.actualizar_bodega(self.bodegaSeleccionada)


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
            print(f"Comparando {vino['nombre']} con los vinos de {self.bodegaSeleccionada.nombre}")
            
            # Verificamos que `self.bodegaSeleccionada.vinos` tenga los vinos esperados
            print("Vinos en la bodega seleccionada:")
            for v in self.bodegaSeleccionada.vinos:
                print(f" - {v.nombre}")
            
            # Comprobamos si el vino ya está en la bodega
            if self.bodegaSeleccionada.tienesEsteVino(vino['nombre']):
                print(f"ESTE SE VA A AGREGAR: {vino['nombre']}")
                self.vinosParaActualizar.append(vino)
            else:
                print(f"{vino['nombre']} NO está en los vinos de la bodega.")
        
        print("Lista final de vinos para actualizar:", [v['nombre'] for v in self.vinosParaActualizar])



    def actualizarOCrearVinos(self):

        # Listas para almacenar los vinos actualizados y creados
        self.vinosActualizados = []
        self.vinosCreados = []

        # Itera sobre cada vino en la lista de vinos proporcionada por la API
        for vino in self.vinosApi:
            if vino in self.vinosParaActualizar:
                self.actualizarVino(vino)
                # Añade el vino a la lista de vinos actualizados
                self.vinosActualizados.append(vino)
            else:
                # Si el vino no está en la lista de vinos para actualizar, se crea como un nuevo vino
                self.iniciarCreacionVino(vino)
                # Añade el vino a la lista de vinos creados
                self.vinosCreados.append(vino)
        
        


    def actualizarVino(self, vino):
        # Busca el ID de la bodega en la base de datos cuyo nombre coincida con la bodega seleccionada
        bodega_db = session.query(BodegaDB).filter_by(nombre=self.bodegaSeleccionada.nombre).first()
        
        if bodega_db:
            # Encuentra el vino en la base de datos que coincide con el nombre y el id de la bodega
            vino_db = session.query(VinoDB).filter_by(nombre=vino['nombre'], id_bodega=bodega_db.id_bodega).first()
            
            if vino_db:
                # Actualiza los campos del vino encontrado
                vino_db.nombre = vino["nombre"]
                vino_db.precioArs = vino['precioArs']
                vino_db.notaCata = vino['notaCata']
                vino_db.fechaActualizacion = self.fechaActual
                vino_db.imagenEtiqueta = vino['imagenEtiqueta']
                
                # Guarda los cambios en la base de datos
                session.commit()
                print(f"Vino '{vino['nombre']}' actualizado en la bodega '{self.bodegaSeleccionada.nombre}'.")
            else:
                print(f"No se encontró el vino '{vino['nombre']}' en la bodega '{self.bodegaSeleccionada.nombre}'.")
        else:
            print(f"No se encontró la bodega '{self.bodegaSeleccionada.nombre}' en la base de datos.")
        
        # Cierra la sesión
        session.close()


    def iniciarCreacionVino(self, vino):
        # Busca los maridajes asociados al vino
        maridajes = self.buscarMaridaje(vino)
        # Busca los tipos de uva asociados al vino
        tiposUva = self.buscarTipoUva(vino)

        self.crearVino(vino, maridajes, tiposUva)

    def crearVino(self, vino, maridajes, tiposUva):
        # Inicializamos una lista para los varietales que existen en la BD
        varietales_en_bd = []
        for i in range(len(vino['varietales'])):
            varietal_desc = vino['varietales'][i]
            porcentajeComposicion = vino['porcentaje'][i]
            tipoUva = vino['tipoUva'][i]

            # Busca el varietal en la base de datos
            varietal = session.query(VarietalDB).filter_by(descripcion=varietal_desc).first()
            print("VARIETAL OBJETO:", varietal)
            if not varietal:
                # Crea nuevo varietal si no existe
                tipo_uva_instance = session.query(TipoUvaDB).filter_by(nombre=tipoUva).first()
                print("TIPO UVA INSTANCIA:", tipo_uva_instance)
                if tipo_uva_instance:
                    varietal = VarietalDB(
                        descripcion=varietal_desc,
                        porcentajeComposicion=porcentajeComposicion,
                        tipoUva=tipo_uva_instance
                    )
                    print("VARIETAL CREADO: ", varietal)
                    session.add(varietal)
                    session.commit()
                else:
                    print(f"Tipo de uva '{tipoUva}' no encontrado.")
                    continue  # Salta este varietal si el tipo de uva no existe

            varietales_en_bd.append(varietal)
        
        # Crea un nuevo objeto Vino con los datos proporcionados y las búsquedas realizadas
        nuevoVino = Vino.new(
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
            tiposUvas=tiposUva,
        )
            # Convertir el objeto Vino a la entidad de persistencia y guardarlo en la base de datos
        nuevoVino.varietal = varietales_en_bd
        nuevoVinoDB = VinoConversor.guardar_vino(nuevoVino)

        # Añade el nuevo objeto Vino a la lista de vinos
        self.vinos.append(nuevoVino)
        
        session.merge(nuevoVinoDB)
        session.commit()


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

    def buscarSeguidores(self):
        self.buscarSeguidoresDeBodega()

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
            nomUsuarios = seguidor.nombre
            self.nombresUsuarios.append(nomUsuarios)
        
        self.generarNotificacionNovedades(self.seguidoresDeBodega)

    def generarNotificacionNovedades(self, seguidoresBodega):
        observadores_nuevos = []
        for seguidor in seguidoresBodega:
            observador_nuevo = InterfazNotificacionPush(None, None, None, None)
            observadores_nuevos.append(observador_nuevo)
       
        self.suscribir(observadores_nuevos)
        self.notificar()



    # METODOS IMPLEMENTADOS DE INTERFAZ

    def suscribir(self, observers: list):
        for observer in observers:
            if observer not in self.observadores:
                self.observadores.append(observer)

    def quitar(self, observers: list):
        for observer in observers:
            if observer in self.observadores:
                self.observadores.remove(observer)

    def notificar(self):
        for observer in self.observadores:

            observer.enviarNotificacion(self.bodegaSeleccionada.getNombre(), self.fechaActual, [vino['nombre'] for vino in self.vinosActualizados], [vino['nombre'] for vino in self.vinosCreados])
            print("\n---------------")
            print("Notificado...")
            print("---------------\n")

    def finCU(self):
        """ Termina la ejecución del programa. """
        session.close()
        sys.exit()

