# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 17:40:35 2020

@author: 57313
"""

import numpy as np
import numpy.random as rnd

#from archivo import JuegoTragaperras
class JuegoTragaperras:
    def __init__(self):
        self.n = 3
        self.multiplicador = 3
#        self.resultado = rnd.randint(1, 7, self.n)
        self.resultado = np.array([3, 3, 3])
        
    def Apostar(self, _mod, _r):
        
        self.mod = _mod
        self.r = _r
        self.cuota = 0
        self.dinGanado = 0
        self.saldo = 10000
        
        if self.mod == 1:
            self.cuota = 2
            for i in range(self.n):
                if self.r == self.resultado[i]:
                    self.dinGanado = self.cuota * self.multiplicador
        elif self.mod == 2:
            self.cuota = 3
            self.arreglo = np.unique(self.resultado)
            if len(self.arreglo)  < 3:
                self.dinGanado = self.cuota * self.multiplicador
        elif self.mod == 3:
            self.cuota = 36
            self.contador = 0
            for i in range(self.n):
                if self.r == self.resultado[i]:
                    self.contador += 1
            if self.contador >= 2:
                self.dinGanado = self.cuota * self.multiplicador
        elif self.mod == 4:
            self.cuota = 36
            self.arreglo = np.unique(self.resultado)
            if len(self.arreglo) == 1:
                self.dinGanado = self.cuota * self.multiplicador
        elif self.mod == 5:
            self.cuota = 216
            self.arreglo = np.array([self.r, self.r, self.r])
            if (self.arreglo == self.resultado).all():
                self.dinGanado = self.cuota * self.multiplicador
                
        self.saldo += self.dinGanado - self.cuota

Juego = JuegoTragaperras()
Juego.Apostar(5, 3)
print(Juego.dinGanado)
print(Juego.saldo)