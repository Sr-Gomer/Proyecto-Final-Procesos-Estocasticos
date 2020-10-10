#Copiar el el script y no el .py, El .py lo llaman igual que su juego 

import sys,re
from PyQt5 import uic, QtWidgets, QtGui

from PyQt5.QtWidgets import QMessageBox
from Juego1.BaseCode import RuletaClass 

uiFile = "./" +__package__+ "./ruletaui.ui" # Nombre del archivo aquí. Debe estar en la misma carpeta
ruedaImage ="./"+__package__+ "./imagenejemplo.png"
Ui_MainWindow, QtBaseClass = uic.loadUiType(uiFile)


class UIWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Mijuego= RuletaClass(self.showmessage)
        self.img = QtGui.QPixmap(ruedaImage) # carga la imagen
        self._imagen.setPixmap(self.img) #Le pone la imagen al label
        self._Lanzar.clicked.connect(self.Lanzar)#Conecta el boton a el metodo

        self._mod.currentIndexChanged.connect(self.MakeCurrentWidgetVisible)
        self.MakeCurrentWidgetVisible()
        self.UpdateData()
    def Lanzar(self):
        if self.isInputANumber() == True:
            if self.Mijuego.Saldo >= int(str(self._valorApostar.text())):
                print(int(str(self._valorApostar.text())))
                if self._mod.currentIndex() == 0:
                    self.Mijuego.Lanzar(self._mod.currentIndex(),self._numerospinbox.value(),int(str(self._valorApostar.text())))
                elif self._mod.currentIndex() == 1:
                    self.Mijuego.Lanzar(self._mod.currentIndex(),self._colores.currentIndex(),int(str(self._valorApostar.text())))
                elif self._mod.currentIndex() == 2 or self._mod.currentIndex() == 3 :
                    self.Mijuego.Lanzar(self._mod.currentIndex(),0,int(str(self._valorApostar.text())))
                elif self._mod.currentIndex() == 4:
                    self.Mijuego.Lanzar(self._mod.currentIndex(),self._opciones.currentIndex(),int(str(self._valorApostar.text())))
                self.UpdateData()
                
            else:
                QMessageBox.about(self, "Insuficiente dinero", "No posee el saldo suficiente")
                
    def isInputANumber(self):#Checa si el input es un número
        self.toReturn : bool
        try:
            int(str(self._valorApostar.text()))
            self.toReturn = True
        except:
            QMessageBox.about(self, "Error", "El valor ingresado es incorrecto asegurate de que sea un numero entero")
            self.toReturn = False
        return self.toReturn

    def UpdateData(self):
        print("money " + str(self.Mijuego.getSaldo()))
        self._saldotexto.setText(str(self.Mijuego.getSaldo()))
    
    def MakeCurrentWidgetVisible(self):
        self._numerospinbox.setHidden(True)
        self._opciones.setHidden(True)
        self._colores.setHidden(True)

        if self._mod.currentIndex() == 0:
            self._numerospinbox.setHidden(False)
        elif self._mod.currentIndex() == 1:
            self._colores.setHidden(False)
        elif self._mod.currentIndex() == 2 or self._mod.currentIndex() == 3 :
            pass
        elif self._mod.currentIndex() == 4:
            self._opciones.setHidden(False)

    def showmessage(self,text):
        QMessageBox.about(self, "Success", text)

def Run():
    app =  QtWidgets.QApplication(sys.argv)
    window = UIWindow()
    window.show()
    sys.exit(app.exec_())
    

# Run()#Descomentar esta linea cuando se quiera probar individualmente.