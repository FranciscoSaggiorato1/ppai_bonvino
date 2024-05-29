import os
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton, QMessageBox
from PyQt6 import uic, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from functools import partial
import recursos


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from Controlador.gestorImportarActualizacion import GestorImportadorBodega

class InterfazImportarActualizaciones(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gestor = GestorImportadorBodega()
        ui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interfazDiseño.ui')
        uic.loadUi(ui_path, self)
        self.habilitarPantalla()
        self.pushButton.clicked.connect(self.cambiarPag)
        self.pushButton.clicked.connect(self.seleccionarOpImportarActVinos)
        self.pushButtonVolver.clicked.connect(self.volverAlInicio)
        self.pushButtonVolverBodega.clicked.connect(self.volverAlInicio)

    def habilitarPantalla(self):
        self.setWindowTitle("BonVino - Importar Actualizacion")
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'imagenes', 'utnLogo.ico')
        self.setWindowIcon(QIcon(icon_path))
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowMaximizeButtonHint)
        self.show()
    
    def volverAlInicio(self):
        self.stackedWidget.setCurrentIndex(0)

    def cambiarPag(self):
        self.stackedWidget.setCurrentIndex(1)

    def mostrar_mensaje_error(self, mensaje):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setWindowTitle("Error")
        msg_box.setText(mensaje)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def seleccionarOpImportarActVinos(self):
        bodegas = self.gestor.buscarBodegasConActualizaciones() #[] Para la ALTERNATIVA
        self.mostrarParaSeleccionarBodegasConActualizaciones(bodegas)
    
    def mostrarParaSeleccionarBodegasConActualizaciones(self, bodegas):
        row_count = len(bodegas)
        if len(bodegas) == 0:
            self.mostrar_mensaje_error("No se encontraron bodegas con actualizaciones.")
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
        print('La bodega desde interfaz es:', bodega)
        self.gestor.tomarBodegaSeleccionada(bodega)
        # Cambiar a la pagina donde se mostraran los vinos
        self.stackedWidget.setCurrentIndex(2)
        #self.cargarVinosActualizados()

    def cargarVinosActualizados(self):
        # Obtener datos de vinos actualizados desde el gestor o alguna fuente de datos
        vinos_actualizados = self.gestor.obtenerVinosActualizados() #None para LA ALTERNATIVA
        self.mostrarResumenVinosActualizados(vinos_actualizados)
    
    def mostrarResumenVinosActualizados(self, vinos_actualizados):
        if vinos_actualizados is None:
            self.mostrar_mensaje_error("ERROR 503: El servidor no está disponible en este momento, devoró.")
            return
        else:
            row_count = len(vinos_actualizados)
            column_count = 8  # Número de columnas

            self.tableWidgetVinos.setRowCount(row_count)
            self.tableWidgetVinos.setColumnCount(column_count)
            self.tableWidgetVinos.verticalHeader().hide()
            headers = ["Etiqueta", "Nombre", "Varietal", "Tipo Uva", "Maridaje", "Fecha Actualización", "Añada", "Precio"]
            self.tableWidgetVinos.setHorizontalHeaderLabels(headers)

            # Ajustar el tamaño de las columnas al contenido
            self.tableWidgetVinos.horizontalHeader().setStretchLastSection(True)
            self.tableWidgetVinos.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.tableWidgetVinos.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
            self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
            #self.tableWidgetVinos.setMinimumSize(400, 300)  # Ajustar el tamaño mínimo según sea necesario

            for row_index, vino in enumerate(vinos_actualizados):
                for col_index, value in enumerate(vino.values()):
                    self.tableWidgetVinos.setItem(row_index, col_index, QTableWidgetItem(str(value)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    interfazImportarActualizaciones = InterfazImportarActualizaciones()
    sys.exit(app.exec())