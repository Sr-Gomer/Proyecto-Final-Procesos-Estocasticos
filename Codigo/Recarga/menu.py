# -*- coding: utf-8 -*-
import sys,re
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase,QSqlQuery, QSqlTableModel
import ctypes
import bd
qtCreatorFile ="./"+__package__+ "./menu.ui" # Nombre del archivo qt aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
#valodacion de conexion a la base de datos
        self.dinero=float(bd.traerValor())
        self.saldo.setText(str(self.dinero))
        print(self.dinero)
        self.botonganancia.clicked.connect(self.recargando)
        self.eliminar.clicked.connect(self.eliminacion)
        self.dinero=float(bd.traerValor())
        self.saldo.setText(str(self.dinero))

    def recargando(self):
        self.total_transaccion=int(self.entradaganancia.toPlainText())
        self.dinero=float(bd.traerValor())
        self.total=self.dinero+self.total_transaccion
        bd.recargar(self.total)
        #recargar(total_transaccion)
        self.dinero=float(bd.traerValor())
        self.saldo.setText(str(self.dinero))

    def eliminacion(self):
        bd.reiniciar()
        self.dinero=float(bd.traerValor())
        self.saldo.setText(str(self.dinero))


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())