#Copiar el el script y no el .py, El .py lo llaman igual que su juego 

import sys,re
import numpy as np
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from Juego4.Tragaperras import JuegoTragaperras

uiFile = "./Juego4/SuperTragaperrasUltimateEdition.ui" # Nombre del archivo aquí. Debe estar en la misma carpeta

Ui_MainWindow, QtBaseClass = uic.loadUiType(uiFile)


class UIWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self._apostar.clicked.connect(self.printapostar)
        self._modalidad.currentIndexChanged.connect(self.comboboxChanged)
        self.comboboxChanged()
        self.migame = JuegoTragaperras()
        self._saldo.setText(str(self.migame.saldo))
        #Insertadatos a la basededatos
        #creo el juego

    def comboboxChanged(self):
        self.cuotas = np.array([2*10000, 3*10000, 36*10000, 36*10000, 216*10000])
        self._cuota.setText(str(self.cuotas[self._modalidad.currentIndex()]))
        
    def printapostar(self):
        self.migame.Apostar(self._modalidad.currentIndex()+1, self._nseleccionado.currentIndex()+1)
        self._resultado.setText(str(self.migame.resultado))
        self._saldo.setText(str(self.migame.saldo))
        self._valorganado.setText(str(self.migame.dinGanado))
        #self._saldo.setText(str(self._modalidad.currentIndex() + self._nseleccionado.currentIndex()+2))
        
        

def Run():
    if __name__ == "__main__":
        app =  QtWidgets.QApplication(sys.argv)
    window = UIWindow()
    window.show()
    if __name__ == "__main__":
        sys.exit(app.exec_())
    

# Run()#Descomentar esta linea cuando se quiera probar individualmente.
print("Done importing")