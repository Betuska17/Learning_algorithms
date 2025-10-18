import csv

csv_file = open("/workspaces/Learning_algorithms/bootcamp_ia/clase3/canciones_programadas.csv", 'r')
lector = csv.reader(csv_file, delimiter= ',')

lineas = 0

for renglon in lector:
    if lineas == 0: # el primer renglon es lo de los encabezados
        titulos = ""  #
        for columna in  renglon:
            titulos += columna + " "
        print(titulos.strip())
        lineas += 1

    else:
        print(renglon)


