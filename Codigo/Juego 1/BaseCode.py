# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import numpy.random as rnd


class RuletaClass:
   
   def __init__(self,Saldo,PlataJugar):
         self.Saldo = 7000 #Saldo con el que va a jugar el jugador 
         self.PlataJugar = 100; #plata con la que se va apostar 
        
   def Lanzar(self,index,value):
       if index == 0:
          self.Modo1(value)
       if index == 1:
          self.Modo2(value)
       if index == 2:
          self.Modo3()
       if index == 3:
          self. Modo4()
       if index == 4:
          self.Modo5(value) 
        
   def Modo1(self,value): #apuesta numero
        numero = rnd.randint(0,37,1) #generador de la bola
        numeroApostado = value #numero con el que vamos a apostar
        
        if numero == numeroApostado:
            self.Saldo += self.PlataJugar * 37
        else:
            self.Saldo-= self.PlataJugar
            
   def Modo2(self,value): #apuesta color
         numero = rnd.randint(0,37,1) #generador de la bola
         colorApostado = value #color que aposto
         colorResultado = 0
         multiplicador = 0 #valor de multiplicador
         
         if numero > 0 and numero <= 17:
            colorResultado = 0
            multiplicador  = 2
         elif numero > 17 and numero <=35:
            colorResultado = 1
            multiplicador = 2
         elif numero == 0 or numero == 36:
            colorResultado = 2
            multiplicador = 18
            
         if colorResultado == colorApostado:
            self.Saldo+=self.PlataJugar * multiplicador
         else:
            self.Saldo-= self.PlataJugar
            
   def Modo3(self):#apuesta par
        numero = rnd.randint(0,37,1) #generador de la bola
        
        if numero % 2 == 0:
            self.Saldo += self.PlataJugar * 2
        else:
            self.Saldo-= self.PlataJugar
   
   def Modo4(self):#apuesta impar
        numero = rnd.randint(0,37,1) #generador de la bola
        
        if numero % 2 != 0:
            self.Saldo += self.PlataJugar * 2
        else:
            self.Saldo-= self.PlataJugar
            
 
   def Modo5(self,value): #apuesta rango Numeros
         numero = rnd.randint(0,37,1) #generador de la bola
         rangoApostado = value #rango que aposto
         RangoResultado = 0 #rango de numeros que salio        
         multiplicador = 0 #valor de multiplicador
         
         if numero > 0 and numero <= 12:
            RangoResultado = 0
            multiplicador  = 3
         elif numero > 12 and numero <=24:
            RangoResultado = 1
            multiplicador = 3
         elif numero > 24 and numero <=36:
            RangoResultado = 2
            multiplicador = 3
         else:
            RangoResultado = 3
            multiplicador = 37
         if rangoApostado == RangoResultado:
            self.Saldo += self.PlataJugar * multiplicador
         else:
            self.Saldo -= self.PlataJugar
            
            
       
    