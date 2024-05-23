import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from ClaseEventos import Ui_Calculadora
#from clase/archivoQueGeneramos import Ui_MainWindow 
class ClaseEventos(QMainWindow, Ui_Calculadora):#editar "ClaseEventos" con el nombre de nuestra clase
    def __init__(self, parent = None):
        super(ClaseEventos, self).__init__(parent)
        self.setupUi(self)
        self.setup()

    def setup(self):
        # def resta(valorA,ValorB):
        #     resultado = valorA - ValorB
        #     return resultado
        # def multiplicacion(valorA,valorB):
        #     resultado = valorA * valorB
        #     return resultado
        # def division(valorA,valorB):
        #     try:
        #         resultado = valorA/valorB
        #     except:
        #         print("valor invalido")
        # self.pshBtn_Suma.clicked.connect(lambda:suma(self.lnEdit_Nm1.text(),self.lnEdit_Nm2.text()))
        #-----------------------------------------
        #Conectar los eventos de los botones
        self.pshBtn_Suma.clicked.connect(self.suma)
        self.pshBtn_Resta.clicked.connect(self.resta)
        self.pshBtn_Multiplicacion.clicked.connect(self.multiplicar)
        self.pshBtn_Division.clicked.connect(self.dividir)
    def suma(self):
        try:
            valor1 = int(self.lnEdit_Nm1.text())
            valor2 = int(self.lnEdit_Nm2.text())
            resultado = str(valor1+valor2)
            self.lbl_Resultado.setStyleSheet("background-color:white")
            self.lbl_Resultado.setText(resultado)
        except:
            print("valor invalido")    
            self.lbl_Resultado.setStyleSheet("background-color:red")
            self.lbl_Resultado.setText("Rellene correctamente todos los campos")
    def resta(self):
        try:
            valor1 = int(self.lnEdit_Nm1.text())
            valor2 = int(self.lnEdit_Nm2.text())
            resultado = str(valor1-valor2)
            self.lbl_Resultado.setStyleSheet("background-color:white")
            self.lbl_Resultado.setText(resultado)
        except:
            print("valor invalido")    
            self.lbl_Resultado.setStyleSheet("background-color:red")
            self.lbl_Resultado.setText("Rellene correctamente todos los campos")
    def multiplicar(self):
        try:
            valor1 = int(self.lnEdit_Nm1.text())
            valor2 = int(self.lnEdit_Nm2.text())
            resultado = str(valor1*valor2)
            self.lbl_Resultado.setStyleSheet("background-color:white")
            self.lbl_Resultado.setText(resultado)
        except:
            print("valor invalido")    
            self.lbl_Resultado.setStyleSheet("background-color:red")
            self.lbl_Resultado.setText("Rellene correctamente todos los campos")
    def dividir(self):
        try:
            valor1 = int(self.lnEdit_Nm1.text())
            valor2 = int(self.lnEdit_Nm2.text())
            resultado = str(valor1/valor2)
            self.lbl_Resultado.setStyleSheet("background-color:white")
            self.lbl_Resultado.setText(resultado)
        except:
            print("valor invalido")    
            self.lbl_Resultado.setStyleSheet("background-color:red")
            self.lbl_Resultado.setText("Rellene correctamente todos los campos")
    
def main():
    app = QApplication(sys.argv)
    ventana = ClaseEventos()
    ventana.show()
    app.exec()

if __name__ == "__main__":
    main()