# rama base de datos utilizando mysql y pyqt5

* ##  aqui van a encontrar el video donde explico como instalar python de manera correcta en windows, y como poder usar y ejecutar correctamente el programa, aparte de sulución al posible error de el driver de mysql. 


***
# conexion
## para hacer la conexion se necesitan los siguientes datos
* ## servidor de conexion de la base de datos, por defecto el puerto es 3306
* ###       self.db.setHostName("192.168.100.243")
* ## nombre de la base de datos
* ### self.db.setDatabaseName("casino")
* ## usuario para conectarse a la base de datos
* ### self.db.setUserName("usuariocasino")
* ## contraseña del usuario para la base de datos
* ### self.db.setPassword("casino")
## estos son solo datos de ejemplo

***

# video donde explica como hacer la correcta instalación de python y las librerias
## https://www.youtube.com/watch?v=WVUjvJHvjbc

***
# datos  que se deben pasar a la base de datos
## solo necesitamos el valor que genera el total de la perdida y el valor de la perdida

# ejemplo
## dinero recargado: 5000
## valor de perdida: 3000 (generado por la apuesta)
##  valor recargado - valor perdida =valor que genera total (5000-3000=2000)
## valor de la perdida : 3000







