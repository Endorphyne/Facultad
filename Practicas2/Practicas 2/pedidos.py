# Importacion
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QLabel, QRadioButton, QButtonGroup, QGroupBox, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

# TODO: Definir la hoja de estilos de la aplicacion
hoja_estilos = """
"""


class Pedidos(QWidget):
    def __init__(self):
        super().__init__()
        self.configurar()

    def configurar(self):
        # Inicializar la ventana y mostrar su contenido
        self.setMinimumSize(600, 700)
        self.setWindowTitle("Ventana de pedidos")
        self.configurarInterfaz()
        self.conectar()
        self.show()

    def configurarInterfaz(self):
        # Configurar el contenedor de pestañas
        # Crear el widget lateral para mostrar los items seleccionados
        # Crear el tab bar, las pestanias y los nombres de objeto
        self.barra_pestanias = QTabWidget(self)

        self.tab_pizza = QWidget()
        self.tab_pizza.setObjectName("Tabs")
        self.tab_papas = QWidget()
        self.tab_papas.setObjectName("Tabs")
        self.barra_pestanias.addTab(self.tab_pizza, "Pizza")
        self.barra_pestanias.addTab(self.tab_papas, "Papas")

        # Llamar a metodos que contienen los widgets para cada pestaña
        self.tabPizza()
        self.tabPapas()

        # Configurar el widget lateral (que no forma parte del TabWidget)
        self.contenedor_lateral = QWidget()
        self.contenedor_lateral.setObjectName("Tabs")
        lab_orden = QLabel("TU ORDEN")
        lab_orden.setObjectName("Encabezado")

        caja_items = QWidget()
        caja_items.setObjectName("Lateral")
        lab_pizza = QLabel("Tipo de Pizza: ")
        self.lab_mostrar_pizza = QLabel("")
        lab_relleno = QLabel("Rellenos: ")
        self.lab_mostrar_rellenos = QLabel("")
        lab_extra = QLabel("Extra: ")
        self.lab_mostrar_extra = QLabel("")

        # Configurar el GridLayout para ubicar los objetos del widget lateral
        grilla_items = QGridLayout()
        grilla_items.addWidget(lab_pizza, 0, 0, Qt.AlignRight)
        grilla_items.addWidget(self.lab_mostrar_pizza, 0, 1)
        grilla_items.addWidget(lab_relleno, 1, 0, Qt.AlignRight)
        grilla_items.addWidget(self.lab_mostrar_rellenos, 1, 1)
        grilla_items.addWidget(lab_extra, 2, 0, Qt.AlignRight)
        grilla_items.addWidget(self.lab_mostrar_extra, 2, 1)
        caja_items.setLayout(grilla_items)

        # Definir el layout principal del widget lateral
        caja_lateral = QVBoxLayout()
        caja_lateral.addWidget(lab_orden)
        caja_lateral.addWidget(caja_items)
        caja_lateral.addStretch()
        self.contenedor_lateral.setLayout(caja_lateral)

        # Agregar widgets y definir layout de la ventana principal
        caja_principal = QHBoxLayout()
        caja_principal.addWidget(self.barra_pestanias)
        caja_principal.addWidget(self.contenedor_lateral)
        self.setLayout(caja_principal)

    def tabPizza(self):
        # Crea los elementos de la pestaña de pizza

        # Configurar los widgets y layouts para mostrar información
        lab_tab_pizza = QLabel("CREA TU PROPIA PIZZA")
        lab_tab_pizza.setObjectName("Encabezado")
        caja_descripcion = QWidget()
        caja_descripcion.setObjectName("BordeImagen")
        ruta_imagen_pizza = "img/pizza.png"
        imagen_pizza = self.cargarImagen(ruta_imagen_pizza)
        descripcion_pizza = QLabel()
        descripcion_pizza.setObjectName("InfoImagen")
        descripcion_pizza.setText("Crea una pizza a tu medida. Empieza con tu preparacion favorita y agrega rellenos, más los extras que desees agregar")
        descripcion_pizza.setWordWrap(True)

        caja_horizontal = QHBoxLayout()
        caja_horizontal.addWidget(imagen_pizza)
        caja_horizontal.addWidget(descripcion_pizza)

        caja_descripcion.setLayout(caja_horizontal)

        # Crear el grupo que tendrá la opción de preparación
        caja_grupo_preparacion = QGroupBox()
        caja_grupo_preparacion.setTitle("ELIGE LA PREPARACION")

        # Crear el grupo para los botones internos
        self.grupo_preparacion = QButtonGroup()
        layout_grupo_preparacion = QVBoxLayout()
        # TODO: definir los tipos de preparacion
        lista_preparacion = []

        # Usar un for para crear los RadioButton
        for lp in lista_preparacion:
            rb_preparacion = QRadioButton(lp)
            layout_grupo_preparacion.addWidget(rb_preparacion)
            self.grupo_preparacion.addButton(rb_preparacion)

        caja_grupo_preparacion.setLayout(layout_grupo_preparacion)

        # Crear el grupo que tendrá la opción de rellenos
        caja_grupo_rellenos = QGroupBox()
        caja_grupo_rellenos.setTitle("ELIGE LOS RELLENOS")

        # Crear el grupo para los botones internos
        self.grupo_rellenos = QButtonGroup()
        layout_grupo_rellenos = QVBoxLayout()
        # TODO: definir los tipos de rellenos disponibles
        lista_rellenos = []

        # Usar un for para crear los RadioButton
        for lr in lista_rellenos:
            rb_rellenos = QRadioButton(lr)
            layout_grupo_rellenos.addWidget(rb_rellenos)
            self.grupo_rellenos.addButton(rb_rellenos)

        self.grupo_rellenos.setExclusive(False)
        caja_grupo_rellenos.setLayout(layout_grupo_rellenos)

        # Crear el boton que permita añadir a la orden
        btn_agregar_orden = QPushButton("Agregar a la orden")

        # Crear el layout para la pestaña de pizzas (pagina 1)
        caja_tab_pizza = QVBoxLayout()
        caja_tab_pizza.addWidget(lab_tab_pizza)
        caja_tab_pizza.addWidget(caja_descripcion)
        caja_tab_pizza.addWidget(caja_grupo_preparacion)
        caja_tab_pizza.addWidget(caja_grupo_rellenos)
        caja_tab_pizza.addStretch()
        caja_tab_pizza.addWidget(btn_agregar_orden, alignment=Qt.AlignRight)

        self.tab_pizza.setLayout(caja_tab_pizza)

    def tabPapas(self):
        lab_tab_papas = QLabel("PRUEBA NUESTRAS INCREIBLES PAPAS")
        lab_tab_papas.setObjectName("Encabezado")
        caja_descripcion = QWidget()
        caja_descripcion.setObjectName("BordeImagen")
        ruta_imagen_papas = "img/papas.png"
        imagen_papas = self.cargarImagen(ruta_imagen_papas)
        descripcion_papas = QLabel()
        descripcion_papas.setObjectName("InfoImagen")
        descripcion_papas.setText("Nuestras papas son superiores a la de la competencia. No te vayas sin probar una porción.")
        descripcion_papas.setWordWrap(True)

        caja_horizontal = QHBoxLayout()
        caja_horizontal.addWidget(imagen_papas)
        caja_horizontal.addWidget(descripcion_papas)

        caja_descripcion.setLayout(caja_horizontal)
        caja_grupo_papas = QGroupBox()
        caja_grupo_papas.setTitle("ELIGE EL SABOR")

        self.grupo_papas = QButtonGroup()
        layout_grupo_papas = QVBoxLayout()
        # TODO: definir los tipos de papas disponibles
        lista_papas = []

        # Usar un for para crear los RadioButton
        for lp in lista_papas:
            rb_papas = QRadioButton(lp)
            layout_grupo_papas.addWidget(rb_papas)
            self.grupo_papas.addButton(rb_papas)

        caja_grupo_papas.setLayout(layout_grupo_papas)

        # Crear el boton que permita añadir a la orden
        btn_agregar_orden = QPushButton("Agregar a la orden")

        # Crear el layout para la pestaña de papas (pagina 2)
        caja_tab_papas = QVBoxLayout()
        caja_tab_papas.addWidget(lab_tab_papas)
        caja_tab_papas.addWidget(caja_descripcion)
        caja_tab_papas.addWidget(caja_grupo_papas)
        caja_tab_papas.addWidget(btn_agregar_orden, alignment=Qt.AlignRight)
        caja_tab_papas.addStretch()

        self.tab_papas.setLayout(caja_tab_papas)

    def conectar(self):
        # TODO: conectar eventos
        pass

    def obtenerListaRellenos(self):
        # TODO: Crear una lista de todos los radio buttons seleccionados para rellenos
        pass

    def mostrarPizzaEnOrden(self):
        # TODO: Obtener los textos de las opciones seleccionadas y mostrar en la columna
        pass

    def mostrarPapasEnOrden(self):
        # TODO: Obtener los textos de las opciones seleccionadas y mostrar en la columna
        pass

    def cargarImagen(self, ruta_imagen):
        # TODO: Cargar y escalar una imagen
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # TODO: establecer estilos de la aplicacion
    ventana = Pedidos()
    sys.exit(app.exec_())
