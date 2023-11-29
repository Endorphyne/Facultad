from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
app = QApplication([])
main_window = QMainWindow()
loadUi("gastosDiarios.ui", main_window)
def sumarGastos():
    monto = int(main_window.monto.text())
    aux = int(main_window.total.text())
    main_window.total.setText(f"{monto+aux}")
def restarGastos():
    monto = int(main_window.monto.text())
    aux = int(main_window.total.text())
    main_window.total.setText(f"{aux-monto}")
main_window.sumar.clicked.connect(lambda:sumarGastos())
main_window.Restar.clicked.connect(lambda:restarGastos())
main_window.show()
app.exec()