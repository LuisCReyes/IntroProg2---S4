#adivinar un número

import random


numero_secreto = random.randint(1,10)

while(True):
    numero_usuario = int(input("Dime un númeor del 1 al 10: "))
    print(numero_secreto)
     
    if (numero_secreto == numero_usuario):
        print("Felicidades, te ganaste 10 puntos extras")
        break
    else:
        print("Lo siento, tenes que invitar a un churro a todos los compañeros.")