filepath = '/workspaces/Learning_algorithms/python_crash_course/files_and_exceptions/learning_python.txt'


with open(filepath) as file:
    contents = file.readlines()
    for line in contents:
        print(line.replace('Python' , 'C').rstrip())