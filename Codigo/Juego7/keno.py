# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 18:37:43 2020

@author: JEAN PIERRE
"""

import sys,re
from PyQt5 import uic, QtWidgets, QtGui
if __name__ == "__main__":
    sys.path.append("..")
from PyQt5.QtWidgets import QMessageBox
# from bd import *
import bd
import numpy as np
import numpy.random as rnd

imgKeno = "./" + __package__+"./descarga.jpg"
uiFile = "./" +__package__ + "./Proyecto.ui" # Nombre del archivo aquí. Debe estar en la misma carpeta

Ui_MainWindow, QtBaseClass = uic.loadUiType(uiFile)


class UIWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.label2_5.setText("%s"%bd.traerValor())
        self.btnjugar.clicked.connect(self.jugarui)
        self.img = QtGui.QPixmap(imgKeno) # carga la imagen
        self._img.setPixmap(self.img) #Le pone la imagen al label
        print("este es el print")
        print(self.lineEdit2.text())
        
        
            
    def jugarui(self):
        if(self.isInputANumber() == True and self.HasBalota() == True):
            pass
        else:
            return

        t = self.lineEdit2.text()
        m = self.comboBox.currentIndex()
        k = float(self.label2_5.text())
        j = True
        
        
        if((m == 0 and len(t)<3) or (m == 1 and len(t)<9 and len(t)>4) or (m == 2 and len(t)<15 and len(t)>8) or (m == 3 and len(t)<24 and len(t)>14) or (m == 4 and len(t)<30 and len(t)>18)):
            j = True
            self.label2_4.setText("     ¡Formato Correcto!")
            self.label2_4.setStyleSheet("color: rgb(226, 240, 57);")
        else:
            self.label2_4.setText("     ¡Formato Invalido!")
            self.label2_4.setStyleSheet("color: rgb(255, 0, 4);")
            j= False
        if(float(self.lineEdit.text()) < 10000):
            self.label4.setText("Mínimo 10.000")
            j = False
            
        if(k < float(self.lineEdit.text())):
            self.label4.setText("¡Sin Saldo!")
            self.label4.setStyleSheet("color: rgb(255, 0, 4);")
            j = False
            
        if j == True:
            texto = jugar(self.comboBox.currentIndex(),self.lineEdit2.text(),self.lineEdit.text())
            ver = "$"
            ver += str(texto)
            self.label2_3.setText(ver)
            
            if(texto==0):
              self.label4.setText("    ¡Perdiste!")
              self.label4.setStyleSheet("color: rgb(255, 0, 4);")
              ver += str(texto)*2
              self.label2_3.setText(ver)
              bd.insertarDatos(float(self.label2_5.text())-float(self.lineEdit.text()),-1*float(self.lineEdit.text()))
              self.label2_5.setText("%s"%bd.traerValor())
            else:
              self.label4.setText("    ¡Ganaste!")
              self.label4.setStyleSheet("color: rgb(226, 240, 57);")
              bd.insertarDatos(float(self.label2_5.text())+texto,float(self.lineEdit.text()))
              self.label2_5.setText("%s"%bd.traerValor())
    def isInputANumber(self):#Checa si el input es un número
        self.toReturn : bool
        try:
            float(self.lineEdit.text())
            self.toReturn = True
        except:
            QMessageBox.about(self, "Error", "Por favor ingrese un valor valido")
            self.toReturn = False
        return self.toReturn
    def HasBalota(self):
        if(self.lineEdit2.text() != ""):
            return True
        else:
            QMessageBox.about(self, "Error", "Por favor ingrese un balota valida")
            return False
    
            
         
        
def jugar(Mod,Balotas, Valor):
    print("Estas Jugando")
    Premio = 0
    valor = int(Valor)
    g = np.sort(rnd.randint(1,81,20))
    gu = np.unique(g)
    while len(g)!=len(gu):
        g=np.sort(rnd.randint(1,81,20))
        gu = np.unique(g)
       
    if(Mod == 0):
        ganador = Balotas
        print("Balotas jugadas", ganador)
        for i in range(20):
          if(g[i] == int(ganador)):
              print("Ganaste")
              Premio = valor*3
        print("Ganaste Un premio De: ",Premio)
    elif(Mod == 1):
        ganador = Balotas.split(",")
        Bal1= ganador[0]
        Bal2 = ganador[1]
        Bal3 = ganador[2]
        w =  0
        print("Balotas jugadas", ganador)
        
    
        for i in range(20):
          if(g[i] == int(Bal1)):
              print("ganaste en 1")
              w += 1
          elif(g[i] == int(Bal2)):
              print("Ganaste en 2")
              w += 1
          elif(g[i] == int(Bal3)):
              print("Ganaste en 3")
              w += 1
        print("Acertasten en ", w ," Balotas")
                 
        if(w == 3):
            Premio = valor*45
        elif(w==2):
            Premio = valor*2
            
        print("Ganaste Un premio De: ",Premio)
              
              
    elif(Mod == 2):
        ganador = Balotas.split(",")
        print("Balotas jugadas", ganador)
        Bal1= ganador[0]
        Bal2 = ganador[1]
        Bal3 = ganador[2]
        Bal4 = ganador[3]
        Bal5 = ganador[4]
        w =  0
        for i in range(20):
          if(g[i] == int(Bal1)):
              print("ganaste en 1")
              w += 1
          elif(g[i] == int(Bal2)):
              print("Ganaste en 2")
              w += 1
          elif(g[i] == int(Bal3)):
              print("Ganaste en 3")
              w += 1
          elif(g[i] == int(Bal4)):
              print("Ganaste en 4")
              w += 1
          elif(g[i] == int(Bal5)):
              print("Ganaste en 5")
              w += 1
        print("Acertasten en ", w ," Balotas")
        
        if(w == 5):
            Premio = valor*150
        elif(w==4):
            Premio = valor*20
        elif(w==3):
            Premio = valor*3
       
        print("Ganaste Un premio De: ",Premio)
        
    elif(Mod == 3):
        ganador = Balotas.split(",")
        print("Balotas jugadas", ganador)
        Bal1= ganador[0]
        Bal2 = ganador[1]
        Bal3 = ganador[2]
        Bal4 = ganador[3]
        Bal5 = ganador[4]
        Bal6 = ganador[5]
        Bal7 = ganador[6]
        Bal8 = ganador[7]
        w =  0
        for i in range(20):
          if(g[i] == int(Bal1)):
              print("ganaste en 1")
              w += 1
          elif(g[i] == int(Bal2)):
              print("Ganaste en 2")
              w += 1
          elif(g[i] == int(Bal3)):
              print("Ganaste en 3")
              w += 1
          elif(g[i] == int(Bal4)):
              print("Ganaste en 4")
              w += 1
          elif(g[i] == int(Bal5)):
              print("Ganaste en 5")
              w += 1
          elif(g[i] == int(Bal6)):
              print("Ganaste en 6")
              w += 1
          elif(g[i] == int(Bal7)):
              print("Ganaste en 7")
              w += 1
          elif(g[i] == int(Bal8)):
              print("Ganaste en 8")
              w += 1
        print("Acertasten en ", w ," Balotas")
        
        if(w == 8):
            Premio = valor*2000
        elif(w==7):
            Premio = valor*200
        elif(w==6):
            Premio = valor*50
        elif(w==5):
            Premio = valor*15
       
        print("Ganaste Un premio De: ",Premio)
    else:
        ganador = Balotas.split(",")
        print("Balotas Jugadas", ganador)
        Bal1= ganador[0]
        Bal2 = ganador[1]
        Bal3 = ganador[2]
        Bal4 = ganador[3]
        Bal5 = ganador[4]
        Bal6 = ganador[5]
        Bal7 = ganador[6]
        Bal8 = ganador[7]
        Bal9 = ganador[8]
        Bal10 = ganador[9]
        w =  0
        for i in range(20):
          if(g[i] == int(Bal1)):
              print("ganaste")
              w += 1
          elif(g[i] == int(Bal2)):
              print("Ganaste en 2")
              w += 1
          elif(g[i] == int(Bal3)):
              print("Ganaste en 3")
              w += 1
          elif(g[i] == int(Bal4)):
              print("Ganaste en 4")
              w += 1
          elif(g[i] == int(Bal5)):
              print("Ganaste en 5")
              w += 1
          elif(g[i] == int(Bal6)):
              print("Ganaste en 6")
              w += 1
          elif(g[i] == int(Bal7)):
              print("Ganaste en 7")
              w += 1
          elif(g[i] == int(Bal8)):
              print("Ganaste en 8")
              w += 1
          elif(g[i] == int(Bal9)):
              print("Ganaste en 9")
              w += 1
          elif(g[i] == int(Bal10)):
              print("Ganaste en 10")
              w += 1
        print("Acertasten en ", w ," Balotas")
        
        if(w == 10):
            Premio = valor*10000
        elif(w==9):
            Premio = valor*2000
        elif(w==8):
            Premio = valor*300
        elif(w==7):
            Premio = valor*100
        elif(w==6):
            Premio = valor*30
       
        print("Ganaste Un premio De: ",Premio)
    
    
    print(gu)
    print("Lo Modalidad es, ")
    print(Mod)
    print("Las Balotas jugadas Son ")
    print(ganador)
    print("El Valor a jugar es ")
    print(Valor)
    
    
    return Premio
    

def Run():
    app =  QtWidgets.QApplication(sys.argv)
    window = UIWindow()
    window.show()
    sys.exit(app.exec_())
    

# Run()#Descomentar esta linea cuando se quiera probar individualmente.