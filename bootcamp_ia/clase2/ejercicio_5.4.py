import operator
frase = input("Ingresa una frase: ").lower()
dic = {}
for letra in frase:
    if letra != ' ':
        if letra in dic:
            dic[letra] += 1
        else:
            dic[letra] = 1


dic_lst = dic.items()

"""operator.itemgetter(1) accede al segundo elemeto de cada tupla (los valores)  y con reverse True los ordeno de mayor a menor"""
ordenados = sorted(dic_lst, key = operator.itemgetter(1), reverse=True)

for clave, valor in ordenados:
    print(f"'{clave}': {valor}")