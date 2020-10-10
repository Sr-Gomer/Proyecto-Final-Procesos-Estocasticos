
import numpy as np
import numpy.random as rnd
    
if __name__ == "__main__":
    from winFunctions import win,lose
else:
    from Juego6.winFunctions import win, lose
feedback="s"
resultadoC=0
def Jugar(modo,cartaJugador,pintaJugador,colorJugador,saldo,apuesta):
    global feedback
    global resultadoC
    
    #modo="IMPARES"
    #cartaJugador="Q"
    #pintaJugador="DIAMANTES"
    #colorJugador="NEGRO"
    
   
    
    if(cartaJugador=="A"):
        int_cartaJugador=1
    elif(cartaJugador=="J"):
        int_cartaJugador=11
    elif(cartaJugador=="Q"):
        int_cartaJugador=12
    elif(cartaJugador=="K"):
        int_cartaJugador=13
    else:
        int_cartaJugador=int(cartaJugador)
    
    n=1
    
    for i in range(n):
        numCartaAleatorio=np.sort(rnd.randint(1,14,1))
        if(numCartaAleatorio==1):
            cartaAleatoria="A"
        elif(numCartaAleatorio==11):
            cartaAleatoria="J"
        elif(numCartaAleatorio==12):
            cartaAleatoria="Q"
        elif(numCartaAleatorio==13):
            cartaAleatoria="K"
        else:
            cartaAleatoria=str(numCartaAleatorio)
    for i in range(n):
        pintaCartaAleatorio=np.sort(rnd.randint(1,5,1))
        if(pintaCartaAleatorio==1):
            pintaCarta="DIAMANTES"
            colorCarta="ROJO"
        elif(pintaCartaAleatorio==2):
            pintaCarta="PICAS"
            colorCarta="NEGRO"
        elif(pintaCartaAleatorio==3):
            pintaCarta="TREBOLES"
            colorCarta="NEGRO"
        elif(pintaCartaAleatorio==4):
            pintaCarta="CORAZONES"
            colorCarta="ROJO"
    
    
    if(modo=="CARTA"):
        cuota=52
        print("elegiste la carta",cartaJugador,"de",pintaJugador)
        print("salio la carta",cartaAleatoria,"de",pintaCarta)
        feedback=("salio la carta",cartaAleatoria,"de",pintaCarta)
        
        if(int_cartaJugador==numCartaAleatorio and pintaCarta==pintaJugador):
            
            resultadoC = win(apuesta,cuota,saldo)
            return resultadoC
        else:
            resultadoC = lose(apuesta,cuota,saldo)
            return resultadoC
    
    if(modo=="NUMEROS"):
        cuota=13
        print("elegiste la carta",cartaJugador)
        print("salio la carta",cartaAleatoria)
        feedback=("salio la carta",cartaAleatoria)
        
        if(int_cartaJugador==numCartaAleatorio):
            resultadoC = win(apuesta,cuota,saldo)
            return resultadoC
        else:
            resultadoC = lose(apuesta,cuota,saldo)
            return resultadoC
            
    if(modo=="PARES"):
        cuota=2.16
        print("elegiste PARES")
        print("salio la carta",cartaAleatoria)
        
        feedback=("salio la carta",cartaAleatoria)
        
        
        if (numCartaAleatorio % 2 == 0):
            resultadoC = win(apuesta,cuota,saldo)
            return resultadoC
        else:
            resultadoC = lose(apuesta,cuota,saldo)
            return resultadoC
    
    if(modo=="IMPARES"):
        cuota=1.85
        print("elegiste IMPARES")
        print("salio la carta",cartaAleatoria)
        feedback=("salio la carta",cartaAleatoria)
       
        
        if (numCartaAleatorio % 2 == 0):
            resultadoC = lose(apuesta,cuota,saldo)
            return resultadoC
        else:
            resultadoC = win(apuesta,cuota,saldo)
            return resultadoC
        
                     
    if(modo=="COLOR"):
        cuota=2
        print("elegiste el color",colorJugador)
        print("salio la carta",cartaAleatoria,"de",pintaCarta,"la carta es de color",colorCarta)
        feedback=("salio la carta",cartaAleatoria,"de",pintaCarta,"la carta es de color",colorCarta)
        
        
        if(colorJugador==colorCarta):
           
            
            resultadoC = win(apuesta,cuota,saldo)
            return resultadoC
            
        else:
            
            resultadoC = lose(apuesta,cuota,saldo)
            return resultadoC
            
    if(modo=="PINTA"):
        cuota=4
        print("elegiste la pinta",pintaJugador)
        print("salio la carta",cartaAleatoria,"de",pintaCarta)
        feedback=("salio la carta",cartaAleatoria,"de",pintaCarta)
        
        if(pintaJugador==pintaCarta):
            
            resultadoC = win(apuesta,cuota,saldo)
            return resultadoC
        else:
            
            resultadoC = lose(apuesta,cuota,saldo)
            return resultadoC
           

      
        
    
