class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attemps = 0
    
    def greetings(self): #Metodo que da un saludo a el user
        print(f"Hello {self.first_name} {self.last_name}")
    
    def describe_user(self): #Metodo que da los datos del user
        print(f"User's name is {self.first_name} {self.last_name} and the user is {self.age}\nthe privilages this user has are: ")
    
    def increment_login_attemps(self): #metodo que incrementa en uno el attribute login_attemps cada que lo llamo
        self.login_attemps += 1


    def reset_login_attempts(self):  #metodo que vuelva a poner en cero el atributo login_attemps cada que se llam
        self.login_attemps = 0

class Admin(User):
    def __init__(self, first_name, last_name, age, privilages):
        super().__init__(first_name, last_name, age)
        self.privilages = privilages
    
    def show_privilages(self):
        for privilage in self.privilages:
            print(privilage.title())


adminrights = Admin('Luis', 'Gonzales', 25, ["can add post", "can delete post", "can ban user"] )
adminrights.greetings()
adminrights.describe_user()
adminrights.show_privilages()