import sys
from PyQt6.QtWidgets import QApplication
from Interfaz.interfazImportarActualizacion import Ventana

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec())
