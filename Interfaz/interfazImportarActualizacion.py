import sys
import os
import csv
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import recursos
from functools import partial

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interfazDiseño.ui')
        uic.loadUi(ui_path, self)
        self.habilitarPantalla()
        self.pushButton.clicked.connect(self.cambiarPag)
        self.pushButton.clicked.connect(self.cargar_csv)
        
    def habilitarPantalla(self):
        self.setWindowTitle("BonVino - Importar Actualizacion")
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'imagenes', 'utnLogo.ico')
        self.setWindowIcon(QIcon(icon_path))
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowMaximizeButtonHint)
        self.show()

    def cambiarPag(self):
        self.stackedWidget.setCurrentIndex(1)

    def cargar_csv(self):
        # Buscar el archivo csv
        filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ppaiDataExcel.csv')
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            self.cargar_data(reader)
    
    def cargar_data(self, reader):
        # Leer todas las filas del CSV
        data = list(reader)

        # Número de filas y columnas
        row_count = len(data)
        column_count = 6  # Incrementamos el número de columnas en 1 para la nueva columna de botones

        # Establecer número de filas y columnas en el QTableWidget
        self.tableWidget.setRowCount(row_count)
        self.tableWidget.setColumnCount(column_count)

        # Ocultar los números de fila y columna
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.horizontalHeader().hide()

        # Rellenar el QTableWidget con los datos del CSV
        for row_index, row_data in enumerate(data):
            if row_index != 0:
                # Crear un botón para cada fila
                button = QtWidgets.QPushButton("Seleccionar")
                button.clicked.connect(partial(self.select_bodega, row_index))  # Conectar el botón a un método que maneje la selección de la bodega
                self.tableWidget.setCellWidget(row_index, 0, button)  # Agregar el botón a la primera columna de la fila

            for column_index, cell_data in enumerate(row_data):
                if column_index == 5:
                    break
                else:
                    # Ajustamos el índice de la columna en 1 para tener en cuenta la nueva columna de botones
                    self.tableWidget.setItem(row_index, column_index + 1, QtWidgets.QTableWidgetItem(cell_data))

    def select_bodega(self, row_index):
        # Este método maneja la selección de una bodega
        # Puedes reemplazar este código con el código que necesites para manejar la selección de una bodega
        print("Bodega seleccionada:", row_index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec())

