class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attemps = 0
    def greetings(self):
        print(f"Hello {self.first_name} {self.last_name}")
    def describe_user(self):
        print(f"User's name is {self.first_name} {self.last_name} and the user is {self.age}\n")
    def increment_login_attemps(self):
        self.login_attemps += 1


    def reset_login_attempts(self):
        self.login_attemps = 0
    
user = User('Alberto', 'Montalva', 25)

user.increment_login_attemps()
user.increment_login_attemps()
user.increment_login_attemps()
user.increment_login_attemps()

print(f"The total of user attemps is now {user.login_attemps}")
user.reset_login_attempts()
print(f"The count has been reset user attemps is now {user.login_attemps}")