
import random
import time


def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista: # O(n)
        if elemento == objetivo:
            match = True
            break
    
    return match


def busqueda_bianria(lista, comienzo, final, objetivo):
    if comienzo > final:
        return False
    
    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_bianria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_bianria(lista, comienzo, medio - 1, objetivo)



if __name__ == '__main__':
    tamano_de_la_lista = int(input('De que tamaño será la lista? '))
    objetivo = int(input('Qué número quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_la_lista)])

    inicio = time.time()
    encontrado = busqueda_lineal(lista, objetivo)
    fin = time.time()
    print(lista)
    print(f'EL tiempo de recorrida fue de: {fin - inicio}')
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')


    inicio = time.time()
    encontrado = busqueda_bianria(lista, 0 , len(lista), objetivo)
    fin = time.time()
    print(lista)
    print(f'EL tiempo de recorrida fue de: {fin - inicio}')
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')