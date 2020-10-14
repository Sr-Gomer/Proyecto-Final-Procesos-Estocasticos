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
qtCreatorFile = "./" +__package__+"./Lootbox.ui" # Nombre del archivo qt aquí.
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
            self.setTier_Costo(1,150000)
        elif(self.rbtnTier2.isChecked() == True):
            self.setTier_Costo(2,200000)
        elif(self.rbtnTier3.isChecked() == True):
            self.setTier_Costo(3,250000)
        elif(self.rbtnTier4.isChecked() == True):
            self.setTier_Costo(4,350000)  
        elif(self.rbtnTier5.isChecked() == True):
            self.setTier_Costo(5,450000)
        self.hasmoney()

    def Play(self,tier, costo, dinero):
        self.dinero -= costo
        self.lootBox = np.array([1, 2, 2, 3, 3, 3])
        self.ganancia = 0        
        self.CAoro = 6
        self.CAplata = 3

        self.profitOro = costo * self.CAoro
        self.profitPlata = costo * self.CAplata
        self.ResetUi()
        for i in range(tier):
          self.shot = rnd.randint(0, 6)
          if self.lootBox[self.shot] == 1:
            self.ganancia += self.profitOro
            self.triunfo = "Ganaste el premio de oro!"
            self.ShowResultLbl(i+1,self.triunfo)
          elif self.lootBox[self.shot] == 2:
            self.ganancia += self.profitPlata
            self.triunfo = "Ganaste el premio de plata!"
            self.ShowResultLbl(i+1,self.triunfo)
          elif self.lootBox[self.shot] == 3:
            self.ganancia += 0
            self.triunfo = "Ganaste el premio de bronce!"
            self.ShowResultLbl(i+1,self.triunfo)
        
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