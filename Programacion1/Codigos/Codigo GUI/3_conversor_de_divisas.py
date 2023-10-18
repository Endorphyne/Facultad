from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
app = QApplication([])
main_window = QMainWindow()
loadUi("conversor_divisa.ui", main_window)
def cargar_cambio():
    tasa = float(main_window.tasa_cambio.text())
def cargar_valores():
    pesos = float(main_window.cnt_pesos.text())
    dolares = float(main_window.cnt_dolares.text())
    return pesos,dolares
def convertir_dinero(pesos,dolares):
    pass
def eleccion_1():
    return 1 
def moneda_default():
    if main_window.eleccion_1.clicked.connect(): 
        main_window.moneda_default.setText("wakanda")
    elif main_window.eleccion_2.clicked.connect():
        main_window.moneda_default.setText("Mordor")
main_window.show()
app.exec()