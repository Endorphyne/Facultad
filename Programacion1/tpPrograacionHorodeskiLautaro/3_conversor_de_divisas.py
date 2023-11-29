from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
app = QApplication([])
main_window = QMainWindow()
loadUi("conversor_divisa.ui", main_window)
def moneda_Base():
    moneda = main_window.moneda_base.text()
    moneda = moneda.lower()
    if moneda == "pesos":
        main_window.moneda_default.setText("Pesos")
    elif moneda == "dolares":
        main_window.moneda_default.setText("Dolares")
    elif moneda == "euros":
        main_window.moneda_default.setText("Euros")
    else: 
        main_window.moneda_default.setText("Moneda mal escrita o no disponible")
def moneda_Objetivo():
    moneda = main_window.moneda_Objetivo.text()
    moneda = moneda.lower()
    if moneda == "pesos":
        main_window.conversion.setText("Pesos")
    elif moneda == "dolares":
        main_window.conversion.setText("Dolares")
    elif moneda == "dolar blue":
        main_window.conversion.setText("Dolar Blue")

    elif moneda == "euros":
        main_window.conversion.setText("Euros")
    else: 
        main_window.conversion.setText("Moneda mal escrita o no disponible")
def taza():
    cambio = int(main_window.tasa_cambio.text())
    return cambio
def conversion(taza = 1):
    base = int(main_window.cnt_Base.text())
    resultado = base * taza 
    main_window.cnt_Objetivo.setText(str(resultado))
main_window.fijar_moneda.clicked.connect(lambda:moneda_Base())
main_window.fijar_moneda.clicked.connect(lambda:moneda_Objetivo())
main_window.convert_Btn.clicked.connect(lambda:conversion(taza()))
main_window.show()
app.exec()