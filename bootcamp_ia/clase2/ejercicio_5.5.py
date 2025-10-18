import random

corchetes = ['(', ')', '[', ']']

cadena = ''.join(random.choice(corchetes) for _ in range(10))
print("Cadena generada:", cadena)


grupos = []
i = 0
while i < len(cadena):
    if i + 2 <= len(cadena):
        grupos.append(cadena[i:i+2])
        i += 2
    else:
        grupos.append(cadena[i:])
        break

for grupo in grupos:
    pila = []
    correcto = True
    for c in grupo:
        if c in '([':
            pila.append(c)
        elif c in ')]':
            if not pila:
                correcto = False
                break
            ultimo = pila.pop()
            if (ultimo == '(' and c != ')') or (ultimo == '[' and c != ']'):
                correcto = False
                break
    if pila:
        correcto = False
    print(grupo, "correcto" if correcto else "incorrecto")
