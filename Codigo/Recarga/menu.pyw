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
#valodacion de conexion a la base de datos
        dinero=float(traerValor())
        self.saldo.setText(str(dinero))
        print(dinero)
        self.botonganancia.clicked.connect(self.recargando)
        self.eliminar.clicked.connect(self.eliminacion)
        dinero=float(traerValor())
        self.saldo.setText(str(dinero))

    def recargando(self):
        total_transaccion=int(self.entradaganancia.toPlainText())
        dinero=float(traerValor())
        total=dinero+total_transaccion
        recargar(total)
        #recargar(total_transaccion)
        dinero=float(traerValor())
        self.saldo.setText(str(dinero))

    def eliminacion(self):
        reiniciar()
        dinero=float(traerValor())
        self.saldo.setText(str(dinero))


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())