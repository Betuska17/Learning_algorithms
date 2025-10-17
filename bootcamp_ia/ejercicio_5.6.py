# Abrir y leer el archivo
with open("archivo.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read()

# Normalizar el texto: convertir a minúsculas y eliminar signos de puntuación
import string
texto = texto.lower()
for signo in string.punctuation:
    texto = texto.replace(signo, "")

# Separar palabras
palabras = texto.split()

# Contar frecuencia de cada palabra
frecuencia = {}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

# Contar hápax (palabras con frecuencia 1)
hapax = 0
for palabra in frecuencia:
    if frecuencia[palabra] == 1:
        hapax += 1

print("Cantidad de hápax en el documento:", hapax)
