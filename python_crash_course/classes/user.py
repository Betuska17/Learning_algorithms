class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def greetings(self):
        print(f"Hello {self.first_name} {self.last_name}")
    def describe_user(self):
        print(f"User's name is {self.first_name} {self.last_name} and the user is {self.age}\n")

user = User('Alberto', 'Montalva', 50)
user2= User('Luis', 'Torres', 25)
user3 = User('Maria', 'Hernandez', 25)
    
user.greetings()
user.describe_user()
user2.greetings()
user2.describe_user()
user3.greetings()
user3.describe_user()

