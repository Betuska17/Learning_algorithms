## Agremos un if / elif para que si solo tiene un favorito imprima el nombre 
## y el lengauge si tiene mas de uno se queda igual

#condicion nueva es que si la persona solo tiene un lenguaje favotio va a imprimir en usa sola linea
favorite_language = {
    'jen': ['java'],
    'sarah': ['c'],
    'edward': ['rust' , 'go'],
    'phil': ['python' , 'haskell']
}


for name, languages in favorite_language.items():
    if len(languages) == 1:
        for language in languages:
            print(f"{name.title()}'s favorite language is {language.title()}")
    else:
        print(f"\n{name.title()} favorites languages are:")
        for language in languages:
            print(f"\t{language.title()}")
