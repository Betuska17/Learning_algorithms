class Restaurant: #Genero mi clase que se llama restaurant
    def __init__(self, name, cuisine):  #defino mi metodo init que se va a ejecutar cada que cree un instance nuevo
        self.name = name  #variable name
        self. cuisine = cuisine #variable cuisine

    def describe_restaurant(self): #Creando mi primer metodo que imprime el nombre y la tipo de comida
        print(f"This is the restaurant {self.name}")
        print(f"The cuisine that we have in here is {self.cuisine}")
    
    def open_restaurant(self): #Segundo metodo que nos dice que el restaurante esta abierto
        print(f"{self.name} is now open!")

#defino un primer instance de la clase restaurant
restaurant = Restaurant('Mister Taco', 'Mexican')
restaurant2 = Restaurant('Five Guys', 'Burgers')
restaurant3 = Restaurant('Mediterranean Spot', 'Mediterranean')
#Accedo a los dos attributes por separado y las imprimo
print(f"Restaurant is called {restaurant.name}")
print(f"They serve {restaurant.cuisine} food")
print(f"\nRestaurant is called {restaurant2.name}")
print(f"They serve {restaurant2.cuisine} food")
print(f"\nRestaurant is called {restaurant3.name}")
print(f"They serve {restaurant3.cuisine} food")

#llamo a los dos metodos
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant2.describe_restaurant()
restaurant2.open_restaurant()
restaurant3.describe_restaurant()
restaurant3.open_restaurant()




