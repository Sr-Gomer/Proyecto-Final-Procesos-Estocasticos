# -*- coding: utf-8 -*-
"""
Created on Domingo 4 de Octubre

@author: José Manuel Gutiérrez Sosa (Mechas)
"""

import sys,re
import numpy as np
from PyQt5 import uic, QtWidgets, QtGui

message=""
sys.argv.pop(0)
for x in sys.argv:
    
    message += x + " "

from PyQt5.QtWidgets import QMessageBox

uiFile = "./MEssageBox.ui" # Nombre del archivo aquí. Debe estar en la misma carpeta

Ui_MainWindow, QtBaseClass = uic.loadUiType(uiFile)


class UIWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.label.setText(message)
        self.btnCerrar.clicked.connect(self.Cerrar)
    def Cerrar(self):
        self.close()
        
        
def Run():
    app =  QtWidgets.QApplication(sys.argv)
    window = UIWindow()
    window.show()
    sys.exit(app.exec_())
    
    

Run()#Descomentar esta linea cuando se quiera probar individualmente.