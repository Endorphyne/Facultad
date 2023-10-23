from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
app = QApplication([])
main_window = QMainWindow()
loadUi("gastosDiarios.ui", main_window)

main_window.show()
app.exec()