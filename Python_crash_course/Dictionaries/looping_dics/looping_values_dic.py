# favorite_language = {
#     'phil': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'jen': 'java'
# }

# print('The following languages have been mentioned: ')
# for language in favorite_language.values():
#     print(language.title())


#Podemos tener el caso en el que tenemos un diccionario con valores que son iguales
#Si queremos mostrar solo las que son diferentes usar un set que es como un distinct

# for language in set(favorite_language.values()):
#     print(language.title())



# glossary = {

#     'variable' : "something you can assign the value to",
#     'list': "Multiple elements together you can modify them",
#     'tuple': "Multiple elements together but you cant modify them",
#     "for": "Loop to iterate throught something",
#     "integer": "Numbers"
#     }


# for key , value in glossary.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")




# rivers = {
#     "Amazonas": "Brasil",
#     "Nilo": "Egipt",
#     "Yangtese": "China",
#     "Bravo" : "Mexico",
#     "Missisipi": "USA"

# }

# for name, country in rivers.items():
#     print(f"The {name.title()} runs throught {country}")

# for name in rivers:
#     print(name)
# print("#####")
# for country in rivers.values():
#     print(country)


favorite_language = {
    'phil': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'jen': 'java'
}


for key, value in favorite_language.items():
    print(f"{key.title()} favorite language is {value.title()}")

coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']

for coder in coders:
    if coder in favorite_language:
        print(f"Thanks for taking our pool {key.title()}")
    else:
        print(f"{coder}, you should start taking our course")
    