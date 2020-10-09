import sys,re
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase,QSqlQuery, QSqlTableModel
import ctypes
qtCreatorFile = "lootbox.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #self.showMaximized()

    #def showEvent(self,event):


    # def validar_ganancia(self):
    #     entradaganancia=self.entradaganancia.text()
    #     validar=re.match('0-9-[.]',entradaganancia,re.I)

    # def validar_perdida(self):
    #     validar=re.match('0-9-[.]',entradaperdida,re.I)
    #     entradaperdida=self.entradaperdida.text()

def Run(): 
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

Run()