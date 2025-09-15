class Restaurant: #Genero mi clase que se llama restaurant
    def __init__(self, name, cuisine):  #defino mi metodo init que se va a ejecutar cada que cree un instance nuevo
        self.name = name  #variable name , attributes
        self. cuisine = cuisine #variable cuisine, attributes
        self.number_served = 0

    def describe_restaurant(self): #Creando mi primer metodo que imprime el nombre y la tipo de comida
        print(f"This is the restaurant {self.name}")
        print(f"The cuisine that we have in here is {self.cuisine}")
    
    def open_restaurant(self): #Segundo metodo que nos dice que el restaurante esta abierto
        print(f"{self.name} is now open!")
    
    def set_number_set(self, customers):  ##Cree este nuevo metodo para poder ver los customers y ponerlo en number_served
        self.number_served = customers
        print(f"Starting the day with {self.number_served} customer served")
    
    def increment_number_served(self, increment):  #luego incremente el numero de clientes que ya estaban servidos con el number de incremento
        self.number_served += increment
        print(f"The total of customers served in the day is {self.number_served} during the day we increased {increment} customers")

restaurant = Restaurant('La ahumadera', 'Mexican')
restaurant.set_number_set(10)
restaurant.increment_number_served(10)