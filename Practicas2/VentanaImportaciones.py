# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClaseImportaciones.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ventana_Importaciones(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_Salir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Salir.setEnabled(True)
        self.btn_Salir.setGeometry(QtCore.QRect(230, 440, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_Salir.setFont(font)
        self.btn_Salir.setIconSize(QtCore.QSize(20, 20))
        self.btn_Salir.setObjectName("btn_Salir")
        self.lab_Titulo = QtWidgets.QLabel(self.centralwidget)
        self.lab_Titulo.setGeometry(QtCore.QRect(140, 40, 481, 91))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lab_Titulo.setFont(font)
        self.lab_Titulo.setObjectName("lab_Titulo")
        self.lab_Imagen = QtWidgets.QLabel(self.centralwidget)
        self.lab_Imagen.setGeometry(QtCore.QRect(170, 180, 311, 191))
        self.lab_Imagen.setText("")
        self.lab_Imagen.setObjectName("lab_Imagen")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clase importaciones"))
        self.btn_Salir.setText(_translate("MainWindow", "Salir"))
        self.lab_Titulo.setText(_translate("MainWindow", "TextLabel"))