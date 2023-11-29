from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
app = QApplication([])
main_window = QMainWindow()
loadUi("distancias.ui", main_window)
def convertir_kilometros():
    ref = float(main_window.dist_default.text())
    kilometros = ref
    metros = ref * 1000 
    millas = ref *  0.621371192237
    yardas = ref * 1093.61329834 
    main_window.km.setText(str(kilometros))
    main_window.mts.setText(str(metros))
    main_window.yardas.setText(str(yardas))
    main_window.millas.setText(str(millas))
def convertir_metros():
    ref = float(main_window.dist_default.text())
    kilometros = ref / 1000
    metros =  ref
    millas = ref * 0.000621371192237 
    yardas = ref * 1.09361329834 
    main_window.km.setText(str(kilometros))
    main_window.mts.setText(str(metros))
    main_window.yardas.setText(str(yardas))
    main_window.millas.setText(str(millas))
def convertir_millas():
    ref = float(main_window.dist_default.text())
    kilometros = ref * 1.609344
    metros = ref * 1609.344
    millas = ref
    yardas = ref * 1760  
    main_window.km.setText(str(kilometros))
    main_window.mts.setText(str(metros))
    main_window.yardas.setText(str(yardas))
    main_window.millas.setText(str(millas))
def convertir_yardas():
    ref = float(main_window.dist_default.text())
    kilometros = ref * 0.0009144 
    metros = ref * 0.9144
    millas = ref * 0.000568181818182
    yardas = ref
    main_window.km.setText(str(kilometros))
    main_window.mts.setText(str(metros))
    main_window.yardas.setText(str(yardas))
    main_window.millas.setText(str(millas))
def elegir_Referencia():
    distElegida = main_window.eleccion_dist.text()
    if distElegida == "Kilometros":
        main_window.conversor.clicked.connect(lambda:(convertir_kilometros()))
        main_window.chequeo.setText("Todo correcto")
        main_window.dist_defecto.setText("Kilometros")
    elif distElegida == "Metros":
        main_window.conversor.clicked.connect(lambda:(convertir_metros()))
        main_window.chequeo.setText("Todo correcto")
        main_window.dist_defecto.setText(" Metros")
    elif distElegida == "Millas":
        main_window.conversor.clicked.connect(lambda:(convertir_millas()))
        main_window.chequeo.setText("Todo correcto")
        main_window.dist_defecto.setText("Millas")
    elif distElegida == "Yardas":
        main_window.conversor.clicked.connect(lambda:(convertir_yardas()))
        main_window.chequeo.setText("Todo correcto")
        main_window.dist_defecto.setText("Yardas")
    else :
        main_window.chequeo.setText("Distancia no disponible o mal escrita")
main_window.btton_ok.clicked.connect(lambda:elegir_Referencia())

main_window.show()
app.exec()