import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

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
        try:
            # Instanciar el gestor y buscar las bodegas con actualizaciones disponibles
            gestor = GestorImportadorBodega()
            bodegas = gestor.buscarBodegasConActualizaciones()
            self.cargar_data(bodegas)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar los datos: {str(e)}")

    def cargar_data(self, bodegas):
        # Número de filas y columnas
        row_count = len(bodegas)
        column_count = 6  # Ajusta esto según el número de atributos que deseas mostrar
        
        # Establecer número de filas y columnas en el QTableWidget
        self.tableWidget.setRowCount(row_count)
        self.tableWidget.setColumnCount(column_count)
        
        # Rellenar el QTableWidget con los datos de las bodegas
        for row_index, bodega in enumerate(bodegas):
            self.tableWidget.setItem(row_index, 0, QtWidgets.QTableWidgetItem(bodega.nombre))
            self.tableWidget.setItem(row_index, 1, QtWidgets.QTableWidgetItem(bodega.coordenadasUbicacion))
            self.tableWidget.setItem(row_index, 2, QtWidgets.QTableWidgetItem(bodega.descripcion))
            self.tableWidget.setItem(row_index, 3, QtWidgets.QTableWidgetItem(bodega.historia))
            self.tableWidget.setItem(row_index, 4, QtWidgets.QTableWidgetItem(str(bodega.periodoActualizacion)))
            self.tableWidget.setItem(row_index, 5, QtWidgets.QTableWidgetItem(str(bodega.actualizacionDisponible)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()  # Asegúrate de mostrar la ventana
    sys.exit(app.exec())