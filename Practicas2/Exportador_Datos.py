import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from Clase_Formulario_Hogar import Ui_Formulario 
class ClaseFormularioHogar(QMainWindow, Ui_Formulario):#editar "ClaseFormularioHogar" con el nombre de nuestra clase
    def __init__(self, parent = None):
        super(ClaseFormularioHogar, self).__init__(parent)
        self.setupUi(self)
        self.setup()
    def setup(self):
        self.btn_Aceptar.clicked.connect(self.data_Harvest)
        pass
    #Funcion para extraer los datos del formularios
    def data_Harvest(self):
        datos={}
        
def main():
    app = QApplication(sys.argv)
    ventana = ClaseFormularioHogar()
    ventana.show()
    app.exec()

if __name__ == "__main__":
    main()