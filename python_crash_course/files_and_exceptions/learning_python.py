filepath = '/workspaces/Learning_algorithms/python_crash_course/files_and_exceptions/learning_python.txt'

with open(filepath) as file_reader:
    #Como leer todas las lineas del archivo
    content = file_reader.read()
    print(content.rstrip())

    #leer linea por linea con un loop
    for line in file_reader:
        #le pongo rstrip para que no salga el espacio en blanco cada que se imprime una linea
        print(line.rstrip())

    #Leer line por linea y que las ponga en una lista
    #parece que readline solo lee la primer linea
    content = file_reader.readlines()
    print(content)