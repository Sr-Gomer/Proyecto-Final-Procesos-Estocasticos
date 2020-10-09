import sys,re
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase,QSqlQuery, QSqlTableModel
import ctypes
from bd import *
from Funciones import *
import numpy as np
import numpy.random as rnd

qtCreatorFile = "Lootbox.ui" # Nombre del archivo qt aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        dinero=float(traerValor())
        self.saldoTotal.setText(str(dinero))

        self.btnPlay.clicked.connect(self.Verify)

    def Verify(self):
        
        
        if(self.rbtnTier1.isChecked() == True):
            tier = 1
        if(self.rbtnTier2.isChecked() == True):
            tier = 2
        if(self.rbtnTier3.isChecked() == True):
            tier = 3
        if(self.rbtnTier4.isChecked() == True):
            tier = 4
        if(self.rbtnTier5.isChecked() == True):
            tier = 5
           
        Play(tier)

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())