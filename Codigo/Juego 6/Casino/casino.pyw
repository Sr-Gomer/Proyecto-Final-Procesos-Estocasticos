import numpy as np
import numpy.random as rnd
from winFunctions import win,lose
import sys,re


from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialog,QLabel,QTextEdit
from PyQt5.QtSql import QSqlDatabase,QSqlQuery, QSqlTableModel
from juegofinalcartas import *
import juegofinalcartas as jfc
from casino import Jugar
from bd import *
from winFunctions import diferencia



qtCreatorFile = "casino.ui" # Nombre del archivo qt aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
SALDO=0

class Dialogo(QDialog):



 def __init__(self):
  
  SALDO = traerValor()
  QDialog.__init__(self)
  uic.loadUi("opcion1.ui", self)
  self.saldoActual.setText(str(SALDO)) 
  self.butD1.clicked.connect(self.jugarCarta)
  
 def jugarCarta(self):
   
   
   SALDO = traerValor()
   
   cantidadApuesta= int(self.cantApuesta.toPlainText())
   if(cantidadApuesta<SALDO):
       
       
   
       carta = self.TD1.toPlainText()
       pinta = self.TD2.toPlainText()
       
       
       
       nuevoSaldo =float(jfc.Jugar("CARTA",carta,pinta,"carta",SALDO,cantidadApuesta))
       self.nuevoSaldo.setText(str(nuevoSaldo))
       self.Rd12.setText(str(jfc.feedback))
       detalle=diferencia(float(SALDO),float(nuevoSaldo))
       insertarDatos(nuevoSaldo,detalle)
  
   
  
   
  

class Dialogo2(QDialog):
 def __init__(self):
  
  SALDO = traerValor()
  QDialog.__init__(self)
  uic.loadUi("opcion2.ui", self)
  self.saldoActual.setText(str(SALDO)) 
  self.butD1.clicked.connect(self.jugarNumero)
  
 def jugarNumero(self):
   
   
   SALDO = traerValor()
   
   cantidadApuesta= int(self.cantApuesta.toPlainText())
   if(cantidadApuesta<SALDO):
       
       
   
       carta = self.TD1.toPlainText()
       
       
       self.Rd11.setText(carta)
       nuevoSaldo =float(jfc.Jugar("NUMEROS",carta,"carta","carta",SALDO,cantidadApuesta))
       self.nuevoSaldo.setText(str(nuevoSaldo))
       self.Rd12.setText(str(jfc.feedback))
       detalle=diferencia(float(SALDO),float(nuevoSaldo))
       
       insertarDatos(nuevoSaldo,detalle)

class Dialogo3(QDialog):
 def __init__(self):
  
  SALDO = traerValor()
  QDialog.__init__(self)
  uic.loadUi("opcion3.ui", self)
  self.saldoActual.setText(str(SALDO)) 
  self.butD1.clicked.connect(self.jugarPares)
  
 def jugarPares(self):
   
   
   SALDO = traerValor()
   
   cantidadApuesta= int(self.cantApuesta.toPlainText())
   if(cantidadApuesta<SALDO):
       
       
   
       carta = self.TD1.toPlainText()
       
       
       self.Rd11.setText(carta)
       nuevoSaldo =float(jfc.Jugar("PARES","Q","carta","carta",SALDO,cantidadApuesta))
       self.nuevoSaldo.setText(str(nuevoSaldo))
       self.Rd12.setText(str(jfc.feedback))
       detalle=diferencia(float(SALDO),float(nuevoSaldo))
       insertarDatos(nuevoSaldo,detalle)

