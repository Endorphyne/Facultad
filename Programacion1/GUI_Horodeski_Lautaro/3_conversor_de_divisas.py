from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
app = QApplication([])
main_window = QMainWindow()
loadUi("conversor divisa.ui", main_window)
def cargar_cambio():
    tasa = float(main_window.tasa_cambio.text())
    return tasa
def cargar_valores():
    pesos = float(main_window.cnt_Pesos.text())
    dolares = float(main_window.cnt_Dolares.text())
    return pesos,dolares
def convertir_dinero(pesos,dolares,tasa,base = 1):
    if base == 1: 
        conversion = pesos / tasa 
        main_window.cnt_Dolates.setText(conversion)
    elif base == 2:
        conversion = dolares * tasa
        main_window.cnt_Pesos.setText(conversion)
def eleccion_1():
    return 1
def eleccion_2():
    return 2
def moneda_default(condicion = 1):
    if condicion == 1: 
        main_window.moneda_Default.setText("Pesos")
        main_window.cnt_Dolares.setText("0")
        return 1
    elif condicion == 2:
        main_window.cnt_Pesos.setText("0")
        main_window.moneda_Default.setText("Dolares")
        return 2 
main_window.eleccion_2.clicked.connect(lambda:moneda_default(eleccion_1()))
main_window.eleccion_1.clicked.connect(lambda:moneda_default(eleccion_2()))
main_window.convert_Btn.clicked.connect(lambda:convertir_dinero(cargar_valores(),cargar_cambio(),moneda_default()))
main_window.show()
app.exec()