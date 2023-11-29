from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
app = QApplication([])
main_window = QMainWindow()
loadUi("bascula.ui", main_window)#carga de la UI

def calcular():#funcion para calcular la diferencia de yerba
    entrada = float(main_window.peso_entrada.text())#obtencion del peso en entrada
    salida = float(main_window.peso_Salida.text())#obtencion del peso en salida
    kgs_yerba = entrada - salida #calculo de la cantidad de yerba
    main_window.yerba_Verde_Kgs.setText(str(kgs_yerba))#display visual de la diferencia de yerba 

def nuevo_pesaje():#funcion para reiniciar los valor a valores vacios
    main_window.peso_entrada.setText(" ")#reinicio del valor de entrada
    main_window.peso_Salida.setText(" ")#reinicio del valor de salida
    main_window.yerba_Verde_Kgs.setText(" ")#reinicio del valor de diferencia de yerba
    main_window.patente.setText(" ")#reinicio de la patente
main_window.calcular.clicked.connect(lambda:calcular())
main_window.nuevo_Pesaje.clicked.connect(lambda:nuevo_pesaje())#funciones a llamar en el clickeo de los botones

main_window.show()
app.exec()#presentacion de la ventana y ejecucion de la aplicacion
