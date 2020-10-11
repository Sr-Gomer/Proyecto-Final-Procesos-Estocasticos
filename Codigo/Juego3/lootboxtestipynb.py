"""LootboxTestipynb
By: Juan Fernando Ramírez y Mariana Serna
"""

import numpy as np
import numpy.random as rnd

lootBox = np.array([1, 2, 2, 3, 3, 3])
profit = 0
tier = 1
#print(lootBox)

for i in range (tier):
  shot = rnd.randint(0, 6)
  #print(lootBox[shot])

  if lootBox[shot] == 1:
    profit += 500000
    print("Felicidades! Ganaste el premio mayor(oro)")
    print("Se han añadido $500000")
    print("Tu saldo actual es de: ${}".format(profit))
  elif lootBox[shot] == 2:
    profit += 300000
    print("Ganaste el premio de plata")
    print("Se han añadido $300000")
    print("Tu saldo actual es de: ${}".format(profit))
  elif lootBox[shot] == 3:
    print("Ganaste el premio de bronce")
    print("Tu saldo actual es de: ${}".format(profit))

    #Nota: Considerar balancear un poco más el juego.