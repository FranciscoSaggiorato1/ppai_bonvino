import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from PyQt6.QtCore import Qt
import recursos

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("interfazDiseño.ui", self)
        self.habilitarPantalla()
        self.pushButton.clicked.connect(self.cambiarPag)

        

    def habilitarPantalla(self):
        self.setWindowTitle("BonVino - Importar Actualizacion")
        self.show()

    def cambiarPag(self):
        self.stackedWidget.setCurrentIndex(1)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec())

