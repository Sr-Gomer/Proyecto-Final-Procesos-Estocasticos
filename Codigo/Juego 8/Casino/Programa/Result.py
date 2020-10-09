# -*- coding: utf-8 -*-
"""
Created on Domingo 4 de Octubre

@author: José Manuel Gutiérrez Sosa (Mechas)
"""
import sys,re
import numpy as np
from PyQt5 import uic, QtWidgets, QtGui

from PyQt5.QtWidgets import QMessageBox


prize = sys.argv[1]
Disco1 = np.array([sys.argv[2],sys.argv[3],sys.argv[4]])
Disco2 = np.array([sys.argv[5],sys.argv[6],sys.argv[7]])
Disco3 = np.array([sys.argv[8],sys.argv[9],sys.argv[10]])
Disco4 = np.array([sys.argv[11],sys.argv[12],sys.argv[13]])
Disco5 = np.array([sys.argv[14],sys.argv[15],sys.argv[16]])
mensaje = sys.argv[17]
Mensaje = mensaje.replace("@"," ")


    
uiFile = "./jackpotResult.ui" # Nombre del archivo aquí. Debe estar en la misma carpeta

Ui_MainWindow, QtBaseClass = uic.loadUiType(uiFile)


class UIWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnClose.clicked.connect(self.Cerrar)
        self.lbCantCreditosWin.setText("%s Pesos"%prize)
        self.lbWinOrLose.setText(""+Mensaje)
        self.lb11.setText(Disco1[0])
        self.lb12.setText(Disco1[1])
        self.lb13.setText(Disco1[2])
        
        self.lb21.setText(Disco2[0])
        self.lb22.setText(Disco2[1])
        self.lb23.setText(Disco2[2])
        
        self.lb31.setText(Disco3[0])
        self.lb32.setText(Disco3[1])
        self.lb33.setText(Disco3[2])
        
        self.lb41.setText(Disco4[0])
        self.lb42.setText(Disco4[1])
        self.lb43.setText(Disco4[2])
        
        self.lb51.setText(Disco5[0])
        self.lb52.setText(Disco5[1])
        self.lb53.setText(Disco5[2])
    def Cerrar(self):
        self.close()
        
      
        


def Run():
    app =  QtWidgets.QApplication(sys.argv)
    window = UIWindow()
    window.show()
    sys.exit(app.exec_())
    
    

Run()#Descomentar esta linea cuando se quiera probar individualmente.