import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QDialog, QFormLayout


class ContactoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.contactos = []  # Lista de diccionarios para almacenar información de contactos

        self.initUI()

    def initUI(self):
        # Widgets
        self.lista_contactos = QListWidget()
        self.btn_agregar = QPushButton('Agregar')
        self.btn_editar = QPushButton('Editar')
        self.btn_eliminar = QPushButton('Eliminar')

        # Layout principal
        layout_principal = QVBoxLayout()
        layout_principal.addWidget(self.lista_contactos)

        # Layout de botones
        layout_botones = QHBoxLayout()
        layout_botones.addWidget(self.btn_agregar)
        layout_botones.addWidget(self.btn_editar)
        layout_botones.addWidget(self.btn_eliminar)

        layout_principal.addLayout(layout_botones)
        self.setLayout(layout_principal)

        # Conectar señales a funciones
        self.btn_agregar.clicked.connect(self.agregar_contacto)
        self.btn_editar.clicked.connect(self.editar_contacto)
        self.btn_eliminar.clicked.connect(self.eliminar_contacto)

    def agregar_contacto(self):
        dialogo = AgregarContactoDialog()
        if dialogo.exec_():
            contacto = dialogo.obtener_contacto()
            self.contactos.append(contacto)
            self.actualizar_lista_contactos()

    def editar_contacto(self):
        if self.lista_contactos.currentRow() != -1:
            index = self.lista_contactos.currentRow()
            contacto_actual = self.contactos[index]

            dialogo = AgregarContactoDialog(contacto_actual)
            if dialogo.exec_():
                contacto_modificado = dialogo.obtener_contacto()
                self.contactos[index] = contacto_modificado
                self.actualizar_lista_contactos()

    def eliminar_contacto(self):
        if self.lista_contactos.currentRow() != -1:
            index = self.lista_contactos.currentRow()
            del self.contactos[index]
            self.actualizar_lista_contactos()

    def actualizar_lista_contactos(self):
        self.lista_contactos.clear()
        for contacto in self.contactos:
            self.lista_contactos.addItem(f"{contacto['Nombre']} - {contacto['Teléfono']}")


class AgregarContactoDialog(QDialog):
    def __init__(self, contacto=None):
        super().__init__()

        self.contacto = contacto

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Agregar Contacto')

        layout = QFormLayout()

        self.txt_nombre = QLineEdit()
        self.txt_telefono = QLineEdit()
        self.txt_correo = QLineEdit()

        layout.addRow('Nombre:', self.txt_nombre)
        layout.addRow('Teléfono:', self.txt_telefono)
        layout.addRow('Correo:', self.txt_correo)

        if self.contacto:
            # Si se proporciona un contacto, llenar los campos con la información actual
            self.txt_nombre.setText(self.contacto.get('Nombre', ''))
            self.txt_telefono.setText(self.contacto.get('Teléfono', ''))
            self.txt_correo.setText(self.contacto.get('Correo', ''))

        btn_aceptar = QPushButton('Aceptar')
        btn_cancelar = QPushButton('Cancelar')

        btn_aceptar.clicked.connect(self.accept)
        btn_cancelar.clicked.connect(self.reject)

        layout.addRow(btn_aceptar, btn_cancelar)

        self.setLayout(layout)

    def obtener_contacto(self):
        # Obtener la información del contacto ingresada por el usuario
        nombre = self.txt_nombre.text()
        telefono = self.txt_telefono.text()
        correo = self.txt_correo.text()

        return {'Nombre': nombre, 'Teléfono': telefono, 'Correo': correo}


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = ContactoApp()
    ventana.show()
    sys.exit(app.exec_())
