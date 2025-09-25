filepath = '/workspaces/Learning_algorithms/python_crash_course/files_and_exceptions/guest_book.txt'


with open(filepath, 'a') as file:

    print("Write exit whenever you want to leave")
    while True:
        name = input("Enter your name: ")
        if name == 'exit':
            break
        else:
            print(f"Hello {name}, your visit will be register")
            file.write(f"{name.rstrip().title()}\n")

