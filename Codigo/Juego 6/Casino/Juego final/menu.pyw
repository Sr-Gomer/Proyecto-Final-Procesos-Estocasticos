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
        #self.showMaximized()

    #def showEvent(self,event):


    # def validar_ganancia(self):
    #     entradaganancia=self.entradaganancia.text()
    #     validar=re.match('0-9-[.]',entradaganancia,re.I)

    # def validar_perdida(self):
    #     validar=re.match('0-9-[.]',entradaperdida,re.I)
    #     entradaperdida=self.entradaperdida.text()

#establecer conexion con la base de datos



#valodacion de conexion a la base de datos
        dinero=traerValor()
        print(dinero)
        #self.showMaximized()
        #self.bienvenida.setText(traerValor())
        total_transaccion=12265.124
        detalle_transacion=-56.0
        #valores=insertarDatos(total_transaccion,detalle_transacion)
        self.botonganancia.clicked.connect(lambda: insertarDatos(total_transaccion,detalle_transacion))



if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())