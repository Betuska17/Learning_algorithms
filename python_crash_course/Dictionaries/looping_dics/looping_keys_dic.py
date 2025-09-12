person = {
    'first_name' : 'Alberto',
    'last_name' : 'Montalva',
    'age': 25,
    'city': 'Mx'
}

for key, value in person.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


# ## cuando queremos imprimir las llaves se pueden usar estas dos formas 

for name in person.keys():
    pass

# #por default python iteara con las llaves y se vera asi , entonces usar cualquiera de las dos nos dara el mismo resultado

for name in person:
    pass



favorite_language = {
    'phil': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'jen': 'java'
}


friends = ['phil' , 'sarah']
for name in favorite_language:
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_language[name].title()
        print(f"\t{name.title()}. I see you love {language}")

#siempre se va a loopear de forma en la que se fueron agregando los diccionarios,
#para ordenarlos puedo usar sorted por ejemplo
for name in sorted(favorite_language):
    print(f"{name.title()}, thank you for taking our pool")