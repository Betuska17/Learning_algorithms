import random
nombre = input("Hola, como te llamas? ").capitalize()

numero = random.randint(1,20)

print(f"Muy bien {nombre}, Adivina un numero entre el uno y el 20:  ")
print(f"{nombre}, recuerda que solo tienes 5 intentos")

count = 0
while count <= 5:
    guess = int(input())
    if guess < numero:
        print("Tu numero es muy bajo, dame otro numero")
    elif guess > numero:
        print("Tu numero es muy alto, dame otro numero")
    elif guess > 20:
        print("El numero es mayor a 20, intenta de nuevo")
    else:
        break
    count += 1

print(f"Buen trabajo {nombre} atinaste en {count} intentos")
    
    

    
