# Ejercio donde solo tengo el numero de una persona dentro de un 
# phonebook y el unico valor que conozco de la persona es el nombre
# usando big O

def finding_number(phonebook, name):
    low = 0
    high = len(phonebook) -1
    while low <= high:
        mid = (low + high) // 2
        if phonebook[mid][0] == name:
            return phonebook[mid][1]
        elif phonebook[mid][0] <  name:
            high = mid + 1
        else:
            low = mid + 1

# En este ejercicio use una lista de tuplas y no una lista
# la tuplas transmiten la idea de que esos dos valores estan
# pegados el uno con el otro, y para este caso las tuplas son 
# mas rapidas que las listas
my_phonebook = [('Alberto' , 5555) , ('Turan', 44444) , ('Jake' , 33333)]  
phone = (finding_number(my_phonebook, 'Jake'))

