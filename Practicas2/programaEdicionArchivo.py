import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from edicionArchivo import Ui_ventanaEdicionArchivo
class claseEditorArchivos(QMainWindow, Ui_ventanaEdicionArchivo):#editar "ClaseVentana" con el nombre de nuestra clase
    #variables globales
    id_nota = 1
    lista_notas = []
    def __init__(self, parent = None, nota_ref =str()):
        super(claseEditorArchivos, self).__init__(parent)
        self.nota_ref = nota_ref
        #agregar la nota acutal a la lista de notas
        claseEditorArchivos.lista_notas.append(self)
        self.setupUi(self)
        self.setup()
        self.conectar()
        self.clipboard()
    def setup(self):
        #atajos
        self.actionAbrir.setShortcut("Ctrl+Q")
        self.actionGuardar.setShortcut("Ctrl+S")
        self.actionSalir.setShortcut("Ctrl+W")
        #iconos
        self.actionAbrir.setIcon(QIcon("Practicas2/Practicas 2/img/abrir.png"))
        self.actionGuardar.setIcon(QIcon("Practicas2\Practicas 2\img\guardar.png"))
        self.actionLimpiar.setIcon(QIcon("Practicas2\Archivos de interfaz\Recursos\imagenes\ling-face.png"))
        self.actionSalir.setIcon(QIcon("Practicas2\Practicas 2\img\salir.png"))
        self.actionNueva_Nota.setIcon(QIcon("Practicas2/Practicas 2/img/nuevo.png"))
        self.actionPegar.setIcon(QIcon("Practicas2\Practicas 2\img\pegar.png"))
        self.menuColor.setIcon(QIcon("Practicas2\Practicas 2\img\color.png"))
        self.actionAmarillo.setIcon(QIcon("Practicas2\Archivos de interfaz\Recursos\imagenes\Amarillo.jpeg"))
        self.actionAzul.setIcon(QIcon("Practicas2\Archivos de interfaz\Recursos\imagenes\Azul.jpeg"))
        self.actionVerde.setIcon(QIcon("Practicas2\Archivos de interfaz\Recursos\imagenes/verde.jpeg"))

    def conectar(self):
        self.actionAbrir.triggered.connect(self.abrirArchivo)
        self.actionGuardar.triggered.connect(self.guardarArchivo)
        self.actionSalir.triggered.connect(self.close)
        self.actionNueva_Nota.triggered.connect(self.nueva_Nota)
        #acciones de colores
        self.actionAmarillo.triggered.connect(lambda: self.cambiarColor(self.actionAmarillo.text()))
        self.actionAzul.triggered.connect(lambda: self.cambiarColor(self.actionAzul.text()))
        self.actionVerde.triggered.connect(lambda: self.cambiarColor(self.actionVerde.text()))

        self.actionPegar.triggered.connect(self.pegarClipboard)
        self.actionLimpiar.triggered.connect(self.limpiar)
    def abrirArchivo(self):
        nombre_archivo, _ = QFileDialog.getOpenFileName(self, "Abrir", "", "UI Files(*.ui);;py Files(*.py);;HTML files(*.html)")
        if nombre_archivo:
            with open(nombre_archivo,"r") as archivoAbierto:
                texto = archivoAbierto.read()
            self.textEdit.setText(texto)
        else:
            QMessageBox.information(self,"Error","No se pudo abrir ningun Archivo",QMessageBox.Ok)
    def guardarArchivo(self):
        nombre_archivo, _ = QFileDialog.getSaveFileName(self, "Guardar", "", "UI Files(*.ui);;py Files(*.py);;HTML files(*.html)" )
        if nombre_archivo.endswith(".ui") or nombre_archivo.endswith(".py"):
            texto = self.textEdit.toPlainText()
            with open(nombre_archivo,"w") as archivo:
                archivo.write(texto)
            print("se guardo el cont al arch")
        elif nombre_archivo.endswith(".html"):
            textoEnriquecido = self.textEdit.toHtml()
            with open(nombre_archivo,"w") as archivo:
                archivo.write(textoEnriquecido)
        else:
            QMessageBox.warning(self,"Error","No se puede guardar el archivo con la extension elegida",QMessageBox.Ok)
    def nueva_Nota(self):
        #crear una nueva nota
        self.nota_ref = str("nota%d" % claseEditorArchivos.id_nota)
        ventana = claseEditorArchivos()
        ventana.show()
        claseEditorArchivos.id_nota += 1

    def clipboard(self):
        #configurar el clipboard
        self.clipboard = QApplication.clipboard()
        #controlar que el buffer copiado de windows, haya cambiado
        self.clipboard.dataChanged.connect(self.copiarClipboard)
    
    def copiarClipboard(self):
        return self.clipboard.text()#leer el clipboard del SO

    def pegarClipboard(self):
        #leer el clipboard de la app y pegarlo en la nota
        texto = self.copiarClipboard()
        self.textEdit.insertPlainText(texto)
    def limpiar(self):
        self.textEdit.clear()
    def cambiarColor(self,nombre_Color):
        #cambiar el color del fondo de la nota
        color = "rgb(0,0,0)"
        if nombre_Color == "Amarillo":
            color = "rgb(255, 255, 0)"
        elif nombre_Color == "Azul":
            color = "rgb(0, 0, 145)"
        elif nombre_Color == "Verde":
            color = "rgb(148, 253, 145)"
        self.textEdit.setStyleSheet(f"background-color:{color}")
def main():
    app = QApplication(sys.argv)
    ventana = claseEditorArchivos()
    ventana.show()
    app.exec()

if __name__ == "__main__":
    main()