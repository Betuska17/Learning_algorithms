filepath = '/workspaces/Learning_algorithms/python_crash_course/files_and_exceptions/pi_digits.txt'
with open(filepath) as file_object:
    lines = file_object.readlines()

#Cree una vriable para manener los digitos de pi
pi_string = ''

#loop that adds each line of digits to pi_string
#but removes the whithe space of the end
for line in lines:
    pi_string += line.rstrip()


birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi")
else:
    print("Your birthdat does not appear in the first million of pi")