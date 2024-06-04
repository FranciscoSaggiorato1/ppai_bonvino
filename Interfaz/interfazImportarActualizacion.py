# Interfaz/interfazImportarActualizacion.py

import os
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton, QMessageBox
from PyQt6 import uic, QtWidgets
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap
from functools import partial
import recursos
import requests

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from Controlador.gestorImportarActualizacion import GestorImportadorBodega


def get_image_data(url):
    response = requests.get(url)
    return response.content

class PantallaImportadorBodega(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gestor = GestorImportadorBodega()
        ui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interfazDiseño.ui')
        uic.loadUi(ui_path, self)
        self.habilitarPantalla()
        self.pushButton.clicked.connect(self.cambiarPag)
        self.pushButton.clicked.connect(self.seleccionarOpImportarAct)
        self.pushButtonVolver.clicked.connect(self.volverAlInicio)
        self.pushButtonVolverBodega.clicked.connect(self.volverAlInicio)
        self.pushButtonFinalizar.clicked.connect(self.finalizar)


    def habilitarPantalla(self):
        self.setWindowTitle("BonVino - Importar Actualizacion")
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'imagenes', 'utnLogo.ico')
        self.setWindowIcon(QIcon(icon_path))
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowMaximizeButtonHint)
        self.show()
    
    def volverAlInicio(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def finalizar(self):
        self.gestor.finCU()

    def cambiarPag(self):
        self.stackedWidget.setCurrentIndex(1)

    def mostrarMensajeError(self, mensaje):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setWindowTitle("Error")
        msg_box.setText(mensaje)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def mostrarMensajeEnofilo(self, mensaje):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("Notificación")
        msg_box.setText(mensaje)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def seleccionarOpImportarAct(self):
        bodegas = self.gestor.nuevaImportacionActualizacionVinos() #[] Para la ALTERNATIVA
        self.mostrarParaSeleccionarBodegasConActualizaciones(bodegas)
    
    def mostrarParaSeleccionarBodegasConActualizaciones(self, bodegas):
        row_count = len(bodegas)
        if len(bodegas) == 0:
            self.mostrarMensajeError("No se encontraron bodegas con actualizaciones.")
            return
        else:
            column_count = 2  # Número de columnas

            self.tableWidget.setRowCount(row_count)
            self.tableWidget.setColumnCount(column_count)
            self.tableWidget.verticalHeader().hide()
            headers = ["Acción", "Nombre"]
            self.tableWidget.setHorizontalHeaderLabels(headers)

            # Ajustar el tamaño de las columnas al contenido
            self.tableWidget.horizontalHeader().setStretchLastSection(True)
            self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.tableWidget.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
            self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

            for row_index, bodega in enumerate(bodegas):
                button = QtWidgets.QPushButton("Seleccionar")
                button.clicked.connect(partial(self.tomarBodegaSeleccionada, bodega))
                self.tableWidget.setCellWidget(row_index, 0, button)
                self.tableWidget.setItem(row_index, 1, QTableWidgetItem(bodega['nombre']))


    def tomarBodegaSeleccionada(self, bodega):
        # print('La bodega desde interfaz es:', bodega)
        self.gestor.tomarBodegaSeleccionada(bodega)
        # Cambiar a la pagina donde se mostraran los vinos
        self.stackedWidget.setCurrentIndex(2)
        self.cargarVinosActualizados()

    def cargarVinosActualizados(self):
        # Obtener datos de vinos actualizados desde el gestor o alguna fuente de datos
        vinos_actualizados, vinos_creados = self.gestor.actualizarOCrearVinos() #None para LA ALTERNATIVA
        self.mostrarResumenActualizacionVinos(vinos_actualizados, vinos_creados)
    
    def mostrarResumenActualizacionVinos(self, vinos_actualizados, vinos_creados):
        if vinos_actualizados is None:
            self.mostrarMensajeError("ERROR 503: El servidor no está disponible en este momento")
            return
        else:
            self.mostrarMensajeEnofilo("Se generaron las notificaciones a los enofilos seguidores de la bodega seleccionada.")

            if len(vinos_actualizados) != 0:
                row_count = len(vinos_actualizados)
                column_count = 8  # Número de columnas

                self.tableVinoActualizados.setRowCount(row_count)
                self.tableVinoActualizados.setColumnCount(column_count)
                self.tableVinoActualizados.verticalHeader().hide()
                headers = ["Bodega", "Nombre", "Varietal", "Tipo Uva", "Maridaje", "Fecha Actualización", "Añada", "Precio"]
                self.tableVinoActualizados.setHorizontalHeaderLabels(headers)

                # Ajustar el tamaño de las columnas al contenido
                self.tableVinoActualizados.horizontalHeader().setStretchLastSection(True)
                self.tableVinoActualizados.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
                self.tableVinoActualizados.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
                self.tableVinoActualizados.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
                self.tableVinoActualizados.setIconSize(QSize(50, 50))
                #self.tableWidget.setMinimumSize(400, 300)  # Ajustar el tamaño mínimo según sea necesario

                for row_index, vino in enumerate(vinos_actualizados):
                    self.tableVinoActualizados.setItem(row_index, 0, QTableWidgetItem(vino['nombreBodega']))
                    self.tableVinoActualizados.setItem(row_index, 1, QTableWidgetItem(vino['nombre']))

                    # Convertir lista a cadena si es necesario
                    varietales = ", ".join(vino['varietales']) if isinstance(vino['varietales'], list) else vino['varietales']
                    self.tableVinoActualizados.setItem(row_index, 2, QTableWidgetItem(varietales))

                    tipo_uva = vino['tipoUva'] if isinstance(vino['tipoUva'], str) else ", ".join(vino['tipoUva'])
                    self.tableVinoActualizados.setItem(row_index, 3, QTableWidgetItem(tipo_uva))

                    maridajes = ", ".join(vino['maridajes']) if isinstance(vino['maridajes'], list) else vino['maridajes']
                    self.tableVinoActualizados.setItem(row_index, 4, QTableWidgetItem(maridajes))

                    self.tableVinoActualizados.setItem(row_index, 5, QTableWidgetItem(vino['fechaActualizacion']))
                    self.tableVinoActualizados.setItem(row_index, 6, QTableWidgetItem(str(vino['añada'])))
                    self.tableVinoActualizados.setItem(row_index, 7, QTableWidgetItem(str(vino['precioArs'])))
            else:
                self.tableVinoActualizados.setRowCount(0)
                self.tableVinoActualizados.setColumnCount(1)
                self.tableVinoActualizados.verticalHeader().hide()
                headers = ["No existen vinos actualizados para mostrar"]
                self.tableVinoActualizados.setHorizontalHeaderLabels(headers)

                # Ajustar el tamaño de las columnas al contenido
                self.tableVinoActualizados.horizontalHeader().setStretchLastSection(True)
                self.tableVinoActualizados.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
                self.tableVinoActualizados.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
                self.tableVinoActualizados.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
                self.tableVinoActualizados.setIconSize(QSize(50, 50))

            if len(vinos_creados) != 0:
                row_count = len(vinos_creados)
                column_count = 8  # Número de columnas

                self.tableVinoCreados.setRowCount(row_count)
                self.tableVinoCreados.setColumnCount(column_count)
                self.tableVinoCreados.verticalHeader().hide()
                headers = ["Bodega", "Nombre", "Varietal", "Tipo Uva", "Maridaje", "Fecha Creacion", "Añada", "Precio"]
                self.tableVinoCreados.setHorizontalHeaderLabels(headers)

                # Ajustar el tamaño de las columnas al contenido
                self.tableVinoCreados.horizontalHeader().setStretchLastSection(True)
                self.tableVinoCreados.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
                self.tableVinoCreados.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
                self.tableVinoCreados.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
                self.tableVinoCreados.setIconSize(QSize(50, 50))
                #self.tableWidget.setMinimumSize(400, 300)  # Ajustar el tamaño mínimo según sea necesario

                for row_index, vino in enumerate(vinos_creados):
                    self.tableVinoCreados.setItem(row_index, 0, QTableWidgetItem(vino['nombreBodega']))
                    self.tableVinoCreados.setItem(row_index, 1, QTableWidgetItem(vino['nombre']))

                    # Convertir lista a cadena si es necesario
                    varietales = ", ".join(vino['varietales']) if isinstance(vino['varietales'], list) else vino['varietales']
                    self.tableVinoCreados.setItem(row_index, 2, QTableWidgetItem(varietales))

                    tipo_uva = vino['tipoUva'] if isinstance(vino['tipoUva'], str) else ", ".join(vino['tipoUva'])
                    self.tableVinoCreados.setItem(row_index, 3, QTableWidgetItem(tipo_uva))

                    maridajes = ", ".join(vino['maridajes']) if isinstance(vino['maridajes'], list) else vino['maridajes']
                    self.tableVinoCreados.setItem(row_index, 4, QTableWidgetItem(maridajes))

                    self.tableVinoCreados.setItem(row_index, 5, QTableWidgetItem(vino['fechaActualizacion']))
                    self.tableVinoCreados.setItem(row_index, 6, QTableWidgetItem(str(vino['añada'])))
                    self.tableVinoCreados.setItem(row_index, 7, QTableWidgetItem(str(vino['precioArs'])))
            else:
                self.tableVinoCreados.setRowCount(0)
                self.tableVinoCreados.setColumnCount(1)
                self.tableVinoCreados.verticalHeader().hide()
                headers = ["No existen vinos creados para mostrar"]
                self.tableVinoCreados.setHorizontalHeaderLabels(headers)

                # Ajustar el tamaño de las columnas al contenido
                self.tableVinoCreados.horizontalHeader().setStretchLastSection(True)
                self.tableVinoCreados.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
                self.tableVinoCreados.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
                self.tableVinoCreados.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
                self.tableVinoCreados.setIconSize(QSize(50, 50))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    interfazImportarActualizaciones =PantallaImportadorBodega()
    sys.exit(app.exec())