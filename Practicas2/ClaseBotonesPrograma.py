import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from ClaseBotones import Ui_ClaseBotones
#from clase/archivoQueGeneramos import Ui_ClaseBotones 
class ClaseVentana(QMainWindow, Ui_ClaseBotones):#editar "ClaseVentana" con el nombre de nuestra clase
    def __init__(self, parent = None):
        super(ClaseVentana, self).__init__(parent)
        self.setupUi(self)
        self.setup()
    def setup(self):
        #Propiedades del checkbox
        #cambiar el valor de un checkbox
        self.check_Terminos.setChecked(True)
        print(self.check_Terminos.isChecked())#metodo para saber si un termino esta marcado
        #propiedades de los RadioButon
        self.btn_Azul.setChecked(True)#cambiar el valor del radioBtn a verdadero
        print(self.btn_Azul.isChecked())
        #Propiedades del LineEdit
        self.txt_Nombre.setText("Lautaro")
        #limpiar lineEdit
        self.txt_Nombre.clear()
        #propiedades del spinbox
        self.spnBx_Edad.setMinimum(18)#establecer minimo
        self.spnBx_Edad.setMaximum(120)#establecer maximo
        self.spnBx_Edad.setValue(50)#establecer un valor
        self.spnBx_Edad.setPrefix("^")#poner algun strin delante del numero
def main():
    app = QApplication(sys.argv)
    ventana = ClaseVentana()
    ventana.show()
    app.exec()

if __name__ == "__main__":
    main()