from PyQt6.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt6.uic import loadUi
app = QApplication([])
main_window = QMainWindow()
loadUi("calculadora_de_interes.ui", main_window)
bandera_compuesta = False
def chequear(bandera):
    global bandera_compuesta
    if bandera == 2 :
        bandera_compuesta = True
    else:
        bandera_compuesta = False
def cargar_datos():
    capital_inicial = float(main_window.capital_inicial.text())
    tiempo = int(main_window.tiempo.text())
    tasa_interes = float(main_window.tasa_de_interes.text())
    def calcular():
        if bandera_compuesta == True:
            aux = pow(1+(tasa_interes/100),tiempo)
            capital_final = (capital_inicial*aux)
            capital_final = round(capital_final)
        else:
            aux = (1+(tasa_interes/100)*tiempo)
            capital_final = (capital_inicial*aux)
            capital_final = round(capital_final)
        main_window.capital_final.setText(str(capital_final))
    calcular()

main_window.interes_compuesto.stateChanged.connect(chequear)
main_window.calcular.clicked.connect(lambda:cargar_datos())
main_window.show()
app.exec()