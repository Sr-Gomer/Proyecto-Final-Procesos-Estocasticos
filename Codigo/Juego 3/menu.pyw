import sys,re
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase,QSqlQuery, QSqlTableModel
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
import ctypes
from bd import *
#from Funciones import *
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
        #print("init {}".format(dinero))
        
        self.btnPlay.clicked.connect(self.Verify)

    def Verify(self):
        dinero=float(traerValor())
        #print("verify {}".format(dinero))
        
        if(self.rbtnTier1.isChecked() == True):
            tier = 1
            costo = 30
            if(dinero >= costo):
                self.Play(tier, costo, dinero)
                #self.informacion.setText()
            else:
                self.informacion.setText("Recarga tu saldo!")
                
        elif(self.rbtnTier2.isChecked() == True):
            tier = 2
            costo = 70
            if(dinero >= costo):
                self.Play(tier, costo, dinero)
            else:
                self.informacion.setText("Recarga tu saldo!")
                
        elif(self.rbtnTier3.isChecked() == True):
            tier = 3
            costo = 250000
            if(dinero >= costo):
                self.Play(tier, costo, dinero)
            else:
                self.informacion.setText("Recarga tu saldo!")
                
        elif(self.rbtnTier4.isChecked() == True):
            tier = 4
            costo = 350000
            if(dinero >= costo):
                self.Play(tier, costo, dinero)
            else:
                self.informacion.setText("Recarga tu saldo!")
                
        elif(self.rbtnTier5.isChecked() == True):
            tier = 5
            costo = 450000
            if(dinero >= costo):
                self.Play(tier, costo, dinero)
            else:
                self.informacion.setText("Recarga tu saldo!")

    def Play(self,tier, costo, dinero):
            # print("soy la funcion",tier)
        # print("soy la funcion",dinero)
        # print("soy la funcion",costo)
        dinero -= costo
        print("dinero - costo {}".format(dinero))
        
        lootBox = np.array([1, 2, 2, 3, 3, 3])
        ganancia = 0
        print("loot",lootBox.size)
        #saldo = traerValor()
        
        CAoro = 1 / (1 / lootBox.size)
        CAplata = 1 / (2 / lootBox.size)

        profitOro = costo * CAoro
        print("profitoro {}".format(profitOro))
        profitPlata = costo * CAplata
        print("profitplata {}".format(profitPlata))

        for i in range (tier):
          shot = rnd.randint(0, 6)
          print(lootBox[shot])

          if lootBox[shot] == 1:
            ganancia += profitOro
            print("ganancia {}".format(ganancia))
            #dinero += profitOro
            print("dinero + profit {}".format(dinero))
            triunfo = "Ganaste el premio de oro!"
            print("Ganaste el premio de oro")

          elif lootBox[shot] == 2:
            ganancia += profitPlata
            print("ganancia {}".format(ganancia))
            #dinero += profitPlata
            triunfo = "Ganaste el premio de plata!"
            print("dinero + profit {}".format(dinero))
            print("Ganaste el premio de plata")

          elif lootBox[shot] == 3:
            #dinero += 0
            triunfo = "Ganaste el premio de bronce!"
            print("dinero + profit {}".format(dinero))
            print("Ganaste el premio de bronce")
            
        #totalGanancias = 
        #1 2 2 1 3 === oros*2 + 0 + platas*2
        self.ganancia.setText(str(ganancia))
            
        dinero=float(traerValor())
        self.saldoTotal.setText(str(dinero))
        print("init {}".format(dinero))


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())