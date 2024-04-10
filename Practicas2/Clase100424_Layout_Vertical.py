import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout, QGridLayout
#layouts --> reglas de distribucion de elementos graficos
#HBoxLayout,VBoxLayout,GridLayout,FormLayout

class ClaseLayoutVertical(QMainWindow):#clase hijo con todos sus metodos
    def __init__(self, parent = None):
        super(ClaseLayoutVertical, self).__init__(parent)
        self.setup()
    
    def setup(self):
        self.resize(1000,600)
        self.setWindowTitle("Ejercicios con Layouts")
        self.setMinimumSize(600,600)
        self.setMaximumSize(1908,1080)
        #creacion del contenedor principal
        self.contenedorPrincipal = QWidget(self)
        #Layout Principal
        self.layoutPrincipal = QVBoxLayout(self.contenedorPrincipal)
        # self.btn1 = QPushButton(self.contenedor)
        # self.btn1.setText("boton 1")

        # self.btn2 = QPushButton(self.contenedor)
        # self.btn2.setText("boton 2")

        # self.layoutPrincipal.addWidget(self.btn1)
        # self.layoutPrincipal.addWidget(self.btn2)
        self.contenedorPrincipal.setLayout(self.layoutPrincipal)
        self.setCentralWidget(self.contenedorPrincipal)

        #controlar tamaños de la ventana
        # self.setMinimumSize(400,500)

        #crear el primer grupo de elementos
        self.contenedorNombre = QWidget(self.contenedorPrincipal)
        self.layoutNombre = QHBoxLayout(self.contenedorNombre)
        self.labnombre = QLabel()
        self.labnombre.setText("Nombre:")
        self.leNombre = QLineEdit()
        self.layoutNombre.addWidget(self.labnombre)
        self.layoutNombre.addWidget(self.leNombre)
        self.layoutPrincipal.addWidget(self.contenedorNombre)

        #crear el segundo grupo de elementos
        self.contenedorEmail = QWidget(self.contenedorPrincipal)
        self.layoutEmail = QHBoxLayout(self.contenedorEmail)
        self.labnombre = QLabel()
        self.labnombre.setText("Email:")
        self.leEmail = QLineEdit()
        self.layoutEmail.addWidget(self.labnombre)
        self.layoutEmail.addWidget(self.leEmail)
        self.layoutPrincipal.addWidget(self.contenedorEmail)

        #Crear tercer contenedor de elementos
        self.contenedorBoton = QWidget(self.contenedorPrincipal)
        self.layoutBoton = QHBoxLayout(self.contenedorBoton)
        self.btnEnviar =QPushButton(self.contenedorBoton)
        self.btnEnviar.setText("Enviar")
        self.layoutBoton.addWidget(self.btnEnviar)
        self.layoutPrincipal.addWidget(self.contenedorBoton)
        
        #Crear cuarto contenedor de elementos
        self.contenedorGrilla = QWidget(self.contenedorPrincipal)
        self.layoutGrilla = QGridLayout(self.contenedorGrilla)
        self.btn1 =QPushButton(self.contenedorGrilla)
        self.btn1.setText("1")
        self.layoutGrilla.addWidget(self.btn1, 0,0)
        self.btn2 =QPushButton(self.contenedorGrilla)
        self.btn2.setText("2")
        self.layoutGrilla.addWidget(self.btn2,1,0)
        self.btn3 =QPushButton(self.contenedorGrilla)
        self.btn3.setText("3")
        self.layoutGrilla.addWidget(self.btn3,0,1)
        self.btn4 =QPushButton(self.contenedorGrilla)
        self.btn4.setText("4")
        self.layoutGrilla.addWidget(self.btn4,1,1)
        self.layoutPrincipal.addWidget(self.contenedorGrilla)
  
def main():
    app = QApplication(sys.argv)
    ventana = ClaseLayoutVertical()
    ventana.show()
    app.exec()

if __name__ == "__main__":
    main()