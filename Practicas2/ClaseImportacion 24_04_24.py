import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from VentanaImportaciones import Ventana_Importaciones
import random
class ClaseImportaciones(QMainWindow, Ventana_Importaciones):#editar "ClaseVentana" con el nombre de nuestra clase
    def __init__(self, parent = None):
        super(ClaseImportaciones, self).__init__(parent)
        self.setupUi(self)
        self.setup()

    def setup(self):
        #cambiar texto del boton
        self.btn_Salir.setText("Wakanda")
        #agregar o cambiar un icono
        self.btn_Salir.setIcon(QIcon("Practicas2\Archivos de interfaz\Recursos\imagenes\ling-mad-head.png"))
        #agregar un atajo
        self.btn_Salir.setShortcut("Ctrl+W")
        #agregar un evento o accionar al click del boton
        self.btn_Salir.clicked.connect(self.close)
        #mover a una posicion deltro de la ventana
        # self.btn_Salir.move(100,100)
        #Establecer elemento por defecto
        self.btn_Salir.setDefault(True)
        #habilitar/deshabilitar elementos
        self.btn_Salir.setEnabled(random.randint(1,2)==1)
        #imprimir/leer el texto de un elemento
        print(self.btn_Salir.text())
        #======================Labels====================
        self.lab_Imagen.setScaledContents(True)
        self.lab_Titulo.setText("pepito")
        self.lab_Titulo.setText("<font color=red>www.google.com</font>")#modificar la fuente
        #cambiar alienacion
        self.lab_Titulo.setAlignment(Qt.AlignCenter)
        #cambiar el tooltip de la etiqueta
        self.lab_Titulo.setToolTip("Esta es la direccion de google")
        #limpiar el texto de la etiqueta
        self.lab_Imagen.clear()
        #poner una imagen en la etiqueta
        self.lab_Imagen.setPixmap(QPixmap("Practicas2\Archivos de interfaz\Recursos\imagenes\ling-mad.gif"))
        # modificar el estilo de un elemento
        self.btn_Salir.setStyleSheet("background-color: lightblue")

def main():
    app = QApplication(sys.argv)
    ventana = ClaseImportaciones()
    ventana.show()
    app.exec()

if __name__ == "__main__":
    main()