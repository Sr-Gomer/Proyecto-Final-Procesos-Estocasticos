#Copiar el el script y no el .py, El .py lo llaman igual que su juego 

import sys,re
from PyQt5 import uic, QtWidgets, QtGui

from PyQt5.QtWidgets import QMessageBox

from Juego5.Modalidades_Caps import Craps
uiFile = "./" + __package__ + "./UI_Caps.ui" # Nombre del archivo aquí. Debe estar en la misma carpeta

Ui_MainWindow, QtBaseClass = uic.loadUiType(uiFile)


class UIWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self._jugar.clicked.connect(self.jugar)
        # self.comboboxChanged()
        self.migame = Craps()
        self.UpdateOptions()
        self.UpdateInfo()
        self._modalidad.currentIndexChanged.connect(self.UpdateOptions)
        # self._saldo.setText(self.migame._dineroActual)
        
    def jugar(self):
        if(self.isInputANumber()):
            print("entroaca")
            self.modalidad = self._modalidad.currentIndex() + 1
            self.b = self.migame.Apostar(self.modalidad,int(str(self._apuesta.text())),self._hop1.value,self._hop2.value)
            if(self.b == False):
                QMessageBox.about(self, "Error", "No Tienes Dinero")
            self.UpdateInfo()
                

    def isInputANumber(self):#Checa si el input es un número
        self.toReturn : bool
        try:
            int(str(self._apuesta.text()))
            print("Funciono")
            self.toReturn = True
        except:
            print("No Funciono")
            QMessageBox.about(self, "Error", "El valor ingresado es incorrecto asegurate de que sea un numero entero")
            self.toReturn = False
        return self.toReturn
    
    def UpdateOptions(self):
        if (self._modalidad.currentIndex() + 1) != 5:
            self._hopoption.setHidden(True)
        else:
            self._hopoption.setHidden(False)
    def UpdateInfo(self):
        self.s,self.t = self.migame.getData()
        self._dineroActual.setText(str(self.s))
        self._transaccion.setText(str(self.t))
        self._resultadoDado1.display(self.migame.dado1)
        self._resultadoDado2.display(self.migame.dado2)

def Run():
    app =  QtWidgets.QApplication(sys.argv)
    window = UIWindow()
    window.show()
    sys.exit(app.exec_())
    

# Run()#Descomentar esta linea cuando se quiera probar individualmente.