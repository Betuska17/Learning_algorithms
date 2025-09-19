#abro pi_digits.txt y le damos el nombre de file_object
with open('pi_digits.txt') as file_object:
    #guardo en contents el resultado de leer file_object
    contents = file_object.read()
    print(contents)