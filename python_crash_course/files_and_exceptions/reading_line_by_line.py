filepath = '/workspaces/Learning_algorithms/python_crash_course/files_and_exceptions/pi_digits.txt'
with open(filepath) as file_object:
    for line in file_object:
        print(line.rstrip())

#El resultado de esto es la linea del texto 
#lurgo un espacio en blaco y otra linea de texto
#usando rstrip quitamos esos espacios en blanco