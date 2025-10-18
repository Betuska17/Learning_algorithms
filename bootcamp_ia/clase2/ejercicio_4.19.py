iteraciones = [5,10,15]

for n in iteraciones:
    e = (1+1/n)**n
    print(f"Iteracion {n}, : e aprox, {round(e,6)}")