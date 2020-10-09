import sys,re
from PyQt5 import uic, QtWidgets, QtGui

from PyQt5.QtWidgets import QMessageBox
from PIL import Image
qtCreatorFile = "./Interfaz_Principal/Main.ui" # Nombre del archivo aquí.
plotImg = './Interfaz_Principal/Captura.jpg'
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

from Juego4 import SuperTragaPerras
from Juego5 import CapsUI




class MainW(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.showMaximized()
        
        self.imagen.setText("aaaaaaa")
        myimg = QtGui.QPixmap(plotImg)
        self.imagen.setPixmap(myimg)
        self.Juego4.clicked.connect(self.runjuego4)
        self.Juego5.clicked.connect(self.runjuego5)
    def runjuego4(self):
        self.window = SuperTragaPerras.UIWindow()
        self.window.show()
    def runjuego5(self):
        self.window = CapsUI.UIWindow()
        self.window.show()


if __name__ == "__main__": 
    app =  QtWidgets.QApplication(sys.argv)
    window = MainW()
    window.show()
    sys.exit(app.exec_())