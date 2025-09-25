file =  '/workspaces/Learning_algorithms/python_crash_course/files_and_exceptions/guests.txt'

with open(file, 'a') as file:
    name = input('Enter your name: ')
    file.write(f"{name.rstrip()}\n")