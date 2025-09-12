#creating a dictionary that holds first and last name age and city
person = {
    'first_name' : 'Alberto',
    'last_name' : 'Montalva',
    'age': 25,
    'city': 'Mx'
}


print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

print(f'{person["first_name"]} {person["last_name"]} lives in {person["city"]} and is {person["age"]} years old')