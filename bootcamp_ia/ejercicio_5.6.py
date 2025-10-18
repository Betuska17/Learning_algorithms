with open("archivo.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read()

import string
texto = texto.lower()
for signo in string.punctuation:
    texto = texto.replace(signo, "")

palabras = texto.split()

frecuencia = {}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

hapax = 0
for palabra in frecuencia:
    if frecuencia[palabra] == 1:
        hapax += 1

print("Cantidad de hápax en el documento:", hapax)


    for value in output:
        shuttle = value[0]
        location = value[1]
        state = value[3]
        time = value[2]
        print(f"{shuttle} {state} at {location} since --> {time}")

[('SHUT0316', 'S01.001.15.01.C01', datetime.datetime(2025, 9, 4, 4, 56, 36), 'suspended')]


SHUT1731 suspended at S01.016.45.01.C01 since --> 2025-10-18 11:20:07