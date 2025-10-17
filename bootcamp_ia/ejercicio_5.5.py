import random

# Caracteres válidos
corchetes = ['(', ')', '[', ']']

# Generar cadena de 10 corchetes aleatorios
cadena = ''.join(random.choice(corchetes) for _ in range(10))
print("Cadena generada:", cadena)

# Separar en grupos usando espacios cada 2 o 3 caracteres (simulación)
# Aquí puedes ajustar la lógica de agrupamiento si quieres más control
grupos = []
i = 0
while i < len(cadena):
    if i + 2 <= len(cadena):
        grupos.append(cadena[i:i+2])
        i += 2
    else:
        grupos.append(cadena[i:])
        break

# Verificar cada grupo
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
