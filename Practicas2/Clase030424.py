import sys #libreria para interactuar con el sistema desde el codigo 
from PyQt5 import QApplication, QWidget #IMPORTANTE: importar siempre lo necesario no toda la libreria completa
def main(): #funcion principal donde meteremos todo lo que involucre el programa 
    app = QApplication(sys.argv)#Aplicacion Principal
    ventana = QWidget()#Clase para crear una ventana
    ventana.resize()#Trabajar siempre (ANCHOxALTO)(OPCIONALES)
    ventana.move()#mover la ventan a un punto especifico(OPCIONALES)
    ventana.setWindowTitle()#Poner titulo a la ventana (OPCIONALES)
    ventana.show()#Mostrar la ventana 
    app.exec_()#Iniciar la ejecucion de la aplicacion 
if __name__ == "__main__": #comprobar que el archivo no esta siendo usado en otro modulo
    main()
#-----------------------------------------------------------------------------
#Definicion de clase: especializaicon de un elemento de la vida real
#Caracteristicas:(atributos)
#Funcionamiento(metodo)
#-----------------------------------------------------------------------------