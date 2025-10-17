import random

cadena = ""
for i in range(10):
    if random.randint(0, 1) == 0:
        cadena += "["
    else:
        cadena += "]"

print("Cadena generada:", cadena)

balance = 0   
pares_correctos = 0

for i in range(len(cadena)):
    if cadena[i] == "[":
        balance += 1
    elif cadena[i] == "]" and balance > 0:
        balance -= 1
        pares_correctos += 1

print("Número de pares correctos:", pares_correctos)