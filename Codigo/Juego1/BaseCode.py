# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
if __name__ == "__main__":
   sys.path.append("..") #Necesario para poder importar basedatos
import bd #Importa el script bd.py
import numpy as np
import numpy.random as rnd


class RuletaClass:
   def __init__(self,msgBox):
         self.Saldo = 0 #Saldo con el que va a jugar el jugador 
         self.PlataJugar = 0 #plata con la que se va apostar
         self.transaccion = 0
         self.ActualizarSaldo()
         self.displayer = msgBox
   
   def ActualizarSaldo(self):
      self.Saldo = bd.traerValor()
   def getSaldo(self):
      return self.Saldo
   def Lanzar(self,index,value,plata):
     if plata >= 10000: 
       self.PlataJugar = plata
     else:
        plata = 10000
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
     self.Saldo += self.transaccion
     bd.insertarDatos(self.Saldo,self.transaccion)
     self.ActualizarSaldo()
        
   def Modo1(self,value): #apuesta numero
      self.numero = rnd.randint(0,37,1) #generador de la bola
      if self.numero == value:
         self.transaccion = self.PlataJugar * 37
         self.displayer("!ganaste , tu dado: " + str(value) + " dado resultado : " + str(self.numero))
      else:
         self.transaccion = -self.PlataJugar
         self.displayer("Perdiste , tu dado: " + str(value) + " dado resultado : " + str(self.numero))
            
   def Modo2(self,colorapostado): #apuesta color
      self.numero = rnd.randint(0,37,1) #generador de la bola
      self.colorResultado = 0
      self.multiplicador = 0 #valor de multiplicador
      self.color = ""
      if self.numero > 0 and self.numero <= 17:
         self.colorResultado = 0
         self.multiplicador  = 2
         self.color = "Amarillo"
      elif self.numero > 17 and self.numero <=35:
         self.colorResultado = 1
         self.multiplicador = 2
         self.color = "Azul"
      elif self.numero == 0 or self.numero == 36:
         self.colorResultado = 2
         self.multiplicador = 18
         self.color = "Rojo"
         
      if self.colorResultado == colorapostado:
         self.transaccion=self.PlataJugar * self.multiplicador
         self.displayer("Ganaste " + str(self.transaccion) + ", con el color:" + str(self.color))
      else:
         self.transaccion = -self.PlataJugar
         self.displayer("Perdiste " + str(self.transaccion) + ", con el color:" + str(self.color))
            
   def Modo3(self):#apuesta par
      self.numero = rnd.randint(0,37,1) #generador de la bola
      if self.numero % 2 == 0:
         self.transaccion = self.PlataJugar * 2
         self.displayer("Ganaste "+str(self.transaccion)  + ", el número fue Par")
      else:
         self.transaccion = -self.PlataJugar
         self.displayer("Perdiste "+str(self.transaccion)  + ", el número fue impar")

   def Modo4(self):#apuesta impar
      self.numero = rnd.randint(0,37,1) #generador de la bola
      if self.numero % 2 != 0:
         self.transaccion = self.PlataJugar * 2
         self.displayer("Ganaste "+str(self.transaccion)  + ", el número fue Impar")
      else:
         self.transaccion = -self.PlataJugar
         self.displayer("Perdiste "+str(self.transaccion)  + ", el número fue Par")
         
 
   def Modo5(self,rangoApostado): #apuesta rango Numeros
      self.numero = rnd.randint(0,37,1) #generador de la bola
      self.RangoResultado = 0 #rango de numeros que salio        
      self.multiplicador = 0 #valor de multiplicador
      
      if self.numero > 0 and self.numero <= 12:
         self.RangoResultado = 0
         self.multiplicador  = 3
      elif self.numero > 12 and self.numero <=24:
         self.RangoResultado = 1
         self.multiplicador = 3
      elif self.numero > 24 and self.numero <=36:
         self.RangoResultado = 2
         self.multiplicador = 3
      else:
         self.RangoResultado = 3
         self.multiplicador = 37

      if rangoApostado == self.RangoResultado:
         self.transaccion = self.PlataJugar * self.multiplicador
         self.displayer("Ganaste "+str(self.transaccion)  + ", el número fue: " + str(self.numero))
      else:
         self.transaccion = -self.PlataJugar
         self.displayer("Perdiste "+str(self.transaccion)  + ", el número fue: " + str(self.numero))
            
            
       
