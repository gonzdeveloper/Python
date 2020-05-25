
import random

def ordenamiento_burbuja(lista):
    n = len(lista)

    for i in range(n-1):
        for j in range(0, n-1, 1): # O(n) * O(n-1) ~ O(n) * O(n) = O(n**2)

            if lista[j] > lista[j + 1]:
                # la facilidad de tener el swaping en python
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista



if __name__ == '__main__':
    tamano_de_la_lista = int(input('De que tamaño será la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_la_lista)]
    print(lista)

    lista_ordenada = ordenamiento_burbuja(lista)
    print(lista_ordenada)