#Copiar el el script y no el .py, El .py lo llaman igual que su juego 

import sys,re
from PyQt5 import uic, QtWidgets, QtGui

from PyQt5.QtWidgets import QMessageBox
from BaseCode import RuletaClass as Ruleta

uiFile = "./ruletaui.ui" # Nombre del archivo aquí. Debe estar en la misma carpeta
ruedaImage = "./imagenejemplo.png"
Ui_MainWindow, QtBaseClass = uic.loadUiType(uiFile)


class UIWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.img = QtGui.QPixmap(ruedaImage) # carga la imagen
        self._imagen.setPixmap(self.img) #Le pone la imagen al label
        self._Lanzar.clicked.connect(self.ejemplobotonprint)#Conecta el boton a el metodo
    def ejemplobotonprint(self):
        print("Hola mundo")

def Run():
    app =  QtWidgets.QApplication(sys.argv)
    window = UIWindow()
    window.show()
    sys.exit(app.exec_())
    

Run()#Descomentar esta linea cuando se quiera probar individualmente.