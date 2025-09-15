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

my_used_car = Car('dodge', 'challenger', 2016)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.update_odometer(23100)
#Metodo uno de modificar un el valor de un atributo de forma directa
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

#Metodo de mofificar el valor de un atributo por medio de un metodo definido en la clase
# my_new_car.update_odometer(25)
# my_new_car.read_odometer()

"""
Podemos modificar los valores de un attributo de tres diferentes maneras
1 --> Modificando el valor directo  cuando lo llamamos
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

2--> Modificar el valor de un atribute
def update_odometer(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back an odometer!")

my_new_car.update_odometer(25)
my_new_car.read_odometer()

"""