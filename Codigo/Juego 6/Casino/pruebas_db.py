# -*- coding: utf-8 -*-
#lineas necesarias para usar el fichero
import sys,re
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase,QSqlQuery, QSqlTableModel
import ctypes
from bd import insertarDatos
#fin lineas necesarias para el uso del fichero

#insercion de datos a la bd
total_transaccion=1200
detalle_transacion=1200
valores=insertarDatos(total_transaccion,detalle_transacion)
#self.botonganancia.clicked.connect(insertarDatos)