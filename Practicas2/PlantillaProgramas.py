import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
#from clase/archivoQueGeneramos import Ui_MainWindow 
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