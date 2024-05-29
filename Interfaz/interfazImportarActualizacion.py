import os
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton
from PyQt6 import uic, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from functools import partial
import recursos

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from Controlador.gestorImportarActualizacion import GestorImportadorBodega

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gestor = GestorImportadorBodega()
        ui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interfazDiseño.ui')
        uic.loadUi(ui_path, self)
        self.habilitarPantalla()
        self.pushButton.clicked.connect(self.cambiarPag)
        self.pushButton.clicked.connect(self.cargar_csv1)
        
    def habilitarPantalla(self):
        self.setWindowTitle("BonVino - Importar Actualizacion")
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'imagenes', 'utnLogo.ico')
        self.setWindowIcon(QIcon(icon_path))
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowMaximizeButtonHint)
        self.show()

    def cambiarPag(self):
        self.stackedWidget.setCurrentIndex(1)

    def cargar_csv1(self):
        bodegas = self.gestor.buscarBodegasConActualizaciones()
        self.cargar_data(bodegas)
    
    def cargar_data(self, bodegas):
        row_count = len(bodegas)
        column_count = 2  # Número de columnas

        self.tableWidget.setRowCount(row_count)
        self.tableWidget.setColumnCount(column_count)
        self.tableWidget.verticalHeader().hide()
        headers = ["Acción", "Nombre"]
        self.tableWidget.setHorizontalHeaderLabels(headers)

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec())