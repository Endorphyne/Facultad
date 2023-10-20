from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
app = QApplication([])
main_window = QMainWindow()
loadUi("calculadora.ui", main_window)
def suma():
    n1 = float(main_window.nm1.text())
    n2 = float(main_window.nm2.text())
    res = n1+n2
    main_window.resultado.setText(f"Resultado: {res}")
def resta():
    n1 = float(main_window.nm1.text())
    n2 = float(main_window.nm2.text())
    res = n1-n2
    main_window.resultado.setText(f"Resultado: {res}")
def multiplicacion():
    n1 = float(main_window.nm1.text())
    n2 = float(main_window.nm2.text())
    res = n1*n2

    main_window.resultado.setText(f"Resultado: {res}")
def division(): 
    n1 = float(main_window.nm1.text())
    n2 = float(main_window.nm2.text())
    if float(main_window.nm1.text()) == 0 or float(main_window.nm2.text()) == 0:
        main_window.resultado.setText("ERROR")
    else:
        res = n1/n2
    main_window.resultado.setText(f"Resultado: {res}")
main_window.suma.clicked.connect(lambda:suma())
main_window.resta.clicked.connect(lambda:resta())
main_window.multiplicacion.clicked.connect(lambda:multiplicacion())
main_window.division.clicked.connect(lambda:division())
main_window.show()
app.exec()