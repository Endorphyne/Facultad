#realizar un formulario donde se deberan ingresar los siguientes datos
# -nombre
# -apellido
# -edad
# -DNI
# -Matricula
# -Indicar que carrera cursa= 1)Analista de sistemas, 2)Enfermeria, 3)Abogacia
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from ClaseFormulario import Ui_VentanaFormulario
#from clase/archivoQueGeneramos import Ui_VentanaFormulario 
class ClaseFormulario(QMainWindow, Ui_VentanaFormulario):#editar "ClaseVentana" con el nombre de nuestra clase
    def __init__(self, parent = None):
        super(ClaseFormulario, self).__init__(parent)
        self.setupUi(self)
        self.setup()
    def setup(self):
        pass
def main():
    app = QApplication(sys.argv)
    ventana = ClaseFormulario()
    ventana.show()
    app.exec()

if __name__ == "__main__":
    main()