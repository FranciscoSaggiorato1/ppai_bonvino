import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Modelo.base import *  # Ajusta la importación según la estructura de tu proyecto
from datetime import date
from ConversoresPersistencia.tipoUva_conversor import TipoUvaConversor
from ConversoresPersistencia.varietal_conversor import VarietalConversor
from ConversoresPersistencia.maridaje_conversor import MaridajeConversor
from ConversoresPersistencia.bodega_conversor import BodegaConversor
from ConversoresPersistencia.vino_conversor import VinoConversor
from ConversoresPersistencia.usuario_conversor import UsuarioConversor
from ConversoresPersistencia.siguiendo_conversor import SiguiendoConversor
from ConversoresPersistencia.enofilo_conversor import EnofiloConversor


# Crear el motor de la base de datos
engine = create_engine('sqlite:///ppai.db')  # Ajusta la ruta a tu base de datos


# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

VarietalConversor.guardar_varietal(var12)


# Cerrar la sesión
session.close()

