import sys,re
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase,QSqlQuery, QSqlTableModel
import ctypes
from bd import *
import numpy as np
import numpy.random as rnd

def Play(tier):
        print(tier)
        
        lootBox = np.array([1, 2, 2, 3, 3, 3])
        profit = 0
    
        saldo = traerValor()

        for i in range (tier):
          shot = rnd.randint(0, 6)
         
          if lootBox[shot] == 1:
            profit += 500000
            print("Felicidades! Ganaste el premio mayor(oro)")
            print("Se han añadido $500000")
            print("Tu saldo actual es de: ${}".format(profit))
          elif lootBox[shot] == 2:
            profit += 300000
            print("Ganaste el premio de plata")
            print("Se han añadido $300000")
            print("Tu saldo actual es de: ${}".format(profit))
          elif lootBox[shot] == 3:
            print("Ganaste el premio de bronce")
            print("Tu saldo actual es de: ${}".format(profit))