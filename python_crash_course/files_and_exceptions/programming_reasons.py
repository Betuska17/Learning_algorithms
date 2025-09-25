filepath = '/workspaces/Learning_algorithms/python_crash_course/files_and_exceptions/programming_reasons.txt'

with open(filepath, 'a') as file:
    print("Whenever you are done write 'exit'")
    while True:
        reason = input("Write down why you like to code: ")
        if reason == 'exit':
            break
        else:
            file.write(f"{reason}\n")
