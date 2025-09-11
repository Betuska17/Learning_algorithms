# Ejemplo que va a mostar el nombre de la persona y cuantos lenguajes favoritos tiene
favorite_language = {
    'jen': ['java'],
    'sarah': ['c'],
    'edward': ['rust' , 'go'],
    'phil': ['python' , 'haskell']
}



for name, languages in favorite_language.items():  #Aqui estoy separando los valorees dos listas
    # print(type(name)) --> me muestra que es una lista
    # print(type(languages)) --> me muestra que es una lista
    print(f"\n{name}'s favorite laguages are:")
    for language in languages:  # como ahora aqui la lista donde estan los lenguajes voy a iterar en esa misma
        print(f"\t{language}")  # para imprimir los lenguajes uno por uno
