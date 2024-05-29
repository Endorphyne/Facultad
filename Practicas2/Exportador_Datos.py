import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from Clase_Formulario_Hogar import Ui_Formulario 
class ClaseFormularioHogar(QMainWindow, Ui_Formulario):#editar "ClaseFormularioHogar" con el nombre de nuestra clase
    def __init__(self, parent = None):
        super(ClaseFormularioHogar, self).__init__(parent)
        self.setupUi(self)
        self.setup()
    def setup(self):
        self.btn_Aceptar.clicked.connect(self.data_Harvest)
        pass
    #Funcion para extraer los datos del formularios
    def data_Harvest(self):
        datos={}
        #Datoas de DIRECCION
        datos.update({"DIRECCION":0})
        datos.update({"Direccion Principal":self.lnEdit_Direccion_Principal.text()})
        datos.update({"Direccion Secundaria":self.lnEdit_Direccion_Secundaria.text()})
        datos.update({"Ciudad":self.comboBx_Ciudad.currentText()})
        datos.update({"Provincia":self.comboBx_Provincia.currentText()})
        datos.update({"Codigo Postal":self.lnEdit_Codigo_Postal.text()})
        #Datos de AMBIENTE
        datos.update({"AMBIENTE":0})
        datos.update({"Tipo de Edificio":self.comboBx_Tipo_Edificio.currentText()})
        datos.update({"Ambientes":self.spnBx_Ambientes.text()})
        datos.update({"Habitaciones":self.spnBx_Habitaciones.text()})
        datos.update({"Baños":self.spnBx_Banios.text()})
        #Datos de CAMAS
        datos.update({"CAMAS":0})
        datos.update({"Cama Matrimonial":self.spnBx_Cama_Matrimonial.text()})
        datos.update({"Cama Sommier":self.spnBx_Cama_Sommier.text()})
        datos.update({"Cama Simple":self.spnBX_Cama_Simple.text()})
        datos.update({"Cama Cucheta":self.snpBx_Cama_Cucheta.text()})
        #Formateo e impresion de los datos
        for x,y in datos.items():
            if x == "DIRECCION":
                print("=============DIRECCION=============")
            elif x == "AMBIENTE":
                print("=============AMBIENTE=============")
            elif x == "CAMAS":
                print("=============CAMAS=============")
            else:
                print(f"{x}:{y}")
def main():

    app = QApplication(sys.argv)
    ventana = ClaseFormularioHogar()
    ventana.show()
    app.exec()

if __name__ == "__main__":
    main()