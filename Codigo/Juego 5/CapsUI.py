#Copiar el el script y no el .py, El .py lo llaman igual que su juego 

import sys,re
from PyQt5 import uic, QtWidgets, QtGui

from PyQt5.QtWidgets import QMessageBox

from Craps import juego
uiFile = "./UI_Caps.ui" # Nombre del archivo aquí. Debe estar en la misma carpeta

Ui_MainWindow, QtBaseClass = uic.loadUiType(uiFile)


class UIWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self._apuesta.clicked.connect(self.comboboxChanged)
        self.comboboxChanged()
        self.migame = juego()
        self._saldo.setText(self.migame._dineroActual)
        
    def printApostar(self):
        self.migame.Apostar(self._modalidad.currentIndex()+1)
        self._transaccion.setText(str(self.migame.transaccion))
        self._dineroActual.setText(str(self.migame.saldo))
        self._resultadoDado1.setText(self.migame.dado1)
        self._resultadoDado2.setText(self.migame.dado2)

def Run():
    app =  QtWidgets.QApplication(sys.argv)
    window = UIWindow()
    window.show()
    sys.exit(app.exec_())
    

Run()#Descomentar esta linea cuando se quiera probar individualmente.