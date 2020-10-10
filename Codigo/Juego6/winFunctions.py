# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 00:58:38 2020

@author: judok
"""

def win( apuesta,cuota,saldo ):
   
   ganancia=apuesta*cuota;
   saldoActual=saldo-apuesta+ganancia
   
   return saldoActual

def lose( apuesta,cuota,saldo ):
   
    
   saldoActual=saldo-apuesta
   
   return saldoActual

def diferencia( saldo,saldoActual ):
    detalle=saldoActual-saldo
    return detalle
