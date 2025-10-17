""" Evaluar la funcion con incrementos de .05 en un rango de uno a dos"""

a = 1
b = 2
n = 20
dx = (b -a)/20

x = a
rango = []
for i in range(n + 1):
    fx = x ** 2 - 1
    fx = round(fx, 2)
    rango.append(fx)
    x += dx

print(f"El rango de la funcion evaluada de 1 a 2 con 20 puntos va desde {rango[0]} hasta {rango[-1]}")