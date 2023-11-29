from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
app = QApplication([])
main_window = QMainWindow()
loadUi("ListaContactos.ui", main_window)
contactos=[]
identificador = 0
def mostrar():
    main_window.ventana.clear()
    for contacto in contactos:
        for x,y in contacto.items():
            if x != "ID":
                main_window.ventana.append(f"{x}:{y}")
                main_window.ventana.append('\n')
def agregarContacto():
    global identificador
    nombre = main_window.nombre.text()
    correo = main_window.correo.text()
    telefono = main_window.telefono.text()
    contactos.append({'Nombre':nombre,"Correo":correo,"Telefono":telefono,"ID":identificador})
    mostrar()
    identificador += 1
def buscarContacto():
    nombre = main_window.nombre.text()
    for contacto in contactos:
        for x in contacto.keys():
            if nombre == x :
                mostrar()
def editarContacto():
    pass
def eliminarContacto():
    pass
main_window.agregar.clicked.connect(lambda:agregarContacto())
main_window.show()
app.exec()