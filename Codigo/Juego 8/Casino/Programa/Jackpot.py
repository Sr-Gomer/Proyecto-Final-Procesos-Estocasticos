# -*- coding: utf-8 -*-
"""
Created on Domingo 4 de Octubre

@author: José Manuel Gutiérrez Sosa (Mechas)
"""
try:
    import sys,re
    import os
    import numpy as np
    from bd import *
    from PyQt5 import uic, QtWidgets, QtGui
    
    
    
    from PyQt5.QtWidgets import QMessageBox
    
    uiFile = "./jackpotMain.ui" # Nombre del archivo aquí. Debe estar en la misma carpeta
    
    Ui_MainWindow, QtBaseClass = uic.loadUiType(uiFile)
    
    sys.path.append("..")
    
    class UIWindow(QtWidgets.QMainWindow, Ui_MainWindow):
        def __init__(self):
            QtWidgets.QMainWindow.__init__(self)
            Ui_MainWindow.__init__(self)
            self.setupUi(self)
            self.lbCantCreditos.setText("%s Pesos"%traerValor())
            self.btnPlay.clicked.connect(self.obtener)
        def obtener(self):
            if float(self.lbCantCreditos.text().split()[0]) < self.sbCreditosApostar.value()*200 :
                os.system("MessageBox.py %s"%("Debes tener saldo suficiente para jugar"))
                return
            prize = Jugar(self.cb1A.isChecked(),self.cb1B.isChecked(),self.cb1C.isChecked(),self.cb2A.isChecked(),self.cb2B.isChecked(),self.cb3A.isChecked(),self.cb3B.isChecked(),self.cb4A.isChecked(),self.cb4B.isChecked(),self.sbCreditosApostar.value())
            if prize == 0:
                return
            self.lbCantCreditos.setText("%s Pesos"%(float(self.lbCantCreditos.text().split()[0])+prize))
            insertarDatos(float(self.lbCantCreditos.text().split()[0]),prize)
            
        
            
    
    def Run():
        os.system("MessageBox.py %s"%("Cada Credito apostado tiene un valor de 200 Pesos"))
        app =  QtWidgets.QApplication(sys.argv)
        window = UIWindow()
        window.show()
        sys.exit(app.exec_())
        
    #Mi code
    def Jugar(cb1A, cb1B, cb1C, cb2A, cb2B, cb3A, cb3B, cb4A, cb4B, apuesta):
        
        selectedLines = Contar(cb1A, cb1B, cb1C, cb2A, cb2B, cb3A, cb3B, cb4A, cb4B)
        
        ganancia = 0
        posibles=759375
        simbolos = np.array(["A", "B", "C", "D"])
        try:
            if( apuesta%selectedLines != 0):
                os.system("MessageBox.py %s"%("La Cantidad de creditos a jugar no es multiplo de las lineas seleccionadas"))
                return 0
        except:
            return 0
    
        if (apuesta/selectedLines)*200 < 10000:
            os.system("MessageBox.py %s (%s Creditos)"%("La cantidad a apostar debe ser mayor a 10000 pesos", 50*selectedLines))
            return 0
        
        
        apuesta = apuesta/selectedLines
        Disco1 = GirarRuleta()
        Disco2 = GirarRuleta()
        Disco3 = GirarRuleta()
        Disco4 = GirarRuleta()
        Disco5 = GirarRuleta()
        
        win = False
        for x in simbolos:
            if cb1A and Disco1[0] == x and Disco2[0] == x and Disco3[0] == x and Disco4[0] == x and Disco5[0] == x:
                if x == "A":
                    ganancia += apuesta * (posibles/3125*selectedLines)
                    AAA = ("ha@Ganado@con@la@combinación@A")
                elif x == "B":
                    ganancia += apuesta * (posibles/1024*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@B")
                elif x == "C":
                    ganancia += apuesta * (posibles/243*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@C")
                elif x == "D":
                    ganancia += apuesta * (posibles/32*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@D")
                win = True
            if cb1B and Disco1[1] == x and Disco2[1] == x and Disco3[1] == x and Disco4[1] == x and Disco5[1] == x:
                if x == "A":
                    ganancia += apuesta * (posibles/3125*selectedLines)
                    AAA = ("ha@Ganado@con@la@combinación@A")
                elif x == "B":
                    ganancia += apuesta * (posibles/1024*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@B")
                elif x == "C":
                    ganancia += apuesta * (posibles/243*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@C")
                elif x == "D":
                    ganancia += apuesta * (posibles/32*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@D")
                win = True
            if cb1C and Disco1[2] == x and Disco2[2] == x and Disco3[2] == x and Disco4[2] == x and Disco5[2] == x:
                if x == "A":
                    ganancia += apuesta * (posibles/3125*selectedLines)
                    AAA = ("ha@Ganado@con@la@combinación@A")
                elif x == "B":
                    ganancia += apuesta * (posibles/1024*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@B")
                elif x == "C":
                    ganancia += apuesta * (posibles/243*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@C")
                elif x == "D":
                    ganancia += apuesta * (posibles/32*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@D")
                win = True
            if cb2A and Disco1[2] == x and Disco2[1] == x and Disco3[1] == x and Disco4[1] == x and Disco5[0] == x:
                if x == "A":
                    ganancia += apuesta * (posibles/3125*selectedLines)
                    AAA = ("ha@Ganado@con@la@combinación@A")
                elif x == "B":
                    ganancia += apuesta * (posibles/1024*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@B")
                elif x == "C":
                    ganancia += apuesta * (posibles/243*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@C")
                elif x == "D":
                    ganancia += apuesta * (posibles/32*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@D")
                win = True
            if cb2B and Disco1[0] == x and Disco2[1] == x and Disco3[1] == x and Disco4[1] == x and Disco5[2] == x:
                if x == "A":
                    ganancia += apuesta * (posibles/3125*selectedLines)
                    AAA = ("ha@Ganado@con@la@combinación@A")
                elif x == "B":
                    ganancia += apuesta * (posibles/1024*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@B")
                elif x == "C":
                    ganancia += apuesta * (posibles/243*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@C")
                elif x == "D":
                    ganancia += apuesta * (posibles/32*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@D")
                win = True
            if cb3A and Disco1[2] == x and Disco2[1] == x and Disco3[2] == x and Disco4[1] == x and Disco5[2] == x:
                if x == "A":
                    ganancia += apuesta * (posibles/3125*selectedLines)
                    AAA = ("ha@Ganado@con@la@combinación@A")
                elif x == "B":
                    ganancia += apuesta * (posibles/1024*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@B")
                elif x == "C":
                    ganancia += apuesta * (posibles/243*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@C")
                elif x == "D":
                    ganancia += apuesta * (posibles/32*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@D")
                win = True
            if cb3B and Disco1[0] == x and Disco2[1] == x and Disco3[0] == x and Disco4[1] == x and Disco5[0] == x:
                if x == "A":
                    ganancia += apuesta * (posibles/3125*selectedLines)
                    AAA = ("ha@Ganado@con@la@combinación@A")
                elif x == "B":
                    ganancia += apuesta * (posibles/1024*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@B")
                elif x == "C":
                    ganancia += apuesta * (posibles/243*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@C")
                elif x == "D":
                    ganancia += apuesta * (posibles/32*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@D")
                win = True
            if cb4A and Disco1[0] == x and Disco2[1] == x and Disco3[2] == x and Disco4[1] == x and Disco5[0] == x:
                if x == "A":
                    ganancia += apuesta * (posibles/3125*selectedLines)
                    AAA = ("ha@Ganado@con@la@combinación@A")
                elif x == "B":
                    ganancia += apuesta * (posibles/1024*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@B")
                elif x == "C":
                    ganancia += apuesta * (posibles/243*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@C")
                elif x == "D":
                    ganancia += apuesta * (posibles/32*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@D")
                win = True
            if cb4B and Disco1[2] == x and Disco2[1] == x and Disco3[0] == x and Disco4[1] == x and Disco5[2] == x:
                if x == "A":
                    ganancia += apuesta * (posibles/3125*selectedLines)
                    AAA = ("ha@Ganado@con@la@combinación@A")
                elif x == "B":
                    ganancia += apuesta * (posibles/1024*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@B")
                elif x == "C":
                    ganancia += apuesta * (posibles/243*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@C")
                elif x == "D":
                    ganancia += apuesta * (posibles/32*selectedLines)
                    AAA =("ha@Ganado@con@la@combinación@D")
                win = True
        
        if cb1B and Disco1[1] == "E" and Disco2[1] == "E" and Disco3[1] == "E" and Disco4[1] == "E" and Disco5[1] == "E":
            ganancia += apuesta * posibles
            AAA =("¡JACKPOT!")
            win=True
        if win == False:
            AAA =("Usted@ha@perdido@:c ")
            ganancia = apuesta*selectedLines*-1
        
        ganancia *= 200
        
        os.system("Result.py %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s"%(ganancia,Disco1[0],Disco1[1],Disco1[2],Disco2[0],Disco2[1],Disco2[2],Disco3[0],Disco3[1],Disco3[2],Disco4[0],Disco4[1],Disco4[2],Disco5[0],Disco5[1],Disco5[2], AAA))
        return ganancia
            
        
    
    def GirarRuleta():
        Ruleta = np.array(["A", "B", "A", "C", "B", "E", "A", "B", "D", "B", "A", "C", "A", "D", "C"])
        
        i = np.random.randint(0,15)
        if i == 0:
            P0 = Ruleta[14]
            P1 = Ruleta[0]
            P2 = Ruleta[1]
        elif i == 14:
            P0 = Ruleta[13]
            P1 = Ruleta[14]
            P2 = Ruleta[0]
        else:
            P0 = Ruleta[i-1]
            P1 = Ruleta[i]
            P2 = Ruleta[i+1]
        
        dev = np.array([P0,P1,P2])
            
        return dev
        
    def Contar(cb1A, cb1B, cb1C, cb2A, cb2B, cb3A, cb3B, cb4A, cb4B):
        selected =0
        if cb1A:
            selected += 1
        if cb1B:
            selected += 1
        if cb1C:
            selected += 1
        if cb2A:
            selected += 1
        if cb2B:
            selected += 1
        if cb3A:
            selected += 1
        if cb3B:
            selected += 1
        if cb4A:
            selected += 1
        if cb4B:
            selected += 1
        if selected > 5:
            os.system("MessageBox.py %s"%("Como maximo puedes jugar 5 lineas"))
            return
        if selected == 0:
            os.system("MessageBox.py %s"%("Como minimo debes jugar 1 linea"))
            return
        return selected;
        
    
        
    
    Run()
    #Descomentar esta linea cuando se quiera probar individualmente.
except:
    print("a")