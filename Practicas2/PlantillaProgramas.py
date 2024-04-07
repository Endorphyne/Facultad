import sys
from PyQt5 import QtWidgets
class ClaseVentana(QtWidgets.QMainWindow):#clase hijo con todos sus metodos
    def __init__(self, parent = None):
        super(ClaseVentana, self).__init__(parent)
        self.setup()
    def setup(self):
        self.resize(500, 400)
        #crear contenedor
        self.contenedor = QtWidgets.QWidget(self)
        # self.contenedor.setStyleSheet('background-color:red')
        self.crearElementos()

    def crearElementos(self, parent = None):#crear una clase encargada de crear los botones y colocarlos en el contenedor
        #crear los botones
        self.btnEjemplo= QtWidgets.QPushButton(self.contenedor)#
        self.btnEjemplo.setText("boton de ejemplo")
        self.btnEjemplo2 = QtWidgets.QPushButton(self.contenedor)
        self.btnEjemplo2.setText("boton de ejemplo 2")
        self.btnEjemplo.move(100,200)
        self.setCentralWidget(self.contenedor)
        self.setWindowTitle("Ventana con clase")
def main():
    app = QtWidgets.QApplication(sys.argv)
    ventana = ClaseVentana()
    ventana.show()
    app.exec()

if __name__ == "__main__":
    main()