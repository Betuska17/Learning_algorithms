aliens = []

for alien in range(30):
    new_allien = {'color' : 'green', 'points' : 5, 'speed': 'slow'}
    aliens.append(new_allien)

for alien in aliens[:5]:
    print(alien)

print('...')



aliens_created = len(aliens)

print(f"Aliens created: {aliens_created}")



for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens:
    print(alien)