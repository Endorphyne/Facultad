from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
app = QApplication([])
main_window = QMainWindow()
loadUi("inventario.ui", main_window)
inv = {}
#funcion para agregar items al inventario
def agregar():
    main_window.inventario.clear()
    item = main_window.nombre.text()
    if main_window.cantidad.text() == "":#revisa que la cantidad no este vacia
        main_window.inventario.setText("CANTIDAD INVALIDA!!")#mensaje de error
    else:
        cantidad = int(main_window.cantidad.text())
    if len(item)==0 :#comprueba que no se intente agregar un item vacio
        main_window.inventario.setText("INGRESAR ITEM!!")#mensaje de error
    elif item not in inv:#comparativa para ver si esta o no en la lista
        inv.update({item:cantidad})
        main_window.inventario.append(f'{item}:{inv[item]}')
        main_window.statusBar().showMessage(f"Producto {item.upper()} agregado al inventario")
    else:
        inv[item] += cantidad
        main_window.inventario.append(f'{item}:{inv[item]}')
        main_window.statusBar().showMessage(f"Producto {item.upper()} agregado al inventario")
#funcion para actualizar la informacion en pantalla del inventario
def actualizar():
    main_window.inventario.clear()
    item = main_window.nombre.text()
    cantidad = int(main_window.cantidad.text())
    if len(item)==0 :#comprobacion de que el item no este vacio
        main_window.inventario.setText("INGRESAR ITEM!!")
    elif item in inv:#actualizacion del item sobreescribiendo la cantidad
        inv.update({item:cantidad})
    main_window.inventario.append(f'{item}:{inv[item]}')
#funcion para mostrar el informe del inventario
def informe():
    main_window.inventario.clear()#limpieza de la ventana a mostrar
    main_window.inventario.append("Inventario:\n")
    for k,v in inv.items():#iteracion del inventario para mostrar todos los items
        main_window.inventario.append(f"{k}:{v}")#formateo de la muestra
#coneccion a los botones clickados
main_window.agregar.clicked.connect(lambda:agregar())
main_window.informe.clicked.connect(lambda:informe())
main_window.actualizar.clicked.connect(lambda:actualizar())
main_window.show()
app.exec()