class Dialogo4(QDialog):
 def __init__(self):
  
  SALDO = traerValor()
  QDialog.__init__(self)
  uic.loadUi("opcion4.ui", self)
  self.saldoActual.setText(str(SALDO)) 
  self.butD1.clicked.connect(self.jugarImpares)
  
 def jugarImpares(self):
   
   SALDO = traerValor()
   
   cantidadApuesta= int(self.cantApuesta.toPlainText())
   if(cantidadApuesta<SALDO):
       
       
   
       carta = self.TD1.toPlainText()
       
       
       self.Rd11.setText(carta)
       nuevoSaldo =float(jfc.Jugar("IMPARES","Q","DIAMANTES","carta",SALDO,cantidadApuesta))
       self.nuevoSaldo.setText(str(nuevoSaldo))
       self.Rd12.setText(str(jfc.feedback))
       detalle=diferencia(float(SALDO),float(nuevoSaldo))
       insertarDatos(nuevoSaldo,detalle)

class Dialogo5(QDialog):
 def __init__(self):
  
  SALDO = traerValor()
  QDialog.__init__(self)
  uic.loadUi("opcion5.ui", self)
  self.saldoActual.setText(str(SALDO)) 
  self.butD1.clicked.connect(self.jugarColor)
  
 def jugarColor(self):
   
   SALDO = traerValor()
   
   cantidadApuesta= int(self.cantApuesta.toPlainText())
   if(cantidadApuesta<SALDO):
       
       
   
       carta = self.TD1.toPlainText()
       
       
       self.Rd11.setText(carta)
       nuevoSaldo =float(jfc.Jugar("COLOR","Q","DIAMANTES",carta,SALDO,cantidadApuesta))
       self.nuevoSaldo.setText(str(nuevoSaldo))
       self.Rd12.setText(str(jfc.feedback))
       detalle=diferencia(float(SALDO),float(nuevoSaldo))
       insertarDatos(nuevoSaldo,detalle)
  
class Dialogo6(QDialog):
 def __init__(self):
  
  SALDO = traerValor()
  QDialog.__init__(self)
  uic.loadUi("opcion6.ui", self)
  self.saldoActual.setText(str(SALDO)) 
  self.butD1.clicked.connect(self.jugarPinta)
  
 def jugarPinta(self):
   
   SALDO = traerValor()
   
   cantidadApuesta= int(self.cantApuesta.toPlainText())
   if(cantidadApuesta<SALDO):
       
       
   
       carta = self.TD1.toPlainText()
       
       
       self.Rd11.setText(carta)
       nuevoSaldo =float(jfc.Jugar("PINTA","Q",carta,"carta",SALDO,cantidadApuesta))
       self.nuevoSaldo.setText(str(nuevoSaldo))
       self.Rd12.setText(str(jfc.feedback))
       detalle=diferencia(float(SALDO),float(nuevoSaldo))
       insertarDatos(nuevoSaldo,detalle)
 
        
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #self.showMaximized()
        self.butJu.clicked.connect(self.getItem)
        self.dialogo = Dialogo()
        self.dialogo2 = Dialogo2()
        self.dialogo3 = Dialogo3()
        self.dialogo4 = Dialogo4()
        self.dialogo5 = Dialogo5()
        self.dialogo6 = Dialogo6()
        
    def closeEvent(self,event):
        
        resultado = QMessageBox.question(self, "Regresar", "Seguro que quieres regresar?", QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes: event.accept()
        else: event.ignore()
    
    def getItem(self):
        item = self.opciones.currentText()
        if item == "CARTA":
            self.abrirDia()
        if item == "NUMEROS":
            self.abrirDia2()
        if item == "PARES":
            self.abrirDia3()
        if item == "IMPARES":
            self.abrirDia4()
        if item == "COLOR":
            self.abrirDia5()
        if item == "PINTA":
            self.abrirDia6()
            
    def abrirDia(self):
        
        self.dialogo.exec_()
    def abrirDia2(self):

        self.dialogo2.exec_()
    def abrirDia3(self):
        
        self.dialogo3.exec_()
    def abrirDia4(self):
        
        self.dialogo4.exec_()
    def abrirDia5(self):
        
        self.dialogo5.exec_()
    def abrirDia6(self):
        
        self.dialogo6.exec_()
        
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
        
    
    
    
    
    
    
    
    
    
    



        