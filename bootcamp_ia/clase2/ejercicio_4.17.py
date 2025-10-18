count = 0
lst = []
while count < 10:
    nombre = input("Ingresa un nombre:")
    if nombre not in lst:
        lst.append(nombre)
    else:
        print("El nombre ya esta en la lista, adios :) ")
        break
    count += 1

print("Has ingresado, 10 nombres diferentes, no puedes ingresar mas")