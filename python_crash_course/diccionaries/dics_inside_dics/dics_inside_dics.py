users = {
    'montalva' : {
        'first'  : 'Alberto',
        'last' : 'Montalva',
        'location': 'mx'
    },

    'abignale' : {
        'first' : 'Jake',
        'last' : 'Abignale',
        'location': 'usa'
    }
}



for username, user_info in users.items():
    print(f"\n{username}")
    fullname = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']
    print(f"\tFullname: {fullname.title()}")
    print(f"\tLocation: {location.title()}")
