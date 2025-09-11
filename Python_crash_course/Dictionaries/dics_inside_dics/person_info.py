person1 = {
    'first_name' : 'Alberto',
    'last_name' : 'Montalva',
    'age': 25,
    'city': 'Harrisburgh'
}

person2 = {
    'first_name': 'Luis',
    'last_name': 'Hernandez',
    'age': 24,
    'city': 'Frederick'
}

person3 = {
    'first_name' : 'Luisa',
    'last_name' : 'Gutierrez',
    'age' : 26,
    'city' : 'Hagerstown'
}

personas = [person1 , person2, person3]  # meti los tres diccionarios a una lista

for persona in personas:  # para cada diccionario en la lista, y de ahi saco los valores de los dic
    print(f"This is {persona['first_name']} {persona['last_name']}, and I am {persona['age']}, currently at {persona['city']}")