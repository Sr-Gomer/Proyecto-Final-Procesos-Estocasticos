
import bd
import numpy as np
class Juegojackpot:
    def __init__(self,msg):
        self.Saldo = 0
        self.ganancia = 0
        self._msgbox = msg
        self.Disco1 = self.GirarRuleta()
        self.Disco2 = self.GirarRuleta()
        self.Disco3 = self.GirarRuleta()
        self.Disco4 = self.GirarRuleta()
        self.Disco5 = self.GirarRuleta()
        self.AAA = ""
        self.actualizarSaldo()
    
    def actualizarSaldo(self):
        self.Saldo = bd.traerValor()
    def getInfo(self):
        return [[self.Disco1,self.Disco2,self.Disco3,self.Disco4,self.Disco5],self.Saldo]
    def getResults(self):
        return[self.AAA,self.ganancia]
    def Jugar(self,cb1A, cb1B, cb1C, cb2A, cb2B, cb3A, cb3B, cb4A, cb4B, apuesta):
        self.actualizarSaldo()
        if self.Validar([cb1A, cb1B, cb1C, cb2A, cb2B, cb3A, cb3B, cb4A, cb4B]) != True:
            return
        self.selectedLines = self.Contar([cb1A, cb1B, cb1C, cb2A, cb2B, cb3A, cb3B, cb4A, cb4B])
        
        self.ganancia = 0
        self.posibles=759375
        self.simbolos = np.array(["A", "B", "C", "D"])
        try:
            if( apuesta%self.selectedLines != 0):
                self._msgbox("Error","La Cantidad de creditos a jugar no es multiplo de las lineas seleccionadas")
                return 0
        except:
            return 0

        if (apuesta*1000) < 10000:
            self._msgbox("Error","La cantidad a apostar debe ser mayor a 10000 pesos")
            return 0
        
        
        apuesta = apuesta/self.selectedLines
        self.Disco1 = self.GirarRuleta()
        self.Disco2 = self.GirarRuleta()
        self.Disco3 = self.GirarRuleta()
        self.Disco4 = self.GirarRuleta()
        self.Disco5 = self.GirarRuleta()
        
        self.win = False
        for x in self.simbolos:
            if cb1A and self.Disco1[0] == x and self.Disco2[0] == x and self.Disco3[0] == x and self.Disco4[0] == x and self.Disco5[0] == x:
                self.AddvalorGanancia(x,apuesta,self.posibles,self.selectedLines)
                self.win = True
            if cb1B and self.Disco1[1] == x and self.Disco2[1] == x and self.Disco3[1] == x and self.Disco4[1] == x and self.Disco5[1] == x:
                self.AddvalorGanancia(x,apuesta,self.posibles,self.selectedLines)
                self.win = True
            if cb1C and self.Disco1[2] == x and self.Disco2[2] == x and self.Disco3[2] == x and self.Disco4[2] == x and self.Disco5[2] == x:
                self.AddvalorGanancia(x,apuesta,self.posibles,self.selectedLines)
                self.win = True
            if cb2A and self.Disco1[2] == x and self.Disco2[1] == x and self.Disco3[1] == x and self.Disco4[1] == x and self.Disco5[0] == x:
                self.AddvalorGanancia(x,apuesta,self.posibles,self.selectedLines)
                self.win = True
            if cb2B and self.Disco1[0] == x and self.Disco2[1] == x and self.Disco3[1] == x and self.Disco4[1] == x and self.Disco5[2] == x:
                self.AddvalorGanancia(x,apuesta,self.posibles,self.selectedLines)
                self.win = True
            if cb3A and self.Disco1[2] == x and self.Disco2[1] == x and self.Disco3[2] == x and self.Disco4[1] == x and self.Disco5[2] == x:
                self.AddvalorGanancia(x,apuesta,self.posibles,self.selectedLines)
                self.win = True
            if cb3B and self.Disco1[0] == x and self.Disco2[1] == x and self.Disco3[0] == x and self.Disco4[1] == x and self.Disco5[0] == x:
                self.AddvalorGanancia(x,apuesta,self.posibles,self.selectedLines)
                self.win = True
            if cb4A and self.Disco1[0] == x and self.Disco2[1] == x and self.Disco3[2] == x and self.Disco4[1] == x and self.Disco5[0] == x:
                self.AddvalorGanancia(x,apuesta,self.posibles,self.selectedLines)
                self.win = True
            if cb4B and self.Disco1[2] == x and self.Disco2[1] == x and self.Disco3[0] == x and self.Disco4[1] == x and self.Disco5[2] == x:
                self.AddvalorGanancia(x,apuesta,self.posibles,self.selectedLines)
                self.win = True
        
        if cb1B and self.Disco1[1] == "E" and self.Disco2[1] == "E" and self.Disco3[1] == "E" and self.Disco4[1] == "E" and self.Disco5[1] == "E":
            self.ganancia += apuesta * self.posibles
            self.AAA =("¡JACKPOT!")
            self.win=True
        if self.win == False:
            self.AAA =("Usted ha perdido :c ")
            self.ganancia = apuesta*self.selectedLines*-1
        
        self.ganancia *= 1000
        
        self.Saldo += self.ganancia
        bd.insertarDatos(self.Saldo,self.ganancia)

    def AddvalorGanancia(self,stringX,apuesta,posibles,nlineas):
        if stringX == "A":
            self.ganancia += self.calcularGanancia(apuesta,posibles,3125,nlineas)
            self.AAA = ("ha Ganado con la combinación A")
        elif stringX == "B":
            self.ganancia += self.calcularGanancia(apuesta,posibles,1024,nlineas)
            self.AAA =("ha Ganado con la combinación B")
        elif stringX == "C":
            self.ganancia += self.calcularGanancia(apuesta,posibles,243,nlineas)
            self.AAA =("ha Ganado con la combinación C")
        elif stringX == "D":
            self.ganancia += self.calcularGanancia(apuesta,posibles,32,nlineas)
            self.AAA =("ha Ganado con la combinación D")

    def calcularGanancia(self,apuesta,posibles,cuota,nlineas):
        return apuesta * (posibles/cuota*nlineas)
        

    def GirarRuleta(self):
        self.Ruleta = np.array(["A", "B", "A", "C", "B", "E", "A", "B", "D", "B", "A", "C", "A", "D", "C"])
        
        self.i = np.random.randint(0,15)
        if self.i == 0:
            self.P0 = self.Ruleta[14]
            self.P1 = self.Ruleta[0]
            self.P2 = self.Ruleta[1]
        elif self.i == 14:
            self.P0 = self.Ruleta[13]
            self.P1 = self.Ruleta[14]
            self.P2 = self.Ruleta[0]
        else:
            self.P0 = self.Ruleta[self.i-1]
            self.P1 = self.Ruleta[self.i]
            self.P2 = self.Ruleta[self.i+1]
        
        self.dev = np.array([self.P0,self.P1,self.P2])
            
        return self.dev
        
    def Contar(self,arrayBooleans):
        self.selected =0
        for x in arrayBooleans:
            if x ==True:
                self.selected +=1
        return self.selected
    def Validar(self,arrayBooleans):
        self.cantidad = self.Contar(arrayBooleans)
        if self.selected > 5 or self.selected == 0:
            self._msgbox("Error","Debes jugar entre 1 y 5 lineas")
            return False
        else:
            return True