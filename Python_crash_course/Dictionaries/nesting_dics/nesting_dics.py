aliens = [] 

for alien in range(30):
    new_allien = {'color' : 'green', 'points' : 5, 'speed': 'slow'}  #cree 30 aliens con estas caracteristicas
    aliens.append(new_allien)  #metemos cada alien creado en la lista aliens

for alien in aliens[:5]: #mostramos los primeros 5 aliens
    print(alien)

print('...')



aliens_created = len(aliens)

print(f"Aliens created: {aliens_created}")



for alien in aliens[:3]:     #voy a modificar los primeros tres aliens
    if alien['color'] == 'green': #si el color de el aline es verde, cambiamos por los valores de abajo
        alien['color'] = 'yellow' 
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens:
    print(alien)