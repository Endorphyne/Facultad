from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
from PyQt6 import QtTest
app = QApplication([])
main_window = QMainWindow()
loadUi("cronometro.ui", main_window)
bandera = True
def iniciar():
        global bandera
        bandera = True
        while bandera == True:
            segundos = int(main_window.segundos.text())
            minutos = int(main_window.minutos.text())
            horas = int(main_window.horas.text())
            segundos += 1 
            if segundos == 60:
                minutos += 1
                segundos = 0 
            if minutos == 60 :
                horas +=1 
                minutos = 0 
            main_window.segundos.setText(str(segundos))
            main_window.minutos.setText(str(minutos))
            main_window.horas.setText(str(horas))
            QtTest.QTest.qWait(1000)
def reiniciar():
        main_window.segundos.setText(str(0))
        main_window.minutos.setText(str(0))
        main_window.horas.setText(str(0))
def pausar():
      global bandera
      bandera = False
main_window.stop.clicked.connect(lambda:pausar())
main_window.start.clicked.connect(lambda:iniciar())
main_window.restart.clicked.connect(lambda:reiniciar())

main_window.show()
app.exec()