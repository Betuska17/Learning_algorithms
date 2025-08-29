# La busqueda binaria es la forma de buscar la posicion de un numero de la forma mas rapida posible
# ejemplo yo pienso una lista de numeros del uno al 10 y te digo que adivines el numero, tu puedes decir
# los numero de el 1 al 10 y te tomaria 10 intentos, pero para hacerlo mas facil se puede dividir la lista
# en dos y si el numero es mas alto elimino los numero anteriores y la vuelvo a dividir en dos hasta
# que logre cerrar la distacia de los elementos


def binary_search(array, item):
    low = 0 #limite menor de la lista
    high = len(array) -1 #limite mayor de la lista
    while low <= high:
        mid = (low + high) // 2 # partimos la lista en dos y agarramos la parte entera de la division
        num = array[mid]
        if num == item:
            return mid
        elif num >= item:
            high = mid - 1
        else:
            low = mid + 1

my_lst = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(my_lst,3))