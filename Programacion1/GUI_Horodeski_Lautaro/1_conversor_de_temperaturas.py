from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
app = QApplication([])
main_window = QMainWindow()
loadUi("temperaturas.ui", main_window)
def convertirTemperaturas_celsius():
    celsius = float(main_window.temp_default.text())
    kelvin = (celsius + 274.15)
    newton = (celsius * (33/100))
    fahrenheit = (celsius * (9/5) + 32)
    main_window.temp_Kelvin.setText(str(kelvin))
    main_window.temp_Newton.setText(str(newton))
    main_window.temp_Fahrenheit.setText(str(fahrenheit))
    main_window.temp_Celsius.setText(str(celsius))
def convertirTemperaturas_fahrenheit():
    fahrenheit = float(main_window.temp_default.text())
    kelvin = ((fahrenheit + 459.67) * (5/9))
    newton = ((fahrenheit - 32)* (11/60))
    celsius = ((fahrenheit - 32) * (5/9))
    main_window.temp_Kelvin.setText(str(kelvin))
    main_window.temp_Newton.setText(str(newton))
    main_window.temp_Celsius.setText(str(celsius))
    main_window.temp_Fahrenheit.setText(str(fahrenheit))
def convertirTemperaturas_newton():
    newton = float(main_window.temp_default.text())
    kelvin = ((newton * (100/33) +  273,15))
    celsius = ((newton *(100/33)))
    fahrenheit = ((newton * (60/11)+ 32))
    main_window.temp_Kelvin.setText(str(kelvin))
    main_window.temp_Celsius.setText(str(celsius))
    main_window.temp_Fahrenheit.setText(str(fahrenheit))
    main_window.temp_Newton.setText(str(newton))
def convertirTemperaturas_kelvin():
    kelvin = float(main_window.temp_default.text())
    celsius = (kelvin - 274,15)
    newton = ((kelvin - 273,15)* (33/100))
    fahrenheit = (kelvin *(9/5)- 459.67)
    main_window.temp_Celsius.setText(str(celsius))
    main_window.temp_Newton.setText(str(newton))
    main_window.temp_Fahrenheit.setText(str(fahrenheit))
    main_window.temp_Kelvin.setText(str(kelvin))
def elegirTemperatura():
    tempElegida = main_window.eleccion_temp.text()
    if tempElegida == "Celsius":
        main_window.conversor.clicked.connect(lambda:convertirTemperaturas_celsius())
        main_window.chequeo.setText("Todo correcto")
        main_window.termp_defecto.setText("Celsius")
    elif tempElegida == "Fahrenheit":
        main_window.conversor.clicked.connect(lambda:convertirTemperaturas_fahrenheit())
        main_window.chequeo.setText("Todo correcto")
        main_window.termp_defecto.setText("Fahrenheit")
    elif tempElegida == "Newton":
        main_window.conversor.clicked.connect(lambda:convertirTemperaturas_newton())
        main_window.chequeo.setText("Todo correcto")
        main_window.termp_defecto.setText("Newton")
    elif tempElegida == "Kelvin":
        main_window.conversor.clicked.connect(lambda:convertirTemperaturas_kelvin())
        main_window.chequeo.setText("Todo correcto")
        main_window.termp_defecto.setText("Kelvin")
    else :
        main_window.chequeo.setText("Temperatura no disponible o mal escrita")
main_window.btton_ok.clicked.connect(lambda:elegirTemperatura())

main_window.show()
app.exec()