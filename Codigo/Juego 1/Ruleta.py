# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 21:03:53 2020

@author: HP
"""
import sys,re
from PyQt5 import uic, QtWidgets, QtGui

from PyQt5.QtWidgets import QMessageBox

uiFile = "Interface1.ui" # Nombre del archivo aquí. Debe estar en la misma carpeta
Ui_Dialog, QtBaseClass = uic.loadUiType(uiFile)


class UIWindow(QtWidgets.QDialog, Ui_Dialog):
    def init(self):
        QtWidgets.QMainWindow.init(self)
        Ui_Dialog.init(self)
        self.setupUi(self)
       
def Run():
    app =  QtWidgets.QApplication(sys.argv)
    window = UIWindow()
    window.show()
    sys.exit(app.exec())
    
Run() 