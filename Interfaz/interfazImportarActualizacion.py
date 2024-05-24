import sys
from PyQt6.QtWidgets import QApplication, QWidget

class InterfazImportarActualizaciones(QWidget):
    def __init__(self):
        super().__init__()
        self.habilitarPantalla()

    def habilitarPantalla(self):
        self.setGeometry(500, 500, 800, 800)
        self.setWindowTitle("BonVino - Importar Actualizacion")
        self.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = InterfazImportarActualizaciones()
    sys.exit(app.exec())