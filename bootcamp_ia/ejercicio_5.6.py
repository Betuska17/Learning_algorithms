lo with open("archivo.txt", "r", encoding="utf-8") as archivo:
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

from datetime import datetime

output = [
    ('SHUT0316', 'S01.001.15.01.C01', datetime(2025, 10, 18, 11, 20, 7), 'suspended'),
    ('SHUT1731', 'S01.016.45.01.C01', datetime(2025, 10, 18, 12, 45, 0), 'suspended')
]

now = datetime.now()

for value in output:
    shuttle = value[0]
    location = value[1]
    state = value[3]
    event_time = value[2]
    
    delta_minutes = (now - event_time).total_seconds() / 60
    formatted_time = event_time.strftime("%Y-%m-%d %H:%M:%S")
    
    if delta_minutes < 20:
        color = "\033[92m"  # green
    elif delta_minutes < 60:
        color = "\033[93m"  # yellow/orange
    else:
        color = "\033[91m"  # red
    
    reset = "\033[0m"
    print(f"{color}{shuttle} {state} at {location} since --> {formatted_time} ({int(delta_minutes)} min ago){reset}")

