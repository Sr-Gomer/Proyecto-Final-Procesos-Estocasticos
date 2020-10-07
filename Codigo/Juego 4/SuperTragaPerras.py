#Copiar el el script y no el .py, El .py lo llaman igual que su juego 

import sys,re
from PyQt5 import uic, QtWidgets, QtGui

from PyQt5.QtWidgets import QMessageBox
from ..tst import *
from Tragaperras import JuegoTragaperras
uiFile = "./SuperTragaperrasUltimateEdition.ui" # Nombre del archivo aquí. Debe estar en la misma carpeta

Ui_MainWindow, QtBaseClass = uic.loadUiType(uiFile)


class UIWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self._apostar.clicked.connect(self.printapostar)
        self._nseleccionado.currentIndexChanged.connect(self.comboboxChanged)
        self.comboboxChanged()
        self.migame = JuegoTragaperras()
        self.migame.hahaprintxd()
        test()
        #creo el juego

    def comboboxChanged(self):
        self._cuota.setText(str(self._nseleccionado.currentIndex()))
    def printapostar(self):
        self._saldo.setText(str(self._modalidad.currentIndex() + self._nseleccionado.currentIndex()+2))

        

def Run():
    app =  QtWidgets.QApplication(sys.argv)
    window = UIWindow()
    window.show()
    sys.exit(app.exec_())
    

Run()#Descomentar esta linea cuando se quiera probar individualmente.