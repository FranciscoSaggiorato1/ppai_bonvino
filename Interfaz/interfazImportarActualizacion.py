import sys
import os
import csv
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import recursos

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
        column_count = 6
        
        # Establecer número de filas y columnas en el QTableWidget
        self.tableWidget.setRowCount(row_count)
        self.tableWidget.setColumnCount(column_count)
        
        # Rellenar el QTableWidget con los datos del CSV
        for row_index, row_data in enumerate(data):
            for column_index, cell_data in enumerate(row_data):
                self.tableWidget.setItem(row_index, column_index, QtWidgets.QTableWidgetItem(cell_data))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec())

