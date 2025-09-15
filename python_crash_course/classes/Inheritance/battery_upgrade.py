class Car: #Defino el nombre de mi class car
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self): #metodo que regresa una descripcion formal
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self): #agregando un nuevo metodo para que lea el velocimetro
        print(f"This car has a {str(self.odometer_reading)} miles on it")
    
    #Agrefo un metdo para que modifique un attribute dentro de la class
    def update_odometer(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, milage):
        self.odometer_reading += milage

"""Agrego una clase para la bateria, en vez de ponerla en un metodo, revisar la linea 34 para el ejemplo"""
class Baterry(): #creo una clase para la bateria
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {str(self.battery_size)}-kWh battery.")
        
    #Con la nueva class de bateria la podemos detallar tanto como queramos

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge"
        print(message)
    
    def upgrade_battery(self):
        if self.battery_size != 85:
            pass
        else:
            self.battery_size = 85


## Agrego una child class
#Se empiza siempre con la clase padre, por eso es que esta definida
#la clase padre siempre debe de aparecer en el archivo y siempre va primero

class ElectricCar(Car): #creamos la clase child, con la clase padre siempre incluida en parentesis
    def __init__(self, make, model, year): #toma toda la informacion para hacer un instance de Car
        super().__init__(make, model, year)
        
        #agregando los atributos de la child class
        self.battery = Baterry() 


my_tesla = ElectricCar('tesla', 'model s', 2016) #cree una instance de ElectriCar
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()