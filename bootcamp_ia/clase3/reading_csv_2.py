with open("canciones_programadas.csv") as file:
    file = file.readlines()
    lines = 0
    for renglon in file:
        if lines == 0: # es el inicio del archivo las columnas
            titulo = ""
        for columna in renglon:
            titulo += columna + " "
        print(titulo.strip())
        lines += 1

    else:
        print(renglon)
