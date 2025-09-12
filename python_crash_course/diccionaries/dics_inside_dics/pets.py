pet1 = {
    'animal type' : 'dog',
    'ownsers name' : 'Alberto'
}

pet2 = {
    'animal type' : 'cat',
    'ownsers name' : 'jose'
}

pet3 = {
    'animal type' : 'fish',
    'ownsers name' : 'laura'
}

animal_lst = [pet1, pet2, pet3]

for animal in animal_lst:
    print(f"Hey this is a {animal["animal type"].title()}, my owner's name is {animal["ownsers name"].title()} ")