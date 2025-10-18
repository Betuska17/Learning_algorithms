frase = input("Ingresa una frase: ").lower()
dic = {}
for letra in frase:
    if letra != ' ':
        if letra in dic:
            dic[letra] += 1
        else:
            dic[letra] = 1

print("Estas son las letras y las veces que se repiten")
print(dic)

    