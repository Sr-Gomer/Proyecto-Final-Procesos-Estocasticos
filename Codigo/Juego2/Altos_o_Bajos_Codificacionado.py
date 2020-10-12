# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:56:43 2020

@author: Andrew
"""

import sys,re 

if __name__ == "__main__":
    sys.path.append("..")


import bd

from Juego2.AltosBajos import *
import numpy as np
import numpy.random as rnd
from PyQt5 import QtCore, QtGui, QtWidgets
class MainWindow(QtWidgets.QDialog, Ui_Dialog):
    
    dineroBase = bd.traerValor() #Con esto se van a hacer las operaciones del saldo
    def __init__(self, *args, **kwargs): #Al iniciar la ventana
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton.setText("Jugar")
        self.Apuesta.setText("Inserte la cantidad de su apuesta")
        self.Altos.isChecked()
        self.pushButton.clicked.connect(self.EscogerModalidad)
        self.SaldoLabel.setText(str(self.dineroBase))

    def EscogerModalidad(self): #Revisa la lista de moalidades al presionar el botón
        modalidad = self.Modalidad.currentIndex() 
        if modalidad==0:
            self.Modalidad_1()
        elif modalidad==1:
            self.Modalidad_2()
        elif modalidad==2:
            self.Modalidad_3()
        elif modalidad==3:
            self.Modalidad_4()
        elif modalidad==4:
            self.Modalidad_5()
    
    def Modalidad_1(self): #Todas las modalidades tienen la misma estructura que esta
        dinero = float(self.Apuesta.text()) #Valor de la apuesta insertado por el usuario
        
        if dinero < 10000 or dinero > 20000 or dinero>bd.traerValor(): #Limite de apuesta por modalidad
            dineroCambio = self.dineroBase
            self.Apuesta.setText("Inserte una apuesta Valida")
            return dineroCambio
        else:
            if self.Altos.isChecked():
                apuesta = 1    
                
            elif self.Bajos.isChecked():
                apuesta = 0
                
            v=rnd.randint(1,101,1) #Número aleatorio para verificar si el núero que salió es alto o bajo
            if apuesta == 0:# bajos
                
                if v <= 50:
                    dg=dinero*(1/0.5)
                    dineroCambio=self.dineroBase+(dg-dinero)   
                    self.label.setText("Ganaste")
                else:
                    dg=0
                    #dineroCambio=(dg-dinero)
                    dineroCambio=self.dineroBase+(dg-dinero)
                    self.label.setText("Perdiste")
            elif apuesta == 1: # altos
                if v >= 51:
                    dg=dinero*(1/0.5)
                    #dineroCambio=(dg-dinero)
                    dineroCambio=self.dineroBase+(dg-dinero)
                    self.label.setText("Ganaste")
                else:       
                    dg=0
                    #dineroCambio=(dg-dinero)
                    dineroCambio=self.dineroBase+(dg-dinero)
                    self.label.setText("Perdiste")
                    
        self.ResultadoLabel.setText(str(v)) #Actualziar los datos en la interface
        self.SaldoLabel.setText(str(dineroCambio))
        self.GananciaLabel.setText(str(dg-dinero))
        self.ActualizarDinero(dineroCambio,(dg-dinero))
        
    def Modalidad_2(self):
        dinero = float(self.Apuesta.text())
        
        if dinero < 20000 or dinero > 30000 or dinero>bd.traerValor():
            dineroCambio = self.dineroBase
            self.Apuesta.setText("Inserte una apuesta Valida")
            return dineroCambio
        else:
            if self.Altos.isChecked():
                apuesta = 1    
                
            elif self.Bajos.isChecked():
                apuesta = 0
                
            v=rnd.randint(1,101,1)
            if apuesta == 0:# bajos
                
                if v <= 35:
                    dg=dinero*(1/0.35)
                    dineroCambio=self.dineroBase+(dg-dinero)   
                    self.label.setText("Ganaste")
                else:
                    dg=0
                    #dineroCambio=(dg-dinero)
                    dineroCambio=self.dineroBase+(dg-dinero)
                    self.label.setText("Perdiste")
            elif apuesta == 1: # altos
                if v >= 76:
                    dg=dinero*(1/0.35)
                    #dineroCambio=(dg-dinero)
                    dineroCambio=self.dineroBase+(dg-dinero)
                    self.label.setText("Ganaste")
                else:       
                    dg=0
                    #dineroCambio=(dg-dinero)
                    dineroCambio=self.dineroBase+(dg-dinero)
                    self.label.setText("Perdiste")
                    
        self.ResultadoLabel.setText(str(v))
        self.SaldoLabel.setText(str(dineroCambio))
        self.GananciaLabel.setText(str(dg-dinero))
        self.ActualizarDinero(dineroCambio,(dg-dinero))
    
    def Modalidad_3(self):
        dinero = float(self.Apuesta.text())
        
        if dinero < 30000 or dinero > 40000 or dinero>bd.traerValor():
            dineroCambio = self.dineroBase
            self.Apuesta.setText("Inserte una apuesta Valida")
            return dineroCambio
        else:
            if self.Altos.isChecked():
                apuesta = 1    
                
            elif self.Bajos.isChecked():
                apuesta = 0
                
            v=rnd.randint(1,101,1)
            if apuesta == 0:# bajos
                
                if v <= 20:
                    dg=dinero*(1/0.20)
                    dineroCambio=self.dineroBase+(dg-dinero)   
                    self.label.setText("Ganaste")
                else:
                    dg=0
                    #dineroCambio=(dg-dinero)
                    dineroCambio=self.dineroBase+(dg-dinero)
                    self.label.setText("Perdiste")
            elif apuesta == 1: # altos
                if v >= 81:
                    dg=dinero*(1/0.2)
                    #dineroCambio=(dg-dinero)
                    dineroCambio=self.dineroBase+(dg-dinero)
                    self.label.setText("Ganaste")
                else:       
                    dg=0
                    #dineroCambio=(dg-dinero)
                    dineroCambio=self.dineroBase+(dg-dinero)
                    self.label.setText("Perdiste")
                    
        self.ResultadoLabel.setText(str(v))
        self.SaldoLabel.setText(str(dineroCambio))
        self.GananciaLabel.setText(str(dg-dinero))
        self.ActualizarDinero(dineroCambio,(dg-dinero))
    
    def Modalidad_4(self):
        dinero = float(self.Apuesta.text())
        
        if dinero < 40000 or dinero > 50000 or dinero>bd.traerValor():
            dineroCambio = self.dineroBase
            self.Apuesta.setText("Inserte una apuesta Valida")
            return dineroCambio
        else:
            if self.Altos.isChecked():
                apuesta = 1    
                
            elif self.Bajos.isChecked():
                apuesta = 0
                
            v=rnd.randint(1,101,1)
            if apuesta == 0:# bajos
                
                if v <= 10:
                    dg=dinero*(1/0.10)
                    dineroCambio=self.dineroBase+(dg-dinero)   
                    self.label.setText("Ganaste")
                else:
                    dg=0
                    #dineroCambio=(dg-dinero)
                    dineroCambio=self.dineroBase+(dg-dinero)
                    self.label.setText("Perdiste")
            elif apuesta == 1: # altos
                if v >= 91:
                    dg=dinero*(1/0.10)
                    #dineroCambio=(dg-dinero)
                    dineroCambio=self.dineroBase+(dg-dinero)
                    self.label.setText("Ganaste")
                else:       
                    dg=0
                    #dineroCambio=(dg-dinero)
                    dineroCambio=self.dineroBase+(dg-dinero)
                    self.label.setText("Perdiste")
        
        self.ResultadoLabel.setText(str(v))            
        self.SaldoLabel.setText(str(dineroCambio))
        self.GananciaLabel.setText(str(dg-dinero))
        self.ActualizarDinero(dineroCambio,(dg-dinero))
    
    def Modalidad_5(self):
        dinero = float(self.Apuesta.text())
        
        if dinero < 50000 or dinero>bd.traerValor():
            dineroCambio = self.dineroBase
            self.Apuesta.setText("Inserte una apuesta Valida")
            return dineroCambio
        else:
            if self.Altos.isChecked():
                apuesta = 1    
                
            elif self.Bajos.isChecked():
                apuesta = 0
                
            v=rnd.randint(1,101,1)
            if apuesta == 0:# bajos
                
                if v <= 5:
                    dg=dinero*(1/0.05)
                    dineroCambio=self.dineroBase+(dg-dinero)   
                    self.label.setText("Ganaste")
                else:
                    dg=0
                    #dineroCambio=(dg-dinero)
                    dineroCambio=self.dineroBase+(dg-dinero)
                    self.label.setText("Perdiste")
            elif apuesta == 1: # altos
                if v >= 96:
                    dg=dinero*(1/0.05)
                    #dineroCambio=(dg-dinero)
                    dineroCambio=self.dineroBase+(dg-dinero)
                    self.label.setText("Ganaste")
                else:       
                    dg=0
                    #dineroCambio=(dg-dinero)
                    dineroCambio=self.dineroBase+(dg-dinero)
                    self.label.setText("Perdiste")
                    
        self.ResultadoLabel.setText(str(v))
        self.SaldoLabel.setText(str(dineroCambio))
        self.GananciaLabel.setText(str(dg-dinero))
        self.ActualizarDinero(dineroCambio,(dg-dinero))
        
    def ActualizarDinero(self,dineroNuevo,cambioDinero):
        if (dineroNuevo<0):
            self.dineroBase = 0
            self.SaldoLabel.setText(str(self.dineroBase))
            bd.insertarDatos(self.dineroBase,cambioDinero)
        else:
            self.dineroBase = dineroNuevo
            bd.insertarDatos(self.dineroBase,cambioDinero)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
#Esto existe