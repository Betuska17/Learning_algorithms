# Podemos poner multiples argumentos dentro de una function
# *args --> nos permite poner mukltiples argumentos, se pudiera decir que ilimitados
# **kwargs --> Convierte esos argumentos en diccionarios lo que al momento de poner lo
# argumentos en la funcion nos va a permitir tratarlos como diccionarios


# Ejemplo de un restaurante donde vamos agregando clientes y vamos poniendo sus bebidas y comidas
tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
#print(tables)


# Write your code below: 
def assign_table(table_number, name, vip_status = False):
  tables[table_number]['name'] = name                      #Ocupamos [][] basados en los argumentos que tenemos de la funcion
  tables[table_number]['vip_status'] = vip_status
  
  
def assign_food_items(table_number, **order_items):
  print(order_items)
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['food'] = food
  tables[table_number]['drinks'] = drinks
#   print(food)
#   print(drinks)


# Example Call
assign_table(2, 'Alberto' , True)
assign_food_items(2, food='Pancakes, Poached Egg', drinks='Water')
print(tables)