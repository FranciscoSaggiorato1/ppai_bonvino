import os
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton, QMessageBox
from PyQt6 import uic, QtWidgets
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon
from functools import partial
import recursos

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from Controlador.gestorImportarActualizacion import GestorImportadorBodega

class InterfazNotificacionPush(QMainWindow):
    def __init__(self, bodega, fechaActualizacion, vinosActualizados, vinosCreados):
        super().__init__()
        self.gestor = GestorImportadorBodega()
        ui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interfazDiseño.ui')
        uic.loadUi(ui_path, self)
        self.bodega = bodega
        self.fechaActualizacion = fechaActualizacion
        self.vinosActualizados = vinosActualizados
        self.vinosCreados = vinosCreados

    def generarNotificacionNovedades(self, bodega, fechaActualizacion, vinosActualizados, vinosCreados):
        self.set_bodega(bodega)
        self.set_fechaActualizacion(fechaActualizacion)
        self.set_vinosActualizados(vinosActualizados)
        self.set_vinosCreados(vinosCreados)

    def enviarNotificacion(self, bodega, fechaActualizacion, vinosActualizados, vinosCreados):
        self.generarNotificacionNovedades(bodega, fechaActualizacion, vinosActualizados, vinosCreados)
        #self.setWindowTitle("Notificación de actualización de vinos")
        #self.setWindowIcon(QIcon(":/icono.png"))
        #self.setFixedSize(800, 600)
        #self.setCentralWidget(self.crearTabla())
        #self.show()

    def set_bodega(self, bodega):
        self.bodega = bodega

    def set_fechaActualizacion(self, fechaActualizacion):
        self.fechaActualizacion = fechaActualizacion

    def set_vinosActualizados(self, vinosActualizados):
        self.vinosActualizados = vinosActualizados

    def set_vinosCreados(self, vinosCreados):
        self.vinosCreados = vinosCreados