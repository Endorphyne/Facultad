import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from clasePrueba import Ui_MainWindow
class ClaseVentana(QMainWindow, Ui_MainWindow):#editar "ClaseVentana" con el nombre de nuestra clase
    def __init__(self, parent = None):
        super(ClaseVentana, self).__init__(parent)
        self.setupUi(self)
        self.setup()
    def setup(self):
        pass
def main():
    app = QApplication(sys.argv)
    ventana = ClaseVentana()
    ventana.show()
    app.exec()

if __name__ == "__main__":
    main()
#crear el diseño con QT-Designer
#guardar el archivo del diseño en su carpeta
#en consola ejecutar el comando "pyuic5 (nombre del archivo.ui) -o (nombre del archivo.py)"
#usar la plantilla dela clase para crear una clase nueva
#en la clase nueva editar el nombre de esa clase y el de la clase importada