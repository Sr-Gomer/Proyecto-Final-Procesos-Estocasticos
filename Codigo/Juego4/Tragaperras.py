# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 17:40:35 2020

@author: 57313
"""

import numpy as np
import numpy.random as rnd
import sys
import bd

#from archivo import JuegoTragaperras
class JuegoTragaperras:
    def __init__(self):
        self.n = 3
        self.multiplicador = 3
        self.resultado = np.array([3, 3, 3])
        self.saldo = bd.traerValor()

        
    def Apostar(self, _mod, _r):
        
        self.resultado = rnd.randint(1, 7, self.n)
        self.mod = _mod
        self.r = _r
        self.cuota = 0
        self.dinGanado = 0
        self.saldo = bd.traerValor()
        
        if self.mod == 1:
            self.cuota = 2 * 10000
            if self.saldo >= self.cuota:
                for i in range(self.n):
                    if self.r == self.resultado[i]:
                        self.dinGanado = self.cuota * self.multiplicador
            else:
                self.cuota = 0
        elif self.mod == 2:
            self.cuota = 3 * 10000
            if self.saldo >= self.cuota:
                self.arreglo = np.unique(self.resultado)
                if len(self.arreglo)  < 3:
                    self.dinGanado = self.cuota * self.multiplicador
            else:
                self.cuota = 0
        elif self.mod == 3:
            self.cuota = 36 * 10000
            if self.saldo >= self.cuota:
                self.contador = 0
                for i in range(self.n):
                    if self.r == self.resultado[i]:
                        self.contador += 1
                if self.contador >= 2:
                    self.dinGanado = self.cuota * self.multiplicador
            else:
                self.couta = 0
        elif self.mod == 4:
            self.cuota = 36 * 10000
            if self.saldo >= self.cuota:
                self.arreglo = np.unique(self.resultado)
                if len(self.arreglo) == 1:
                    self.dinGanado = self.cuota * self.multiplicador
            else:
                self.couta = 0
        elif self.mod == 5:
            self.cuota = 216 * 10000
            if self.saldo >= self.cuota:
                self.arreglo = np.array([self.r, self.r, self.r])
                if (self.arreglo == self.resultado).all():
                    self.dinGanado = self.cuota * self.multiplicador
            else:
                self.cuota = 0
                
        self.saldo += self.dinGanado - self.cuota
        bd.insertarDatos(self.saldo, self.dinGanado - self.cuota)
    def hahaprintxd(self):
        print("SIMEDISCULPANPROCEDOAXDDDDDD")
