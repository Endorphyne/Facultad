import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from Clase_Parcial_Horodeski_Lautaro import Ui_Parcial 
class Clase_Parcial_Horodeski_Lautaro(QMainWindow, Ui_Parcial):#editar "Clase_Parcial_Horodeski_Lautaro" con el nombre de nuestra clase
    def __init__(self, parent = None):
        super(Clase_Parcial_Horodeski_Lautaro, self).__init__(parent)
        self.setupUi(self)
        self.conectar()
        self.setup()
    def setup(self):
        self.btn_Guardar.setShortcut("Ctrl+S")
        # self.btn_Guardar.setIcon("Practicas2/Practicas 2/img/guardar.png")
        self.btn_Salir.setShortcut("Ctrl+W")
        # self.btn_Salir.setIcon("Practicas2/Practicas 2/img/salir.png")
    def conectar(self):
        self.btn_Guardar.clicked.connect(self.guardar)
        
    def guardar(self):
        bandera_curso = False
        bandera_instructor = False
        if len(self.line_Nombre_Curso.text()) <= 5:
            bandera_curso = True
        if len(self.line_Instructor.text()) <= 5:
            bandera_instructor = True
        if bandera_instructor:
            QMessageBox.warning(self,"ERROR","Corregir el nombre del instructror",QMessageBox.Ok)
        if bandera_curso:
            QMessageBox.warning(self,"ERROR","Corregir el nombre del instructror",QMessageBox.Ok)
        if not bandera_curso and not bandera_instructor:
            QMessageBox.warning(self,"Exito",f"Curso:{self.line_Nombre_Curso.text()}\n Nivel:{self.cmbo_Nivel_Curso.currentText()} \n Categoria: {self.cmbo_Categoria.currentText()} \n Instructor: {self.line_Instructor.text()} Duracion:{self.spn_Duracion.text()} \n Precio: {self.spn_Precio.text()}")
def main():
    app = QApplication(sys.argv)
    ventana = Clase_Parcial_Horodeski_Lautaro()
    ventana.show()
    app.exec()

if __name__ == "__main__":
    main()