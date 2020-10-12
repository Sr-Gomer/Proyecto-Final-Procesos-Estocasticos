# -*- coding: utf-8 -*-
"""
Created on Domingo 4 de Octubre

@author: José Manuel Gutiérrez Sosa (Mechas)
"""

import sys,re
import os
import numpy as np

from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from Juego8 import JackpotGame
_1afile = "./" +__package__+ "./Fotos/1a.png"
_1bfile = "./" +__package__+ "./Fotos/1b.png"
_1cfile = "./" +__package__+ "./Fotos/1c.png"
_2afile = "./" +__package__+ "./Fotos/2a.png"
_2bfile = "./" +__package__+ "./Fotos/2b.png"
_3afile = "./" +__package__+ "./Fotos/3a.png"
_3bfile = "./" +__package__+ "./Fotos/3b.png"
_4afile = "./" +__package__+ "./Fotos/4a.png"
_4bfile = "./" +__package__+ "./Fotos/4b.png"

uiFile = "./" +__package__+ "./jackpotMain.ui" # Nombre del archivo aquí. Debe estar en la misma carpeta

Ui_MainWindow, QtBaseClass = uic.loadUiType(uiFile)
if __name__ == "__main__":
    sys.path.append("..")
    

class UIWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnPlay.clicked.connect(self.obtener)
        self.juego = JackpotGame.Juegojackpot(self.setMsg)

        self._1aimg = QtGui.QPixmap(_1afile)
        self._1bimg = QtGui.QPixmap(_1bfile)
        self._1cimg = QtGui.QPixmap(_1cfile)
        self._2aimg = QtGui.QPixmap(_2afile)
        self._2bimg = QtGui.QPixmap(_2bfile)
        self._3aimg = QtGui.QPixmap(_3afile)
        self._3bimg = QtGui.QPixmap(_3bfile)
        self._4aimg = QtGui.QPixmap(_4afile)
        self._4bimg = QtGui.QPixmap(_4bfile)

        self._cb1aimg.setPixmap(self._1aimg)
        self._cb1bimg.setPixmap(self._1bimg)
        self._cb1cimg.setPixmap(self._1cimg)
        self._cb2aimg.setPixmap(self._2aimg)
        self._cb2bimg.setPixmap(self._2bimg)
        self._cb3aimg.setPixmap(self._3aimg)
        self._cb3bimg.setPixmap(self._3bimg)
        self._cb4aimg.setPixmap(self._4aimg)
        self._cb4bimg.setPixmap(self._4bimg)
        self.ShowResultado()
        
    def obtener(self):
        if float(self.lbCantCreditos.text().split()[0]) < self.sbCreditosApostar.value()*1000 :
            self.setMsg("Error","Debes tener saldo suficiente para jugar")
            return
        self.prize = self.juego.Jugar(self.cb1A.isChecked(),self.cb1B.isChecked(),self.cb1C.isChecked(),self.cb2A.isChecked(),self.cb2B.isChecked(),self.cb3A.isChecked(),self.cb3B.isChecked(),self.cb4A.isChecked(),self.cb4B.isChecked(),self.sbCreditosApostar.value())
        if self.prize == 0:
            # print("CRASHEO")
            return
        self.ShowResultado()
        self.ShowEndResult()
        # self.lbCantCreditos.setText("%s Pesos"%(float(self.lbCantCreditos.text().split()[0])+prize))#Saldo

    def setMsg(self,titulo,texto):
        QMessageBox.about(self,titulo, texto)
    def ShowEndResult(self):
        self.m,self.g = self.juego.getResults()
        self.lbWinOrLose.setText(str(self.m))
        self.lbCantCreditosWin.setText(str(self.g))
        pass
    def ShowResultado(self):
        self.Discos,self.s = self.juego.getInfo()
        self.lbCantCreditos.setText(str(self.s))
        
        self.lb11.setText(self.Discos[0][0])
        self.lb12.setText(self.Discos[0][1])
        self.lb13.setText(self.Discos[0][2])
        
        self.lb21.setText(self.Discos[1][0])
        self.lb22.setText(self.Discos[1][1])
        self.lb23.setText(self.Discos[1][2])
        
        self.lb31.setText(self.Discos[2][0])
        self.lb32.setText(self.Discos[2][1])
        self.lb33.setText(self.Discos[2][2])
        
        self.lb41.setText(self.Discos[3][0])
        self.lb42.setText(self.Discos[3][1])
        self.lb43.setText(self.Discos[3][2])
        
        self.lb51.setText(self.Discos[4][0])
        self.lb52.setText(self.Discos[4][1])
        self.lb53.setText(self.Discos[4][2])
        # self.lbCantCreditosWin.setText("%s Pesos"%prize)
        # self.lbWinOrLose.setText(""+Mensaje)
    
        

def Run():
    os.system("MessageBox.py %s"%("Cada Credito apostado tiene un valor de 200 Pesos"))
    app =  QtWidgets.QApplication(sys.argv)
    window = UIWindow()
    window.show()
    sys.exit(app.exec_())
# Run()
#Descomentar esta linea cuando se quiera probar individualmente.