# -*- coding: utf-8 -*-
import sys,re
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase,QSqlQuery, QSqlTableModel
import ctypes
from bd import *
qtCreatorFile = "menu.ui" # Nombre del archivo qt aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        print(traerValor())
        #self.showMaximized()
        total_transaccion=4356
        detalle_transacion=4356
        #valores=insertarDatos(total_transaccion,detalle_transacion)
        self.botonganancia.clicked.connect(lambda: insertarDatos(total_transaccion,detalle_transacion))



if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())