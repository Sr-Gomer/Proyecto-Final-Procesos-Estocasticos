import sys,re
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase,QSqlQuery, QSqlTableModel
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
import ctypes
import bd
#from Funciones import *
import numpy as np
import numpy.random as rnd
imgbox = "./" + __package__ +"./Lootbox.png"
qtCreatorFile = /Lootbox.ui" # Nombre del archivo qt aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.dinero = 0
        self.ganancia = 0
        self.actualizarSaldo()
        self.btnPlay.clicked.connect(self.Verify)
        self.tier = 0
        self.costo = 0
        self.img = QtGui.QPixmap(imgbox) # carga la imagen
        self._img.setPixmap(self.img) #Le pone la imagen al label
        self.ResetUi()

    def actualizarSaldo(self):
        self.dinero=float(bd.traerValor())
        self.saldoTotal.setText(str(self.dinero))

    def setTier_Costo(self,_tier,_costo):
        self.tier = _tier
        self.costo = _costo

    def hasmoney(self):
        if(self.dinero >= self.costo):
            self.Play(self.tier, self.costo, self.dinero)
        else:
            self.informacion.setText("Recarga tu saldo!")
    def Verify(self):
        self.actualizarSaldo()
        if(self.rbtnTier1.isChecked() == True):
            self.setTier_Costo(1,15000)
        elif(self.rbtnTier2.isChecked() == True):
            self.setTier_Costo(2,25000)
        elif(self.rbtnTier3.isChecked() == True):
            self.setTier_Costo(3,40000)
        elif(self.rbtnTier4.isChecked() == True):
            self.setTier_Costo(4,55000) 
        elif(self.rbtnTier5.isChecked() == True):
            self.setTier_Costo(5,70000)
        self.hasmoney()

    def Play(self,tier, costo, dinero):
        self.dinero -= costo
        self.ganancia = 0
        self.CAoro = 20
        self.CAplata = 4

        self.profitOro = costo * self.CAoro
        self.profitPlata = costo * self.CAplata
        self.ResetUi()
        for i in range(tier):
          self.shot = rnd.rand()
          print(str(self.shot))
          if  self.shot <= 0.05:
            self.ganancia += self.profitOro
            self.triunfo = "Ganaste el premio de oro!"
            self.ShowResultLbl(i+1,self.triunfo)
          elif self.shot <= 0.25:
            self.ganancia += self.profitPlata
            self.triunfo = "Ganaste el premio de plata!"
            self.ShowResultLbl(i+1,self.triunfo)
          else:
            self.ganancia += 0
            self.triunfo = "Ganaste el premio de bronce!"
            self.ShowResultLbl(i+1,self.triuCAoronfo)

        self.dinero += self.ganancia
        self._txtg.setText(str(self.ganancia))
        self.saldoTotal.setText(str(self.dinero))
        bd.insertarDatos(self.dinero,self.ganancia)

    def ResetUi(self):
        self.lblAnnounce1.setText("")
        self.lblAnnounce2.setText("")
        self.lblAnnounce3.setText("")
        self.lblAnnounce4.setText("")
        self.lblAnnounce5.setText("")
    def ShowResultLbl(self,index,texto):
        if index == 1:
            self.lblAnnounce1.setText(texto)
        elif index == 2:
            self.lblAnnounce2.setText(texto)
        elif index == 3:
            self.lblAnnounce3.setText(texto)
        elif index == 4:
            self.lblAnnounce4.setText(texto)
        elif index == 5:
            self.lblAnnounce5.setText(texto)

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
