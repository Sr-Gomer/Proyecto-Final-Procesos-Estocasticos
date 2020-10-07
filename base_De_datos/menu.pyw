# -*- coding: utf-8 -*-
import sys,re
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase,QSqlQuery, QSqlTableModel
import ctypes
qtCreatorFile = "menu.ui" # Nombre del archivo qt aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #self.showMaximized()

    #def showEvent(self,event):


    # def validar_ganancia(self):
    #     entradaganancia=self.entradaganancia.text()
    #     validar=re.match('0-9-[.]',entradaganancia,re.I)

    # def validar_perdida(self):
    #     validar=re.match('0-9-[.]',entradaperdida,re.I)
    #     entradaperdida=self.entradaperdida.text()

#establecer conexion con la base de datos



#valodacion de conexion a la base de datos
        self.db = QSqlDatabase.addDatabase('QMYSQL')#driver de la base de datos en este caso mysql tambien funciona para mariadb
        self.db.setHostName("186.147.72.83")#servidor de conexion de la base de datos, por defecto el puerto es 3306
        self.db.setDatabaseName("casino")#nombre de la base de datos
        self.db.setUserName("usuariocasino")#usuario para conectarse a la base de datos
        self.db.setPassword("casino")#contraseña del usuario para la base de datos
        #validaciones de conexion a la base de datos
        self.botonganancia.clicked.connect(self.insertarDatos)
    def insertarDatos(self):
     estado=self.db.open()
     if estado == False:
      self.bienvenida.setText("no se pudo conectar")
      QMessageBox.warning(self,"error",self.db.lastError().text(),QMessageBox.Discard)
     else:
      self.bienvenida.setText("conexion a base de datos correcta")
      entradaganancia=self.entradaganancia.text()
        #aqui se hace una inserccion a la base da datos en la tabla transacion la tabla se define despues del "insert into "
      sql="INSERT INTO transacciones(total_transaccion) VALUES(:entradaganancia)"
      consulta=QSqlQuery()
      consulta.prepare(sql)
      consulta.bindValue(":entradaganancia",entradaganancia)
      #aqui se ejecuta la consulta
      estado=consulta.exec_()
      if estado==True:
       QMessageBox.warning(self,"correcto","datos guardados",QMessageBox.Discard)
      else:
       QMessageBox.warning(self,"error",self.db.lastError().text(),QMessageBox.Discard)
       self.db.close()


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())