#abro pi_digits.txt y le damos el nombre de file_object
with open('pi_digits.txt') as file_object:
    #guardo en contents el resultado de leer file_object
    contents = file_object.read()
    print(contents)




>>> /home/codespace/.python/current/bin/python /workspaces/Learning_algorithms/python_crash_course/files_and_exceptions/file_reader.py
  File "<stdin>", line 1
    /home/codespace/.python/current/bin/python /workspaces/Learning_algorithms/python_crash_course/files_and_exceptions/file_reader.py
    ^
SyntaxError: invalid syntax