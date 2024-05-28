import os
import csv
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6 import uic, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import recursos
from functools import partial

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from Controlador.gestorImportarActualizacion import GestorImportadorBodega

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
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
        gestor = GestorImportadorBodega()
        bodegas = gestor.buscarBodegasConActualizaciones()
        self.cargar_data(bodegas)
    
    def cargar_data(self, bodegas):
        # Número de filas y columnas
        row_count = len(bodegas)
        column_count = 6  # Incrementamos el número de columnas en 1 para la nueva columna de botones

        # Establecer número de filas y columnas en el QTableWidget
        self.tableWidget.setRowCount(row_count)
        self.tableWidget.setColumnCount(column_count)

        # Ocultar los números de fila y columna
        self.tableWidget.verticalHeader().hide()

        # Configurar los encabezados de la tabla
        headers = ["Acción", "Nombre", "Coordenadas", "Descripción", "Historia", "Periodo de Actualización"]
        self.tableWidget.setHorizontalHeaderLabels(headers)


        # Rellenar el QTableWidget con los datos del CSV
        for row_index, bodega in enumerate(bodegas):
            # Crear un botón para cada fila
            button = QtWidgets.QPushButton("Seleccionar")
            button.clicked.connect(partial(self.tomarBodegaSeleccionada, bodega))  # Conectar el botón a un método que maneje la selección de la bodega
            self.tableWidget.setCellWidget(row_index, 0, button)  # Agregar el botón a la primera columna de la fila

                  # Agregar los atributos de la bodega a las celdas del QTableWidget
            self.tableWidget.setItem(row_index, 1, QTableWidgetItem(bodega['nombre']))
            self.tableWidget.setItem(row_index, 2, QTableWidgetItem(bodega['coordenadasUbicacion']))
            self.tableWidget.setItem(row_index, 3, QTableWidgetItem(bodega['descripcion']))
            self.tableWidget.setItem(row_index, 4, QTableWidgetItem(bodega['historia']))
            self.tableWidget.setItem(row_index, 5, QTableWidgetItem(str(bodega['periodoActualizacion'])))

    def tomarBodegaSeleccionada(self, bodega):
        # Este método maneja la selección de una bodega
        # Puedes reemplazar este código con el código que necesites para manejar la selección de una bodega
        return bodega

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec())