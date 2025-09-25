filepath = '/workspaces/Learning_algorithms/python_crash_course/files_and_exceptions/pi_digits.txt'
with open(filepath) as file_object:
    #readlines toma cada linea del texto y lo pone en una lista
    lines = file_object.readlines()

#print(lines) imprime una lista

#imprimo cada linea que esta en la lista
for line in lines:
    print(line.rstrip())