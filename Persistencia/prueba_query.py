'''
from Entidades.vino import Vino
from database_config import session
res = session.query(Vino).all()
# print(res)
for r in res:
    print(r)
# init_db.py

from sqlalchemy import create_engine
from database_config import Base
# Importa todas las entidades aquí
from Entidades.usuarioDB import Usuario
from Entidades.bodegaDB import Bodega
from Entidades.enofiloDB import Enofilo
from Entidades.siguiendoDB import Siguiendo
from Entidades.tipoUvaDB import TipoUva
from Entidades.varietalDB import Varietal
from Entidades.maridajeDB import Maridaje
from Entidades.vinoDB import Vino
# Crea el motor (reemplaza con la URI de tu base de datos)
engine = create_engine('sqlite:///ppai.db')
# Crea todas las tablas
Base.metadata.create_all(engine)
print("Tablas creadas correctamente.")
'''

'''
import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Modelo.base import *  
from ConversoresPersistencia.tipoUva_conversor import TipoUvaConversor
from ConversoresPersistencia.varietal_conversor import VarietalConversor
from ConversoresPersistencia.maridaje_conversor import MaridajeConversor
from ConversoresPersistencia.bodega_conversor import BodegaConversor
from ConversoresPersistencia.vino_conversor import VinoConversor
from ConversoresPersistencia.usuario_conversor import UsuarioConversor
from ConversoresPersistencia.siguiendo_conversor import SiguiendoConversor
from ConversoresPersistencia.enofilo_conversor import EnofiloConversor

engine = create_engine('sqlite:///ppai.db')
Session = sessionmaker(bind=engine)
session = Session()

# Agregar los tipos de uva
TipoUvaConversor.guardar_tipo_uva(tipo1)
TipoUvaConversor.guardar_tipo_uva(tipo2)
TipoUvaConversor.guardar_tipo_uva(tipo3)
TipoUvaConversor.guardar_tipo_uva(tipo4)
TipoUvaConversor.guardar_tipo_uva(tipo5)
TipoUvaConversor.guardar_tipo_uva(tipo6)
TipoUvaConversor.guardar_tipo_uva(tipo7)
TipoUvaConversor.guardar_tipo_uva(tipo8)
TipoUvaConversor.guardar_tipo_uva(tipo9)
TipoUvaConversor.guardar_tipo_uva(tipo10)


# Agregar los varietales
VarietalConversor.guardar_varietal(var1)
VarietalConversor.guardar_varietal(var2)
VarietalConversor.guardar_varietal(var3)
VarietalConversor.guardar_varietal(var4)
VarietalConversor.guardar_varietal(var5)
VarietalConversor.guardar_varietal(var6)
VarietalConversor.guardar_varietal(var7)
VarietalConversor.guardar_varietal(var8)
VarietalConversor.guardar_varietal(var9)
VarietalConversor.guardar_varietal(var10)

# Agregar los maridajes
MaridajeConversor.guardar_maridaje(m1)
MaridajeConversor.guardar_maridaje(m2)
MaridajeConversor.guardar_maridaje(m3)
MaridajeConversor.guardar_maridaje(m4)
MaridajeConversor.guardar_maridaje(m5)
MaridajeConversor.guardar_maridaje(m6)
MaridajeConversor.guardar_maridaje(m7)
MaridajeConversor.guardar_maridaje(m8)
MaridajeConversor.guardar_maridaje(m9)
MaridajeConversor.guardar_maridaje(m10)

# Agregar las bodegas
BodegaConversor.guardar_bodega(bod1)
BodegaConversor.guardar_bodega(bod2)
BodegaConversor.guardar_bodega(bod3)
BodegaConversor.guardar_bodega(bod4)
BodegaConversor.guardar_bodega(bod5)
BodegaConversor.guardar_bodega(bod6)
BodegaConversor.guardar_bodega(bod7)
BodegaConversor.guardar_bodega(bod8)
BodegaConversor.guardar_bodega(bod9)
BodegaConversor.guardar_bodega(bod10)
BodegaConversor.guardar_bodega(bod11)
BodegaConversor.guardar_bodega(bod12)
BodegaConversor.guardar_bodega(bod13)
BodegaConversor.guardar_bodega(bod14)
BodegaConversor.guardar_bodega(bod15)
BodegaConversor.guardar_bodega(bod16)
BodegaConversor.guardar_bodega(bod17)
BodegaConversor.guardar_bodega(bod18)
BodegaConversor.guardar_bodega(bod19)
BodegaConversor.guardar_bodega(bod20)

# Agregar los vinos
VinoConversor.guardar_vino(v1)
VinoConversor.guardar_vino(v2)
VinoConversor.guardar_vino(v3)
VinoConversor.guardar_vino(v4)
VinoConversor.guardar_vino(v5)
VinoConversor.guardar_vino(v6)
VinoConversor.guardar_vino(v7)
VinoConversor.guardar_vino(v8)
VinoConversor.guardar_vino(v9)
VinoConversor.guardar_vino(v10)
VinoConversor.guardar_vino(v11)
VinoConversor.guardar_vino(v12)
VinoConversor.guardar_vino(v13)
VinoConversor.guardar_vino(v14)
VinoConversor.guardar_vino(v15)
VinoConversor.guardar_vino(v16)
VinoConversor.guardar_vino(v17)
VinoConversor.guardar_vino(v18)
VinoConversor.guardar_vino(v19)
VinoConversor.guardar_vino(v20)
VinoConversor.guardar_vino(v21)
VinoConversor.guardar_vino(v22)
VinoConversor.guardar_vino(v23)
VinoConversor.guardar_vino(v24)
VinoConversor.guardar_vino(v25)
VinoConversor.guardar_vino(v26)
VinoConversor.guardar_vino(v27)
VinoConversor.guardar_vino(v28)
VinoConversor.guardar_vino(v29)
VinoConversor.guardar_vino(v30)
VinoConversor.guardar_vino(v31)
VinoConversor.guardar_vino(v32)
VinoConversor.guardar_vino(v33)
VinoConversor.guardar_vino(v34)
VinoConversor.guardar_vino(v35)
VinoConversor.guardar_vino(v36)
VinoConversor.guardar_vino(v37)
VinoConversor.guardar_vino(v38)
# Agregar los usuarios
UsuarioConversor.guardar_usuario(u1)
UsuarioConversor.guardar_usuario(u2)
UsuarioConversor.guardar_usuario(u3)
UsuarioConversor.guardar_usuario(u4)
UsuarioConversor.guardar_usuario(u5)
UsuarioConversor.guardar_usuario(u6)
UsuarioConversor.guardar_usuario(u7)
UsuarioConversor.guardar_usuario(u8)
UsuarioConversor.guardar_usuario(u9)
UsuarioConversor.guardar_usuario(u10)
VarietalConversor.guardar_varietal(var12)
'''
'''
# Agregar los enofillos
EnofiloConversor.guardar_enofilo(e3)
EnofiloConversor.guardar_enofilo(e1)
EnofiloConversor.guardar_enofilo(e4)
EnofiloConversor.guardar_enofilo(e2)
EnofiloConversor.guardar_enofilo(e9)
EnofiloConversor.guardar_enofilo(e10)
EnofiloConversor.guardar_enofilo(e5)
EnofiloConversor.guardar_enofilo(e8)
EnofiloConversor.guardar_enofilo(e6)
EnofiloConversor.guardar_enofilo(e7)


# Agregar los siguiendo
SiguiendoConversor.guardar_siguiendo(s6)
SiguiendoConversor.guardar_siguiendo(s1)
SiguiendoConversor.guardar_siguiendo(s2)
SiguiendoConversor.guardar_siguiendo(s3)
SiguiendoConversor.guardar_siguiendo(s17)
SiguiendoConversor.guardar_siguiendo(s7)
SiguiendoConversor.guardar_siguiendo(s5)
SiguiendoConversor.guardar_siguiendo(s18)
SiguiendoConversor.guardar_siguiendo(s19)
SiguiendoConversor.guardar_siguiendo(s20)
SiguiendoConversor.guardar_siguiendo(s8)
SiguiendoConversor.guardar_siguiendo(s9)
SiguiendoConversor.guardar_siguiendo(s15)
SiguiendoConversor.guardar_siguiendo(s16)
SiguiendoConversor.guardar_siguiendo(s4)
SiguiendoConversor.guardar_siguiendo(s11)
SiguiendoConversor.guardar_siguiendo(s12)
SiguiendoConversor.guardar_siguiendo(s13)
SiguiendoConversor.guardar_siguiendo(s10)
SiguiendoConversor.guardar_siguiendo(s14)


# Cerrar la sesión
session.close()
'''