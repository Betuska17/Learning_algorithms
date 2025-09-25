#abro pi_digits.txt y le damos el nombre de file_object puse al path completo para que lo pueda correr desde donde sea en la terminal
#si no lo pongo completo tengo que abrir esa carpeta en la terminal
#tambien se puede poner en una variable

filepath = '/workspaces/Learning_algorithms/python_crash_course/files_and_exceptions/pi_digits.txt'
with open(filepath) as file_object:
    #guardo en contents el resultado de leer file_object
    contents = file_object.read()
    #Quito el espacio en blanco de la derecha
    print(contents.rstrip())



