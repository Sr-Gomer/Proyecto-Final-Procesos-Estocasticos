# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:56:43 2020

@author: Andrew
"""

import sys,re 

sys.path.append("..")


import bd

from AltosBajos import *
import numpy as np
import numpy.random as rnd

class MainWindow(QtWidgets.QDialog, Ui_Dialog):
    
    dineroBase = 1000
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton.setText("Jugar")
        self.Apuesta.setText("Inserte la cantidad de su apuesta")
        self.Altos.isChecked()
        self.pushButton.clicked.connect(self.EscogerModalidad)
        self.SaldoLabel.setText(str(self.dineroBase))

    def EscogerModalidad(self):
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
    
    def Modalidad_1(self):
        dinero = int(self.Apuesta.text())
        
        if dinero < 1 or dinero > 5:
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
                    
        self.SaldoLabel.setText(str(dineroCambio))
        self.ActualizarDinero(dineroCambio)
        
    def Modalidad_2(self):
        dinero = int(self.Apuesta.text())
        
        if dinero < 10 or dinero > 35:
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
                    
        self.SaldoLabel.setText(str(dineroCambio))
        self.ActualizarDinero(dineroCambio)
    
    def Modalidad_3(self):
        dinero = int(self.Apuesta.text())
        
        if dinero < 40 or dinero > 60:
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
                    
        self.SaldoLabel.setText(str(dineroCambio))
        self.ActualizarDinero(dineroCambio)
    
    def Modalidad_4(self):
        dinero = int(self.Apuesta.text())
        
        if dinero < 50 or dinero > 70:
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
                    
        self.SaldoLabel.setText(str(dineroCambio))
        self.ActualizarDinero(dineroCambio)
    
    def Modalidad_5(self):
        dinero = int(self.Apuesta.text())
        
        if dinero < 70:
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
                    
        self.SaldoLabel.setText(str(dineroCambio))
        self.ActualizarDinero(dineroCambio)
        
    def ActualizarDinero(self,dineroNuevo):
        if (dineroNuevo<0):
            dineroBase = 0
        else:
            self.dineroBase = dineroNuevo
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
#Esto existe