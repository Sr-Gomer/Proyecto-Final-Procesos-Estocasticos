# -*- coding: utf-8 -*-
import sys,re
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase,QSqlQuery, QSqlTableModel


db = QSqlDatabase.addDatabase('QMYSQL')#driver de la base de datos en este caso mysql tambien funciona para mariadb
db.setHostName("186.147.72.83")#servidor de conexion de la base de datos, por defecto el puerto es 3306
db.setDatabaseName("casino")#nombre de la base de datos
db.setUserName("usuariocasino")#usuario para conectarse a la base de datos
db.setPassword("casino")#contraseña del usuario para la base de datos
        #validaciones de conexion a la base de datos

def insertarDatos(total_transaccion,detalle_transacion):
 estado=db.open()
 if estado == False:
  print("no se pudo conectar")
  #QMessageBox.warning("error",db.lastError().text(),QMessageBox.Discard)
  print("error",db.lastError().text())
 else:
  print("conexion a base de datos correcta")
  #total_transaccion=entradaganancia.text()
    #aqui se hace una inserccion a la base da datos en la tabla transacion la tabla se define despues del "insert into "
  sql="INSERT INTO transacciones(total_transaccion,detalle_transacion) VALUES(:total_transaccion,:detalle_transacion)"
  consulta=QSqlQuery()
  consulta.prepare(sql)
  consulta.bindValue(":total_transaccion",total_transaccion)
  consulta.bindValue(":detalle_transacion",detalle_transacion)
  #print(total_transaccion)
  #aqui se ejecuta la consulta
  estado=consulta.exec_()
  if estado==True:
   #QMessageBox.warning("correcto","datos guardados",QMessageBox.Discard)
   print("correcto","datos guardados")
  else:
   #QMessageBox.warning("error",db.lastError().text(),QMessageBox.Discard)
   print("error",db.lastError().text())
   db.close()

def traerValor():
     estado=db.open()
     query=QSqlQuery()
     query.exec_("SELECT total_transaccion  FROM  transacciones ORDER BY id_transaccion DESC LIMIT 1")
     while query.next():
        total=query.value(0)
     #estado=consulta.exec_()
     db.close()
     #print("soy total",total)
     return total