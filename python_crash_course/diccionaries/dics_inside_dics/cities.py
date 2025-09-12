cities = {
    'japon' : {'pais' : 'tokio', 
               'poblacion': '37.7  millones',
               'fact': 'comen ratas'},


    'nueva york': {'pais' : 'usa', 
                   'poblacion': '19 millones',
                   'fact': 'tiene la dona mas cara del mundo'},

    'munich' : {'pais': 'alemania',
                'poblacion': '84 millones',
                'fact': 'se pude tomar agua de las fuentes'}
}

for city, value in cities.items():
    print(f"La ciudad de {city.title()} esta en {value['pais'].title()}, tiene una poblacion de {value['poblacion']}, su fun fact es que: {value['fact']}")